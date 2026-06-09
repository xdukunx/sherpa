// SHERPA Client-Side JavaScript Logic

// State Management
let state = {
    activeTab: 'dashboard',
    documents: [],
    matrix: [],
    reader: {
        activeDocId: null,
        activeDocTitle: '',
        totalPages: 0,
        currentPage: 1,
        pagesText: {}
    },
    pollingInterval: null
};

// DOM Elements
const elements = {
    // Navigation
    navItems: document.querySelectorAll('.nav-item'),
    tabPanes: document.querySelectorAll('.tab-pane'),
    tabTitle: document.getElementById('current-tab-title'),
    tabSubtitle: document.getElementById('current-tab-subtitle'),
    
    // Stats
    statsTotalDocs: document.getElementById('stats-total-docs'),
    statsTotalPages: document.getElementById('stats-total-pages'),
    statsMatrixRows: document.getElementById('stats-matrix-rows'),
    
    // Dashboard / Library
    libraryDocsList: document.getElementById('library-docs-list'),
    btnRefreshLibrary: document.getElementById('btn-refresh-library'),
    
    // Scraper
    scraperForm: document.getElementById('scraper-form'),
    scrapeTitle: document.getElementById('scrape-title'),
    scrapeSource: document.getElementById('scrape-source'),
    scrapeUrl: document.getElementById('scrape-url'),
    btnStartScrape: document.getElementById('btn-start-scrape'),
    progressBox: document.getElementById('progress-box'),
    progressStatus: document.getElementById('progress-status'),
    progressPercentage: document.getElementById('progress-percentage'),
    progressBarFill: document.getElementById('progress-bar-fill'),
    progressMessage: document.getElementById('progress-message'),
    progressPageCount: document.getElementById('progress-page-count'),
    itsInstructionsBox: document.getElementById('its-instructions-box'),
    
    // Document Reader
    readerDocSelect: document.getElementById('reader-doc-select'),
    readerPagesList: document.getElementById('reader-pages-list'),
    readerActiveDocTitle: document.getElementById('reader-active-doc-title'),
    readerPageIndicator: document.getElementById('reader-page-indicator'),
    btnReaderPrev: document.getElementById('btn-reader-prev'),
    btnReaderNext: document.getElementById('btn-reader-next'),
    btnOpenPdf: document.getElementById('btn-open-pdf'),
    readerImageContainer: document.getElementById('reader-image-container'),
    readerPageTextarea: document.getElementById('reader-page-textarea'),
    btnCopyPageText: document.getElementById('btn-copy-page-text'),
    
    // Search
    searchInput: document.getElementById('search-input'),
    btnExecuteSearch: document.getElementById('btn-execute-search'),
    searchResultsArea: document.getElementById('search-results-area'),
    
    // Literature Matrix
    matrixTbody: document.getElementById('matrix-tbody'),
    btnMatrixAdd: document.getElementById('btn-matrix-add'),
    btnMatrixSave: document.getElementById('btn-matrix-save'),
    btnMatrixExportMd: document.getElementById('btn-matrix-export-md'),
    btnMatrixExportCsv: document.getElementById('btn-matrix-export-csv'),
    
    // Toast Notification
    toast: document.getElementById('toast'),
    toastIcon: document.getElementById('toast-icon'),
    toastMessage: document.getElementById('toast-message')
};

// Page Descriptions for Header Info
const tabInfo = {
    dashboard: {
        title: 'Dashboard',
        subtitle: 'Selamat datang di SHERPA! Ringkasan dokumen skripsi Anda.'
    },
    scraper: {
        title: 'Scraper Repository',
        subtitle: 'Unduh dan ekstraksi otomatis teks skripsi dari repository UNAIR & ITS.'
    },
    reader: {
        title: 'Document Reader',
        subtitle: 'Baca halaman skripsi dan salin hasil pembacaan teks OCR.'
    },
    search: {
        title: 'Full-Text Search',
        subtitle: 'Cari kata kunci atau topik penelitian di semua koleksi skripsi Anda.'
    },
    matrix: {
        title: 'Matriks Sintesis Literatur',
        subtitle: 'Penyusunan tinjauan pustaka (Bab 2) terstruktur.'
    }
};

