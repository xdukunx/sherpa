import os
import io
import re
import json
import requests
import pytesseract
import shutil
import asyncio
import xml.etree.ElementTree as ET
from PIL import Image, ImageOps, ImageEnhance
import pikepdf
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
os.makedirs(DATA_DIR, exist_ok=True)

DOCUMENTS_JSON = os.path.join(DATA_DIR, 'documents.json')
if not os.path.exists(DOCUMENTS_JSON):
    with open(DOCUMENTS_JSON, 'w', encoding='utf-8') as f:
        json.dump([], f)

_HTTP_HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}


def load_documents():
    try:
        with open(DOCUMENTS_JSON, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []


def save_documents(docs):
    with open(DOCUMENTS_JSON, 'w', encoding='utf-8') as f:
        json.dump(docs, f, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Image preprocessing
# ---------------------------------------------------------------------------

def preprocess_image_for_ocr(img_path, target_max_side=1800):
    """
    Load and enhance an image for Tesseract OCR.

    - Upscales small images (< 1000px) to improve OCR accuracy.
    - Downscales very large images (> 2200px) to keep PDF size reasonable.
    - Applies auto-contrast, mild sharpening, and contrast boost.

    Target: ≤ 150 MB total PDF for ~100-page thesis.
    """
    img = Image.open(img_path).convert('RGB')
    w, h = img.size
    max_side = max(w, h)

    if max_side < 1000:
        # Upscale low-res mobile images for better OCR
        scale = min(target_max_side / max_side, 2.5)
        img = img.resize((int(w * scale), int(h * scale)), Image.BICUBIC)
    elif max_side > 2200:
        # Downscale huge images to control output file size
        scale = 2200 / max_side
        img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)

    # Normalise brightness range (helps faded prints / pale flipbook renders)
    img = ImageOps.autocontrast(img, cutoff=1)
    # Mild sharpening (improves character edge definition)
    img = ImageEnhance.Sharpness(img).enhance(1.4)
    # Slight contrast boost
    img = ImageEnhance.Contrast(img).enhance(1.15)

    return img


def _ocr_page_task(file_path):
    """Thread-safe worker: preprocess + OCR one image page."""
    img = preprocess_image_for_ocr(file_path)
    config = '--oem 1 --psm 3'
    pdf_bytes = pytesseract.image_to_pdf_or_hocr(img, extension='pdf', lang='ind+eng', config=config)
    text = pytesseract.image_to_string(img, lang='ind+eng', config=config)
    return pdf_bytes, text


# ---------------------------------------------------------------------------
# URL resolution (UNAIR)
# ---------------------------------------------------------------------------

def resolve_unair_url(url):
    """
    Resolves any UNAIR repository URL to the base flipbook images folder URL
    (ending in /files/mobile/ or /files/large/).
    """
    url = url.strip()

    if '/files/mobile/' in url or '/files/large/' in url:
        return url if url.endswith('/') else url + '/'

    if 'index.html' in url:
        base = url.split('index.html')[0]
        return base + 'files/mobile/'

    if 'ir.unair.ac.id/handle/' in url or 'repository.unair.ac.id/' in url:
        try:
            resp = requests.get(url, headers=_HTTP_HEADERS, verify=False, timeout=15)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, 'html.parser')
                for a in soup.find_all('a', href=True):
                    href = a['href']
                    if 'DigitalCollection' in href:
                        if 'index.html' in href or '/files/mobile/' in href:
                            return resolve_unair_url(href)
                        href = href.rstrip('/') + '/'
                        return href + 'files/mobile/'
        except Exception as e:
            print(f"Error resolving UNAIR landing page: {e}")

    if 'DigitalCollection' in url:
        return url.rstrip('/') + '/files/mobile/'

    return url


def _probe_large_resolution(mobile_base_url):
    """
    Check if a /files/large/ folder exists for this flipbook.
    Returns the large URL if available, otherwise None.
    """
    large_url = mobile_base_url.replace('/files/mobile/', '/files/large/')
    if large_url == mobile_base_url:
        return None
    try:
        resp = requests.head(f"{large_url}1.jpg", headers=_HTTP_HEADERS, verify=False, timeout=10)
        if resp.status_code == 200:
            return large_url
    except Exception:
        pass
    return None


# ---------------------------------------------------------------------------
# UNAIR scraper
# ---------------------------------------------------------------------------

