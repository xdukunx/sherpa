import os
import io
import requests
import urllib3
import certifi
import img2pdf
import pytesseract
from PIL import Image
from PyPDF2 import PdfWriter, PdfReader

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set Tesseract CMD path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def download_and_ocr_hd(base_url, output_folder, pdf_filename):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    print(f"Mengunduh gambar ke folder '{output_folder}' secara otomatis sampai habis...")
    
    downloaded_files = []
    i = 1
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    while True:
        image_url = f"{base_url}{i}.jpg"
        file_name = f"{i}.jpg"
        file_path = os.path.join(output_folder, file_name)

        # If file already exists locally, skip downloading to save time
        if os.path.exists(file_path):
            print(f"File {file_name} sudah ada, melewati unduhan.")
            downloaded_files.append(file_path)
            i += 1
            continue

        try:
            response = requests.get(image_url, headers=headers, verify=False, timeout=30)
            if response.status_code == 404:
                print(f"Halaman {i} tidak ditemukan (404). Asumsi ini adalah akhir dokumen.")
                break
            
            response.raise_for_status()
            
            if response.status_code == 200:
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print(f"Berhasil mengunduh: {file_name}")
                downloaded_files.append(file_path)
            
        except Exception as e:
            print(f"Gagal terhubung untuk mengunduh {file_name}. Alasan: {e}")
            break
            
        i += 1

    if not downloaded_files:
        print("\nTidak ada gambar yang diunduh, proses dibatalkan.")
        return

    # Sort numerically just to be safe
    downloaded_files.sort(key=lambda f: int(os.path.basename(f).split('.')[0]))

    print(f"\nMemulai proses pembuatan PDF HD dengan teks OCR...")
    print(f"Total halaman yang akan diproses: {len(downloaded_files)}")

    output_pdf = PdfWriter()
    
    # Keep references to the streams so PyPDF2 doesn't lose them!
    stream_refs = []

    for filename in downloaded_files:
        print(f"Memproses halaman: {os.path.basename(filename)}...")
        
        try:
            # 1. Generate 100% HD Image PDF
            img_pdf_bytes = img2pdf.convert(filename)
            img_stream = io.BytesIO(img_pdf_bytes)
            stream_refs.append(img_stream)
            img_reader = PdfReader(img_stream)
            img_page = img_reader.pages[0]
            
            # 2. Generate invisible OCR Text PDF
            text_pdf_bytes = pytesseract.image_to_pdf_or_hocr(filename, extension='pdf', lang='ind', config='-c textonly_pdf=1')
            text_stream = io.BytesIO(text_pdf_bytes)
            stream_refs.append(text_stream)
            text_reader = PdfReader(text_stream)
            text_page = text_reader.pages[0]
            
            # 3. Merge Text onto HD Image
            img_page.merge_page(text_page)
            output_pdf.add_page(img_page)
            
        except Exception as e:
            print(f"Gagal memproses {filename}: {e}")

    try:
        with open(pdf_filename, "wb") as f:
            output_pdf.write(f)
        print(f"\nBerhasil! PDF HD yang bisa dicari (OCR) telah dibuat: '{pdf_filename}'")
    except Exception as e:
        print(f"\nTerjadi error saat penulisan PDF: {e}")


# Konfigurasi
BASE_URL = "https://ir.unair.ac.id/uploaded_files/temporary/DigitalCollection/NmM0YjE4NzU4YWYxNWM3NTEwMGI2MTQ0YjAxNTk5MjQ5YmY3NTQ1Nw==/files/mobile/"
OUTPUT_FOLDER = "Judul Skripsi Kating"
PDF_OUTPUT_FILENAME = "Judul Skripsi Kating (HD).pdf"

if __name__ == "__main__":
    download_and_ocr_hd(BASE_URL, OUTPUT_FOLDER, PDF_OUTPUT_FILENAME)