// Initialize App
document.addEventListener('DOMContentLoaded', () => {
    setupTabNavigation();
    loadLibrary();
    loadMatrix();
    
    // Add event listeners
    elements.btnRefreshLibrary.addEventListener('click', loadLibrary);
    elements.scraperForm.addEventListener('submit', handleScrapeSubmit);
    elements.scrapeSource.addEventListener('change', handleSourceChange);
    
    // Reader events
    elements.readerDocSelect.addEventListener('change', handleDocSelectChange);
    elements.btnReaderPrev.addEventListener('click', () => navigatePage(-1));
    elements.btnReaderNext.addEventListener('click', () => navigatePage(1));
    elements.btnOpenPdf.addEventListener('click', openOriginalPdf);
    elements.btnCopyPageText.addEventListener('click', copyPageText);
    
    // Search events
    elements.btnExecuteSearch.addEventListener('click', executeSearch);
    elements.searchInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') executeSearch();
    });
    
    // Matrix events
    elements.btnMatrixAdd.addEventListener('click', addNewMatrixRow);
    elements.btnMatrixSave.addEventListener('click', saveMatrixToServer);
    elements.btnMatrixExportMd.addEventListener('click', exportMatrixToMarkdown);
    elements.btnMatrixExportCsv.addEventListener('click', exportMatrixToCSV);
});

// Toast Notifications
function showToast(message, type = 'info') {
    elements.toastMessage.textContent = message;
    elements.toastIcon.className = 'fa-solid toast-icon';
    
    if (type === 'success') {
        elements.toastIcon.classList.add('fa-circle-check', 'success');
        elements.toast.style.border = '1px solid var(--accent-teal)';
    } else if (type === 'error') {
        elements.toastIcon.classList.add('fa-circle-exclamation', 'error');
        elements.toast.style.border = '1px solid var(--accent-pink)';
    } else {
        elements.toastIcon.classList.add('fa-circle-info', 'info');
        elements.toast.style.border = '1px solid var(--secondary)';
    }
    
    elements.toast.classList.remove('hidden');
    
    setTimeout(() => {
        elements.toast.classList.add('hidden');
    }, 4000);
}

// Tab Navigation logic
function setupTabNavigation() {
    elements.navItems.forEach(item => {
        item.addEventListener('click', () => {
            const targetTab = item.getAttribute('data-tab');
            switchTab(targetTab);
        });
    });
}

function switchTab(tabId) {
    state.activeTab = tabId;
    
    // Update menu state
    elements.navItems.forEach(item => {
        if (item.getAttribute('data-tab') === tabId) {
            item.classList.add('active');
        } else {
            item.classList.remove('active');
        }
    });
    
    // Update panes visibility
    elements.tabPanes.forEach(pane => {
        if (pane.id === `tab-${tabId}`) {
            pane.classList.add('active');
        } else {
            pane.classList.remove('active');
        }
    });
    
    // Update Header Text
    const info = tabInfo[tabId];
    if (info) {
        elements.tabTitle.textContent = info.title;
        elements.tabSubtitle.textContent = info.subtitle;
    }
}

// Scrape Form Source Toggle
function handleSourceChange(e) {
    const val = e.target.value;
    if (val === 'its') {
        elements.itsInstructionsBox.classList.remove('hidden');
        elements.scrapeUrl.placeholder = "https://itsacid-my.sharepoint.com/personal/.../document.pdf";
        elements.scrapeUrlHint.textContent = "Masukkan URL file PDF SharePoint. Jangan lupa nyalakan port debug Opera GX.";
    } else {
        elements.itsInstructionsBox.classList.add('hidden');
        elements.scrapeUrl.placeholder = "https://ir.unair.ac.id/...";
        elements.scrapeUrlHint.textContent = "Tempel URL halaman flipbook, index.html, atau URL landing page repository.";
    }
}

// Load library docs
async function loadLibrary() {
    try {
        const res = await fetch('/api/documents');
        const docs = await res.json();
        state.documents = docs;
        
        renderLibraryTable();
        updateStats();
        populateReaderSelect();
    } catch (e) {
        console.error("Gagal memuat perpustakaan: ", e);
        showToast("Gagal memuat perpustakaan dokumen", "error");
    }
}