async def scrape_unair_job(doc_id, url, progress_tracker):
    base_url = resolve_unair_url(url)
    progress_tracker['status'] = 'Downloading images'
    progress_tracker['message'] = f'Resolved base URL: {base_url}'

    # Try to upgrade to large-resolution images
    loop = asyncio.get_event_loop()
    large_url = await loop.run_in_executor(None, _probe_large_resolution, base_url)
    if large_url:
        base_url = large_url
        progress_tracker['message'] = 'Resolusi tinggi tersedia → menggunakan /files/large/'
    else:
        progress_tracker['message'] = 'Menggunakan /files/mobile/ (large tidak tersedia)'

    doc_folder = os.path.join(DATA_DIR, doc_id)
    img_folder = os.path.join(doc_folder, 'images')
    os.makedirs(img_folder, exist_ok=True)

    i = 1
    downloaded = 0
    consecutive_failures = 0

    while True:
        file_path = os.path.join(img_folder, f"{i}.jpg")

        if os.path.exists(file_path) and os.path.getsize(file_path) > 1000:
            downloaded += 1
            i += 1
            continue

        image_url = f"{base_url}{i}.jpg"
        try:
            response = await loop.run_in_executor(
                None,
                lambda u=image_url: requests.get(u, headers=_HTTP_HEADERS, verify=False, timeout=20)
            )

            if response.status_code == 404:
                print(f"Halaman {i}: 404 → dokumen selesai.")
                break

            response.raise_for_status()

            with open(file_path, 'wb') as f:
                f.write(response.content)

            downloaded += 1
            consecutive_failures = 0
            progress_tracker['current_page'] = i
            progress_tracker['message'] = f"Berhasil mengunduh halaman {i}"
        except Exception as e:
            print(f"Error downloading page {i}: {e}")
            consecutive_failures += 1
            if consecutive_failures >= 3:
                break

        i += 1
        if i > 600:
            break
        await asyncio.sleep(0.05)

    # Save metadata (used later by OCR job for flipbook link probe)
    meta = {
        'root_url': base_url.split('/files/')[0] + '/' if '/files/' in base_url else base_url,
        'img_base_url': base_url,
        'resolution': 'large' if '/files/large/' in base_url else 'mobile'
    }
    with open(os.path.join(doc_folder, 'meta.json'), 'w', encoding='utf-8') as f:
        json.dump(meta, f, indent=2)

    progress_tracker['status'] = 'Downloaded'
    progress_tracker['total_pages'] = downloaded
    return downloaded


# ---------------------------------------------------------------------------
# ITS SharePoint scraper (Opera GX via CDP)
# ---------------------------------------------------------------------------

async def scrape_its_sharepoint_job(doc_id, url, progress_tracker):
    progress_tracker['status'] = 'Connecting to browser'
    progress_tracker['message'] = 'Connecting to Opera GX via CDP port 9222...'

    doc_folder = os.path.join(DATA_DIR, doc_id)
    img_folder = os.path.join(doc_folder, 'images')
    os.makedirs(img_folder, exist_ok=True)

    from playwright.async_api import async_playwright

    CDP_URL = "http://127.0.0.1:9222"
    PAGE_RENDER_WAIT = 3.5
    PORTRAIT_WIDTH = 850
    PORTRAIT_HEIGHT = 1080

    async with async_playwright() as pw:
        try:
            browser = await pw.chromium.connect_over_cdp(CDP_URL)
            context = browser.contexts[0]
        except Exception:
            raise Exception(
                "Gagal terhubung ke Opera GX. "
                "Pastikan Opera GX dibuka dengan flag --remote-debugging-port=9222."
            )

        page = None
        for p in context.pages:
            if "sharepoint.com" in p.url:
                page = p
                break

        if not page:
            progress_tracker['message'] = "Membuka tab baru untuk SharePoint..."
            page = await context.new_page()
            await page.goto(url, wait_until="load", timeout=90000)
            await asyncio.sleep(15)
        else:
            await page.bring_to_front()
            await asyncio.sleep(2)

        # Set window to portrait size
        try:
            cdp = await page.context.new_cdp_session(page)
            res = await cdp.send("Browser.getWindowForTarget")
            wid = res["windowId"]
            await cdp.send("Browser.setWindowBounds", {"windowId": wid, "bounds": {"windowState": "normal"}})
            await asyncio.sleep(0.5)
            await cdp.send("Browser.setWindowBounds", {
                "windowId": wid,
                "bounds": {"width": PORTRAIT_WIDTH, "height": PORTRAIT_HEIGHT}
            })
            await asyncio.sleep(1)
        except Exception as e:
            print(f"Could not resize window: {e}")

        # Detect total pages
        total_pages = 0
        try:
            total_pages = await page.evaluate("""() => {
                const inp = document.querySelector('input[aria-label*="antara 1 dan"]')
                          || document.querySelector('input[aria-label*="between 1 and"]');
                if (inp) {
                    const m = inp.getAttribute('aria-label').match(/(?:antara 1 dan|between 1 and)\\s+(\\d+)/);
                    if (m) return parseInt(m[1]);
                }
                return 0;
            }""")
        except Exception:
            pass

        if not total_pages:
            total_pages = 500

        progress_tracker['status'] = 'Downloading images'
        progress_tracker['total_pages'] = total_pages

        await page.keyboard.press("Control+Home")
        await asyncio.sleep(PAGE_RENDER_WAIT)

        saved = 0
        import hashlib
        prev_hash = None
        same_count = 0

        for pg in range(1, total_pages + 1):
            progress_tracker['current_page'] = pg
            progress_tracker['message'] = f"Mengambil screenshot halaman {pg}..."

            if pg > 1:
                try:
                    await page.evaluate(f"""() => {{
                        const inp = document.querySelector('input[aria-label*="antara 1 dan"]')
                                  || document.querySelector('input[aria-label*="between 1 and"]');
                        if (inp) {{
                            inp.focus();
                            inp.value = '{pg}';
                            inp.dispatchEvent(new Event('change', {{ bubbles: true }}));
                            inp.dispatchEvent(new KeyboardEvent('keydown', {{ key: 'Enter', code: 'Enter' }}));
                        }}
                    }}""")
                    await page.keyboard.press("Enter")
                except Exception:
                    await page.keyboard.press("PageDown")

                await page.mouse.move(10, 10)
                await asyncio.sleep(PAGE_RENDER_WAIT)

            canvas = page.locator("canvas").first
            img_bytes = None
            if await canvas.count() > 0:
                img_bytes = await canvas.screenshot(type="png")
            else:
                img_bytes = await page.screenshot(type="png")

            if not img_bytes:
                continue

            h = hashlib.md5(img_bytes).hexdigest()
            if h == prev_hash:
                same_count += 1
                if same_count >= 3:
                    print("Dokumen selesai (halaman mentok).")
                    break
                continue
            else:
                same_count = 0
                prev_hash = h

            # Save at native canvas resolution (no artificial upscale)
            img = Image.open(io.BytesIO(img_bytes)).convert('RGB')
            out_path = os.path.join(img_folder, f"{saved + 1}.jpg")
            img.save(out_path, format='JPEG', quality=88)
            saved += 1
            progress_tracker['message'] = f"Tersimpan halaman {saved}"

        progress_tracker['status'] = 'Downloaded'
        progress_tracker['total_pages'] = saved
        return saved


