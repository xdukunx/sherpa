import os
import re
import json
import shutil
import threading
import asyncio
from flask import Flask, jsonify, request, render_template, send_from_directory
from scraper import (
    DATA_DIR, DOCUMENTS_JSON, load_documents, save_documents,
    scrape_unair_job, scrape_its_sharepoint_job, process_ocr_job,
    detect_toc
)

app = Flask(__name__, template_folder='templates', static_folder='static')

# Global dict to store active scraping job status
active_jobs = {}

# Ensure matrix file exists
MATRIX_JSON = os.path.join(DATA_DIR, 'matrix.json')
if not os.path.exists(MATRIX_JSON):
    with open(MATRIX_JSON, 'w', encoding='utf-8') as f:
        json.dump([], f)

def sanitize_folder_name(name):
    # Keep only alphanumeric and underscores/spaces
    s = re.sub(r'[^\w\s-]', '', name).strip()
    s = re.sub(r'[-\s]+', '_', s)
    return s.lower()

def run_scrape_thread(doc_id, url, source, title):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        active_jobs[doc_id] = {
            'status': 'Starting',
            'message': 'Inisialisasi scraping...',
            'current_page': 0,
            'total_pages': 0
        }
        
        # Phase 1: Scraping / Downloading
        if source == 'unair':
            pages_downloaded = loop.run_until_complete(
                scrape_unair_job(doc_id, url, active_jobs[doc_id])
            )
        elif source == 'its':
            pages_downloaded = loop.run_until_complete(
                scrape_its_sharepoint_job(doc_id, url, active_jobs[doc_id])
            )
        else:
            raise Exception("Sumber repository tidak didukung.")
            
        if pages_downloaded == 0:
            raise Exception("Gagal mengunduh halaman atau halaman kosong.")
            
        # Phase 2: OCR and compilations
        loop.run_until_complete(
            process_ocr_job(doc_id, active_jobs[doc_id])
        )
        
        # Count bookmarks from the saved pages.json
        n_bookmarks = 0
        try:
            pages_file = os.path.join(DATA_DIR, doc_id, 'pages.json')
            if os.path.exists(pages_file):
                with open(pages_file, 'r', encoding='utf-8') as f:
                    pages_text = json.load(f)
                n_bookmarks = len(detect_toc(pages_text))
        except Exception:
            pass

        # Add to documents list
        docs = load_documents()
        exists = False
        for doc in docs:
            if doc['id'] == doc_id:
                doc['title'] = title
                doc['total_pages'] = pages_downloaded
                doc['source_url'] = url
                doc['source'] = source
                doc['bookmarks'] = n_bookmarks
                exists = True
                break
        if not exists:
            docs.append({
                'id': doc_id,
                'title': title,
                'total_pages': pages_downloaded,
                'source_url': url,
                'source': source,
                'bookmarks': n_bookmarks
            })
        save_documents(docs)
        
        active_jobs[doc_id]['status'] = 'Completed'
        active_jobs[doc_id]['message'] = 'Proses scraping & OCR berhasil selesai!'
        
    except Exception as e:
        print(f"Error in scraping thread: {e}")
        active_jobs[doc_id] = {
            'status': 'Failed',
            'message': f"Error: {str(e)}",
            'current_page': 0,
            'total_pages': 0
        }
    finally:
        loop.close()

# --- ROUTES ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/documents', methods=['GET'])
def get_docs():
    return jsonify(load_documents())

@app.route('/api/documents/<doc_id>', methods=['GET'])
def get_doc_detail(doc_id):
    docs = load_documents()
    doc = next((d for d in docs if d['id'] == doc_id), None)
    if not doc:
        return jsonify({'error': 'Dokumen tidak ditemukan'}), 404
        
    pages_file = os.path.join(DATA_DIR, doc_id, 'pages.json')
    pages_text = {}
    if os.path.exists(pages_file):
        try:
            with open(pages_file, 'r', encoding='utf-8') as f:
                pages_text = json.load(f)
        except Exception as e:
            print(f"Error reading pages text: {e}")
            
    return jsonify({
        'metadata': doc,
        'pages': pages_text
    })

@app.route('/api/documents/<doc_id>', methods=['DELETE'])
def delete_doc(doc_id):
    docs = load_documents()
    docs = [d for d in docs if d['id'] != doc_id]
    save_documents(docs)
    
    # Remove directory
    doc_path = os.path.join(DATA_DIR, doc_id)
    if os.path.exists(doc_path):
        shutil.rmtree(doc_path)
        
    return jsonify({'success': True})