function renderLibraryTable() {
    elements.libraryDocsList.innerHTML = '';
    
    if (state.documents.length === 0) {
        elements.libraryDocsList.innerHTML = `
            <tr>
                <td colspan="4" class="text-center text-muted">Belum ada dokumen. Pergi ke tab Scraper untuk mengunduh.</td>
            </tr>
        `;
        return;
    }
    
    state.documents.forEach(doc => {
        const tr = document.createElement('tr');
        
        const badgeClass = doc.source === 'unair' ? 'badge-unair' : 'badge-its';
        const badgeText = doc.source.toUpperCase();
        
        tr.innerHTML = `
            <td class="font-semibold" style="cursor: pointer;">
                <span class="open-in-reader-link" data-id="${doc.id}">${doc.title}</span>
            </td>
            <td>
                <span class="badge ${badgeClass}">${badgeText}</span>
            </td>
            <td>${doc.total_pages} Hal</td>
            <td>
                <button class="btn btn-secondary btn-sm btn-read-doc" data-id="${doc.id}">
                    <i class="fa-solid fa-book-open"></i> Baca
                </button>
                <button class="btn btn-secondary btn-sm btn-delete-doc text-danger" data-id="${doc.id}">
                    <i class="fa-solid fa-trash-can"></i> Hapus
                </button>
            </td>
        `;
        
        elements.libraryDocsList.appendChild(tr);
    });
    
    // Add Click Listeners
    document.querySelectorAll('.open-in-reader-link, .btn-read-doc').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const id = e.target.getAttribute('data-id');
            openDocInReader(id);
        });
    });
    
    document.querySelectorAll('.btn-delete-doc').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const id = e.target.closest('button').getAttribute('data-id');
            deleteDoc(id);
        });
    });
}

function updateStats() {
    elements.statsTotalDocs.textContent = state.documents.length;
    
    let totalPages = 0;
    state.documents.forEach(doc => {
        totalPages += parseInt(doc.total_pages || 0);
    });
    elements.statsTotalPages.textContent = totalPages;
    elements.statsMatrixRows.textContent = `${state.matrix.length} baris`;
}

function populateReaderSelect() {
    // Keep first placeholder
    elements.readerDocSelect.innerHTML = '<option value="">-- Pilih Dokumen --</option>';
    
    state.documents.forEach(doc => {
        const opt = document.createElement('option');
        opt.value = doc.id;
        opt.textContent = `${doc.title} (${doc.source.toUpperCase()})`;
        elements.readerDocSelect.appendChild(opt);
    });
    
    // Keep selection if active
    if (state.reader.activeDocId) {
        elements.readerDocSelect.value = state.reader.activeDocId;
    }
}

// Delete doc
async function deleteDoc(docId) {
    if (!confirm("Apakah Anda yakin ingin menghapus dokumen ini beserta semua data scraping-nya?")) {
        return;
    }
    
    try {
        const res = await fetch(`/api/documents/${docId}`, { method: 'DELETE' });
        const data = await res.json();
        if (data.success) {
            showToast("Dokumen berhasil dihapus", "success");
            loadLibrary();
            if (state.reader.activeDocId === docId) {
                unloadReader();
            }
        } else {
            showToast("Gagal menghapus dokumen", "error");
        }
    } catch (e) {
        console.error(e);
        showToast("Error koneksi saat menghapus dokumen", "error");
    }
}

// Handle scraping submit
async function handleScrapeSubmit(e) {
    e.preventDefault();
    
    const title = elements.scrapeTitle.value.trim();
    const source = elements.scrapeSource.value;
    const url = elements.scrapeUrl.value.trim();
    
    if (!title || !url) return;
    
    elements.btnStartScrape.disabled = true;
    elements.btnStartScrape.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Memulai...';
    
    try {
        const res = await fetch('/api/scrape', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title, source, url })
        });
        
        const data = await res.json();
        if (res.status === 200 && data.success) {
            showToast("Scraping berhasil ditambahkan ke background queue!", "success");
            startPollingStatus(data.doc_id);
        } else {
            showToast(data.error || "Gagal memulai scraping", "error");
            elements.btnStartScrape.disabled = false;
            elements.btnStartScrape.innerHTML = '<i class="fa-solid fa-circle-play"></i> Mulai Ambil Dokumen';
        }
    } catch (err) {
        console.error(err);
        showToast("Error koneksi ke Flask server", "error");
        elements.btnStartScrape.disabled = false;
        elements.btnStartScrape.innerHTML = '<i class="fa-solid fa-circle-play"></i> Mulai Ambil Dokumen';
    }
}