# ---------------------------------------------------------------------------
# TOC / Bookmark detection
# ---------------------------------------------------------------------------

def _roman_to_int(s):
    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result, prev = 0, 0
    for ch in reversed(s.upper()):
        v = vals.get(ch, 0)
        result += v if v >= prev else -v
        prev = v
    return result


def detect_toc(pages_text):
    """
    Scans OCR'd page text for "DAFTAR ISI" / "TABLE OF CONTENTS",
    parses chapter (BAB) and section (X.Y) entries, then resolves each
    entry to the correct absolute PDF page number.

    Returns a sorted list of:
        {'title': str, 'page': int (1-indexed), 'level': 1|2}
    Returns [] if no TOC is found or parsing fails.
    """
    max_pg = max((int(k) for k in pages_text.keys()), default=0)
    if max_pg == 0:
        return []

    # --- Step 1: Find TOC page ---
    # Use \s* (not \s+) — OCR often merges "DAFTAR ISI" → "DAFTARISI"
    toc_start = None
    for pg in range(1, min(31, max_pg + 1)):
        if re.search(r'DAFTAR\s*ISI|TABLE\s*OF\s*CONTENTS', pages_text.get(str(pg), ''), re.IGNORECASE):
            toc_start = pg
            break
    if toc_start is None:
        return []

    # --- Step 2: Collect TOC lines (up to 4 pages) ---
    toc_lines = []
    for pg in range(toc_start, min(toc_start + 4, max_pg + 1)):
        text = pages_text.get(str(pg), '')
        toc_lines.extend(text.splitlines())
        # Stop once we've passed the TOC and hit a chapter heading
        if pg > toc_start and re.search(r'^\s*BAB\s+I\b', text, re.MULTILINE | re.IGNORECASE):
            if len(toc_lines) > 10:
                break

    # Separator pattern: 3+ dots, spaces, or Unicode ellipsis/middle-dot chars
    SEP = r'[\s.·…·‥…]{3,}'

    chapter_re = re.compile(
        r'^(?P<bab>(?:BAB|CHAPTER)\s+[IVX]+|\d+)\s+'
        r'(?P<title>[A-ZÁÉÍÓÚÑ][^\n]{2,60}?)'
        + SEP +
        r'(?P<page>\d{1,3})\s*$',
        re.IGNORECASE
    )
    section_re = re.compile(
        r'^(?P<num>\d{1,2}\.\d{1,2})\s+'
        r'(?P<title>[A-ZÁÉÍÓÚÑ][^\n]{2,60}?)'
        + SEP +
        r'(?P<page>\d{1,3})\s*$',
        re.IGNORECASE
    )

    raw_entries = []
    for line in toc_lines:
        line = line.strip()
        if not line:
            continue

        m = chapter_re.match(line)
        if m:
            raw_entries.append({
                'title': f"{m.group('bab').upper()} {m.group('title').strip()}",
                'toc_page': int(m.group('page')),
                'level': 1
            })
            continue

        m = section_re.match(line)
        if m:
            raw_entries.append({
                'title': f"{m.group('num')} {m.group('title').strip()}",
                'toc_page': int(m.group('page')),
                'level': 2
            })

    if not raw_entries:
        return []

    # --- Step 3: Find page offset ---
    # Identify the TOC entry for the first chapter (smallest page num ≤ 5)
    chapters = [e for e in raw_entries if e['level'] == 1]
    first_chapter = min(chapters, key=lambda e: e['toc_page'], default=None)
    if first_chapter is None:
        first_chapter = min(raw_entries, key=lambda e: e['toc_page'])

    offset = toc_start + 1  # rough default

    # Search forward from the end of the TOC for the actual BAB I / chapter page
    scan_start = toc_start + 1
    for pdf_pg in range(scan_start, min(scan_start + 40, max_pg + 1)):
        text = pages_text.get(str(pdf_pg), '')
        if re.search(r'PENDAHULUAN|INTRODUCTION|BAB\s+I\b', text, re.IGNORECASE):
            offset = pdf_pg - first_chapter['toc_page']
            break

    # --- Step 4: Build final bookmark list (max 2 levels) ---
    result = []
    for e in raw_entries:
        if e['level'] > 2:
            continue
        pdf_page = max(1, e['toc_page'] + offset)
        if pdf_page > max_pg:
            continue
        result.append({'title': e['title'], 'page': pdf_page, 'level': e['level']})

    return sorted(result, key=lambda e: (e['page'], e['level']))


