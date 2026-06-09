# SHERPA — Skripsi Helper & Repository Scraper

A local web app for scraping, OCR-ing, and managing thesis PDFs from Indonesian university internal repositories (UNAIR & ITS). Built as a thesis research tool.

## Features

- **Scrape** — downloads thesis pages as images from UNAIR flipbook or ITS SharePoint (via Opera GX)
- **OCR** — Tesseract (Indonesian + English) produces fully **searchable PDFs**
- **Bookmarks** — auto-detects *Daftar Isi* and adds clickable PDF sidebar bookmarks (BAB / section hierarchy)
- **Hyperlinks** — injects invisible `/Link` annotations on the *Daftar Isi* page so every TOC entry jumps directly to that page — same as the original flipbook
- **Document Reader** — built-in image + OCR text viewer
- **Full-Text Search** — search keywords across all scraped theses instantly
- **Literature Matrix** — structured table for writing Bab 2 (Tinjauan Pustaka), exportable as CSV / Markdown

## Requirements

- Python 3.10+
- [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) installed at `C:\Program Files\Tesseract-OCR\tesseract.exe` with `ind` and `eng` language packs
- University VPN connected (for accessing internal repository URLs)

```
pip install -r requirements.txt
```

For ITS SharePoint scraping, also install Playwright:
```
pip install playwright
playwright install chromium
```

## Usage

```
python app.py
```

Open `http://localhost:5000` in your browser.

### Scraping a new thesis

1. Go to **Scraper** tab
2. Enter a label (e.g. `Skripsi Alif`), select **UNAIR** as source
3. Paste the flipbook URL (e.g. `https://ir.unair.ac.id/uploaded_files/temporary/DigitalCollection/.../index.html`)
4. Click **Mulai Ambil Dokumen**

The pipeline runs automatically:
- Downloads images (tries high-res `/files/large/` first)
- Enhances images (auto-contrast, sharpening)
- OCR every page (Tesseract `ind+eng`)
- Compiles searchable PDF
- Detects *Daftar Isi* → adds sidebar bookmarks + clickable TOC hyperlinks

## Project structure

```
sherpa/
├── app.py              # Flask server & API routes
├── scraper.py          # Scraping, OCR, TOC detection, PDF assembly
├── templates/
│   └── index.html      # Single-page app shell
├── static/
│   ├── app.js          # All frontend logic
│   └── style.css       # Dark-theme UI
├── data/               # Runtime only — scraped documents (git-ignored)
├── requirements.txt
└── .gitignore
```

## Architecture notes

- `scrape_unair_job` — HTTP image download, probes `/files/large/` before `/files/mobile/`
- `scrape_its_sharepoint_job` — Playwright CDP connecting to Opera GX (port 9222)
- `preprocess_image_for_ocr` — Pillow auto-contrast + sharpening, caps at 2200 px
- `process_ocr_job` — pikepdf PDF assembly, then 3-strategy TOC detection:
  1. Flipbook server probe (JSON data files + index.html JS parsing)
  2. HOCR spatial analysis with OCR-error correction (`V`→1, `T`→7, noise-token filtering)
  3. Regex fallback on OCR text
- `add_pdf_bookmarks` — pikepdf `OutlineItem` for sidebar navigation
- `add_toc_hyperlinks` — pikepdf `/Link` annotations on the *Daftar Isi* page

## License

Personal research tool — use responsibly and in accordance with your institution's repository terms of service.