// Polling scrape status
function startPollingStatus(docId) {
    elements.progressBox.classList.remove('hidden');
    elements.progressStatus.textContent = 'Menghubungkan...';
    elements.progressPercentage.textContent = '0%';
    elements.progressBarFill.style.width = '0%';
    elements.progressPageCount.textContent = '0';
    
    if (state.pollingInterval) clearInterval(state.pollingInterval);
    
    state.pollingInterval = setInterval(async () => {
        try {
            const res = await fetch(`/api/scrape/status/${docId}`);
            const data = await res.json();
            
            elements.progressStatus.textContent = data.status;
            elements.progressMessage.textContent = data.message;
            elements.progressPageCount.textContent = data.current_page || 0;
            
            // Progress Calculation
            let percent = 0;
            if (data.status === 'Downloading images') {
                // Approximate downloader percentage
                const current = parseInt(data.current_page || 0);
                percent = Math.min(95, Math.round((current / (data.total_pages || 111)) * 50));
            } else if (data.status === 'Performing OCR') {
                const current = parseInt(data.current_page || 0);
                const total = parseInt(data.total_pages || 1);
                percent = 50 + Math.round((current / total) * 45);
            } else if (data.status === 'Completed') {
                percent = 100;
                clearInterval(state.pollingInterval);
                state.pollingInterval = null;
                showToast("Proses Scraping & OCR Selesai!", "success");
                
                // Reset form and box
                setTimeout(() => {
                    elements.scraperForm.reset();
                    elements.progressBox.classList.add('hidden');
                    elements.btnStartScrape.disabled = false;
                    elements.btnStartScrape.innerHTML = '<i class="fa-solid fa-circle-play"></i> Mulai Ambil Dokumen';
                }, 2000);
                
                loadLibrary();
            } else if (data.status === 'Failed') {
                percent = 0;
                clearInterval(state.pollingInterval);
                state.pollingInterval = null;
                showToast(data.message || "Proses scraping gagal.", "error");
                elements.btnStartScrape.disabled = false;
                elements.btnStartScrape.innerHTML = '<i class="fa-solid fa-circle-play"></i> Mulai Ambil Dokumen';
            } else {
                percent = 5;
            }
            
            elements.progressPercentage.textContent = `${percent}%`;
            elements.progressBarFill.style.width = `${percent}%`;
            
        } catch (e) {
            console.error("Error status polling: ", e);
        }
    }, 1500);
}

// --- DOCUMENT READER TAB ---
function openDocInReader(docId) {
    switchTab('reader');
    elements.readerDocSelect.value = docId;
    loadDocInReader(docId);
}

function handleDocSelectChange(e) {
    const docId = e.target.value;
    if (docId) {
        loadDocInReader(docId);
    } else {
        unloadReader();
    }
}

async function loadDocInReader(docId) {
    try {
        elements.readerPagesList.innerHTML = '<div class="text-center text-muted p-4 font-sm"><i class="fa-solid fa-spinner fa-spin"></i> Memuat data...</div>';
        
        const res = await fetch(`/api/documents/${docId}`);
        const data = await res.json();
        
        state.reader.activeDocId = docId;
        state.reader.activeDocTitle = data.metadata.title;
        state.reader.totalPages = parseInt(data.metadata.total_pages);
        state.reader.pagesText = data.pages;
        state.reader.currentPage = 1;
        
        elements.readerActiveDocTitle.textContent = state.reader.activeDocTitle;
        elements.btnOpenPdf.disabled = false;
        
        renderReaderPagesList();
        loadReaderPage(1);
    } catch (e) {
        console.error(e);
        showToast("Gagal memuat dokumen ke reader", "error");
        unloadReader();
    }
}