def add_pdf_bookmarks(pdf_path, toc_entries):
    """
    Write a 2-level outline (bookmarks) into an existing PDF using pikepdf.
    Chapters are top-level; sections are nested under their parent chapter.
    """
    if not toc_entries:
        return

    try:
        with pikepdf.open(pdf_path, allow_overwriting_input=True) as pdf:
            total = len(pdf.pages)
            with pdf.open_outline() as outline:
                current_chapter_item = None
                for entry in toc_entries:
                    # Clamp to valid page index (0-based)
                    page_idx = max(0, min(entry['page'] - 1, total - 1))
                    item = pikepdf.OutlineItem(entry['title'], page_idx)
                    if entry['level'] == 1:
                        outline.root.append(item)
                        current_chapter_item = item
                    elif entry['level'] == 2 and current_chapter_item is not None:
                        current_chapter_item.children.append(item)
                    else:
                        outline.root.append(item)
            pdf.save(pdf_path)
        print(f"[bookmarks] Added {len(toc_entries)} entries to {os.path.basename(pdf_path)}")
    except Exception as e:
        print(f"[bookmarks] Error adding bookmarks: {e}")


# ---------------------------------------------------------------------------
# HOCR-based spatial TOC extraction
# ---------------------------------------------------------------------------

def _parse_hocr_lines(hocr_bytes):
    """
    Parse Tesseract HOCR and extract the bounding box of every *line*.
    Returns list of {'text': str, 'x1','y1','x2','y2'}.

    We use line-level spans ('ocr_line') instead of word-level spans because
    a full-line bbox is all we need to place a clickable hyperlink rectangle.
    """
    try:
        text = hocr_bytes.decode('utf-8', errors='replace')
        text = re.sub(r'<!DOCTYPE[^>]*>', '', text)
        root_el = ET.fromstring(text)
    except ET.ParseError as exc:
        print(f"[hocr] XML parse error: {exc}")
        return []

    lines = []
    for elem in root_el.iter():
        local = elem.tag.split('}')[-1] if '}' in elem.tag else elem.tag
        if local == 'span' and 'ocr_line' in elem.get('class', ''):
            title_attr = elem.get('title', '')
            bbox = re.search(r'bbox\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)', title_attr)
            line_text = re.sub(r'\s+', ' ', ''.join(elem.itertext())).strip()
            if bbox and line_text:
                lines.append({
                    'text': line_text,
                    'x1': int(bbox[1]), 'y1': int(bbox[2]),
                    'x2': int(bbox[3]), 'y2': int(bbox[4]),
                })
    return lines


def _match_toc_entries_to_lines(toc_entries, hocr_lines, img_width):
    """
    Match TOC entries (from regex-based detect_toc) to HOCR line bounding boxes.

    Strategy: for each TOC entry, find the HOCR line whose text has the
    highest word-overlap with the entry title. The line bbox becomes the
    clickable hyperlink rectangle for that entry.

    Returns the same list with 'bbox' added to matched entries.
    """
    def _norm(s):
        # Keep only alphanumeric tokens, upper-cased, remove short noise
        tokens = re.sub(r'[^A-Z0-9\s]', ' ', s.upper()).split()
        return {t for t in tokens if len(t) >= 2}

    used = set()
    result = []

    for entry in toc_entries:
        title_tokens = _norm(entry['title'])
        best_idx, best_score = -1, 0.0

        for i, line in enumerate(hocr_lines):
            if i in used:
                continue
            line_tokens = _norm(line['text'])
            if not title_tokens or not line_tokens:
                continue
            inter = len(title_tokens & line_tokens)
            union = len(title_tokens | line_tokens)
            score = inter / union if union else 0.0
            if score > best_score:
                best_score = score
                best_idx = i

        e = dict(entry)
        if best_idx >= 0 and best_score >= 0.35:
            ln = hocr_lines[best_idx]
            used.add(best_idx)
            # Full-width row so the entire line is clickable (easier to hit)
            e['bbox'] = (0, ln['y1'], img_width, ln['y2'])
        # If no match, entry keeps no 'bbox' → no hyperlink, but bookmark still added
        result.append(e)

    return result


def _run_hocr_lines_on_image(img_path):
    """Preprocess image, run Tesseract HOCR, return (lines, img_w, img_h)."""
    img = preprocess_image_for_ocr(img_path)
    iw, ih = img.size
    hocr = pytesseract.image_to_pdf_or_hocr(
        img, extension='hocr', lang='ind+eng', config='--oem 1 --psm 6'
    )
    return _parse_hocr_lines(hocr), iw, ih


# OCR single-char misreads → correct digit (applies to small page numbers)
_OCR_DIGIT_FIXES = {
    'V': 1, 'v': 1, 'I': 1, 'l': 1, '!': 1,
    'O': 0, 'o': 0, 'Q': 0,
    'S': 5, 's': 5, 'T': 7, 'B': 8,
}