@app.route('/api/scrape', methods=['POST'])
def start_scrape():
    data = request.json
    url = data.get('url')
    title = data.get('title')
    source = data.get('source', 'unair') # unair or its
    
    if not url or not title:
        return jsonify({'error': 'URL dan Judul wajib diisi'}), 400
        
    doc_id = sanitize_folder_name(title)
    
    # Check if this doc_id is currently scraping
    if doc_id in active_jobs and active_jobs[doc_id]['status'] in ['Starting', 'Downloading images', 'Performing OCR']:
        return jsonify({'error': 'Dokumen ini sedang diproses'}), 400
        
    # Start thread
    threading.Thread(target=run_scrape_thread, args=(doc_id, url, source, title)).start()
    
    return jsonify({'success': True, 'doc_id': doc_id})

@app.route('/api/scrape/status/<doc_id>', methods=['GET'])
def get_scrape_status(doc_id):
    status = active_jobs.get(doc_id, {'status': 'Idle', 'message': 'Tidak ada proses aktif.'})
    return jsonify(status)

@app.route('/api/search', methods=['GET'])
def search_text():
    query = request.args.get('q', '').strip()
    if not query:
        return jsonify([])
        
    query_lower = query.lower()
    docs = load_documents()
    results = []
    
    for doc in docs:
        doc_id = doc['id']
        pages_file = os.path.join(DATA_DIR, doc_id, 'pages.json')
        if not os.path.exists(pages_file):
            continue
            
        try:
            with open(pages_file, 'r', encoding='utf-8') as f:
                pages_text = json.load(f)
        except:
            continue
            
        doc_matches = []
        for page_num, text in pages_text.items():
            if query_lower in text.lower():
                # Extract clean snippet
                # Find index of match
                idx = text.lower().find(query_lower)
                start = max(0, idx - 80)
                end = min(len(text), idx + len(query_lower) + 120)
                snippet = text[start:end].replace('\n', ' ').strip()
                if start > 0:
                    snippet = "..." + snippet
                if end < len(text):
                    snippet = snippet + "..."
                    
                doc_matches.append({
                    'page': int(page_num),
                    'snippet': snippet
                })
                
        if doc_matches:
            # Sort matches by page number
            doc_matches.sort(key=lambda m: m['page'])
            results.append({
                'id': doc_id,
                'title': doc['title'],
                'matches': doc_matches
            })
            
    return jsonify(results)

@app.route('/api/matrix', methods=['GET'])
def get_matrix():
    try:
        with open(MATRIX_JSON, 'r', encoding='utf-8') as f:
            return jsonify(json.load(f))
    except:
        return jsonify([])

@app.route('/api/matrix', methods=['POST'])
def save_matrix():
    try:
        matrix_data = request.json
        with open(MATRIX_JSON, 'w', encoding='utf-8') as f:
            json.dump(matrix_data, f, indent=2, ensure_ascii=False)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/documents/<doc_id>/bookmarks', methods=['GET'])
def get_doc_bookmarks(doc_id):
    """Return detected TOC bookmark entries for a document."""
    pages_file = os.path.join(DATA_DIR, doc_id, 'pages.json')
    if not os.path.exists(pages_file):
        return jsonify([])
    try:
        with open(pages_file, 'r', encoding='utf-8') as f:
            pages_text = json.load(f)
        return jsonify(detect_toc(pages_text))
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/pdf/<doc_id>')
def get_pdf(doc_id):
    return send_from_directory(os.path.join(DATA_DIR, doc_id), 'document.pdf')

@app.route('/image/<doc_id>/<int:page_num>')
def get_image(doc_id, page_num):
    # Try JPG first, then PNG
    for ext in ['jpg', 'png']:
        img_name = f"{page_num}.{ext}"
        img_path = os.path.join(DATA_DIR, doc_id, 'images', img_name)
        if os.path.exists(img_path):
            return send_from_directory(os.path.join(DATA_DIR, doc_id, 'images'), img_name)
            
    # Return placeholder if image does not exist
    return jsonify({'error': 'Gambar tidak tersedia'}), 404

if __name__ == '__main__':
    print("Starting SHERPA local server at http://localhost:5000 ...")
    app.run(debug=True, host='127.0.0.1', port=5000)