function unloadReader() {
    state.reader.activeDocId = null;
    state.reader.activeDocTitle = '';
    state.reader.totalPages = 0;
    state.reader.pagesText = {};
    state.reader.currentPage = 1;
    
    elements.readerDocSelect.value = '';
    elements.readerActiveDocTitle.textContent = 'Tidak ada dokumen aktif';
    elements.readerPageIndicator.textContent = 'Halaman 0 dari 0';
    elements.btnReaderPrev.disabled = true;
    elements.btnReaderNext.disabled = true;
    elements.btnOpenPdf.disabled = true;
    elements.readerPagesList.innerHTML = '<div class="text-center text-muted p-4 font-sm">Pilih dokumen terlebih dahulu untuk memuat daftar halaman.</div>';
    
    elements.readerImageContainer.innerHTML = `
        <div class="image-placeholder">
            <i class="fa-solid fa-image"></i>
            <span>Gambar Halaman akan Tampil di Sini</span>
        </div>
    `;
    elements.readerPageTextarea.value = '';
}

function renderReaderPagesList() {
    elements.readerPagesList.innerHTML = '';
    
    for (let i = 1; i <= state.reader.totalPages; i++) {
        const btn = document.createElement('button');
        btn.className = `reader-page-item ${i === 1 ? 'active' : ''}`;
        btn.setAttribute('data-page', i);
        btn.innerHTML = `<i class="fa-solid fa-file-lines"></i> Halaman ${i}`;
        
        btn.addEventListener('click', () => {
            loadReaderPage(i);
        });
        
        elements.readerPagesList.appendChild(btn);
    }
}

function loadReaderPage(pageNum) {
    state.reader.currentPage = pageNum;
    
    // Update active class in sidebar list
    document.querySelectorAll('.reader-page-item').forEach(btn => {
        const p = parseInt(btn.getAttribute('data-page'));
        if (p === pageNum) {
            btn.classList.add('active');
            btn.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
        } else {
            btn.classList.remove('active');
        }
    });
    
    // Update toolbar status
    elements.readerPageIndicator.textContent = `Halaman ${pageNum} dari ${state.reader.totalPages}`;
    elements.btnReaderPrev.disabled = pageNum <= 1;
    elements.btnReaderNext.disabled = pageNum >= state.reader.totalPages;
    
    // Load page text
    const text = state.reader.pagesText[String(pageNum)] || '';
    elements.readerPageTextarea.value = text;
    
    // Load page image
    const docId = state.reader.activeDocId;
    elements.readerImageContainer.innerHTML = `<img src="/image/${docId}/${pageNum}" alt="Halaman ${pageNum}" onerror="handleImageError(this)">`;
}

function handleImageError(imgEl) {
    // If image fails to load, replace with a nice message card
    const container = imgEl.parentElement;
    container.innerHTML = `
        <div class="image-placeholder text-center text-muted p-4">
            <i class="fa-solid fa-triangle-exclamation font-lg text-warning"></i>
            <span>Gambar tidak tersedia untuk halaman ini.</span>
        </div>
    `;
}

function navigatePage(direction) {
    const targetPage = state.reader.currentPage + direction;
    if (targetPage >= 1 && targetPage <= state.reader.totalPages) {
        loadReaderPage(targetPage);
    }
}

function openOriginalPdf() {
    if (state.reader.activeDocId) {
        window.open(`/pdf/${state.reader.activeDocId}`, '_blank');
    }
}

function copyPageText() {
    const text = elements.readerPageTextarea.value;
    if (!text) {
        showToast("Teks kosong", "info");
        return;
    }
    
    navigator.clipboard.writeText(text).then(() => {
        showToast("Teks halaman berhasil disalin ke clipboard!", "success");
    }).catch(err => {
        console.error(err);
        showToast("Gagal menyalin teks", "error");
    });
}


// --- SEARCH TAB ---
async function executeSearch() {
    const q = elements.searchInput.value.trim();
    if (!q) return;
    
    elements.btnExecuteSearch.disabled = true;
    elements.btnExecuteSearch.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i>';
    elements.searchResultsArea.innerHTML = '<div class="text-center text-muted p-4"><i class="fa-solid fa-arrows-spin fa-spin font-lg"></i> Mencari kata kunci...</div>';
    
    try {
        const res = await fetch(`/api/search?q=${encodeURIComponent(q)}`);
        const results = await res.json();
        
        renderSearchResults(results, q);
    } catch (e) {
        console.error(e);
        showToast("Gagal melakukan pencarian", "error");
        elements.searchResultsArea.innerHTML = '';
    } finally {
        elements.btnExecuteSearch.disabled = false;
        elements.btnExecuteSearch.innerHTML = 'Cari';
    }
}