def _try_parse_toc_page(token):
    """
    Try to extract a page number (int) from a possibly OCR-corrupted token.
    Returns None for roman-numeral preliminary pages or unrecognisable tokens.
    """
    if not token:
        return None
    # Clean token (remove trailing punctuation)
    tok = token.rstrip('.,;:')
    # Pure arabic number
    if re.match(r'^\d{1,3}$', tok):
        return int(tok)
    # Roman numeral → preliminary page, skip
    if re.match(r'^[ivxlcdmIVXLCDM]{1,5}$', tok):
        return None
    # Single-char OCR misread
    if tok in _OCR_DIGIT_FIXES:
        return _OCR_DIGIT_FIXES[tok]
    # Multi-char with embedded digits (e.g. "1l" → 1)
    digits = re.sub(r'\D', '', tok)
    if digits and len(digits) <= 3:
        return int(digits)
    return None


def _is_noise_token(tok):
    """True when a token looks like OCR dot-leader noise (e.g. 'ooooo', '....', 'rsssnnn')."""
    if len(tok) < 4:
        return False
    tl = tok.lower()
    # Dominant character covers ≥ 70 % of the token
    most = max(set(tl), key=tl.count)
    if tl.count(most) / len(tl) >= 0.70:
        return True
    # Token is mostly 'noise' characters (dots, dashes, o/s/r/n common in OCR dots)
    noise_count = sum(1 for c in tl if c in '.orsn-_')
    if noise_count / len(tl) >= 0.70:
        return True
    return False


def detect_toc_from_hocr(hocr_lines, pages_text, toc_page_num, img_width):
    """
    Extract TOC entries AND their on-page bounding boxes from HOCR line data.

    Handles:
      • OCR-merged "DAFTARISI" (filtered before calling this function)
      • OCR noise in the dotted-leader area (repeated-char runs like 'ooooo')
      • Single-char OCR misreads of page numbers:
          V→1  T→7  O→0  S→5  B→8  (common in mobile-resolution flipbooks)
      • Roman numerals correctly distinguished from number misreads:
          — For BAB/section lines, single uppercase letters are treated as
            misread digits (V=1 is more likely than roman numeral V=5).
          — For preliminary lines we don't create entries at all.

    Returns list of:
        {'title', 'page': abs_pdf_page, 'level': 1|2, 'bbox': (x1,y1,x2,y2)}
    """
    max_pg = max((int(k) for k in pages_text.keys()), default=0) or 1
    raw = []

    for line in hocr_lines:
        text = line['text'].strip()
        tokens = text.split()
        if len(tokens) < 2:
            continue

        # Pre-classify the line type from its first tokens
        is_bab     = bool(re.match(r'(?i)^(?:BAB|CHAPTER)\s+[IVX]+', text))
        is_section = bool(re.match(r'^\d{1,2}\.\d{1,2}', text))

        if not (is_bab or is_section):
            continue   # only process chapter/section lines

        # Extract page number from end of line.
        # For BAB/section lines we treat single-char tokens as OCR misreads
        # FIRST (before treating them as roman numerals).
        pg = None
        title_end_idx = len(tokens)

        for back in (1, 2):
            if len(tokens) < back + 1:
                break
            tok = tokens[-back].rstrip('.,;:')
            if not tok:
                continue

            # 1. Arabic digit
            if re.match(r'^\d{1,3}$', tok):
                pg = int(tok)
                title_end_idx = len(tokens) - back
                break
            # 2. Single-char OCR misread (higher priority than roman-numeral check
            #    for chapter/section lines where pages are always arabic)
            if tok in _OCR_DIGIT_FIXES:
                pg = _OCR_DIGIT_FIXES[tok]
                title_end_idx = len(tokens) - back
                break
            # 3. Embedded digits ONLY for short, non-noise tokens (e.g. "1l"→1)
            #    Skip noise tokens like "ooooooo2" — that's the dot-leader, not a page num
            if not _is_noise_token(tok):
                digits = re.sub(r'\D', '', tok)
                if digits and len(digits) <= 3:
                    pg = int(digits)
                    title_end_idx = len(tokens) - back
                    break

        if pg is None or pg == 0:
            continue

        # Title: tokens from line start, stopping at any OCR noise token
        title_tokens = []
        for tok in tokens[:title_end_idx]:
            if _is_noise_token(tok):
                break
            title_tokens.append(tok)

        title = re.sub(r'[\s.·\-]+$', '', ' '.join(title_tokens)).strip()
        # Strip trailing dot-noise globs and isolated low-value tokens
        title = re.sub(r'[\-\.oOsS]{3,}$', '', title).strip()
        # Remove trailing 1-4 char tokens that look like OCR garbage
        # (single lowercase blobs, lone special chars like '@', '~', '€')
        title = re.sub(r'\s+[a-z]{1,4}\s*$', '', title).strip()
        title = re.sub(r'\s+[@~€•°·\-_]{1,3}\s*$', '', title).strip()

        if len(title) < 3:
            continue

        level = 1 if is_bab else 2

        raw.append({
            'title':    title,
            'toc_page': pg,
            'level':    level,
            'bbox':     (0, line['y1'], img_width, line['y2']),
        })

    if not raw:
        return []

    # Calculate page offset
    chapters = [e for e in raw if e['level'] == 1]
    first_ch = min(chapters, key=lambda e: e['toc_page'],
                   default=min(raw, key=lambda e: e['toc_page']))

    offset = toc_page_num + 1   # rough default
    for scan_pg in range(toc_page_num + 1, min(toc_page_num + 45, max_pg + 1)):
        if re.search(r'PENDAHULUAN|INTRODUCTION|BAB\s+I\b',
                     pages_text.get(str(scan_pg), ''), re.IGNORECASE):
            offset = scan_pg - first_ch['toc_page']
            break

    # Convert and validate: TOC page numbers must be monotonically increasing
    result   = []
    last_pg  = 0
    for e in raw:
        pdf_page = max(1, e['toc_page'] + offset)
        # Skip entries where page order regresses significantly (likely OCR error)
        if pdf_page < last_pg - 2:
            print(f"[hocr] Skipping out-of-order entry: '{e['title']}' p.{pdf_page} (prev={last_pg})")
            continue
        if pdf_page <= max_pg:
            result.append({
                'title': e['title'],
                'page':  pdf_page,
                'level': e['level'],
                'bbox':  e['bbox'],
            })
            last_pg = pdf_page

    return sorted(result, key=lambda e: (e['page'], e['level']))