function renderSearchResults(results, query) {
    elements.searchResultsArea.innerHTML = '';
    
    if (results.length === 0) {
        elements.searchResultsArea.innerHTML = `
            <div class="glass-card p-4 text-center text-muted">
                <i class="fa-solid fa-ban font-lg"></i>
                <p class="mt-2">Tidak ditemukan kecocokan untuk kata kunci "<strong>${query}</strong>".</p>
            </div>
        `;
        return;
    }
    
    // Sort query regex safely
    const escapedQuery = query.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&');
    const regex = new RegExp(`(${escapedQuery})`, 'gi');
    
    results.forEach(doc => {
        const card = document.createElement('div');
        card.className = 'search-result-doc-card';
        
        let matchesHtml = '';
        doc.matches.forEach(m => {
            // Highlight matching keyword
            const highlightedSnippet = m.snippet.replace(regex, '<mark>$1</mark>');
            
            matchesHtml += `
                <div class="search-match-item" data-id="${doc.id}" data-page="${m.page}">
                    <span class="match-page"><i class="fa-solid fa-file"></i> Halaman ${m.page}</span>
                    <p class="match-snippet">${highlightedSnippet}</p>
                </div>
            `;
        });
        
        card.innerHTML = `
            <h4><i class="fa-solid fa-file-lines"></i> ${doc.title}</h4>
            <div class="matches-list">
                ${matchesHtml}
            </div>
        `;
        
        elements.searchResultsArea.appendChild(card);
    });
    
    // Add Click listener to match items to jump to reader
    document.querySelectorAll('.search-match-item').forEach(item => {
        item.addEventListener('click', (e) => {
            const docId = item.getAttribute('data-id');
            const pageNum = parseInt(item.getAttribute('data-page'));
            
            switchTab('reader');
            elements.readerDocSelect.value = docId;
            
            // Load and set specific page
            loadDocInReader(docId).then(() => {
                loadReaderPage(pageNum);
            });
        });
    });
}


// --- LITERATURE REVIEW MATRIX ---
async function loadMatrix() {
    try {
        const res = await fetch('/api/matrix');
        const matrix = await res.json();
        state.matrix = matrix;
        
        renderMatrixTable();
        updateStats();
    } catch (e) {
        console.error("Gagal memuat matriks: ", e);
    }
}

function renderMatrixTable() {
    elements.matrixTbody.innerHTML = '';
    
    if (state.matrix.length === 0) {
        addNewMatrixRow(); // Add an empty row if matrix is empty
        return;
    }
    
    state.matrix.forEach((row, index) => {
        appendMatrixRowHtml(row, index);
    });
}

function appendMatrixRowHtml(row, index) {
    const tr = document.createElement('tr');
    tr.setAttribute('data-index', index);
    
    tr.innerHTML = `
        <td><div class="matrix-cell-editable" contenteditable="true" data-field="title">${row.title || ''}</div></td>
        <td><div class="matrix-cell-editable" contenteditable="true" data-field="author">${row.author || ''}</div></td>
        <td><div class="matrix-cell-editable" contenteditable="true" data-field="objective">${row.objective || ''}</div></td>
        <td><div class="matrix-cell-editable" contenteditable="true" data-field="methodology">${row.methodology || ''}</div></td>
        <td><div class="matrix-cell-editable" contenteditable="true" data-field="findings">${row.findings || ''}</div></td>
        <td><div class="matrix-cell-editable" contenteditable="true" data-field="notes">${row.notes || ''}</div></td>
        <td class="text-center">
            <button class="btn-delete-row" title="Hapus Baris"><i class="fa-solid fa-trash-can"></i></button>
        </td>
    `;
    
    // Add delete event
    tr.querySelector('.btn-delete-row').addEventListener('click', () => {
        tr.remove();
        saveMatrixFromUI(false); // Save silently after deletion
    });
    
    // Add auto-save listeners on blur
    tr.querySelectorAll('.matrix-cell-editable').forEach(cell => {
        cell.addEventListener('blur', () => {
            saveMatrixFromUI(false); // Save silently on typing exit
        });
    });
    
    elements.matrixTbody.appendChild(tr);
}

function addNewMatrixRow() {
    const emptyRow = {
        title: '',
        author: '',
        objective: '',
        methodology: '',
        findings: '',
        notes: ''
    };
    
    const index = elements.matrixTbody.querySelectorAll('tr').length;
    appendMatrixRowHtml(emptyRow, index);
}

async function saveMatrixFromUI(showNotification = true) {
    const rows = elements.matrixTbody.querySelectorAll('tr');
    const matrixData = [];
    
    rows.forEach(tr => {
        const title = tr.querySelector('[data-field="title"]').textContent.trim();
        const author = tr.querySelector('[data-field="author"]').textContent.trim();
        const objective = tr.querySelector('[data-field="objective"]').textContent.trim();
        const methodology = tr.querySelector('[data-field="methodology"]').textContent.trim();
        const findings = tr.querySelector('[data-field="findings"]').textContent.trim();
        const notes = tr.querySelector('[data-field="notes"]').textContent.trim();
        
        // Skip entirely empty rows
        if (title || author || objective || methodology || findings || notes) {
            matrixData.push({ title, author, objective, methodology, findings, notes });
        }
    });
    
    state.matrix = matrixData;
    updateStats();
    
    try {
        const res = await fetch('/api/matrix', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(matrixData)
        });
        
        if (res.status === 200 && showNotification) {
            showToast("Matriks berhasil disimpan ke server!", "success");
        }
    } catch (e) {
        console.error(e);
        if (showNotification) {
            showToast("Gagal menyimpan matriks", "error");
        }
    }
}

function saveMatrixToServer() {
    saveMatrixFromUI(true);
}

// Export Matrix functions
function exportMatrixToMarkdown() {
    if (state.matrix.length === 0) {
        showToast("Matriks kosong, tidak ada data untuk diexport", "info");
        return;
    }
    
    let md = "# Matriks Sintesis Literatur\n\n";
    md += "| Judul / Topik | Penulis & Tahun | Tujuan Penelitian | Metodologi | Temuan Kunci / Hasil | Catatan / Sitasi |\n";
    md += "| --- | --- | --- | --- | --- | --- |\n";
    
    state.matrix.forEach(row => {
        md += `| ${row.title.replace(/\|/g, '\\|')} | ${row.author.replace(/\|/g, '\\|')} | ${row.objective.replace(/\|/g, '\\|')} | ${row.methodology.replace(/\|/g, '\\|')} | ${row.findings.replace(/\|/g, '\\|')} | ${row.notes.replace(/\|/g, '\\|')} |\n`;
    });
    
    downloadFile(md, 'matriks_sintesis_literatur.md', 'text/markdown');
    showToast("Matriks diexport sebagai Markdown!", "success");
}

function exportMatrixToCSV() {
    if (state.matrix.length === 0) {
        showToast("Matriks kosong, tidak ada data untuk diexport", "info");
        return;
    }
    
    const escapeCsv = (str) => {
        return '"' + str.replace(/"/g, '""') + '"';
    };
    
    let csv = "Judul / Topik,Penulis & Tahun,Tujuan Penelitian,Metodologi,Temuan Kunci / Hasil,Catatan / Sitasi\n";
    
    state.matrix.forEach(row => {
        csv += `${escapeCsv(row.title)},${escapeCsv(row.author)},${escapeCsv(row.objective)},${escapeCsv(row.methodology)},${escapeCsv(row.findings)},${escapeCsv(row.notes)}\n`;
    });
    
    downloadFile(csv, 'matriks_sintesis_literatur.csv', 'text/csv');
    showToast("Matriks diexport sebagai CSV!", "success");
}

function downloadFile(content, fileName, contentType) {
    const a = document.createElement("a");
    const file = new Blob([content], { type: contentType });
    a.href = URL.createObjectURL(file);
    a.download = fileName;
    a.click();
    URL.revokeObjectURL(a.href);
}