# ---------------------------------------------------------------------------
# Flipbook server probe (bonus: accurate page numbers from source data)
# ---------------------------------------------------------------------------

def _probe_flipbook_links(root_url):
    """
    Try to pull pre-computed bookmark / TOC data from the UNAIR flipbook server.
    Tries common JSON endpoints then parses index.html for embedded JS data.
    Returns list of {'title', 'page'} or None.
    """
    if not root_url:
        return None

    root = root_url.rstrip('/') + '/'

    for ep in ('bookmarks.json', 'toc.json', 'outline.json', 'data.json',
               'book.json', 'files/bookmarks.json', 'files/toc.json'):
        try:
            r = requests.get(root + ep, headers=_HTTP_HEADERS, verify=False, timeout=6)
            if r.status_code == 200:
                body = r.text.strip()
                if body.startswith(('{', '[')):
                    result = _parse_flipbook_json(r.json())
                    if result:
                        print(f"[flipbook] Link data found in {ep}")
                        return result
        except Exception:
            pass

    try:
        r = requests.get(root + 'index.html', headers=_HTTP_HEADERS, verify=False, timeout=12)
        if r.status_code == 200:
            result = _parse_flipbook_html(r.text)
            if result:
                print("[flipbook] Link data found in index.html")
                return result
    except Exception:
        pass

    return None


def _parse_flipbook_json(data):
    """Recursively extract [{title, page}] from arbitrary flipbook JSON."""
    results = []

    def walk(obj):
        if isinstance(obj, list):
            for item in obj:
                walk(item)
        elif isinstance(obj, dict):
            title = (obj.get('title') or obj.get('name')
                     or obj.get('text') or obj.get('label'))
            page  = (obj.get('page') or obj.get('pageNumber')
                     or obj.get('dest') or obj.get('p'))
            if title and page:
                try:
                    results.append({'title': str(title).strip(), 'page': int(page)})
                except (ValueError, TypeError):
                    pass
            for key in ('children', 'items', 'entries', 'bookmarks', 'toc', 'outline'):
                if key in obj:
                    walk(obj[key])

    walk(data)
    return results if results else None


def _parse_flipbook_html(html):
    """Extract embedded JS bookmark/TOC arrays from a flipbook index.html."""
    patterns = [
        r'(?:var\s+)?bookmarks\s*[=:]\s*(\[.*?\])\s*[;,]',
        r'(?:var\s+)?toc\s*[=:]\s*(\[.*?\])\s*[;,]',
        r'(?:var\s+)?outline\s*[=:]\s*(\[.*?\])\s*[;,]',
        r'"bookmarks"\s*:\s*(\[.*?\])',
        r'"toc"\s*:\s*(\[.*?\])',
    ]
    for pat in patterns:
        m = re.search(pat, html, re.DOTALL | re.IGNORECASE)
        if m:
            try:
                data = json.loads(m.group(1))
                result = _parse_flipbook_json(data)
                if result:
                    return result
            except (json.JSONDecodeError, Exception):
                continue
    return None


# ---------------------------------------------------------------------------
# PDF in-page link annotation injection
# ---------------------------------------------------------------------------

def add_toc_hyperlinks(pdf_path, toc_page_idx, link_entries, img_width, img_height):
    """
    Inject invisible /Link annotations on the TOC page of the PDF so every
    Daftar Isi entry becomes a clickable jump to its target page.

    Args:
        toc_page_idx  : 0-indexed page number in the PDF
        link_entries  : list of {'bbox': (x1,y1,x2,y2), 'target_page': int (0-indexed)}
        img_width/height : dimensions of the source image (for coordinate conversion)
    """
    if not link_entries:
        return

    try:
        with pikepdf.open(pdf_path, allow_overwriting_input=True) as pdf:
            total   = len(pdf.pages)
            page    = pdf.pages[toc_page_idx]
            mb      = page.mediabox
            pdf_w   = float(mb[2])
            pdf_h   = float(mb[3])
            sx      = pdf_w / img_width
            sy      = pdf_h / img_height

            new_annots = []
            for entry in link_entries:
                tgt = entry['target_page']
                if not (0 <= tgt < total):
                    continue

                ix1, iy1, ix2, iy2 = entry['bbox']
                # Add a small vertical padding so the click area is generous
                iy1 = max(0, iy1 - 4)
                iy2 = min(img_height, iy2 + 4)

                # Convert to PDF coordinates (y-axis is flipped in PDF: 0 = bottom)
                px1 = ix1 * sx
                py1 = pdf_h - iy2 * sy
                px2 = ix2 * sx
                py2 = pdf_h - iy1 * sy

                dest_obj = pdf.pages[tgt].obj
                annot = pdf.make_indirect(pikepdf.Dictionary(
                    Type    = pikepdf.Name('/Annot'),
                    Subtype = pikepdf.Name('/Link'),
                    Rect    = pikepdf.Array([px1, py1, px2, py2]),
                    Border  = pikepdf.Array([0, 0, 0]),   # invisible border
                    Dest    = pikepdf.Array([dest_obj, pikepdf.Name('/Fit')]),
                ))
                new_annots.append(annot)

            if new_annots:
                if '/Annots' in page:
                    page['/Annots'] = pikepdf.Array(list(page.Annots) + new_annots)
                else:
                    page['/Annots'] = pikepdf.Array(new_annots)

            pdf.save(pdf_path)

        print(f"[links] {len(new_annots)} clickable links added to TOC page {toc_page_idx + 1}")
    except Exception as exc:
        print(f"[links] Error adding hyperlinks: {exc}")


# ---------------------------------------------------------------------------
# OCR + PDF compilation
# ---------------------------------------------------------------------------

async def process_ocr_job(doc_id, progress_tracker):
    """
    Full OCR + PDF pipeline:
      1. Preprocess every image and run Tesseract (ind+eng) → searchable PDF pages.
      2. Combine into a single PDF with pikepdf.
      3. Detect DAFTAR ISI via three strategies (best result wins):
           A. Flipbook server probe  → exact page numbers from source data
           B. HOCR spatial analysis → word-position-based detection (main strategy)
           C. Regex on OCR text     → fallback
      4. Add sidebar bookmarks (BAB / X.Y hierarchy).
      5. Inject invisible /Link annotations on the TOC page(s) so every
         Daftar Isi entry is clickable exactly like the original flipbook.
      6. Save pages.json, document.txt, document.md.
    """
    doc_folder = os.path.join(DATA_DIR, doc_id)
    img_folder = os.path.join(doc_folder, 'images')

    if not os.path.exists(img_folder):
        raise Exception("Folder gambar tidak ditemukan!")

    all_files = sorted(
        [f for f in os.listdir(img_folder) if f.lower().endswith(('.jpg', '.png'))],
        key=lambda x: int(os.path.splitext(x)[0])
    )
    if not all_files:
        raise Exception("Tidak ada gambar untuk di-OCR!")

    total_pages = len(all_files)
    progress_tracker['status']      = 'Performing OCR'
    progress_tracker['total_pages'] = total_pages
    progress_tracker['current_page'] = 0

    output_pdf_path = os.path.join(doc_folder, 'document.pdf')
    pages_json_path = os.path.join(doc_folder, 'pages.json')
    output_txt_path = os.path.join(doc_folder, 'document.txt')
    output_md_path  = os.path.join(doc_folder, 'document.md')

    pages_text  = {}
    full_text   = []
    out_pdf     = pikepdf.Pdf.new()
    src_pdfs    = []
    page_streams = []

    loop = asyncio.get_event_loop()

    # ── Phase 1: OCR every page ───────────────────────────────────────────
    for i, file_name in enumerate(all_files, 1):
        progress_tracker['current_page'] = i
        progress_tracker['message'] = f"OCR halaman {i}/{total_pages}"

        file_path = os.path.join(img_folder, file_name)
        try:
            pdf_bytes, page_text = await loop.run_in_executor(None, _ocr_page_task, file_path)

            stream = io.BytesIO(pdf_bytes)
            page_streams.append(stream)

            src = pikepdf.Pdf.open(stream)
            src_pdfs.append(src)
            out_pdf.pages.append(src.pages[0])

            pages_text[str(i)] = page_text
            full_text.append(f"## Halaman {i}\n\n{page_text}\n\n")
        except Exception as exc:
            print(f"[ocr] Error page {i} ({file_name}): {exc}")
            pages_text[str(i)] = f"[Gagal mengekstrak teks pada halaman {i}]"

    # ── Phase 2: Save combined PDF ────────────────────────────────────────
    progress_tracker['status']  = 'Saving files'
    progress_tracker['message'] = 'Menyimpan PDF gabungan...'
    out_pdf.save(output_pdf_path)
    for src in src_pdfs:
        try:
            src.close()
        except Exception:
            pass
    out_pdf.close()

    # ── Phase 3: TOC detection ────────────────────────────────────────────
    progress_tracker['message'] = 'Mendeteksi Daftar Isi...'

    # Read meta.json (written by scrape_unair_job)
    root_url = None
    meta_path = os.path.join(doc_folder, 'meta.json')
    if os.path.exists(meta_path):
        try:
            with open(meta_path, 'r', encoding='utf-8') as f:
                root_url = json.load(f).get('root_url')
        except Exception:
            pass

    # --- Find TOC page(s) in OCR text ---
    toc_pages = []   # list of (1-indexed page num, img_path)
    for pg in range(1, min(31, total_pages + 1)):
        if re.search(r'DAFTAR\s*ISI|TABLE\s*OF\s*CONTENTS',
                     pages_text.get(str(pg), ''), re.IGNORECASE):
            toc_pages.append((pg, os.path.join(img_folder, all_files[pg - 1])))
            # Include next page if it looks like it continues the TOC
            if pg < total_pages:
                nxt = pages_text.get(str(pg + 1), '')
                if not re.search(r'^\s*BAB\s+I\b', nxt, re.MULTILINE | re.IGNORECASE):
                    toc_pages.append((pg + 1, os.path.join(img_folder, all_files[pg])))
            break

    # --- Strategy A: Flipbook server probe ---
    flipbook_link_map = {}   # title_lower → page_num
    if root_url:
        try:
            fb_links = await loop.run_in_executor(None, _probe_flipbook_links, root_url)
            if fb_links:
                flipbook_link_map = {e['title'].lower(): e['page'] for e in fb_links}
                progress_tracker['message'] = (
                    f"Data flipbook ditemukan: {len(flipbook_link_map)} entri!"
                )
        except Exception as exc:
            print(f"[flipbook] Probe error: {exc}")

    # ── Phase 4 & 5: TOC detection + bookmarks + hyperlinks ─────────────
    # Primary strategy: run HOCR on each TOC page → get line text + bboxes.
    # detect_toc_from_hocr() extracts page numbers (with OCR correction) AND
    # line bounding boxes in one pass, so hyperlinks come for free.
    # Fallback: regex on OCR text (detect_toc) if HOCR yields nothing.

    progress_tracker['message'] = 'Mendeteksi Daftar Isi (HOCR + koreksi OCR)...'
    bookmark_entries = []
    total_links      = 0

    for toc_pgnum, toc_imgpath in toc_pages:
        pdf_pg_idx = toc_pgnum - 1   # 0-indexed

        # Run HOCR
        try:
            hocr_lines, iw, ih = await loop.run_in_executor(
                None, _run_hocr_lines_on_image, toc_imgpath
            )
            progress_tracker['message'] = (
                f"HOCR halaman {toc_pgnum}: {len(hocr_lines)} baris"
            )
        except Exception as exc:
            print(f"[hocr] TOC page {toc_pgnum}: {exc}")
            continue

        # Strategy B: HOCR with OCR correction (also gives bboxes)
        hocr_entries = detect_toc_from_hocr(hocr_lines, pages_text, toc_pgnum, iw)

        if not hocr_entries:
            # Strategy C fallback: regex on OCR text
            hocr_entries = detect_toc(pages_text)
            # For fallback, still try to match to HOCR lines for hyperlinks
            if hocr_entries:
                hocr_entries = _match_toc_entries_to_lines(hocr_entries, hocr_lines, iw)

        # Collect bookmarks (de-duplicated across TOC pages)
        existing_titles = {e['title'] for e in bookmark_entries}
        for e in hocr_entries:
            if e.get('level', 0) in (1, 2) and e['title'] not in existing_titles:
                bookmark_entries.append({k: e[k] for k in ('title', 'page', 'level')})
                existing_titles.add(e['title'])

        # Inject hyperlinks on this TOC page
        link_entries = []
        for e in hocr_entries:
            if 'bbox' not in e:
                continue
            tgt_page = max(0, e['page'] - 1)   # 0-indexed
            if 0 <= tgt_page < total_pages:
                link_entries.append({'bbox': e['bbox'], 'target_page': tgt_page})

        if link_entries:
            add_toc_hyperlinks(output_pdf_path, pdf_pg_idx, link_entries, iw, ih)
            total_links += len(link_entries)

    # Final fallback: no TOC pages found at all
    if not bookmark_entries:
        bookmark_entries = detect_toc(pages_text)

    # Add sidebar bookmarks
    progress_tracker['message'] = 'Menambahkan bookmark PDF...'
    if bookmark_entries:
        bookmark_entries.sort(key=lambda e: (e['page'], e['level']))
        add_pdf_bookmarks(output_pdf_path, bookmark_entries)
        progress_tracker['message'] = (
            f"{len(bookmark_entries)} bookmark · {total_links} hyperlink ditambahkan."
        )

    # ── Phase 6: Save text files ──────────────────────────────────────────
    with open(pages_json_path, 'w', encoding='utf-8') as f:
        json.dump(pages_text, f, indent=2, ensure_ascii=False)

    txt_content = ''.join(full_text)
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        f.write(txt_content)
    with open(output_md_path, 'w', encoding='utf-8') as f:
        f.write(f"# {doc_id.replace('_', ' ')}\n\n" + txt_content)

    progress_tracker['status'] = 'Completed'
    progress_tracker['message'] = (
        f"Selesai! {total_pages} halaman · "
        f"{len(bookmark_entries)} bookmark · "
        f"{total_links} hyperlink pada Daftar Isi."
    )
    return total_pages
