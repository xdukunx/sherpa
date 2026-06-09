# skripsi arkan

## Halaman 1

SKRIPSI

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

SKRIPSI

PERBANDINGAN METODE DAN IMPLEMENTASI DETEKSI
KERUSAKAN MOBIL BERBASIS CONVOLUTIONAL
NEURAL NETWORK (CNN) DAN TRANSFORMER

ARKAN SYAFIQ AT'TAOY
NIM. 164221062

PROGRAM SARJANA
TEKNOLOGI SAINS DATA
DEPARTEMEN TEKNIK
FAKULTAS TEKNOLOGI MAJU DAN MULTIDISIPLIN
UNIVERSITAS AIRLANGGA
2026

PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 2

Ppap Phi Jangka
900900900026
s00tEBa00

906 tee @ @ 6

ebagai Salah heb ngga

“Arkan Syafig Attaqy

KE FH 00 0
88 A99 a93

2020 o. KU + © @ @ é
>8 oe ee 02
SO 9 OOOO AO


## Halaman 3

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

PERNYATAAN ORISINALITAS SKRIPSI

Saya, Arkan Syafig Ar'tagy, 164221062, penulis Skripsi yang berjudul
Perbandingan Metode dan Implementasi Deteksi Kerusakan Mobil Berbasis
Convolutional Neural Network (CNN) dan Transformer menyatakan bahwa:

1. “Skripsi ini adalah asli dan benar-benar hasil karya saya sendiri, bukan hasil
karya pihak lain dengan mengatasnamakan saya, bukan merupakan hasil
tiruan atau jiplakan (plagiarism) dari karya pihak lain, dan/atau bukan
tulisan yang dibuat dengan kecerdasan buatan.

2. Skripsi ini belum pernah diajukan untuk mendapatkan gelar akademik, baik
di Universitas Airlangga, maupun di perguruan tinggi lainnya.

3. Dalam Skripsi ini tidak terdapat karya atau pendapat yang telah ditulis atau
dipublikasikan orang lain, kecuali secara tertulis dengan jelas dicantumkan
sebagai acuan dengan disebutkan nama pengarang dan dicantumkan dalam
daftar kepustakaan.

Pernyataan ini saya buat dengan sebenar-benarnya, dan apabila dikemudian hari
terdapat penyimpangan dan ketidakbenaran dalam pernyataan ini, maka saya

bersedia menerima sanksi akademik berupa pencabutan gelar yang telah diperoleh

karena karya tulis Skripsi ini, serta sanksi-sanksi lainnya sesuai dengan norma dan
peraturan yang berlaku di Universitas Airlangga.

Surabaya, Maret 2026
Ni
i

Sei
Sbaluxssanatag

Arkan Syafig At'tagy
NIM. 164221062

SKRIPSI PERBANDINGAN METODE DAN ARKAN SYAFIQ ATTAOY


## Halaman 4

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

KETENTUAN PENGGUNAAN SKRIPSI

Ketentuan hak cipta bagi skripsi yang tidak dipublikasikan, terdaftar, tersedia, serta
terbuka untuk umum di Perpustakaan Universitas Airlangga, dimiliki penulis
dengan mengikuti aturan TIKI yang berlaku di Universitas Airlangga. Referensi
kepustakaan diperkenankan dicatat, tetapi pengutipan atau peringkasan hanya dapat
dilakukan dengan seizin penulis dan harus disitasi sesuai dengan kaidah ilmiah.
Memperbanyak atau menerbitkan sebagian atau seluruh skripsi haruslah seizin
Penulis.

Artagy, A. S. (2026). Perbandingan Metode dan Implementasi Deteksi Kerusakan
Mobil Berbasis Convolutional Neural Network (CNN) dan Transformer. Skripsi.

Surabaya: Universitas Airlangga.

Artagy, A. S. (2026). Comparison of Methods and Implementation of Car Damage
Detection Based on Convolutional Neural Network (CNN) and Transformer.

‘Undergraduate Thesis. Surabaya: Universitas Airlangga.

iv,
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 5

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

KATA PENGANTAR

Puji syukur saya panjatkan ke hadirat Allah SWT yang telah melimpahkan
rahmat, hidayah, serta kemudahan sehingga saya dapat menyelesaikan naskah
skripsi yang berjudul “Perbandingan Metode dan Implementasi Deteksi Kerusakan
Mobil Berbasis Convolutional Neural Network (CNN) dan Transformer” ini dengan
baik. Skripsi ini disusun sebagai langkah awal untuk melanjutkan penelitian yang
merupakan syarat dalam menyelesaikan studi di Program Studi Teknologi Sains
Data.

Pada kesempatan ini, penulis ingin menyampaikan rasa terima kasih kepada:

1. Orang tua tercinta, yang selalu memberikan kasih sayang, dukungan moral,
spiritual, dan materiil sepanjang perjalanan akademik saya. Doa mereka
menjadi pendorong utama yang menguatkan saya untuk mencapai tahap ini

2. Bapak Dr. Aziz Fajar, S.Kom., M.Kom. selaku Dosen Pembimbing T dan Tbu
Dr. Maryamah, S.Kom. selaku Dosen Pembimbing TI, yang dengan sabar dan
penuh keikhlasan telah memberikan bimbingan, arahan, serta masukan yang
sangat berarti selama penyusunan skripsi ini. Saya sangat bersyukur bisa
mendapatkan bimbingan dari Bapak dan Ibu sekalian.

3. Seluruh Dosen Program Studi Teknologi Sains Data, yang telah memberikan
ilmu pengetahuan serta wawasan yang menjadi landasan penting dalam
penyusunan skripsi ini.

4. Tbu Indah Fahmiyah, S.Si., M.Stat. selaku Dosen Wali yang membimbing
saya selama masa perkuliahan di Teknologi Sains Data Universitas Airlangga.

5. Angkatan 22 Teknologi Sains Data “Devaskara”, yang telah menjadi keluarga
“akademik saya selama masa perkuliahan. Kebersamaan dan dukungan mereka
sangat membantu dalam penelitian ini, baik dalam akademik maupun non
akademik.

6. Teman-teman terdekat “AREX GRUP BELAJAR”, yang selalu memberikan
semangat, motivasi, serta bantuan dalam penyusunan skripsi ini

Penulis menyadari bahwa skripsi ini masih jauh dari kata sempurna. Oleh
karena itu, segala kritik dan saran yang membangun sangat penulis harapkan untuk
penyempurnaan penelitian ini kedepannya. Semoga skripsi ini dapat memberikan
manfaat dan menjadi langkah awal menuju keberhasilan penelitian yang akan
penulis jalani.

Surabaya, Maret 2026

Penulis

yy.
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 6

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

ABSTRAK

PERBANDINGAN METODE DAN IMPLEMENTASI DETEKSI
KERUSAKAN MOBIL BERBASIS CONVOLUTIONAL NEURAL
NETWORK (CNN) DAN TRANSFORMER

Oleh
Arkan Syafig Atagy
NIM: 164221062
Program Sarjana Teknologi Sains Data

Deteksi kerusakan kendaraan berbasis citra menjadi topik yang relevan dalam
mendukung proses inspeksi pada industri pembiayaan, asuransi, dan perawatan
otomotif. Penilaian manual yang mengandalkan observasi visual berpotensi
menimbulkan ketidakkonsistenan serta memerlukan waktu yang relatif lebih lama.
Penelitian ini bertujuan untuk membandingkan kinerja arsitektur berbasis
Convolutional Neural Network (CNN) dan Transformer dalam mendeteksi
kerusakan kendaraan, serta mengimplementasikan model terbaik dalam bentuk
prototipe aplikasi web. Eksperimen dilakukan menggunakan dataset Car Damage
Detection (CarDD) enam kelas kerusakan. Dua pendekatan state-of-the-art
dibandingkan, yaitu YOLOY9 sebagai representasi CNN satu tahap dan RT-
DETRv2 sebagai representasi Transformer end-to-end. Evaluasi kinerja dilakukan
menggunakan metrik precision, recall, dan mean Average Precision (MAP), serta
latensi inferensi untuk menganalisis trade-off antara akurasi dan efisiensi
komputasi. Hasil penelitian menunjukkan bahwa pendekatan berbasis CNN,
khususnya YOLOV9-C, menghasilkan performa mAPS0-95 tertinggi sebesar
0,5840 pada data uji dan menunjukkan keseimbangan yang lebih baik antara akurasi
dan latensi dibandingkan RT-DETRv2. Temuan ini mengindikasikan bahwa
karakteristik kerusakan kendaraan pada dataset CarDD yang didominasi detail
spasial lokal lebih sesuai dengan mekanisme ekstraksi fitur konvolusional
dibandingkan pemodelan konteks global berbasis Transformer. Model terbaik
selanjutnya diintegrasikan dalam prototipe aplikasi weh dan dievaluasi
menggunakan System Usability Seale (SUS), dengan skor rata-rata 81,55 yang
termasuk kategori Acceptable (Grade B). Penelitian ini memberikan kontribusi
berupa evaluasi komparatif head-to-head antara YOLOV9 dan RT-DETRV2 pada
dataset CarDD serta pemetaan kompromi akurasi dan efisiensi untuk skenario
implementasi berbasis web.

Kata Kunci: Deteksi Kerusakan Mobil, Deteksi Objek, YOLOv9, RT-DETRv2,
Deep Learning.

ti
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 7

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

ABSTRACT

COMPARISON OF METHODS AND IMPLEMENTATION OF CAR
DAMAGE DETECTION BASED ON CONVOLUTIONAL NEURAL
NETWORK (CNN) AND TRANSFORMER

By
Arkan Syafiq At'tagy
Student ID Number: 164221062
Undergraduate Program in Data Science Technology

Image-based car damage detection has become increasingly relevant in supporting
inspection processes within financing, insurance, and automotive service industries.
‘Manual assessment relying on visual observation may lead to inconsistencies and
requires relatively longer inspection time. This study aims to compare the
performance of Convolutional Neural Network (CNN) and Transformer-based
architectures for car damage detection, as well as to implement the best-performing
‘model in a web-based prototype application. Experiments were conducted using the
six-class Car Damage Detection (CarDD) dataset. Two state-of-the-art approaches
were evaluated: YOLOV9 as a representative one-stage CNN-based detector and
RT-DETRv2 as a Transformer-based end-to-end detection model. Model
performance was assessed using precision, recall, and mean Average Precision
(MAP), along with inference latency to analyze the trade-off between accuracy and
computational efficiency. The results indicate that the CNN-based approach,
particularly YOLOv9-C, achieved the highest mAPSO-95 score of 0.5840 on the
test set and demonstrated a more balanced trade-off between accuracy and latency
compared to RT-DETRY2. These findings suggest that the damage characteristics
in the CarDD dataset, which are dominated by fine-grained local details, are more
effectively captured by convolutional feature extraction mechanisms than by global
context modeling in Transformer-based architectures. The selected model was
subsequently integrated into a web-based prototype and evaluated using the System
Usability Scale (SUS), achieving an average score of 81.55, categorized as
Acceptable (Grade B). This study contributes a head-to-head comparative analysis
between YOLOY9 and RT-DETRV2 on the CarDD dataset and provides empirical
insights into the accuracy-efficiency trade-off for web-based deployment scenarios.

Keywords: Car Damage Detection, Object Detection, YOLOv9, RT-DETRv2,
Deep Learning.

xii
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 8

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

DAFTAR ISI

HALAMAN JUDUL . i
LEMBAR PENGESAHAN
PERNYATAAN ORISINALITAS SKRIPSI.
KETENTUAN PENGGUNAAN SKRIPSI.
KATA PENGANTAR.

DAFTAR GAMBAR.
DAFTAR LAMPIRAN.

BAB I PENDAHULUAN. 1
1.1 Latar Belakang... zal
12 Rumusan Masalah 26
13 Tujuan Penelitian . 86
1.4 Manfaat Penelitian s1
1.5 Batasan Masalah 29
BAB IT TINJAUAN PUSTAKA. 8
2. Penelitian Terkait ......... 18
2.2 Dasar Teori.. .10
2.2.1 Car Damage. .10
2.2.2 Dataset Car Damage Detection (Cad). ul
2.2.3 Data Preprocessing si 1 .13
2.24 Object Detection . 2
223 Convolutional Neural Network ew. .19
2.2.6 You Only Look Once (YOLO) oo... .21
2.2.7 Transformer... 225
2.2.8 Real-Time Detection Transformer RT. ‘DETR) .27
2.2.9 Loss Funetion....... .30
2.2.10 Hyperparameter Tuning... .33
2.2.11 Metrik Evaluasi Model. .38

2.2.12 Sofiware Development Life Cyele (SDLC)
BAB IIT METODOLOGI
34 Lokasi dan Waktu
32 Data dan Alat .
33 Cara Kerja... !

3.3.1 Data Collection......

3.3.2 Data Splitting...

3.3.3 Data Preprocessing

3.3.4 Model Training ...

3.3.3 Model Performance Evaluation.

3.3.6 Web App Implementation ......
BAB IV HASIL DAN PEMBAHASAN.
Al Data Collection ......

iii
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 9

SKRIPSI

42
43
44

45

46

47

BAB V KESIMPULAN DAN SARAN,

54
52

DAFTAR PUSTAKA.
LAMPIRAN.

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Data Splitting cnc...
Data Preprocessing...
Model Training ...
4.4.1 YOLOv9
44.2 RT-DETRV2.
Model Performance Evaluation
4.5.1 Analisis Perbandingan Model Terbaik.
4.5.2 Analisis Pareto Frontier.....
Web App Implementation sc...
4.6.1 Pengembangan Prototipe ....
4.6.2 Evaluasi Prototipe. :

Diskusi .

Kesimpulan
Saran,

ix,
PERBANDINGAN METODE DAN.

ARKAN SYAFIQ ATTAOY


## Halaman 10

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

DAFTAR TABEL
Tabel 2.1 Tabel Penelitian Terkait: 8
Tabel 2.2 Varian YOLOV9.. 24
Tabel 23 Varian RT-DETRV2.. .30
Tabel 24 Pertanyaan System Usability Scale (SUS) 43
Tabel 3.1 Deskripsi Data......... .46
Tabel 3.2 Deskripsi Library Penelitan. .47
Tabel 3.3 Kriteria Augmentasi Data. .50
Tabel 3.4 Arsitektur YOLOV9 . .51
Tabel 3.5 Tipe Model YOLOV yang Diuji 1 .52
Tabel 3.6 Hyperparameter Tuning Model YOLOv9 .52
Tabel 3.7 Arsitektur RT-DETRY2......... .53
Tabel 3.8 Tipe Model RT-DETRv2 yang Diu i 53
Tabel 3.9 Hyperparameter Tuning Model RT-DETRY? ... 53
Tabel 3.10 Kebutuhan Fungsional Prototip . 56
Tabel 3.11 Tabel Rancang Uji Black Box. .61
Tabel 3.12 Rancangan Kuesioner System Usability Scale (SUS). .62
Tabel 4.1 Jumlah Citra dan Instance Kerusakan pada Subset Dataset CarDD..... 64
Tabel 4.2 Statistik Jumlah Bounding Box per Citra pada Dataset CarDD.......... 66
Tabel 4.3 Hasil Baseline Model untuk YOLOv9-S . .69
Tabel 4.4 Hasil Hyperparameter Tuning dengan Optuna untuk YOLONS.S...... 69
Tabel 4.5 Hasil Baseline Model untuk YOLOY9-M... el

Tabel 4.6 Hasil Hyperparameter Tuning dengan Optuna untuk YOLOV9-M... 71
Tabel 4.7 Hasil Baseline Model untuk YOLO¥9-C.... 73
Tabel 48 Hasil Hyperparameter Tuning dengan Optuna untuk YOLOv9-C..... 74
Tabel 4.9 Hasil Baseline Model untuk RT-DETRW2-S ..... .76
Tabel 4.10 Hasil Hyperparameter Tuning dengan Optuna untuk RT-DETRV2-8 76
Tabel 4.11 Hasil Baseline Model untuk RT-DETRV2-M... .78
Tabel 4.12 Hasil Hyperparameter Tuning dengan optuna untuk RT-DETR2.M78
Tabel 4.13 Hasil Baseline Model untuk RT-DETRV2-L .. .80
Tabel 4.14 Hasil Hyperparameter Tuning dengan Optuna untuk RT-DETRV2-L 80
Tabel 4.15 Ringkasan Performa Model Terbaik YOLOv9 dan RT-DETRv2...... 82
Tabel 4.16 Distribusi Error Instance pada Data Test... .86
Tabel 4.17 Distribusi Ukuran Objek pada Data Tes ........ .88
Tabel 4.18 Hasil Pengujian Black Box System Pada Prototipe Aplikasi .97

x,
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 11

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

DAFTAR GAMBAR

Gambar 2.1 Contoh Jenis Kerusakan Kendaraan...
Gambar 2.2 Contoh Citra Kerusakan dari Dataset CarDD ...
Gambar 2.3 Tlustrasi Augmentasi HSV atau ColorJiter.........
Gambar 2.4 Tlustrasi SealeJitter melalui Multi-Seale Resizing...
Gambar 2.5 Deteksi Objek dengan Satu atau Lebih Objek ..
Gambar 2.6 Proses Konvolusi 2D...
Gambar 2.7 Lapisan Convolutional Neural Network (CNN)...
(Gambar 2.8 Sistem Deteksi Objek dengan YOLOvI Skema Grid 7x7.
Gambar 2.9 Tlustrasi PGI...
Gambar 2.10 Tlustrasi GELAN .......
Gambar 2.11 Arsitektur YOLOV9....
Gambar 2.12 Arsitektur Dasar Transformer.
Gambar 2.13 Skema Detection Transformer (DETR).. va
Gambar 2.14 Overview Real-Time Detection Transformer (RT-DETR)...
Gambar 2.15 Struktur Varian Encoder
Gambar 2.16 Blok fusi CNN-based Cross-seale Feature Fusion (CCFF) .
Gambar 2.17 Arsitektur RT-DETRv2 dengan Denoising Task On
Gambar 2.18 Perbandingan 12 Loss dan IoU Los
Gambar 2.19 Siklus Prototipe
Gambar 2.20 Black Box Testing...
Gambar 2.21 Skoring pada System Usability Seale (SUS) .
Gambar 3.1 Cara Kerja Penelitian ..
Gambar 3.2 Cara Kerja Sistem...
Gambar 3.3 Halaman Utama...
Gambar 3.4 Halaman Daftar Kelas Kerusakan.
Gambar 3.5 Halaman Deteksi Kerusakan ....... :
Gambar 4.1 Contoh Citra Dataset CarDD dengan Anotasi Bounding Bor...
Gambar 4.2 Distribusi Jumlah Citra per Split Dataset.
Gambar 4.3 Distribusi Jumlah Instance per Split Dataset.
Gambar 4.4 Distribusi Jumlah Instance per Kelas.
Gambar 4.5 Contoh Hasil Penerapan Data Augmentation pada Citra CarDD.
Gambar 4.6 Kurva Hasil Pelatihan Model YOLOv9-S
Gambar 4.7 Kurva Hasil Pelatihan Model YOLOv9-M..
Gambar 4.8 Kurva Hasil Pelatihan Model YOLOv9-C.
Gambar 4.9 Kurva Hasil Pelatihan Model RT-DETRY2-5.......
Gambar 4.10 Kurva Hasil Pelatihan Model RT-DETRV2-M.....
Gambar 4.11 Kurva Hasil Pelatihan Model RT-DETRY2-L..
Gambar 4.12 Confusion Matrix YOLOVI-C woo...

xi
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 12

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Gambar 4.13 Confusion Matrix RT-DETRV2-L
Gambar 4.14 Contoh Kesalahan Prediksi YOLOv9-C pada Data Uji
Gambar 4.15 Pareto Frontier antara mAP50-95 dan Latensi Inferensi
Gambar 4.16 Tampilan Halaman Utama Prototipe
Gambar 4.17 Tampilan Halaman Daftar Kerusakan Prototipe.......
Gambar 4.18 Tampilan Halaman Prediksi Kerusakan Prototipe .....
Gambar 4.19 Tampilan Halaman Prediksi Setelah Mengunggah Gambar
Gambar 4.20 Tampilan Halaman Prediksi Setelah Mendeteksi Gambar..
Gambar 4.21 Contoh Implementasi Sistem Inspeksi Kerusakan Kendaraan.

xii
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 13

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

DAFTAR LAMPIRAN

Lampiran 1. Hasil Hyperparameter Tuning untuk YOLOV9-S...
Lampiran 2. Hasil Hyperparameter Tuning untuk YOLOv9-M.
Lampiran 3. Hasil Hyperparameter Tuning untuk YOLOV9-C..
Lampiran 4. Hasil Hyperparameter Tuning untuk RT-DETRV2-S
Lampiran 5. Hasil Hyperparameter Tuning untuk RT-DETRV2-M...
Lampiran 6. Hasil Hyperparameter Tuning untuk RT-DETRV2-L.
Lampiran 7. Hasil Form System Usability Seale (SUS).
Lampiran 8. Hasil Perhitungan System Usability Seale (SUS).

13
114
15
116
117
118
119
120

aii
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 14

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

BABI
PENDAHULUAN

11 Latar Belakang

Industri otomotif Indonesia mencatat pertumbuhan sebesar 10,26%
pada kuartal tiga 2022, melampaui laju pertumbuhan ekonomi nasional
sebesar 5,72% (Kementerian Koordinator Bidang Perekonomian Republik
Indonesia, 2022). Pasar otomotif Indonesia pada 2024 tercatat sebagai yang
terbesar di ASEAN dengan 791.476 unit penjualan pada Januari hingga
November dan 725.173 unit produksi pada Januari hingga September
(ASEAN Automotive Federation, 2024). Data domestik tahun 2025
menunjukkan 500.951 unit wholesales dan 435.404 unit produksi untuk
periode Januari hingga Agustus (GATKINDO, 2025a: GAIKINDO, 2025b).

Pertumbuhan pesat industri otomotif tersebut mencerminkan
meningkatnya mobilitas masyarakat dan kebutuhan terhadap kendaraan
bermotor, yang secara langsung diikuti oleh bertambahnya kebutuhan layanan
pascaproduksi dan inspeksi kendaraan. Ekosistem otomotif modem
menempatkan inspeksi kendaraan sebagai sarana untuk memastikan
keselamatan, kesesuaian spesifikasi, serta mengurangi risiko cacat
tersembunyi yang dapat menimbulkan biaya garansi atau keluhan purnajual.
Inspeksi juga berfungsi sebagai dasar objektif bagi proses lain seperti klaim
asuransi, valuasi kendaraan bekas, dan layanan bengkel (Hasan dkk., 2025;
Pérez-Zarate dkk., 2024). Pada praktik inspeksi kendaraan berbasis citra,
pengguna umumnya diminta untuk mendokumentasikan empat sisi
kendaraan, yaitu tampak depan, belakang, kanan, dan kiri, agar pemeriksaan
eksterior bersifat menyeluruh. Fungsi inspeksi tidak hanya berfokus pada
identifikasi kerusakan, tetapi juga pada penilaian umum terhadap kondisi
eksterior kendaraan untuk memastikan kelayakan dan konsistensi hasil
evaluasi (Pérez-Zarate dkk., 2024; X. Wang dkk., 2023).

Di sisi lain, praktik inspeksi konvensional masih didominasi oleh

observasi visual manual menggunakan foto atau pengamatan langsung.

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 15

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Metode ini memerlukan waktu yang relatif lama, sangat bergantung pada
pengalaman dan subjektivitas pemeriksa, serta berpotensi menghasilkan
penilaian yang tidak konsisten antarindividu (Pérez-Zarate dkk, 2024: Sarath
dkk, 2020: X. Wang dkk., 2023). Ketidakkonsistenan tersebut meningkat
pada penilaian kerusakan ringan seperti goresan, retakan halus, atau penyok
kecil, terutama jika pencahayaan dan sudut pengambilan gambar bervariasi
(Sarath dkk, 2020; X. Wang dkk, 2023). Kondisi ini menuntut inovasi sistem
yang mampu membantu proses pemeriksaan secara objektif, efisien, dan
seragam antarpengguna. Selain memerlukan waktu yang relatif lama, proses
inspeksi manual juga menimbulkan biaya operasional yang signifikan karena
membutuhkan tenaga abli terlatih serta prosedur verifikasi berulang, terutama
(pada industri asuransi dan layanan purna jual kendaraan. Variasi pengalaman
dan persepsi antar pemeriksa dapat menyebabkan ketidakkonsistenan hasil
penilaian kerusakan, yang berpotensi memicu perbedaan estimasi biaya
perbaikan maupun sengketa klaim. Ketidakefisienan proses inspeksi juga
dapat meningkatkan biaya operasional perusahaan, seperti biaya tenaga kerja,
biaya inspeksi ulang, serta potensi keterlambatan proses klaim yang
berdampak pada kepuasan pelanggan. Permasalahan tersebut menjadi
semakin kompleks ketika jumlah kendaraan yang harus diperiksa meningkat,
sehingga metode inspeksi manual menjadi kurang skalabel dan berpotensi
menurunkan efisiensi operasional secara keseluruhan.

Kebutuhan akan penilaian berbasis citra membuka peluang penerapan
computer vision dan deep learning untuk mendeteksi kerusakan kendaraan
secara otomatis, cepat, dan objektif (Hasan dkk, 2025: X. Wang dkk., 2023).
Dalam penelitian, ketersediaan dataset beranotasi seperti Car Damage
Detection (CarDD) menjadi prasyarat penting untuk evaluasi yang adil
antarmodel. Dataset ini memuat 4.000 citra dengan rata-rata resolusi sekitar
684.231 piksel dan lebih dari 9.000 instance pada enam kelas kerusakan,
sehingga relevan untuk pengujian model deteksi multiobjek berbasis citra di
skenario dunia nyata (X. Wang dkk., 2023). Tantangan utama terletak pada
ukuran objek yang kecil, variasi pencahayaan, pantulan bodi, dan perbedaan

2

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 16

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

sudut pengambilan gambar, yang menuntut arsitektur peka terhadap detail
lokal sekaligus konteks global citra (Pérez-Zarate dkk., 2024; X. Wang dkk,
2023).

Pendekatan machine learning tradisional seperti Support Vector
Machine, Random Forest, dan K-Nearest Neighbor masih bergantung pada
rekayasa fitur manual yang kurang adaptif terhadap citra kompleks
(Goodfellow dkk., 2016). Sebaliknya, deep learning memungkinkan ekstraksi
fitur otomatis dari tingkat piksel hingga semantik, mempertahankan konteks
lokal dan global, serta mengoptimalkan pelokalan dan klasifikasi secara
bersamaan. Pembelajaran end-to-end dengan dukungan GPU menjadikan
inferensi dapat dilakukan hampir secara real-time (LeCun dki, 1989).
Perkembangan deep learning mendorong munculnya arsitektur
Convolutional Neural Network (CNN) yang menjadi fondasi utama dalam
deteksi objek modern karena kemampuannya mengekstraksi fitur spasial
secara hierarkis dan efisien (LeCun dkk., 1989). CNN memungkinkan proses
pelokalan dan klasifikasi dilakukan secara simultan melalui pembelajaran
end-to-end, menjadikannya unggul dalam berbagai aplikasi visual termasuk
identifikasi objek otomotif dan inspeksi berbasis citra (Arkin dkk., 2022).
Salah satu implementasi paling berpengaruh dari pendekatan CNN adalah
model You Only Look Once (YOLO) yang menjadi detektor satu tahap
berkecepatan tinggi. Model ini pertama kali diperkenalkan sebagai
pendekatan real-time yang menggabungkan pelokalan dan klasifikasi dalam
satu jaringan terpadu (Redmon dkk, 2016). Seiring perkembangannya, versi-
versi berikut seperti YOLOv3 hingga YOLOv8 memperkenalkan multi-scale
feature fusion, Cross-Stage Partial Network (CSPNet), dan Efficient Layer
Aggregation Network (ELAN) untuk meningkatkan stabilitas pelatihan serta
efisiensi komputasi.

"Terbaru, YOLOv9 menghadirkan Programmable Gradient Information
(PGI) dan Generalized Efficient Layer Aggregation Network (GELAN) yang
memperbaiki aliran gradien serta utilisasi parameter tanpa mengorbankan
kecepatan inferensi (C.-Y. Wang dkk., 2024). Berdasarkan evaluasi pada

3
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 17

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

dataset MS COCO, YOLOv9 mencatat peningkatan 1-26 MAP dengan
pengurangan hingga 40% Floating Point Operations (FLOPs) dibanding
YOLOV8, menjadikannya representasi CNN satu tahap yang efisien dan
akurat untuk mendeteksi detail kerusakan kendaraan (C.-Y. Wang dkk,
2024). Ramazhan dkk. (2025) mengembangkan varian YOLOV9-CS dengan
modul Convolutional Block Attention Module (CBAM) dan SCYLLA-IoU loss
untuk mendeteksi enam jenis kerusakan mobil pada dataset Car Damage
Detection (CarDD) dan melaporkan peningkatan MAP sebesar 1,75%
dibanding baseline YOLO generasi sebelumnya. Selain itu, implementasi
YOLOV9 banyak digunakan pada sistem inspeksi ringan dan edge devices,
yang menunjukkan efisiensi inferensi pada GPU menengah maupun CPU
modern mosaic (Jocher dkk, 2023). Di sisi lain, model terbaru
memperkenalkan inovasi lanjutan, YOLOVIO dengan pelatihan end-to-end
tanpa NMS, YOLOvI1 dengan blok C3k2/SPPF/C2PSA, dan YOLOvI2
dengan attention-centric, namun hasil evaluasi independen masih beragam
dan bergantung domain serta konfigurasi perangkat keras (Khanam &
Hussain, 2024a; Tian dkk., 2025: Gonzslez-Hernindez dkk., 2025). Pada
dataset HORD, YOLOv9e meraih recall mengungguli model YOLOV8I,
YOLOvIOI, dan YOLOvI1I dan latensi tertinggi kedua setelah model
YOLOVI II (Gonz8lez-Hernindez dkk., 2025).

Sementara itu, pendekatan berbasis Transformer memanfaatkan
mekanisme selfattention dan skala data yang besar sehingga mendorong
kemajuan metode deteksi objek, dengan laporan performa yang pada
sejumlah tolok ukur standar sudah melampaui model CNN (Z. Liu dkk,
2021). Pendekatan Transformer untuk deteksi objek pertama kali
diperkenalkan melalui Detection Transformer (DETR) yang mengubah
proses deteksi menjadi set prediction end-to-end tanpa memerlukan anchor
boxes maupun tahapan Non-Maximum Suppression (NMS) (Carion dkk,
2020). Namun, efisiensi DETR generasi awal masih terbatas akibat
konvergensi lambat dan kompleksitas tinggi. RT-DETRv2 hadir sebagai
pengembangan signifikan dengan memadukan keunggulan backhone

4
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 18

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

convolutional dan mekanisme multi-seale attention untuk mempercepat
inferensi sekaligus mempertahankan akurasi tinggi (Lv dkk., 2024). Model ini
mengimplementasikan dynamic head dan adaptive feature aggregation yang
memungkinkan deteksi multiobjek secara stabil dalam waktu nyata.
Kemampuan tersebut menjadikan RT-DETRv2 relevan untuk konteks
inspeksi kendaraan, karena dapat mendeteksi kerusakan pada area kecil
maupun reflektif secara efisien tanpa kehilangan konsistensi hasil di berbagai
kondisi pencahayaan dan sudut pandang (Zhao dkk., 2024). Selain itu, RT-
DETRv2 menunjukkan keunggulan praktis pada penerapan real-time
detection di lingkungan industri dan otomotif, karena arsitektur end-to-end
tanpa NMS mengurangi Intensi inferensi sekaligus menyederhanakan
integrasi sistem deteksi pada perangkat komputasi modern (Lv dkk., 2024).
Dengan mempertimbangkan karakteristik keduanya, kedua pendekatan
ini sama-sama kuat namun membawa trade-off kinerja yang berbeda pada
tugas deteksi objek. Pertimbangan tersebut mendorong eksplorasi model
state-of-the-art untuk memperoleh peningkatan performa dengan trade-off
yang lebih optimal dibandingkan penelitian terdahulu. Optimalitas pada
penelitian ini didefinisikan sebagai kemampuan model untuk mencapai nilai
mean Average Precision (mAP) yang tinggi dengan waktu inferensi yang
rendah. Representasi state-of-the-art yang saling melengkapi adalah You Only
Look Once v9 (YOLOV9) sebagai CNN satu tahap yang efisien dan teliti pada
detail lokal, serta Real-Time Detection Transformer v2 (RT-DETRv2)
sebagai arsitektur hybrid CNN-Transformer end-to-end dengan
ketergantungan minimal pada NMS (Chua dan Tan, 2025; Lv dkk., 2024; C.-
Y. Wang dkk, 2024; Zhao dkk., 2024). Meskipun berbagai penelitian telah
mengembangkan model deteksi objek berbasis CNN maupun Transformer,
sebagian besar studi hanya berfokus pada peningkatan performa satu
arsitektur tertentu tanpa melakukan evaluasi komparatif secara langsung pada
kondisi dataset dan skenario eksperimen yang sama. Oleh karena itu, masih
terdapat research gap berupa belum adanya komparasi head-to-head antara
YOLOV9 dan RT-DETRY2 pada dataset Car Damage Detection (CarDD)

5

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 19

SKRIPSI

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

enam kelas dengan pelaporan metrik akurasi serta efisiensi inferensi secara
terkontrol. Penelitian komparatif diperlukan untuk memperoleh pemahaman
yang lebih objektif mengenai kompromi performa yang dihasilkan kedua
(pendekatan tersebut.

Berdasarkan research gap tersebut, penelitian ini bertujuan
membandingkan kinerja YOLOv9 dan RT-DETRv2 pada dataset CarDD
enam kelas dengan menilai AP (termasuk mAPS0-9Sdan latensi inferensi
guna memetakan kompromi akurasi-kecepatan. Real-time dalam penelitian
ini merujuk pada implementasi prototipe weh yang menjalankan model
terbaik hasil seleksi pascakomparasi. Evaluasi sistem dilakukan melalui Black
Box Testing dan System Usability Scale (SUS). Kontribusi utama penelitian
mencakup penyediaan baseline kinerja dua model mutakhir, karakterisasi
trade-off akurasi-kecepatan, serta bukti implementatif pada skenario industri
otomotif.

1.2 Rumusan Masalah
Berdasarkan latar belakang, maka rumusan masalah yang diangkat pada

penelitian ini adalah sebagai berikut:

IL Bagaimana proses pembangunan model deteksi kerusakan mobil
menggunakan arsitektur YOLOv9 dan RT-DETRV2?

2. Bagaimana perbandingan performa YOLOv9 dan RT-DETRv2 dalam
mendeteksi kerusakan mobil berdasarkan metrik akurasi dan efisiensi
komputasi?

3. Bagaimana kinerja fungsional dan tingkat usability aplikasi web deteksi
kerusakan mobil menggunakan model terbaik?

13 Tujuan Penelitian
Berdasarkan latar belakang dan rumusan masalah, maka tujuan dari penelitian

yang ingin dicapai adalah sebagai berikut:

IL Membangun model deteksi kerusakan mobil menggunakan arsitektur
YOLOV9 dan RT-DETRY2.

2. Membandingkan performa YOLOv9 dan RT-DETRY2 berdasarkan metrik
akurasi dan efisiensi komputasi

6

PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 20

SKRIPSI

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

3. Mengembangkan prototipe aplikasi web deteksi kerusakan mobil berbasis
‘model terbaik serta mengevaluasi kinerja fungsional dan usability sistem.

1.4 Manfaat Penelitian
Penelitian ini diharapkan dapat memberikan manfaat bagi mahasiswa,

perguruan tinggi, dan masyarakat sebagai berikut:

1. Mahasiswa dapat memahami dan menerapkan Convolution Neural Network
(CNN) serta Transformer untuk deteksi kerusakan eksterior kendaraan
melalui pengalaman riset end-to-end.

2. Perguruan tinggi dapat memperkaya referensi akademik dan pengembangan
kurikulum artificial intelligence dan deep learning berbasis kasus nyata.

3. Bengkel, perusahaan asuransi, dan lembaga pembiayaan kendaraan dapat
memanfaatkan sistem sebagai alat bantu pra-inspeksi untuk meningkatkan
efisiensi, konsistensi, dan transparansi penilaian kerusakan kendaraan.

1S Batasan Masalah
Batasan masalah dalam penelitian ini mencakup beberapa hal berikut:

1. Penelitian ini berfokus pada deteksi kerusakan eksternal kendaraan berbasis
citra digital, tidak mencakup diagnosis kerusakan internal mesin atau
Komponen non-visual.

2. Penelitian ini menggunakan dataset Car Damage Detection (CarDD) yang
disusun berdasarkan citra tunggal (single-view), sehingga setiap citra
diperlakukan sebagai entitas independen tanpa mempertimbangkan relasi

antar-sisi kendaraan.

7

PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 21

SKRIPSI

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

21 Penelitian Terkait

BABIT

TINJAUAN PUSTAKA

Bagian ini meninjau penelitian terdahulu yang relevan dengan topik penelitian

ini. Penelitian-penelitian yang dirujuk dalam Tabel 2.1 telah memberikan kontribusi

signifikan dalam memahami konteks dan isu yang terkait dengan penelitian ini.

Tinjauan literatur yang dirangkum dalam Tabel 2.1 mencakup berbagai pendekatan

dan temuan dari berbagai studi yang sejalan dengan tujuan penelitian yang sedang

dilakukan.
Tabel 2.1 Tabel Penelitian Terkait
No. | Judul dan Pengarang | — Data Metode dan Hasi Relevansi
1 | Smart Car Damage | CaroD YOLOv9-CS Menunjukkan
Assesment Using | (4.000 citra, | (YOLOV9+CBAMHSIaU) | penerapan
Enhanced roro | 9.000 dengan augmentasi warna | YOLOv9 pada
Algorithm and Image | insiance, 6| atau mosaik: precision | dataset” CarDD
Processing Techniques | kelas) 78%, recall 69%, mAPSO | dengan hasil
(Ramazhan, M. Ro S., 73%, mAPSO-95 58%; | lebih — unggul,
Bustamam, A, dan melampaui baseline | penggunaan
Buyung, R.A 2025) YOLOV3-YOLOW, angmentasi
ColorJiter/HSV
dan Brightness
2 | Advances In Atrorafi | Dataset I: | Perbandingan YOLOW9 va | Menunjukkan
Skin Defect Detection | 083 — citra | RT-DETR; optimasi | perbandingan
Using Computer Vision: | (Boeing 727, Bayesian (29 | tangsung
4 Survey and | drone Parrot | hyperparameter) YOLOv9 dan
Comparison of YOLOv9| Bebop, 3 | YOLOV9: — precision | RT-DETR pada
and RT-DETR | kelas 0,786; recall” 0,720; dataset nyata:
Performance defect), MAPSO 0,730; ~66 FPS. | penggunaan
(Suvittawat, N,| Dataset 11 | RT-DETR: precision | Mperparameter
Kumiawan, C,|10722 ciwa | 0,777; recatt 07015 | tuning yang
Datephanyawat, 3, Tay, | (5 kelas | mAPSO 0,710; | berpengaruh
L, Lin, Z, Soh, D. W, | defeet) 'konvergensi lebih cepat. “| terhadap akurasi
dan Ribeiro, N. A, dan trade-off
2025) speed vs
3 | RealTime Image Cityscapes, | Arsitektur hybrid CNN- | Penggunaan
Segmewtation via| ADE20K ” | Transformer: — optimasi | Pareto Frontier
Hybrid Convolutional- mutti-objektif (Pareto). | untuk evatuasi
Transformer Cityscapes: 71496 mIOU | trade-off’ akurasi
Architecture Searoh @ 71 FPS; ADE20K: | dan kecepatan
(HyCTAS) (Yu, HL, 48,6% mloU @ 64 FPS;
Wan, C., Dai, X, Liu, berada pada Pareto-
M., Chen, D., Xiao, B., optimal.
Huang, Y,, Lu, ¥. dan
Wang, L., 2025)

8

PERBANDINGAN METODE DAN.

ARKAN SYAFIQ ATTAOY


## Halaman 22

SKRIPSI

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

No. | Judul dan Pengarang [Dat Metode dan Hasi Relevansh
a | RT-DETRv2: Improved | MS COCO | Varian model S/M/LIX | Landasan utama
Baseline with Bag-of: | 2017 (ResNet-18/34/50/101). | untuk eksperimen
Freebies for Real-Time | (irainival) | “Bag-ofifteehtes”: RT-DETRV2
Detection Transformer dynamic augmentation, | (SIMILIX) di
(ly, W., Zhao, Y., seale-adaplive penefitiannmu;
Chang, Q., Huang, K., foperparameters, dan | televan untuk
Wang, G., dan Liu, Y., diserete sampling untuk | desain augmentasi
2024) mengganti grid sample. | dinamis dan
Hasil (val, — 640°, | penyetetan skala,
‘TensorRT FP16 TA): RT-
DETRY2X (R101)
AP-5435  APS0-72K:
FPS-T4. Peningkatan
103 2d #14 AP vs RT-
DETR pada berbagai
skala tanpa kehilangan
‘kecepatan,

3 | VOLO: Learning | MS COCO] Varian SIMIGIE: | Penggunaan
What You Want to | 2017 Programmable Gradient | varian YOLOY9-
Learn Using Information; augmentasi |S, M, C, E,
Programmable ‘mosaic, mixup, copy: | penggunaan
Gradient Information paste, HSV, | angmentasi HSV
(Wang, C-Y,, Yeh, 1 translas/skala. YOLOV9- | serta Translation,

iao, H-Y. M, E: MAPSO 55,6%; APSO | dan Seale, sena
72.8%; inferensi ~11,5 | evaluasi irade-off
ms: lebih efisien dari | akurasi dan
YOL0vs-x. kecepatan

© | GroundingCarDD: | CaDD + | GroundingCarDD (Swin | Menggunakan
Text-Guided dataset * BERT, integrasi | dataset” CarDD
Multimodal _ Phrase | privat SAM2) versus | dan
Grounding for Car| digabung | DETR/Detectron2/GL1P/ | membandingkan
Damage “Detection | jadi DCNHYOLOV?. Di | langsung:
(Hasan, M. L, Nalwan, | es cardd | CarDD: mAPS0-95 65%, | YOLOV9 dengan
A, Ong, K-L., Jahani, | (8304 cita) | recall 86,796, APSO 80, | metode
HL, Boo, Y. L., Nguyen, APTS. 689; di atas | Transformer
KC, dan Hasan, M YOLOv9 (MAP 60,614). | multimodal
2024)

7 | CarDD: A New Dataset | CaDD Benchmark Mask R-| Dataset utama
for Vision-Based Car | (4.000 citra, | CNN, Cascade, GCNet, | yang — digunakan
Damage Detection | 9.000 HTC, DCN, DCN*. | dalam penelitian
(Wang, X., Li, W., dan | instance, 6 | Terbaite DCN (ResNet- | ini, baseline untuk
Wu, Z.,2023) kelas) 101) dengan APbbox | perbandingan

60676 dan Mask Ap | CNN vs
55.7%, Transformer

& | Automated Detection of | Dataset Transfer learning CNN | Penggunaan
Mult-Class Vehicle | custom 5.117 | (MobileNet, VGG19) + | metode
Exterlor Damages | citra angmentasi angmentasi yaitu
using Deep Learning | dipertuas | rotation/shearfcoomiip; | Rotation,
(Heenaye-Mamode | dengan MobileNet: akurasi latih | Shear/Zoom,
Khan, M., Sk Heerah, | augmentasi | 79,21%, validasi 702654. | Horizontal Flip)

MZ. IL, dan Basgeeth
Z.,2021)

9

PERBANDINGAN METODE DAN.

ARKAN SYAFIQ ATTAOY


## Halaman 23

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Berdasarkan penelitian yang relevan tersebut, arsitektur neural network yang
digunakan berbasis Convolutional Neural Network (CNN) dan Transformer. Pada
basis CNN digunakan YOLOv9 dengan varian S, M, dan C. Pada basis Transformer
digunakan RT-DETRV2 dengan backbone ResNet-50 dan ResNet-101 serta varian
S, M, dan L. Dataset yang digunakan adalah Car Damage Detection (CarDD).
Augmentasi data yang digunakan meliputi RandomHforizontalPlip, HSV atau
ColorJiter, RandomAffine, RandomPerspective, ScaleJiter, serta Gaussian atau
MotionBlur. Evaluasi dilakukan menggunakan mean Average Precision (mAPSO
dan mAPS0-95) serta frames per second (FPS) dengan analisis Pareto Frontier
‘untuk menilai keseimbangan antara akurasi dan latensi.

2.2 Dasar Teori

Bab ini menjelaskan konsep dan model yang menjadi dasar penelitian.
Pembahasan dimulai dengan uraian mengenai car damage serta dataset Car
Damage Detection (CarDD) sebagai sumber data utama penelitian. Teknik data
preprocessing dan data augmentation dipaparkan untuk menunjukkan cara
peningkatan keragaman data train. Bagian berikutnya memaparkan teori object
detection, arsitektur Convolutional Neural Network (CNN) sebagai dasar YOLOV9,
serta arsitektur Transformer yang melandasi Real-Time Detection Transformer v2
(RT-DETRV2). Uraian berlanjut pada fungsi Joss yang digunakan selama pelatihan,
strategi hyperparameter tuning untuk optimasi performa, dan metrik evaluasi yang
mengukur hasil deteksi. Paragraf penutup memaparkan pengembangan prototipe
sistem berbasis Streamlit serta metode pengujian Black Box Testing dan System
Usability Seale (SUS) untuk menilai fungsionalitas dan kegunaan sistem.

2.2.1 Car Damage

Kerusakan kendaraan (car damage) mencakup beragam bentuk seperti
penyok, gores, retak, kaca pecah, lampu rusak, dan ban kempis yang timbul akibat
benturan, gesekan, kegagalan komponen, atau faktor lingkungan. Kategori tersebut
lazim digunakan sebagai taksonomi kerja pada penilaian kerusakan bodi maupun
Komponen eksternal kendaraan (Pérez-Zarate dkk., 2024; X. Wang dkk, 2023).
Dengan penggunaan istilah yang konsisten, identifikasi jenis kerusakan menjadi
lebih terstandar pada proses dokumentasi dan pelaporan (Hasan dkk, 2025).

10

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 24

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Contoh visual dari enam kategori kerusakan kendaraan tersebut ditampilkan pada
Gambar 2.1 untuk memperjelas perbedaan karakteristik antar kelas kerusakan.

@

Gambar 2.1 Contoh Jenis Kerusakan Kendaraan, (a) Serateh, (b) Dent, (€) Crack
‘Sumber: (Hasan dit, 2025)

Secara operasional, penilaian kerusakan memiliki peran penting dalam klaim
asuransi, inspeksi bengkel, dan manajemen armada karena menentukan keputusan
(perbaikan serta estimasi biaya. Prosedur manual berbasis observasi visual rentan
terhadap subjektivitas penilai, variasi kondisi pencahayaan atau sudut pandang, dan
keterbatasan waktu ketika volume kendaraan tinggi. Kondisi ini dapat memicu
ketidakkonsistenan antar kasus dan memperlambat turnaround layanan (Hasan
dkk, 2025; Vanathi dkk, 2025).

Dalam praktiknya, alur penilaian kerusakan mencakup pencatatan identitas
kendaraan dan dokumentasi foto, pemeriksaan per panel untuk menentukan tipe,
lokasi, serta pengukuran tingkat kerusakan. Hasil pemeriksaan kemudian dipetakan
ke kebutuhan perbaikan dan estimasi biaya, dengan menekankan keterlacakan
keputusan serta kesesuaian dengan pedoman yang berlaku. Karena proses ini masih
sangat bergantung pada observasi manual, muncul tantangan berupa yariasi antar
penilai, sensitivitas terhadap kondisi pencahayaan dan sudut pandang, serta
keterbatasan waktu ketika volume layanan tinggi, sehingga diperlukan prosedur
yang lebih terstandar dan objektif (Hasan dkk, 2025: Vanathi dkk., 2025).

2.2.2 Dataset Car Damage Detection (CarDD)

Car Damage Detection (CarDD) merupakan dataset publik berskala besar
untuk penelitian deteksi dan segmentasi kerusakan kendaraan berbasis computer
vision, dengan tujuan mengatasi keterbatasan dataset terdahulu yang berukuran
kecil, bersifat privat, dan hanya berfokus pada klasifikasi tanpa anotasi spasial.

Dataset ini dirancang agar relevan bagi ekosistem otomotif dan asuransi sehingga

1

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 25

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

dapat digunakan sebagai acuan pengembangan sistem penilaian kerusakan
kendaraan yang objektif dan terukur (X. Wang dkk, 2023). Desain kurasinya
menekankan keberagaman kondisi pengambilan gambar agar model yang dilatih
memiliki ketahanan pada skenario dunia nyata (Shorten dan Khoshgoftaar, 2019;
X. Wang dkk, 2023).

Secara komposisi, dataset CarDD memuat 4.000 citra dengan rata-rata
resolusi sekitar 684.231 piksel dan lebih dari 9.000 instance kerusakan yang
dianotasi dalam enam kategori, yaitu crack (retak), dent (penyok), scratch (gores),
glass shatter (kaca pecah), lamp broken (lampu rusak), dan tire flat (ban kempis).
Resolusi yang tinggi memungkinkan tekstur dan kontur kerusakan terekam dengan
jelas sehingga mendukung anotasi yang presisi serta pengujian model terhadap
objek berukuran kecil (X. Wang dkk, 2023). Setiap citra dalam dataset CarDD
beranotasi dalam format COCO yang mendukung deteksi multiohjek, sehingga satu

gambar dapat memuat lebih dari satu jenis kerusakan secara bersamaan. Penetapan

kategori dan kriteria anotasi dilakukan secara terstandar untuk menjaga konsistensi
dan validitas pelabelan (Shorten dan Khoshgoftaar, 2019; X. Wang dkk., 2023).
Contoh representatif citra dan anotasi kerusakan dari dataset CarDD dapat dilihat
pada Gambar 2.2.

[ed — ed — Pe ea — LG

Gambar 2.2 Contoh Citra Kerusakan dari Dataset CarDD
Sumber: (X. Wang dkk, 2023)

12

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 26

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Pipeline kurasi (pengumpulan citra, seleksi kandidat, deduplikasi, dan
anotasi) dataset CarDD dimulai dari pengumpulan citra melalui Flickr dan
Shutterstock untuk menjamin keragaman sudut pandang serta kondisi pencahayaan.
Tahap berikutnya dilakukan penyaringan kandidat menggunakan binary classifier
berbasis VGG16 agar hanya citra yang benar-benar memuat kerusakan yang
diterima, diikuti proses deduplikasi dan anotasi manual oleh anotator terlatih sesuai
(pedoman penilaian klaim asuransi. Proses anotasi mengikuti aturan prioritas kelas
(crack > dent > serateh) dan penggabungan kerusakan sejenis pada panel yang
sama, namun kerusakan yang berbeda kelas atau berbeda lokasi tetap dicatat
sebagai beberapa instance sehingga selaras dengan kebutuhan deteksi multiobjek di
satu cita (X. Wang dkk, 2023). Penekanan pada keberagaman kondisi
pengambilan serta penyeragaman kriteria anotasi sejalan dengan kebutuhan
evaluasi objektif pada konteks asuransi serta praktik augmentasi modem yang
meniru variasi dunia nyata (Pérez-Zarate dkk., 2024; Shorten dan Khoshgoftaar,
2019).
2.2.3 Data Preprocessing

Pada domain computer vision, data preprocessing merupakan langkah awal
penting untuk meningkatkan akurasi dan efisiensi model sebelum pelatihan. Ukuran
citra lazim diseragamkan ke input tetap, misalnya 640x640 untuk stabilitas
pelatihan detektor real-time, kemudian dinormalisasi agar selaras dengan asumsi
backbone pretrained TmageNet (He dkk, 2016; Lv dkk., 2024: Redmon dan
Tarhadi, 2018; C.-Y. Wang dkk, 2024). Selain itu, data augmentation diterapkan
untuk menambah variasi dan mengurangi bias, khususnya ketika menghadapi
ketimpangan kelas dan banyak instance berukuran kecil pada dataset CarDD
sehingga model lebih tangguh terhadap perubahan skala dan kondisi pencahayaan
yang beragam (Shorten dan Khoshgoftaar, 2019: X. Wang dkk., 2023).
22.3.1 Resize

Goodfellow dkk., (2016) menunjukkan, tensor masukan berukuran tetap
mempermudah batching dan menstabilkan optimisasi pada jaringan konvolusional.
Praktik serupa lazim digunakan pada detektor satu-tahap berbasis CNN maupun
detektor berfondasi Transformer, sehingga ukuran input yang konsisten dipilih

13

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 27

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

sebagai kompromi antara konteks dan biaya komputasi. Rasio aspek dipertahankan
dan distorsi bentuk kerusakan dicegah dengan menerapkan resize, yakni citra
diskalakan secara isotropik hingga sisi terpanjang sesuai bingkai, lalu sisa area diisi
padding. Padding menambah area latar kosong, dan selama pelatihan hal ini umum
dipadankan dengan scale jitter atau multi-scale training agar model lebih tangguh
terhadap variasi ukuran objek dan perubahan field of view. Pada evaluasi dan
inferensi, satu resolusi tetap digunakan untuk menjaga fairness perbandingan
antarmodel pada konfigurasi yang identik (Redmon dkk., 2016; Zhu dkk., 2021).
2.2.3.2 Normalize

Normalisasi diperlukan untuk menyeragamkan rentang intensitas piksel dan
menyelaraskan distribusi input dengan asumsi backbone pralatih sehingga aktivasi
lebih stabil dan konvergensi lebih cepat. Setiap citra terlebih dulu dipetakan ke (0,
1), kemudian dilakukan normalisasi per kanal menggunakan rataan dan simpangan
baku yang konsisten dengan skema pralatih ImageNet pada backbone yang
digunakan. Konsistensi prosedur antara train, validation, dan test penting agar
evaluasi adil antarmodel (Dosovitskiy dkk., 2021; He dkk., 2016). He dkk., (2016)
dan Dosovitskiy dkk, (2021) menunjukkan normalisasi z-score per kanal
didefinisikan pada Persamaan (2.1).

Cl)

Keterangan:
nilai piksel kanal ke-c setelah dipetakan ke [0, 1]

nilai piksel kanal ke-c setelah normalisasi

Hg = mean pralatih ImageNet untuk kanal ke-c

@, = standar deviasi pralatih ImageNet untuk kanal ke-c
indeks kanal

223.3 Data Augmentation

Data augmentation merupakan teknik untuk memperluas dataset secara
buatan melalui transformasi citra tanpa mengubah label dan membantu
meningkatkan generalisasi model. Strategi ini terbukti efektif dalam meningkatkan
'kemampuan generalisasi model serta mengurangi risiko overfitting, terutama ketika

14

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 28

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

ketersediaan data terbatas (Shorten dan Khoshgoftaar, 2019). Krizhevsky dkk,
(2017) memperkenalkan penggunaan augmentasi sederhana seperti random
cropping, horizontal flipping, dan variasi intensitas warna berbasis Principal
Component Analysis (PCA) dalam model AlexNet, yang secara signifikan
menurunkan error rate pada dataset ImageNet. Pendekatan tersebut kemudian
menjadi standar dalam pelatihan Convolutional Neural Network (CNN) berskala
besar.

Seiring perkembangan, teknik augmentasi berevolusi dari transformasi dasar
menuju pendekatan yang lebih kompleks. He dkk., (2016) menunjukkan bahwa
transformasi spasial seperti rotasi dan translasi mampu memperkaya representasi
fitur dalam pelatihan ResNet. Berbagai augmentasi yang meliputi random erasing,
micup, dan adversarial augmentation dirangkum sebagai upaya menyimulasikan
kondisi visual dunia nyata. Random erasing, misalnya, terbukti meningkatkan
ketahanan model terhadap occlusion dengan menghapus sebagian area citra secara
acak tanpa mengubah semantik objek (Shorten dan Khoshgoftaar, 2019).

Selain transformasi geometrik dan fotometrik, integrasi model generatif
semakin memperluas cakupan augmentasi. Penggunaan Generative Adversarial
Networks (GANS) memungkinkan penciptaan sampel sintetis yang realistis dan
beragam, sehingga memperkaya distribusi data pelatihan. Shorten dan
Khoshgoftaar (2019) menyintesis temuan bahwa augmentasi berbasis GAN
meningkatkan sensitivitas dan spesifisitas model klasifikasi citra medis, terutama
(pada domain dengan jumlah data terbatas. Metode berbasis Neural Style Transfer
(NST) serta Autodugment memperkenalkan paradigma meta-learning, di mana
kombinasi augmentasi optimal dipilih secara otomatis berdasarkan performa model
terhadap dataset tertentu (Shorten dan Khoshgoftaar, 2019). Contoh penerapan
transformasi fotometrik melalui pengubahan hue, saturation, dan brightness
ditampilkan pada Gambar 2.3, yang memperlihatkan variasi warna hasil augmentasi
FBSY atau ColorJiter.

15
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 29

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

on 90 engan 620%

Gambar 2.3 Ilustrasi Augmentasi //SV atau ColorJitter
Sumber: (Ramazhan dkk., 2025)

Dalam praktik yang lebih kontemporer pada tugas deteksi objek, kombinasi
transformasi fotometrik (misalnya HSV atau ColorJitter) dan geometrik (misalnya
sealing, translation, mosaic, mixup, copy-paste) kerap digunakan untuk
meningkatkan ketahanan terhadap variasi warna, pencahayaan, tata letak, serta
ukuran objek seringkali dengan pengaturan siklus pelatihan yang menonaktifkan
transformasi agresif pada fase akhir agar konvergensi lebih stabil (C.-Y. Wang dkk.,
2024). Pendekatan lain yang banyak diadopsi adalah dynamic augmentation
sebagai bagian dari bag-of-freebies untuk memperbaiki stabilitas dan efisiensi
pelatihan tanpa menambah biaya inferensi, gagasan ini umum pada detektor modem
yang mengejar real-time (Lv dkk., 2024). Hustrasi variasi skala melalui multi-scale
resizing (scale jitter) menegaskan bagaimana augmentasi memaksa model

menghadapi objek kecil maupun besar (X. Wang dkk., 2023). Efek multi-scale

resi

izing terhadap variasi ukuran objek divisualisasikan pada Gambar 2.4,

“et
=

Gambar 24 Ilustrasi ScaleJitter melalui Muli-Scale Resizing
Sumber: (X. Wang dk, 2023)

16

SKRIPSI PERBANDINGAN METODE DAN... ARKAN SYAFIQ ATTAOY


## Halaman 30

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

2.24 Object Detection

Computer vision adalah cabang ilmu komputer yang mempelajari bagaimana
mesin memperoleh, memproses, dan memahami informasi dari citra atau video
untuk mengekstraksi objek, pola, serta fitur yang relevan. Bidang ini memadukan
konsep pengolahan citra, pengenalan pola, kecerdasan buatan, dan grafika
komputer, dengan tahapan umum meliputi akuisisi citra, praproses, ekstraksi atau
representasi fitur, segmentasi, hingga interpretasi hasil (Voulodimos dkk, 2018;
‘Wiley dan Lucas, 2018). Perkembangan deep learning mendorong peralihan dari
fitur buatan menjadi fitur terpelajar, di mana Convolutional Neural Network (CNN)
menjadi arsitektur dominan untuk tugas klasifikasi, deteksi, dan segmentasi,
sementara teknik augmentasi data berperan penting meningkatkan kemampuan
generalisasi model pada data dunia nyata (Shorten dan Khoshgoftaar, 2019;
‘Voulodimos dkk, 2018).

Walaupun efektif menangkap pola lokal, CNN memiliki keterbatasan dalam
memodelkan dependensi jarak jauh atau konteks global karena proses ekstraksi fitur
dilakukan melalui filter konvolusi yang bekerja pada area terbatas. Keterbatasan ini
mendorong adopsi arsitektur berbasis Transformer dalam computer vision (Khan
dkk, 2022). Melalui mekanisme self-attention, Transformer dan rancangan hybrid
CNN dan Transformer mampu memodelkan relasi spasial secara menyeluruh
sambil tetap efisien, sehingga menjadi paradigma penting dalam deteksi objek
model (Khan dkk, 2022; Voulodimos dkk., 2018). Kelebihan ini melengkapi
kekuatan CNN dalam mengekstraksi fitur lokal sehingga keduanya kerap
dipadukan pada sistem deteksi mutakhir (Khan dkk., 2022).

Deteksi objek adalah tugas inti dalam computer vision yang bertujuan
mengidentifikasi dan menentukan lokasi objek semantik pada citra atau video.
Berbeda dengan klasifikasi citra yang memberikan satu label global, deteksi objek
menghasilkan hounding box dan label kelas untuk setiap objek yang ditemukan
sehingga lebih aplikatif bagi berbagai domain seperti kendaraan otonom,
pengawasan, dan penilaian kerusakan kendaraan. Formulasi ini memungkinkan

inferensi multiobjek pada satu citra dengan keluaran yang terlokalisasi (Diwan dkk.,

17

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 31

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

2023; Voulodimos dkk, 2018). Tlustrasi umum proses deteksi objek tunggal
maupun ganda dalam citra ditunjukkan pada Gambar 2.5.

oom

Gambar 2.5 Dereksi Objek dengan Satu atau Lebih Objek
Sumber: (Diwan dik, 2023)

Secara historis, deteksi objek berawal dari pendekatan sliding window di
mana citra dipindai pada berbagai skala dan rasio aspek (Dalal dkk., 2005; Viola
dkk, 2004; Voulodimos dkk, 2018). Setiap jendela kemudian dievaluasi
menggunakan deskriptor seperti Histogram of Oriented Gradients (HOG) dan
Scale-Invariant Feature Transform (SIFT) sebelum diklasifikasikan. Pendekatan
ini efektif pada masanya, namun mahal secara komputasi dan sensitif terhadap
variasi skala, sudut pandang, serta pencahayaan, sehingga kurang sesuai untuk
kebutuhan real-time (Dalal dkk., 2005: Lowe, 2004; Viola dkk., 2004). Metode
berbasis sliding window efektif pada masanya, tetapi mahal secara komputasi dan
sensitif terhadap variasi skala, sudut pandang, dan pencahayaan sehingga kurang
sesuai untuk kebutuhan real-time (Diwan dkk., 2023; Voulodimos dkk, 2018).
Lompatan besar terjadi dengan hadirnya detektor berbasis CNN yang lazim
dibagi menjadi dua rumpun. Pertama, two stage detectors yang diawali oleh Region
based Convolutional Neural Network (R-CNN), kemudian Fast R-CNN, kemudian
Faster R-CNN yang menghasilkan region proposals terlebih dahulu lalu melakukan
klasifikasi dan regresi kotak pembatas, dengan karakteristik akurasi tinggi tetapi
latensi lebih tinggi (Girshick, 2015: Girshick dkk., 2014; Ren dkk., 2016). Kedua,
one stage detectors seperti Single Shot MultiBox Detector serta You Only Look
Once (YOLO) yang langsung memprediksi kotak dan kelas dalam satu tahap
sehingga arsitektur lebih sederhana dan latensi lebih rendah untuk pemakaian real-
time (Liu dkk, 2016; Redmon dkk, 2016). Pemilihan metode umumnya
mempertimbangkan trade-off antara akurasi dan kecepatan, sementara evolusi

18

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 32

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

arsitektur terbaru menunjukkan peningkatan akurasi pada detektor satu tahap
sambil mempertahankan efisiensi inferensi (Diwan dkk, 2023; Voulodimos dkk.,
2018). Selain metrik evaluasi seperti Intersection over Union (IoU) dan mean
Average Precision (MAP), performa deteksi objek juga sering. dianalisis
berdasarkan ukuran objek karena tingkat kesulitan deteksi dapat berbeda pada
setiap skala objek. Pada protokol evaluasi MS COCO, objek dikelompokkan
menjadi tiga kategori berdasarkan Inas bounding box, yaitu small apabila luas area
kurang dari 32x32 piksel, medium apabila berada pada rentang 32x32 hingga
kurang dari 96x96 piksel, dan large apabila luas area lebih besar atau sama dengan
96x96 piksel (Lin dkk,, 2014). Objek berukuran kecil cenderung lebih sulit
dideteksi karena jumlah piksel yang merepresentasikan objek relatif terbatas,
sehingga informasi spasial dapat berkurang selama proses downsampling pada
jaringan konvolusi. Oleh karena itu, analisis berdasarkan ukuran objek sering
digunakan untuk memahami keterbatasan model dalam mendeteksi objek kecil
yang memiliki detail visual lebih halus dibandingkan objek berukuran besar.

2.2.5 Convolutional Neural Network (CNN)

Convolutional Neural Network (CNN) diperkenalkan sebagai arsitektur
pembelajaran end-to-end yang menghubungkan citra ternormalisasi langsung ke
klasifikasi akhir. Studi awal yang berpengaruh menunjukkan efektivitas CNN
dalam pengenalan digit tulisan tangan menggunakan dataset ZIP USPS dengan
9.298 citra (LeCun dkk., 1989). Prinsip peta-fitur dan pembagian bobot menekan
jumlah parameter sekaligus memodelkan invarian translasi, sehingga efektif dalam
‘mengekstraksi fitur lokal dan membangun representasi hierarkis (O'Shea dan Nash,
2015). CNN beroperasi berdasarkan prinsip matematis konvolusi, yaitu operasi
linier yang melibatkan pergeseran (sliding) kernel di atas citra untuk menghasilkan
peta fitur baru. Operasi ini membedakan CNN dari jaringan saraf tradisional yang
menggunakan perkalian matriks penuh antar lapisan (Goodfellow dkk., 2016).

19

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 33

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

f+) (Mamat

4
4

Gambar 2.6 Proses Konvolusi 2D
‘Sumber: (Goodfellow dit, 2016)

Mekanisme dasar konvolusi dua dimensi pada citra dijelaskan pada Gambar 2.6,
sedangkan bentuk matematisnya ditunjukkan dalam Persamaan (2.2) (Goodfellow

ade, 2016).
kok
YGj)= » » WOn,n)X(@+m,j+n) +b 22)
tee
Keterangan:
X5 citra masukan
W - kemel atau filter
b= dias
Y= peta fitur keluaran
(ij) = koordinat posisi peta fitur
k = setengah ukuran kernel

Secara struktural, CNN tersusun atas beberapa lapisan utama, yakni
convolution layer, activation layer, pooling layer, dan fully connected layer.
Lapisan konvolusi bertanggung jawab mengekstraksi fitur lokal, lapisan aktivasi
menambahkan non-linearitas, sementara pooling layer mereduksi dimensi tanpa
kehilangan informasi penting. Kombinasi lapisan ini memungkinkan CNN
membangun representasi dari fitur sederhana ke kompleks secara bertahap,
sebagaimana ditunjukkan pada Gambar 2.7 (Phung dan Rhee, 2018).

20

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 34

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Connected
comokution ag
input rave. o.
a kes
IT: °
oF
8

\ NM J

Ag
Feature Extraction Classification

Gambar 2.7 Lapisan Convolutional Neural Network (CNN)
‘Sumber: (Phung dan Rhee, 2018)

CNN kini menjadi fondasi utama bagi berbagai arsitektur deteksi objek
modem. Detektor dua tahap seperti Faster R-CNN dan Mask R-CNN menawarkan
akurasi yang tinggi, namun memerlukan sumber daya komputasi yang besar,
sedangkan detektor satu tahap seperti YOLO mengutamakan efisiensi untuk
aplikasi real-time (Girshick dkk., 2014: He dkk., 2016; Redmon dkk., 2016: Ren
dkk, 2016). Karena kekuatan CNN dalam mengekstraksi fitur lokal, pendekatan ini
tetap dominan untuk analisis citra dan menjadi basis bagi beragam variasi arsitektur
kontemporer (Li dkk, 2021).

2.2.6 You Only Look Once (YOLO)

You Only Look Once (YOLO) pertama kali diperkenalkan sebagai pendekatan
deteksi objek end-to-end yang membagi citra menjadi grid, di mana setiap sel
memprediksi bounding box dan probabilitas kelas secara langsung dalam satu
forward pass. Pendekatan satu tahap ini menekankan kesederhanaan pipeline serta
efisiensi inferensi tanpa tahap proposal terpisah, sehingga cocok untuk kebutuhan
real-time (Redmon dkk., 2016). Skema pembagian grid dan prediksi simultan pada
YOLOvI divisualisasikan pada Gambar 2.8.

2 Ren comoltinal nab
2 Nonmos pra

(Gambar 2.8 Sistem Deteksi Objek dengan YOLOVI Skema Grid 7x7
‘Sumber: (Redmon dk, 2016)

21

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 35

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Arsitektur YOLO tersusun dari lapisan konvolusi untuk ekstraksi fitur yang
diikuti fully connected layer guna menghasilkan prediksi bounding box dan
probabilitas kelas secara simultan. Versi awal menggunakan grid 7x7: setiap sel
memprediksi beberapa bounding box dengan lima parameter, yaitu koordinat pusat
(x,y), dimensi (width, height), dan confidence score, sehingga prediksi berlangsung
serentak pada seluruh citra. Meskipun efisien, konfigurasi awal ini memiliki
keterbatasan dalam mendeteksi objek kecil serta kesalahan lokalisasi pada area
dengan kepadatan tinggi (Redmon dkk., 2016). Permasalahan tersebut kemudian
menjadi dasar bagi pengembangan varian berikutnya yang menambahkan
mekanisme anchor dan prediksi multiskala untuk meningkatkan sensitivitas
terhadap objek kecil tanpa menurunkan kecepatan inferensi (Redmon dan Farhadi,
2016, 2018). Pengembangan selanjutnya menghadirkan YOLOv2 atau YOLO9000
yang memperkenalkan dimension clusters untuk anchor serta pelatihan multi-seale
yang membuat prediksi lokasi lebih stabil dan recall objek kecil lebih baik tanpa
mengorbankan kecepatan (Redmon dan Farhadi, 2016). Pada YOLOV3, backbone
Darknet-53 berbasis residual dan prediksi multi-skala berbasis Feature Pyramid
Networks (FPN) mendorong kenaikan akurasi pada beragam ukuran objek sambil
mempertahankan latensi rendah (Redmon dan Farhadi, 2018). Evolusi ini
menguatkan posisi YOLO sebagai detektor satu tahap yang kompetitif pada
berbagai skenario aplikasi (Redmon dan Farhadi, 2016, 2018).

Dalam praktik modem, banyak sistem memulai dari YOLOvS yang
memopulerkan mosaic augmentation, penyesuaian anchor berbasis data, serta
Intropy untuk klasifikasi dan

‘Complete Intersection over Union untuk lokalisasi sehingga generalisasi meningkat

rancangan loss komposit seperti Binary Cro:

dengan biaya inferensi yang tetap efisien (Bochkovskiy dkk, 2020: Jocher dkk,
2022, Zheng dkk., 2019). Penerusnya YOLOV8 mengadopsi kepala deteksi anchor-
free dengan decoupled-head untuk klasifikasi dan regresi serta memanfaatkan
Distribution Focal Loss agar regresi kotak lebih halus di berbagai skala, sehingga
pipeline pelatihan tetap sederhana dan mudah diintegrasikan pada lingkungan
produksi modern yang menggunakan mixup dan mosaic (Bochkovskiy dkk., 2020;
Jocher dkk., 2023; Khanam dan Hussain, 2024b; X. Li dkk, 2020).

22

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 36

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Gambar 2.9 Ilustrasi PGIL
Sumber: (C-Y. Wang dk, 2024)

Salah satu inovasi utama pada YOLOv9 adalah Programmable Gradient
Information (PGI), yaitu cabang bantu bersifat reversible yang berfungsi
menyalurkan gradien secara stabil selama pelatihan. Mekanisme ini membantu
mempertahankan informasi penting ketika jaringan semakin dalam dan
menstabilkan aliran gradien menuju fungsi objektif, sebagaimana divisualisasikan
pada Gambar 2.9. Pendekatan tersebut membuat proses optimisasi lebih terarah
pada fitur yang relevan dengan tugas deteksi objek (C.-Y. Wang dkk., 2024).

ema . ,
oo rs oa
C 0 J = 0 B 5 3)
= ata es
ay | 15 | ee i ran |
a z

(4) CSPNet (64) (ELAN (65)

Gambar 2.10 Ilustrasi GELAN
Sumber: (C-Y. Wang dkk, 2024)

Selain PGI, YOLOv9 juga memperkenalkan Generalized Efficient Layer
Aggregation Network (GELAN), yang dirancang untuk meningkatkan efisiensi
agregasi layer melalui kombinasi ide Cross Stage Partial Network (CSPNet) dan
Efficient Layer Aggregation Network (ELAN). Desain ini menjaga kejelasan jalur
gradien dari awal hingga akhir jaringan dan mempertahankan representasi fitur
yang kaya. Visualisasi skematisnya dapat dilihat pada Gambar 2.10, yang

23

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 37

SKRIPSI

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

memperlihatkan bagaimana struktur GELAN menghasilkan peta fitur yang lebih
informatif untuk mendeteksi objek kecil dan kompleks (C.-Y. Wang dkk., 2024).

ooh a Ta YOLOv9
Architecture

Gambar 2.11 Arsitektur YOLOV9
Sumber: (Hidayatullah dan Tubagus, 2024)

Keseluruhan arsitektur YOLOV9 ditunjukkan pada Gambar 2.11, yang

menunjukkan hubungan antara backbone, neck, dan detection head. Visual tersebut

membantu menandai posisi cabang bantu PGI serta aliran fitur multiskala hingga
tahap prediksi (Hidayatullah dan Tubagus, 2024). Pada inferensi, detection head
memanfaatkan beberapa skala fitur untuk menjaga throughput real-time. Pada
pelatihan, kombinasi GELAN dan PGI membuat fase awal pelatihan lebih stabil
dan laju peningkatan kualitas prediksi lebih konsisten dibanding konfigurasi tanpa
PGI, sehingga konvergensi lebih terarah. Varian model disediakan untuk
menyesuaikan kebutuhan sumber daya dan latensi di lingkungan produksi (C.-Y.
Wang dkk., 2024).

Tabel 2.2 Varian YOLOv9
Tipe Tamiah Parameter dalam juta)
[Yor rT
YOLOW-M OT
YOLOWC 253
YOLOW-E 573
‘Sumber (CY Wang dkk 0217

24
PERBANDINGAN METODE DAN... 'ARKAN SYAFIQ ATTAOY


## Halaman 38

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Tabel 2.2 merangkum varian YOLOv9 (Small (S), Medium (M), Compact (C),
dan Extra Large (B)) beserta ukuran parameternya. Varian S cocok untuk perangkat
tepi karena ringan dan responsif M dan C menyeimbangkan akurasi-latensi untuk
kelas menengah sedangkan E ditujukan bagi skenario dengan sumber daya
komputasi besar. Pemilihan varian dalam penelitian ini difokuskan pada kebutuhan
akurasi tinggi dengan waktu inferensi yang tetap memadai untuk aplikasi real-time,
serasi dengan praktik augmentasi umum seperti HSV, mosaic, dan mixup (C.-Y.
Wang dkk., 2024).
2.2.7 Transformer

Transformer adalah arsitektur jaringan saraf yang dirancang untuk mengatasi
keterbatasan model sekuensial konvensional dalam menangkap ketergantungan

jangka panjang dan memproses urutan secara paralel. Inti mekanismenya adalah

vel(-attention, yang menimbang relevansi antar elemen dalam satu urutan sehingga
model dapat memanfaatkan konteks global tanpa bergantung pada jarak spasial atau
temporal yang berurutan (Vaswani dkk, 2023). Keberhasilan konsep ini
mendorong adopsi Transformer secara luas, termasuk pada computer vision melalui
Vision Transformer yang memformulasikan citra sebagai token lalu memprosesnya
dengan self-atention (Dosovitskiy dkk., 2021).

Gambar 2.12 Arsitektur Dasar Transformer
Sumber: (Vaswani dik, 2023)

25

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 39

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Struktur umum Transformer yang terdiri dari encoder dan decoder
diperlihatkan pada Gambar 2.12. Encoder memproyeksikan masukan menjadi
representasi semantik melalui tumpukan blok multi-head self-attention yang diikuti
feed-forward network, lengkap dengan residual connection dan layer normalization
untuk stabilitas pelatihan. Decoder menghasilkan keluaran dengan dua langkah
perhatian, yaitu masked self-attention pada token keluaran sebelumnya dan cross-
attention terhadap representasi encoder. Seluruh arsitektur memanfaatkan
positional encoding sinus-kosinus agar model mengenali urutan posisi token
(Vaswani dkk., 2023).

Vaswani dkk., (2023) menunjukkan perhitungan perhatian pada satu kepala
mengikuti scaled dot-product attention. Diberikan matriks Query 9, Key K, dan
Value V, skor perhatian dirumuskan pada Persamaan (2.3).

Attention(9,K,V) = softmax (=) v (2.3)
ke

Keterangan:
Q = matriks query berukuran ng X dy
K = matriks key berukuran ny x dy
v = matriks value berukuran ny x dy
dy = Dimensi ruang key atau query
sofimax () = Fungsi normalisasi baris-per-baris
Multi = menjalankan beberapa perhatian paralel pada proyeksi

—head attention linier yang berbeda sehingga pola lokal dan global
dapat ditangkap secara komplementer

a
stot mage teatres smotporpedctont parte mating oes

Gambar 2.13 Skema Detection Transformer (DETR)
Sumber: (Carion dkk., 2020)

Pada domain deteksi objek, pendekatan Transformer diadopsi oleh DETR,
yang memformulasikan deteksi sebagai ser prediction end-to-end tanpa anchor
maupun Non-Maximum Suppression (NMS); skemanya ditunjukkan pada Gambar

26

SKRIPSI PERBANDINGAN METODE DAN... 'ARKAN SYAFIQ ATTAOY


## Halaman 40

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

2.13 (Carion dkk., 2020), Deformable DETR kemudian memperkenalkan muti-
scale feature maps dan deformable attention agar konvergensi lebih cepat serta
sensitivitas terhadap objek kecil meningkat (X. Zhu dkk., 2021). Perkembangan ini
menjadi landasan bagi RT-DETR yang menargetkan deteksi real-time dengan tetap
mempertahankan end-to-end (Lv dkk., 2024: Zhao dkk., 2024).

2.2.8 Real-Time Detection Transformer (RT-DETR)

Detection Transformer (DETR) memformulasikan deteksi objek sebagai
masalah set prediction end-to-end dengan bipartite matching sehingga tidak
memerlukan anchor maupun Non-Maximum Suppression (NMS) (Cation dkk.,
2020). Deformable DETR kemudian memperkenalkan multi-scale feature maps
dan deformable attention untuk mempercepat pelatihan sekaligus meningkatkan
sensitivitas terhadap objek kecil (X. Zhu dkk., 2021). Arah pengembangan ini
menjadi landasan bagi Real-Time Detection Transformer (RT-DETR), yang
menargetkan deteksi real-time tetapi tetap mempertahankan end-to-end (Zhao dkk.,
2024), Zhao dkk., (2024) menunjukkan alur RT-DETR bermula dari backbone
Convolutional Neural Network (CNN) yang mengekstraksi fitur multi-skala, lalu
efficient hybrid encoder mengubahnya menjadi urutan fitur sambil memadukan
interaksi dalam-skala dan

intas-skala. Tahap berikutnya, uncertainty-minimal
query selection memilih object queries yang paling informatif sebelum diproses
decoder Transformer hingga menghasilkan prediksi akhir. Gambaran ringkas
Komponen ini ditunjukkan pada Gambar 2.14.

iclent Hybrid

(ooonEcoo

g
P
B
a
P
:
:
P
:
E

oa

Gambar 2.14 Overview Real-Time Detection Transformer (RT-DETR)
Sumber: (Zhao dkk. 2024)

2

SKRIPSI PERBANDINGAN METODE DAN... 'ARKAN SYAFIQ ATTAOY


## Halaman 41

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Evolusi encoder dari varian single-scale (SSE), multi-scale (MSE), dan cross-
scale fusion (CSF) menuju hybrid encoder yang menggabungkan Attention-based
Intra-scale Feature Interaction (AIFI) untuk interaksi dalam-skala serta CNN-
based Cross-scale Feature Fusion (CCFF) untuk fusi
latensi. Struktur varian encoder tersebut dirangkum pada Gambar 2.15. Detail blok

intas-skala yang hemat

fusi CCFF ditunjukkan pada Gambar 2.16, yang mencakup penyesuaian kanal
dengan konvolusi 1x1, penggunaan RepBlock untuk fusi, dan penggabungan
clemen per elemen (Zhao dkk., 2024).

A Hotrescale—t B 4Crovsce— C Decwmpid— DD Enbance— E

Gambar 2.15 Struktur Varian Encoder
Sumber: (Zhao dkk., 2024)

©cConcatenate EHElement-wise add (Flatten

Gambar 2.16 Blok fusi CNN-based Cross-scale Feature Fusion (CCFF)
Sumber: (Chua dan Tan, 2025)

RT-DETRv2 diperkenalkan sebagai pendekatan “bag-of-freebies” yang
meningkatkan stabilitas pelatihan tanpa menambah biaya inferensi. Peningkatan
yang dibawa meliputi penyesuaian jumlah sampling points per skala pada
deformable attention agar agregasi fitur multi-skala lebih efektif, penggantian
grid sample menjadi discrete sample yang lebih ramah deployment, serta
dinamika pelatihan melalui dynamic data augmentation dan scale-adaptive
hyperparameters untuk menjaga generalisasi pada berbagai resolusi. Hasil pada
COCO menunjukkan kenaikan average precision (AP) yang konsisten di seluruh

ukuran model (Lv dkk., 2024). Peningkatan ini sejalan dengan fondasi deformable

28
SKRIPSI PERBANDINGAN METODE DAN... 'ARKAN SYAFIQ ATTAOY


## Halaman 42

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

attention pada Deformable-DETR dan arah efisiensi RT-DETR generasi pertama,
serta telah dipaparkan ulang secara skematis pada kajian arsitektur dan alur
tensornya (Chua dan Tan, 2025: Zhao dkk., 2024: X. Zhu dkk., 2021). Aktivasi
tugas denoising pada RT-DETRV2 berperan sebagai regularisasi yang membantu
model memulihkan target dari gangguan terkontrol sehingga konvergensi lebih
cepat dan stabil, sebagaimana ditunjukkan pada Gambar 2.17. Mekanisme ini juga
mengurangi ketergantungan pada contoh mudah, membuat decoder lebih tangguh

terhadap noise anotasi dan variasi distribusi data (Lv dkk., 2024).
moema

‘oan eho

oman |

Gambar 2.17 Arsitektur RT-DETRv2 dengan Denoising Task On
‘Sumber: (Chua dan Tan, 2025)

i AIFI dan CCFF pada encoder menghasilkan

Secara keseluruhan, kombin:
agregasi fitur multiskala yang efisien, sementara uncertainty-minimal query
selection menyiapkan inisialisasi query yang lebih informatif bagi decoder (Zhao
dkk, 2024). Ketika dikombinasikan dengan denoising, alur end-to-end RT-
DETRv2 cenderung lebih stabil sejak awal pelatihan dan mempertahankan akurasi
tanpa mengorbankan throughput (Lv dkk., 2024). Ilustrasi skematis dengan

29

SKRIPSI PERBANDINGAN METODE DAN... ARKAN SYAFIQ ATTAOY


## Halaman 43

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

denoising aktif dapat dilihat pada rangkaian gambar RT-DETRv2 (Chua dan Tan,

2025).
Tabel 2.3 Varian RT-DETRv2
Tipe Tumlah Parameter (dalam juts)
RIDER 20
RTEDETRVM Bl
RDA 2
REDETRVEX Kg

Sumber (Lv dkk, 2024)
Tabel 2.3 merangkum varian RT-DETRv2 (Small (8), Medium (M), Large

(L), Extra Large (X)) beserta jumlah parameternya yang memudahkan pemilihan
model sesuai batasan perangkat dan target latensi (Lv dkk, 2024). Varian S
dioptimalkan untuk edge devices, M dan L menyeimbangkan akurasi dan waktu
inferensi untuk perangkat menengah, sementara X menargetkan akurasi tertinggi
pada sumber daya komputasi yang lebih besar, sehingga model ini mudah diadopsi
dari perangkat ringan hingga server GPU (Chua dan Tan, 2025: Lv dkk., 2024).
2.2.9 Loss Funetion

Loss function mengukur deviasi antara prediksi dan target, menjadi sinyal
“utama untuk memperbarui parameter selama pelatihan model deep learning. Pada
deteksi objek, Joss function umumnya terdiri atas dua komponen utama, yaitu
classification loss untuk menentukan label objek dan regression loss untuk
memprediksi koordinat hounding box (Girshick, 2015; Redmon dkk., 2016; Ren
dkk, 2016).

Pada regresi bounding box, pendekatan awal menggunakan £ loss yang
kurang representatif karena mengoptimalkan empat koordinat secara terpisah,
padahal kotak deteksi merupakan satu entitas yang saling bergantung. Intersection
over Union (ToU) Joss kemudian digunakan untuk memperlakukan kotak sebagai
satu kesatuan melalui ukuran tumpang:tindih antara prediksi dan ground truth,
sehingga sinyal gradien lebih konsisten terhadap kualitas lokalisasi (Yu dkk., 2016).
Perbandingan intuitif antara £2 loss dan ToU Joss yang menyoroti kelemahan
optimisasi koordinat terpisah dapat dilihat pada Gambar 2.18. Formula ToU
ditunjukkan pada Persamaan (2.4).

30

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 44

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

ToU(A,B) = ar TA
Keterangan:
4 - bounding box prediksi
B = bounding box ground truth
IanBI = luas irisan A dan B
lauBi = luas gabungan A dan B

Down = Fis Fan Bee Fy)
Ft rman: XL (tp tps Hie Xp)
xp
"5 loss OI

Intersectim( 9.0)
Union.)

* fo toss =

PA
Gambar 2.18 Perbandingan fz Loss dan foU Loss
Sumber: (Yu dkk, 2016)
IoU gagal memberikan gradien bermakna saat tidak ada tumpang-tindih, sehingga
Generalized IoU (GloU) memperbaikinya dengan menambahkan penalti area
pembungkus minimum yang tidak ditempati gabungan kotak (Rezatofighi dkk.,
2019). Rumus GIoU dirangkum pada Persamaan (2.5).

IC - @UB)I
GloU(A,B) = IOU(A,B) — —T— 2.5)
Keterangan:
c = Minimum enclosing box yang melingkupi A dan B

Stabilitas dan akurasi lokalisasi, khususnya pada objek berukuran kecil,
ditingkatkan melalui Complete IoU (CIOU) yang mempertimbangkan tiga
komponen utama, yaitu tingkat tumpang tindih, jarak antar pusat bounding box,
serta konsistensi rasio aspek (Zheng dkk., 2019). Defini CloU diberikan pada

Persamaan (2.6).

2
= (oF. &) 29

dengan

3

SKRIPSI PERBANDINGAN METODE DAN... 'ARKAN SYAFIQ ATTAOY


## Halaman 45

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Af ega _ v
Pn Tante
Keterangan:
pbb) = jarak Euclidean
c = diagonal kotak pembungkus minimum
wh = lebar dan tinggi prediksi
wh? = lebar dan tinggi ground truth

Pada sisi klasifikasi, ketidakseimbangan kelas positif dan negatif pada deteksi
dense mendorong penggunaan Focal Loss yang memodifikasi cross entropy dengan
faktor skala (1 — p,)”agar model berfokus pada contoh sulit dan menurunkan bobot
contoh mudah (Lin dkk, 2018). Perkembangan berikutnya, Generalized Focal Loss
menggabungkan sinyal kualitas klasifikasi dan lokalisasi melalui Quality Focal
Loss serta memodelkan posisi kotak sebagai distribusi diskret dengan Distribution
Focal Loss untuk meningkatkan presisi regresi lokasi (X. Li dkk, 2020). Bentuk
'umum ketiganya diringkas pada Persamaan (2.7), (2.8), dan (2.9).
FL) = (1 — pi)"logtp) @n
QFL(@,y) = -Iy — pl lylog(p) + (1 — ylog (A — p)] 28)
29)

wt
Dri =~ qlogto)

Keterangan:

pe = probabilitas prediksi benar

a = faktor penyeimbang kelas

Y = parameter fokus

ye (01) = kualitas berbasis IoU'

GP = distribusi ground truth dan prediksi atas posisi diskrit

Pada banyak arsitektur modem, Binary Cross Entropy with Logits tetap
digunakan sebagai komponen klasifikasi biner karena stabil secara numerik melalui
penggabungan sigmoid dan binary cross entropy dalam satu langkah sehingga
perhitungan lebih stabil pada rentang Jogit luas dan mudah dioptimasi bersama Joss

32

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 46

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

lokalisasi berbasis ToU atau turunannya (Goodfellow dkk., 2016; Ruby dkk., 2020).
Bentuk tertutup BCE with Logits diberikan pada Persamaan (2.10).

BCEWithLogits(x,y) = max(x,0) —x-y + log(1+exp(—lIxl)) (2.10)
Keterangan:
x = logit prediksi
y = label target

2.2.10 Hyperparameter Tuning

‘Fyperparameter adalah variabel yang ditetapkan sebelum proses pelatihan
dan tidak dipelajari langsung dari data. Contohnya meliputi learning rate, batch
size, dan jumlah epoch yang memengaruhi dinamika konvergensi serta kemampuan
generalisasi model (Goodfellow dkk., 2016). Hyperparameter tuning bertujuan
menemukan konfigurasi yang menyeimbangkan akurasi dan generalisasi. Grid

search cenderung mahal pada ruang besar, sedangkan random search lebih efisien
sehingga lazim dijadikan baseline sebelum metode adaptif diterapkan (Bergstra dan
Bengio, 2012).

Pendekatan yang lebih hemat evaluasi dicapai melalui Bayesian optimization
tipe Tree-Structured Parzen Estimator (TPE), yang memisahkan hasil evaluasi
menjadi kelompok “baik” dan “kurang baik”, memodelkan keduanya dengan kernel
density estimator, lalu memilih kandidat baru dengan memaksimalkan rasio
kepadatan sehingga eksploitasi dan eksplorasi berlangsung adaptif (Watanabe,
2025). TPE banyak digunakan di Hyperopt dan Optuna, dan dilaporkan unggul
terhadap pencarian naif pada berbagai studi Hyperparameter Optimization (HPO)
(Masum dkk., 2022).

Di antara hyperparameter, learning rate (LR) paling sensitif karena nilai yang
terlalu besar membuat pembaruan bobot tidak stabil, sedangkan nilai yang terlalu
kecil memperlambat konvergensi dan rawan titik minimum lokal. Praktik umum
menetapkan rentang awal melalui uji singkat seperti LR range test atau skema
@yelic untuk memperkirakan batas kerja yang aman (Smith, 2017). Pemilihan batch
size membentuk kompromi antara stabilitas dan generalisasi. Batch besar
memanfaatkan paralelisme, tetapi cenderung berakhir pada titik minimum yang
tajam, sedangkan batch kecil lebih bersifat stokastik namun mendorong titik

33

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 47

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

minimum yang lebih datar dan umumnya lebih robust terhadap data baru (Keskar
dkk, 2017, Masters dan Luschi, 2018).

Setelah ruang pencarian dan strategi tuning ditetapkan, kualitas hasil sangat
dipengaruhi oleh optimizer yang mengatur dinamika pembaruan parameter pada
setiap iterasi dan meminimalkan fungsi Joss melalui update berbasis gradien
(Cacciola dkk, 2023: Goodfellow dkk., 2016). Optimizer Stochastie Gradient
Descent (SGD) efisien pada mini-batch dan cocok untuk detektor satu tahap
berbasis Convolutional Neural Network (CNN) seperti You Only Look Once
(YOLO) yang menuntut stabilitas update serta latensi inferensi rendah (Redmon
dkk, 2016; C.-Y. Wang dkk., 2024). SGD memiliki efek regularisasi implisit dan,
ketika memakai mini-batch, menambahkan stokastisitas yang membantu keluar dari
titik minimum yang tajam sekaligus meningkatkan efisiensi komputasi (Cacciola
dkk, 2023; M. Wang dan Wu, 2024). Formulasi dasar pembaruan parameter
ditunjukkan pada Persamaan (2.11).

Bee = Op — VLC 59) (au)
Keterangan:
& = vektor parameter pada iterasi ke-t
7 = learning rate
L (Os xi; ya) = fungsi Joss pada sampel (x; yi) atau mini-batch

Val (Os: xi: Vi)
Optimizer AdamW selaras dengan arsitektur deteksi berbasis Transformer

gradien Joss terhadap parameter

seperti Detection Transformer (DETR) dan Real-Time Detection Transformer (RT-
DETR) karena decoupled weight decay menjaga stabilitas pada pelatihan multi-
skala (Carion dkk., 2020; Lv dkk., 2024). Pemisahan weight decay dari pembaruan
‘momen adaptif membuat regularisasi lebih konsisten dibanding Adam klasik dan
'umumnya menghasilkan konvergensi lebih stabil serta generalisasi lebih baik pada
tugas-tugas computer vision modem (Loshchilov dan Hutter, 2019). Pembaruan
‘momen dan parameter dirangkum pada Persamaan (2.12).
m, = met U-09, = Bert A- fg? (212)

34
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 48

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

- — nas,
Gre » )

“vektor parameter pada iterasi ke-t

me ‘momen pertama, rata-rata bergerak gradien

Up 5 momen kedua, rata-rata bergerak kuadrat gradien

B,B. - koefisien peluruhan eksponensial momen

n = learning rate

a koefisien weight decay yang dipisahkan secara eksplisit
€ (konstanta kecil untuk stabilitas numerik

Pemilihan optimizer dalam penelitian ini disesuaikan dengan karakteristik
arsitektur model. YOLOv9 sebagai model berbasis CNN menggunakan SGD
karena lebih stabil pada pembaruan konvolusional dan efisien untuk inferensi real-
time, sedangkan RT-DETRv2 sebagai model berbasis Transformer menggunakan
AdamW untuk menjaga stabilitas pelatihan dan konvergensi pada mekanisme
multi-scale attention (Moraes dkk, 2025: Lv dkk, 2024). Kombinasi ini
memastikan proses optimisasi konsisten dengan prinsip kerja masing-masing
arsitektur.
2.2.11 Metrik Evaluasi Model

Metrik evaluasi digunakan untuk menilai sejauh mana model melakukan
prediksi dengan benar. Indikator yang lazim digunakan meliputi precision, recall,
Fl-seore, accuracy, dan mean Average Precision (MAP). Fl-score merangkum
trade-off antara precision dan recall sehingga relevan ketika distribusi kelas tidak
seimbang dan risiko false positive maupun false negative perlu dikendalikan
(Chico dan Jurman, 2020; Powers, 2020). Precision mengukur proporsi prediksi
positif yang benar, sedangkan recall menilai kemampuan model menangkap
seluruh contoh positif. Definisi operasional untuk precision, recall, FI-seore, dan
accuracy dituliskan pada Persamaan (2.13), (2.14), (2.15), dan (2.16) Powers,
2020).

T
ision = (2. aw
Precision = ppp CAD), Recall ang

35

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 49

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

2 x Precision x Recall

Precision Recall ka)
Accuracy = ee (2.16)
Keterangan:
TP = Jumlah data positif yang terprediksi benar
TN Jumlah data negatif yang terprediksi benar
FP Jumlah data negatif yang salah diprediksi positif
FN Jumlah data positif yang salah diprediksi negatif

Keempat besaran dasar, yaitu TP, TN, FP, dan FN, umumnya diringkas dalam
confusion matrix untuk membantu membaca pola kesalahan per kelas. Visualisasi
ternormalisasi bermanfaat saat dataset timpang karena menampilkan proporsi per
kelas secara lebih adil (Grandini dkk, 2020: Tharwat, 2021). Accuracy mudah
dipahami namun dapat menyesatkan pada data tidak seimbang karena didominasi
kelas mayoritas. Pada deteksi objek, praktik baku lebih mengutamakan mAP karena
‘metrik ini merata-ratakan akurasi deteksi per kelas sekaligus memperhitungkan
lokalisasi dengan ambang Intersection over Union (TOU), misalnya mAPSO yang
menganggap prediksi benar bila ToU > 0,5. Definisi mAP dituliskan pada
Persamaan (2.17) (Muhammad dkk., 2023: B. Wang, 2022).

1
mAP =~ ) AP Can
Keterangan:
n jumlah kelas
AP, rata-rata precision untuk kelas ke-k

Dalam praktik modem, sumber kesalahan biasanya diurai untuk analisis lebih
tajam, misalnya localization error saat ToU di bawah ambang, classification error
ketika label salah, duplicate detection saat satu objek terdeteksi berulang, serta
‘missed detection ketika objek tidak tertangkap. Pembacaan kategori kesalahan ini
membantu intervensi yang tepat pada arsitektur maupun data (Liu dkk., 2024).

Selain akurasi, banyak proyek deteksi real-time menuntut latensi inferensi

rendah sehingga perlu evaluasi multi-tujuan. Pareto Frontier digunakans untuk

36

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 50

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

mengidentifikasi himpunan solusi yang tidak didominasi, yakni titik yang tidak
dapat ditingkatkan akurasinya tanpa mengorbankan latensi atau sebaliknya,
sehingga pemilihan konfigurasi “terbaik” bisa disesuaikan dengan batasan
(perangkat dan target #hroughpu (Deb, 2011). Pendekatan Pareto banyak digunakan
pada Neural Architecture Search dan perancangan sistem untuk menimbang akurasi
versus waktu inferensi secara bersamaan, serta diperluas untuk tujuan lain seperti
fairness, privasi, dan efisiensi komputasi. Pelaporan hasil yang memadukan mAP
dan latensi pada diagram Pareto memberi gambaran praktis tentang trade-off model
di lingkungan nyata (Yaghini dkk., 2023; Ye dk., 2024).

Selain metrik akurasi, evaluasi sistem deteksi objek real-time juga perlu
mempertimbangkan latensi inferensi, terutama pada skenario deployment berbasis
web dan sistem waktu nyata. Latensi merepresentasikan waktu respons sistem
dalam memproses satu citra hingga menghasilkan prediksi, sehingga menjadi faktor
penting dalam menentukan kelayakan penggunaan model pada aplikasi praktis.
Pada sistem real-time, pengukuran latensi tidak cukup direpresentasikan oleh nilai
rata-rata semata, karena fluktuasi waktu inferensi dapat berdampak langsung pada
stabilitas sistem dan pengalaman pengguna. Oleh karena itu, evaluasi performa
sering dikaitkan dengan analisis trade-off antara akurasi dan latensi, sebagaimana
dibahas pada penelitian deteksi objek real-time berbasis CNN dan Transformer
(Redmon dkk., 2016: Bochkovskiy dkk, 2020;Lv dkk., 2024). Analisis performa
‘multi-tujuan umumnya dilakukan menggunakan pendekatan Pareto Frontier untuk
mengidentifikasi konfigurasi model yang memberikan keseimbangan terbaik antara
akurasi deteksi dan efisiensi inferensi. Pendekatan ini memungkinkan pemilihan
model yang sesuai dengan batasan sumber daya komputasi dan kebutuhan respons
sistem, tanpa mengorbankan akurasi secara signifikan, sehingga relevan untuk
evaluasi sistem deteksi objek pada lingkungan implementasi nyata (Deb, 2011;
Zhao dkk., 2024).

2.2.12. Software Development Life Cyele (SDLC)

Software Development Life Cycle (SDLC) merupakan kerangka kerja
sistematis yang digunakan untuk mengelola seluruh siklus hidup perangkat lunak,
mulai dari tahap perencanaan, analisis kebutuhan, perancangan, pembangunan,

37

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 51

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

pengujian, penerapan, hingga pemeliharaan, dengan tujuan menghasilkan
perangkat lunak yang memenuhi kebutuhan pemangku kepentingan serta memiliki
kualitas tinggi (Hossain, 2023). Standar ISO/TECAEEB 12207:2017 menetapkan
(proses, aktivitas, dan tugas yang menjadi acuan organisasi dalam mendefinisikan,
mengendalikan, serta meningkatkan proses daur hidup perangkat lunak baik di
tingkat proyek maupun organisasi. Pada praktik rekayasa perangkat lunak modern,
SDLC dipahami sebagai proses rekayasa yang menekankan disiplin requirements
engineering, desain arsitektural, manajemen konfigurasi, dan jaminan mutu agar
pengembangan dapat dipelihara serta diskalakan sepanjang siklus hidup s

Salah satu model dalam SDLC adalah model Prototipe, yaitu pendekatan
iteratif yang menekankan pembuatan versi awal atau model kerja sistem untuk

tem.

memvisualisasikan kebutuhan dan fungsi utama sebelum implementasi penuh
(Amalia dan Mahyuddin, 2023). Model ini memberikan ruang bagi pengembang
dan pengguna untuk berinteraksi sejak tahap awal, sehingga kebutuhan dapat
diverifikasi lebih dini dan kesalahan desain dapat diminimalkan. Pendekatan
prototipe bersifat fleksibel dan adaptif terhadap perubahan, memungkinkan
perbaikan berulang berdasarkan umpan balik pengguna hingga tercapai versi sistem
yang mememuhi spesifikasi akhir (Pressman dan Maxim, 2015; Sommerville,
2016).

‘Sumber: (Pressman dan Maxim, 2015)

38

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 52

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Pada Gambar 2.19, tahap Communication dimaknai sebagai proses
komunikasi dan analisis kebutuhan antara pengembang dan pengguna untuk
memperoleh pemahaman menyeluruh terhadap tujuan sistem yang akan dibangun.
Tahap ini berfokus pada identifikasi masalah, karakteristik pengguna, serta skenario
penggunaan yang akan diakomodasi. Hasilnya berupa spesifikasi awal yang
mencakup kebutuhan fungsional dan non-fungsional, deskripsi proses utama, serta
alur data yang menjadi dasar bagi perancangan sistem selanjutnya (Pressman dan
Maxim, 2015: Mulyono dan Ardhiyani, 2018).

Tahap Quick Plan berorientasi pada penyusunan rencana kerja cepat yang
mencakup penentuan ruang lingkup sistem, identifikasi komponen inti, serta jadwal
iterasi pengembangan. Tahap ini dilakukan secara adaptif dengan menekankan
fleksibilitas terhadap perubahan kebutuhan. Rencana awal disusun sebagai
kerangka dasar yang akan terus diperbarui seiring ditemukannya masukan dan
kendala pada proses pengujian tahap berikutnya (Sari, 2021).

Tahap Modeling atau Quick Design mencakup kegiatan perancangan
antarmuka dan struktur logika sistem berdasarkan hasil komunikasi dan
(perencanaan yang telah dilakukan. Pada tahap ini biasanya dibuat rancangan alur
pengguna, wireframe, serta skema interaksi antar komponen sistem. Tujuan
“utamanya adalah menghasilkan rancangan visual dan konseptual yang cukup untuk
memandu proses konstruksi prototipe, dengan tetap memperhatikan prinsip
keterpakaian dan efisiensi (Pressman dan Maxim, 2015; Sommerville, 2016).

Tahap Construction of Prototype merupakan tahap ii

plementasi rancangan
menjadi bentuk prototipe yang dapat dijalankan dan diuji. Tahapan ini mencakup
pembangunan fungsi dasar sistem, integrasi komponen awal, serta pengujian
internal untuk memastikan bahwa rancangan konseptual dapat direalisasikan secara
teknis. Umpan balik dari pengujian internal digunakan sebagai dasar revisi cepat
terhadap rancangan sebelumnya sehingga siklus pengembangan dapat terus
berlangsung secara iteratif dan terkontrol (Pressman dan Maxim, 2015: Mulyono
dan Ardhiyani, 2018).

Tahap terakhir, Deployment, Delivery, dan Feedback, menekankan pada

evaluasi prototipe oleh pengguna atau pihak yang berkepentingan. Proses ini

39

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 53

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

bertujuan untuk menilai kesesuaian sistem dengan kebutuhan, mengidentifikasi
kelemahan, dan memperoleh masukan untuk pengembangan lanjutan. Evaluasi
dapat dilakukan melalui pengujian fungsional maupun penilaian kegunaan, yang
hasilnya menjadi dasar bagi iterasi berikutnya hingga sistem mencapai stabilitas
dan tingkat penerimaan yang diharapkan (Sari, 2021; Pressman dan Maxim, 2015).

Secara umum, siklus lima tahap ini menggambarkan bahwa metode
prototyping tidak hanya berfungsi sebagai strategi perancangan sistem yang cepat
dan fleksibel, tetapi juga sebagai pendekatan iteratif yang menekankan umpan balik
berkelanjutan dari pengguna. Pendekatan ini memungkinkan penyempurnaan
sistem secara progresif melalui serangkaian siklus desain, konstruksi, dan evaluasi,
sehingga hasil akhir dapat lebih sesuai dengan kebutuhan nyata pengguna (Amalia
dan Mahyuddin, 2023: Pressman dan Maxim, 2015).
22121 Streamlit

Streamlit adalah framework open-source berbasis Python yang dirancang
untuk membangun dan membagikan aplikasi web secara cepat, terutama untuk
kebutuhan data seience dan machine learning. Framework ini memungkinkan
pengembang mengubah kode Python menjadi antarmuka interaktif hanya dengan
beberapa baris perintah tanpa perlu menangani detail frontend maupun backend,

sehingga mempermudah peneliti dalam memvisualisasikan hasil analisis atau

menjalankan model secara interaktif (Jain dkk., 2022).

Streamlit menyediakan komponen antarmuka seperti slider, select box, dan
file uploader yang terintegrasi langsung dengan pustaka analisis populer seperti
seikit-leam dan PyTorch. Mekanisme ini memungkinkan proses unggah data,
pemanggilan fungsi inferensi, dan visualisasi keluaran berjalan dalam satu alur
komputasi yang efisien dan real-time (Chaudhuri, 2023). Melalui mekanisme
tersebut, proses unggah data, pemanggilan fungsi inferensi, dan visualisasi keluaran
dapat dilakukan dalam satu alur komputasi yang efisien.

Secara konseptual, alur kerja aplikasi berbasis Streamlit terdiri atas tiga
tahapan utama yang saling terhubung. Tahap pertama adalah input dan

prepocessing, yaitu proses peneri

aan data dari pengguna serta normalisasi atau
transformasi awal agar sesuai dengan kebutuhan pemrosesan. Tahap kedua adalah

40
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 54

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

pemrosesan atau inferensi, di mana sistem menjalankan algoritme atau model
machine learning untuk menghasilkan keluaran sesuai tujuan aplikasi. Tahap ketiga
adalah visualisasi hasil, yang menampilkan keluaran tersebut secara interaktif
kepada pengguna melalui elemen visual seperti grafik, tabel, atau anotasi gambar
(Pressman dan Maxim, 2015: Sommerville, 2016). Rangkaian proses ini sejalan
dengan prinsip prototyping, karena setiap hasil dapat langsung dievaluasi oleh
pengguna dan menjadi dasar perbaikan pada iterasi berikutnya.

Dengan fleksibilitas, integrasi Python yang kuat, serta kemampuannya
menampilkan hasil secara instan, Streamlit menjadi pilihan yang ideal untuk tahap
prototyping aplikasi berbasis machine learning. Framework ini mendukung
pengembangan sistem yang cepat, iteratif, dan mudah diuji, sehingga dapat
digunakan untuk menghubungkan komponen analisis, model, serta antarmuka
(pengguna secara efisien sebelum proses deployment dilakukan secara penuh (Jain
dek, 2022).
2.2.12.2 Black Box Testing

Black Box Testing, seperti diperlihatkan pada Gambar 2.20, merupakan
metode pengujian perangkat lunak yang menilai fungsi sistem dari sudut pandang
pengguna tanpa meninjau struktur internal kode atau logika program. Gambar
tersebut menggambarkan alur input yang diberikan pengguna kepada sistem,
kemudian diproses di dalam black box tanpa diketahui mekanisme internalnya, dan
menghasilkan oufpu yang selanjutnya dibandingkan dengan hasil yang diharapkan.
Fokus utama pengujian ini adalah memastikan keluaran sistem sesuai dengan
spesifikasi berdasarkan masukan tertentu (Pressman dan Maxim, 2015:
Sommerville, 2016). Dengan kata lain, penguji hanya mengetahui apa yang
seharusnya dilakukan sistem, bukan bagaimana sistem melakukan prosesnya.
Tujuan pengujian adalah memastikan aplikasi berjalan sesuai kebutuhan dan
terbebas dari kesalahan fungsional, termasuk pada interaksi antarmuka dan alur
kerja utama (Salih dan Saefullah, 2024).

41

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 55

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Input

0
Black Box — EK

Gambar 2.20 Black Box Testing
Sumber: (Salih dan Saefullah, 2024)

Metode ini lazim digunakan pada tahap pengujian fungsional untuk

memverifikasi bahwa setiap fitur memenuhi kebutuhan pengguna dan spesifikasi

yang telah dirancang. Cakupan uji meliputi pemberian input valid, input tidak valid,

serta kondisi batas, serta observasi respons sistem terhadap kesalahan atau anomali
yang mungkin terjadi (Salih dan Saefullah, 2024). Pendekatan ini juga dapat

diperluas ke aspek non-

ingsional seperti kinerja dan keamanan guna memastikan
sistem tetap andal dalam berbagai skenario penggunaan. Keterbatasannya ialah
tidak mampu mengungkap kesalahan logika internal atau ketidakefisienan
algoritma yang tersembunyi (Pressman dan Maxim, 2019; Sommerville, 2016)
2.2.12.3 System Usability Scale (SUS)

System Usability

ale (SUS) merupakan instrumen evaluasi usability yang
banyak digunakan untuk menilai persepsi pengguna terhadap Tingkat kemudahan
penggunaan suatu sistem secara cepat dan reliabel. Metode ini diperkenalkan oleh
John Brooke dan telah digunakan secara luas dalam evaluasi perangkat lunak,
aplikasi web, serta sistem interaktif karena sifatnya yang sederhana namun memiliki
2018). SUS terdiri dari sepuluh

pernyataan yang dirancang untuk mengukur persepsi pengguna terhadap aspek

validitas empiris yang kuat (Brooke, 1996; Lewis,

usability seperti kompleksitas sistem, konsistensi antarmuka, kemudahan
pembelajaran, efisiensi penggunaan, serta tingkat kepercayaan diri pengguna saat
berinteraksi dengan sistem. Konstruk tersebut merepresentasikan dimensi usability
yang mencakup efektivitas, efisiensi, dan kepuasan pengguna dalam menggunakan
sistem interaktif.

Setiap pernyataan dinilai menggunakan skala Likert lima poin, mulai dari
sangat tidak setuju hingga sangat setuju. SUS dikembangkan sebagai instrumen

evaluasi usability yang praktis, cepat digunakan, serta mampu memberikan

42

SKRIPSI PERBANDINGAN METODE DAN... ARKAN SYAFIQ ATTAOY


## Halaman 56

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

gambaran umum tingkat kemudahan penggunaan sistem secara komprehensif
(Brooke, 1996). Penelitian empiris menunjukkan bahwa SUS memiliki reliabilitas
yang tinggi dengan nilai Cronbach's alpha umumnya berada di atas 0,8, sehingga
cukup sensitif untuk membedakan tingkat usability antar sistem (Bangor dkk,
2008; Lewis, 2018). Selain itu, SUS terbukti tetap memberikan hasil yang konsisten
(pada ukuran sampel relatif kecil, dengan stabilitas estimasi yang umumnya tercapai
pada jumlah responden sekitar 10-14 orang (Tullis dan Stetson, 2004: Bangor dkk.,
2008). Hal tersebut menjadikan SUS sesuai digunakan untuk evaluasi prototipe
(pada tahap pengembangan awal.

Dalam praktik penelitian usability, jumlah responden tidak selalu
memerlukan sampel besar sebagaimana penelitian survei inferensial, karena tujuan
utama usability testing adalah memperoleh estimasi awal tingkat kemudahan
penggunaan sistem serta mengidentifikasi potensi permasalahan antarmuka.
Beberapa penelitian empiris menggunakan sekitar 8-15 responden untuk evaluasi
usability berbasis SUS dan tetap menghasilkan interpretasi usability yang memadai
pada tahap pengembangan awal sistem. Penelitian sebelumnya menunjukkan
bahwa penggunaan sekitar 10 responden pada evaluasi usability berbasis SUS
masih dapat memberikan estimasi tingkat kegunaan sistem yang memadai pada
tahap pengembangan awal (Umam dkk., 2023). Oleh karena itu, ukuran sampel
yang relatif kecil masih dapat memberikan estimasi usability yang memadai selama
karakteristik responden sesuai dengan konteks penggunaan sistem. Sepuluh butir
pernyataan dalam kuesioner SUS disusun secara bergantian antara pernyataan
positif dan negatif untuk meminimalkan bias jawaban responden serta
meningkatkan reliabilitas pengukuran persepsi usability (Brooke, 1996). Daftar
lengkap butir pertanyaan SUS yang digunakan dalam penelitian ini ditunjukkan
pada Tabel 2.4.

Tabel 2.4 Pertanyaan System Usability Seale (SUS)

ne raiyiaa ‘Skor Skor Skor | Skor Skor

T_| Saya merasa sistem ini mudah digunakan
2 _| Saya merasa sistem iol terlalu rumit

3 | Saya merasa percaya diri saat menggunakan
sistem ini

43

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 57

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Ha Patan ‘Skor Skor Skor | Skor Skor

4 | Saya merasa butuh bantuan teknis untuk bisa
‘menggunakan sistem ini

SY Fiturtitur dalam sistem Tni terintegrast dengan
baik

@ | Saya merasa ada terlalu banyak Inkosistensi
“dalam sistem ini

7 | Saya merasa orang tain “akan belajar
‘menggunakan sistem ini dengan cepat

W | Saya merasa sistem ini membingungkan untuk
digunakan

® | Saya merasa menggunakan sistem ini tidak
‘memburuhkan banyak usaha

To | Saya merasa banyak hal yang perlu saya pelajari
sebetum bisa menggunakan sistem ini dengan

baik:

‘Sumber: (Brooke, 1990)

Tabel 2.4 menunjukkan bahwa setiap pernyataan dinilai menggunakan skala

Likert 5 poin, mulai dari “Sangat Tidak Setuju” (skor 1) hingga “Sangat Setuju”
(Ekor 5). Perhitungan skor SUS dilakukan dengan menormalkan skor setiap butir
pertanyaan. Pada pernyataan bernomor ganjil (1, 3, 5, 7, 9) yang bersifat positif,
skor dihitung dengan mengurangkan nilai respons terhadap angka satu. Sebaliknya,
pada pernyataan bernomor genap (2, 4, 6, 8, 10) yang bersifat negatif, skor
diperoleh dengan mengurangkan nilai respons dari angka lima. Jumlah skor dari
seluruh butir pertanyaan kemudian dikalikan dengan faktor 2,5 sehingga
menghasilkan rentang nilai SUS antara O hingga 100, sebagaimana dirumuskan
pada Persamaan (2.18) (Brooke, 1996). Skor SUS keseluruhan diperoleh dengan
menghitung rata-rata skor dari seluruh responden sebagaimana dirumuskan pada
Persamaan (2.19).
(S1-1) + G- 52) + (63-1) + 6-54)
+(9-1)+6-Si0)
Dkk Skor SUS,
n

Nilai SUS tidak diinterpretasikan sebagai persentase, melainkan sebagai

Skor Akhir SUS — (2.19)
indeks relatif yang merepresentasikan tingkat usability suatu sistem. Interpretasi
skor umumnya dilakukan menggunakan tiga pendekatan, yaitu acceptability range,
grade scale (A-), dan adjective rating yang berkisar dari worst imaginable hingga
best imaginable. Pendekatan ini membantu memberikan makna praktis terhadap

44

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 58

SKRIPSI

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

skor usability, misalnya nilai di atas 68 secara umum dikategorikan berada di atas
rata-rata kualitas usability sistem interaktif (Bangor dkk, 2009). Interpretasi nilai
SUS berdasarkan kategori acceptability range, grade scale, dan adjective rating
ditunjukkan pada Gambar 2.21, sehingga hasil evaluasi usability dapat dipahami
secara lebih intuitif oleh peneliti maupun pemangku kepentingan (Bangor dkk,
2009).

LY eS aS IKU
A 2 Li
oe

t 5 ae
0 10 20 30 40 50 60 70 80 90 100
SUS Score

Gambar 2.21 Skoring pada System Usability Scale (SUS)
‘Sumber: (Bangor dik 2009)

45

PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 59

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

BAB III
METODOLOGI

34 Lokasi dan Waktu

Penelitian ini dilaksanakan di Ruang Research Teknologi Sains Data, Gedung
‘Nano, Kampus C, Universitas Airlangga, Surabaya. Pemilihan lokasi ini didasarkan
pada ketersediaan fasilitas yang mendukung serta lingkungan yang memungkinkan
penelitian dapat berjalan dengan optimal. Rentang waktu pelaksanaan penelitian ini
dimulai dari bulan Agustus 2025 hingga Maret 2026. Waktu tersebut diperkirakan
cukup untuk menyelesaikan seluruh tahapan penelitian, mulai dari pengumpulan
data, eksplorasi dan analisis data, pemodelan, evaluasi model, hingga penyusunan
laporan akhir dalam bentuk skripsi.
3.2 Data dan Alat

Data yang digunakan pada penelitian ini merupakan data sekunder Car
Damage Detection (CarDD) yang disusun oleh X. Wang dkk. (2023). CarDD
memuat 4.000 citra dengan rata-rata resolusi sekitar 684.231 piksel dan lebih dari
9.000 instance kerusakan yang dianotasi dalam enam kategori, yaitu crack, dent,
scratch, glass shatter, lamp broken, dan tire flat. Anotasi mengikuti skema skema
Common Objects in Context (COCO) pada level instance, sehingga satu citra dapat
‘memuat lebih dari satu objek kerusakan (multiobjek) dengan kelas dan lokasi yang
berbeda. Rincian definisi operasional dan indikator visual untuk keenam kelas

kerusakan pada CarDD dijelaskan pada Tabel 3.1
Tabel 3.1 Deskripsi Data

No | Kelas | Definisi Operasional Indikator Visual
1 | Crack Retakan terbelah pada material (panel | Garis retak dengan kontras
bodi/kaca), menunjukkan pemisahan is dapat bercabang:
‘material yang jelas sering tembus coating/cat.
2 | Dent Deformasi plastis permukzan tanpa | Distorsi bentuk’pantulan:
pecah: kontur” melengkung ke | highlightishadow tidak
dalam/luar. normal.
3 | Scratch Luka linear dangkal pada lapisan | Garis tipis, memanjang:
catipernis tanpa pemisahan material sering mengikuti alur
sesekan.
@ | Glass shatter “| Kerusakan pada kaca (jendela) dengan | Pola renk
retakipecah menyebar. “spiderweb”/ftagmentasi
kaca.
46

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 60

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

No | Kelas | Definisi Operasional Tndikator Visual
5 | Lamp broken | Kerusakan housing/lensafampu| Retak pada lensa_lampu:
retakipecah, serpihan™hole” di unit
lampu.
© | Tire flat Tekanan ban hilang atau ban Tepas dari | Dinding ban tertekan, profil
bead. menyentuh tanah:
deformasi melingkar

Penelitian ini menggunakan berbagai alat yang mendukung proses analisis
dan pemodelan. Alat utama yang digunakan dalam penelitian ini adalah laptop Acer
Swift SF914-511 dengan server atau GPU cloud Video Graphics Adapter (VGA)
NVIDIA RTX A6000 Ada dengan VRAM 48 GB. Spesifikasi ini dipilih karena
mampu menangani kebutuhan analisis data dan pemodelan yang digunakan dalam
penelitian ini. Perangkat lunak pada penelitian ini mencakup Python 3.10 sebagai
bahasa pemrograman utama dengan lingkungan Jupyter Notebook dan PyTorch
untuk — pelatihan/inferensi. ” Implementasi ~YOLOv9 merujuk repo
‘WongKinYiwyolov9, sedangkan RT-DETRv2 memakai implementasi PyTorch.
Visualisasi hasil dan prototipe menggunakan matplotlib dan Streamlit, serta
‘Weights and Biases (wandb) untuk pelacakan eksperimen. Adapun library yang
digunakan dalam ekosistem Python untuk mendukung penelitian ini dijelaskan
lebih lanjut pada Tabel 3.2.

Tabel 3.2 Deskripsi Library Penelitian

No | Nama Package | Deskripsi

1 | torch Library untuk Komputasi tensor dan deep learning; Inti pelatihan atau
inferensi model,

2_| torchvision Utilitas computer vision (ransformasi, model backbone, TO gambar)
berbasis PyTorch,

3_[mumpy ‘Komputasi numerik efisien untuk operasi array atau matriks.

4 [pandas Pengolahan data terstruktur untuk /ogeing/analisis hasil eksperimen.

5 Tenenevpyihon | Pembacsan/penulisan citra, konversi wama, praproses, serta

te penggambaran bounding bar!label.

& | atbumentatioas | Augmentasi citra (fp, affine, color Jiter, blur, cutoul) dengan Kontrol
probabilitas.

T Lnyeoeotoote | Utilitas format dan metik COCO (APimAP) untuk evaluasi deteksi

8 Ttadm Progress bar terasi pelatihan dan evaluasi

9 | matpfatib Visualisasi kurva/metrik pelatihan serta grafik pendukung analisis

10 | scikit-learn Utiltas ML umum (mis. train_fest split, metrik dasar, praproses
ringan).

Ti | thop Estimasi Floating Polat Operations (FLOP3) dan jumlah parameter
‘model untuk pelaporan kompleksitas.

12 | PyVAML Pembacaan/pemulisan berkas konfigurasi yam (model, data, dan
hyperparameter),

13 | wandb Pelacakan eksperimen, logging artefak, dan dashboard hasil pelatihan,

14 | stream Pembuatan aplikasi weh prototipe untuk antarmuka inferensi dan demo
hasil

47

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 61

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

33 Cara Kerja
Proses penerapan dan cara kerja pada penelitian ini menggunakan diagram

alir yang dapat dilihat pada Gambar 3.1.

D

kena arosome

Daan

(Hl

Gambar 3.1 Cara Kerja Penelitian

48

SKRIPSI PERBANDINGAN METODE DAN... 'ARKAN SYAFIO ATTAOY


## Halaman 62

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

33.1 Data Collection
Proses pengumpulan data menggunakan dataset CarDD yang terdiri dari
sekitar 4.000 citra kendaraan dengan lebih dari 9.000 instance anotasi yang terbagi
ke dalam enam kelas kerusakan, yaitu crack, dent, serateh, glass shatter, lamp
broken, dan tire flat. Anotasi disusun pada level instance menggunakan format
COCO sehingga satu citra dapat memuat lebih dari satu objek kerusakan pada lokasi
yang berbeda (multiobjek). Distribusi jumlah instance antar kelas menunjukkan
variasi proporsi yang berpotensi menimbulkan ketidakseimbangan data. Kelas
kerusakan seperti scratch dan dent umumnya memiliki jumlah instance lebih
banyak dibandingkan kelas seperti glass shatter dan tire flat. Ketidakseimbangan
distribusi kelas ini dapat mempengaruhi proses pembelajaran model karena
representasi fitur dari kelas mayoritas lebih sering muncul selama pelatihan.

Selain distribusi kelas, karakteristik ukuran objek juga menjadi perhatian
penting. Sebagian kerusakan, khususnya scratch dan crack, memiliki ukuran
bounding box relatif kecil dibandingkan dimensi citra secara keseluruhan. Objek
berukuran kecil umumnya lebih sulit dideteksi karena informasi detail berpotensi
berkurang selama proses ekstraksi fitur pada jaringan deep learning. Dataset
disusun melalui proses kurasi yang meliputi seleksi citra, penghapusan duplikasi,
serta anotasi manual untuk menjaga kualitas label dan keberagaman kondisi visual,
seperti variasi pencahayaan, sudut pengambilan gambar, dan jarak kamera.
Karakteristik tersebut memungkinkan evaluasi performa model deteksi kerusakan
kendaraan pada kondisi yang lebih representatif terhadap situasi nyata.

3.3.2 Data Splitting

Setelah seluruh data terkumpul, dataset dibagi menjadi training set (70%),
validation set (20%), dan test set (10%) mengikuti pembagian resmi yang
disediakan oleh dataset CarDD. Penggunaan split resmi bertujuan menjaga
konsistensi dengan penelitian terdahulu serta memastikan reproduksibilitas
eksperimen. Distribusi kelas pada masing-masing subset dianalisis untuk
memastikan tidak terjadi perbedaan karakteristik data yang signifikan antar subset.
Hasil analisis menunjukkan bahwa proporsi keenam kelas kerusakan relatif
konsisten pada data train, validation, dan test, sehingga tidak menimbulkan

49

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 63

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

pergeseran distribusi kelas. Selain itu, setiap citra hanya muncul pada satu subset
sehingga tidak terjadi data leakage. Pendekatan ini memastikan bahwa evaluasi
performa model mencerminkan kemampuan generalisasi secara objektif, meskipun
dataset memiliki ketidakseimbangan kelas pada tingkat moderat.
3.3.3 Data Preprocessing

Setelah pembagian data, dilakukan serangkaian preprocessing pada setiap
subset untuk memastikan keseragaman format masukan bagi seluruh model
Seluruh citra pada dataset diubah ke resolusi 640x640 piksel untuk menjaga
konsistensi dimensi input antar arsitektur. Ukuran resolusi tersebut dipilih karena
umum digunakan pada model deteksi objek modem serta memberikan
keseimbangan antara detail spasial dan efisiensi komputasi. Pada training set,
diterapkan augmentasi data yang diseragamkan antar arsitektur guna memastikan
keadilan perbandingan performa model. Augmentasi yang digunakan meliputi
horizontal flipping serta augmentasi berbasis warna untuk meningkatkan ketahanan
model terhadap variasi orientasi objek dan kondisi pencahayaan. Rincian jenis
augmentasi dan tujuan penggunaannya disajikan pada Tabel 3.3.
Tabel 3.3 Kriteria Augmentasi Data

No ‘Augmentasi Kegunaan

1 | RandomborizontalFlip Meningkatkan variasi orientasi objek Kendaraan
sehingga model lebih robust terhadap perbedaan arah
pandang

2 | HSV/RandomPhoiometricDistort | Meningkatkan ketahanan model terhadap Waras
pencahayaan dan perubahan wama bodi kendaraan

pada kondisi lingkungan yang berbeda.

i visual, dataset deteksi objek umumnya memiliki distribusi

Selain vari

jumlah instance yang tidak seimbang antar kelas. Ketidakseimbangan tersebut
berpotensi menyebabkan model lebih sering mempelajari karakteristik kelas
mayoritas dibandingkan kelas minoritas. Dalam penelitian ini, tidak dilakukan
teknik penyeimbangan data secara eksplisit seperti oversampling atau pemberian
bobot kelas tambahan. Pendekatan ini dipilih untuk mempertahankan distribusi asli
dataset serta menjaga konsistensi skenario eksperimen antar model. Augmentasi
data pada training set berfungsi untuk memperkaya keragaman representasi visual
objek tanpa mengubah distribusi kelas secara artifisial, sehingga model diharapkan

tetap mampu mempelajari pola kerusakan secara lebih robust. Pada validation set

50

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 64

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

dan test set, preprocessing dilakukan tanpa augmentasi data untuk menjaga
objektivitas evaluasi performa model. Seluruh citra dikonversi ke format float dan
diskalakan ke rentang 0 hingga 1, dengan skema normalisasi yang mengikuti
pipeline bawaan masing-masing backbone pretrained. Dengan pendekatan ini, hasil
evaluasi yang diperoleh dapat dibandingkan secara adil antar arsitektur karena
seluruh model menerima perlakuan preprocessing yang setara.
3.3.4 Model Training

Setelah pembagian data dan preprocessing, pemodelan dilakukan untuk
mengevaluasi performa dua arsitektur utama, yaitu CNN-based (YOLOV9) dan
Transformer-based (RT-DETRV2). Seluruh eksperimen menggunakan resolusi
input 640x640 piksel, jumlah epoch maksimum 500, serta konfigurasi pelatihan
yang konsisten untuk menjaga keadilan perbandingan. Mekanisme early stopping
diterapkan berdasarkan nilai validation Joss untuk mengendalikan proses pelatihan
dan mencegah overfitting. Proses pelatihan dihentikan apabila tidak terjadi
perbaikan nilai validation loss selama sejumlah epoch tertentu sesuai parameter
patience. Evaluasi performa dilakukan pada setiap epoch menggunakan data
validation, dan bobot model terbaik dipilih berdasarkan nilai mAP50-9S tertinggi
yang dicapai.
3.3.4.1 Model berbasis CNN

YOLOv9 menggunakan backhone Generalized Efficient Layer Aggregation
Network (GELAN) untuk ekstraksi fitur, neck FPN/PAN untuk fusi fitur multi
skala, serta detection head untuk prediksi hounding box dan kelas objek pada tiga
skala. Selama pelatihan, mekanisme Programmable Gradient Information (PGT)
digunakan untuk menjaga kelancaran aliran gradien. Ringkasan arsitektur YOLOv9

disajikan pada Tabel 3.4.
Tabel 3.4 Arsitektur YOLOv9

Block Taput Size Output Size Keterangan

Input dan | (3, 640, 640) | “6, 640, 6407 | Resize 690x640 dan normalisasi piksel
Normalization 01

Backbone |, 640, 640) | (CT, 320, 320) | Eksiraks Ttur awal downsample x2)
(GELAN) - 81
Backbone -S2 | (C1, 320,320) | (C2, 160, 160) | Blok Konvolusi berulang (downsample

x2)
Backhone 83 | (C2, 160, 160) | (C3, 80, 80) Fitur menengah (calon P3)
Backbone-S4| (C3,80,80) | (C4, 40, 40) Fitur tinggi (calon Pa)
s1

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 65

SKRIPSI

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Block Taput Size Output Size Keterangan
Backhone-s5| (C4, 40,40) | CS (oride 32) | Fitur semantik dalam (calon PS)
Neck (C3, C4.C5) | (P3, P4, PS) | Fusi top-down dan bottom-up untuk
(EPN/PAN) rmulti-skala
Detection | (P3,P4,P3) | Kotak + ols par | Prediksi bounding box dan kelas pada
Head skala tiga skala (P3/P4/P5)

Penelitian ini menggunakan tiga skala yang mewakili rentang kapasitas, yaitu

S (small) sebagai kelas kecil, M (medium) sebagai kelas menengah, dan C
(compact) sebagai kelas besar. Pemilihan ketiga varian tersebut bertujuan untuk
menangkap kompromi antara akurasi, latensi, dan kebutuhan komputasi secara
menyeluruh, mulai dari skenario perangkat dengan sumber daya terbatas hingga
konfigurasi berkapasitas lebih besar yang menargetkan akurasi maksimal. Rincian
tipe yang diuji dijelaskan pada Tabel 3.5.

Tabel 3.5 Tipe Model YOLOv9 yang Diuji

Tipe “Tunilah Parameter (dalam Juta)
YOLOWS KAI
YOLOW-M 20
YOL00: 253

Pada pemodelan YOLOV9, proses optimisasi difokuskan pada learning rate,
batch size, momentum, dan weight decay, karena keempat parameter tersebut paling
berpengaruh terhadap stabilitas pelatihan dan kecepatan konvergensi pada
arsitektur berbasis CNN. Parameter lain dijaga konstan untuk memastikan keadilan
perbandingan, termasuk resolusi input 640x640 dan skema augmentasi data yang
seragam. Optimizer yang digunakan adalah Stochastic Gradient Descent (SGD)
dengan cosine learning rate decay dan warm-up singkat, serta Exponential Moving
Average (EMA) untuk meningkatkan stabilitas bobot model. Pencarian kombinasi
hyperparameter dilakukan menggunakan Optuna dengan Tree-structured Parzen
Estimator (TPE) dan mekanisme early stopping untuk efisiensi komputasi. Rincian
tuang pencarian hyperparameter ditampilkan pada Tabel 3.6.

Tabel 3.6 Hyperparameter Tuning Model YOLOY9
Parameter Nila
‘Optimizer ‘SGD
Tearning Rate [o0001; 0017
Batch Size 16: 321
‘Momentum 10.80: 0.97]
Weight Decay 00001: 0,003]
‘Scheduler Cosine Annealing
Epoeh 500
Tmage Size Tanea
Random Seed 7

52
PERBANDINGAN METODE DAN.

ARKAN SYAFIQ ATTAOY


## Halaman 66

SKRIPSI

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

3.3.4.2 Model berbasis Transformer
RT-DETRv2 merupakan model deteksi objek end-to-end berbasis

Transformer yang mengombinasikan backbone CNN multi-skala dengan encoder-

decoder Transformer untuk menghasilkan prediksi bounding box dan kelas secara

langsung tanpa post-processing NMS. Arsitektur RT-DETRV2 yang digunakan

dalam penelitian ini dirangkum pada Tabel 3.7.

Tabel 3.7 Arsitektur RT-DETRV2

Block Input Size —| Output Size Kelerangan
Taput dan | @, 640, 640) TG, 640, 640) | Dynanilo multscale saat training,
Normaizatlon mormalsasi intensitas.
Backhone-C3 |G, 640, 640) | (C3, 80, | Far tingkat menengah ride
Backbone - C4 (C3, 80, 80) (C4, 40, 40) Fitur tingkat tinggi (véride 16).
Zackhone-CS | (C4, 40, 40) | (C3, 04, C5} | Fitur semamik dalam (stride 32)
Pasidonal 7 MC C4, C5} | {E3, B4, 5} | Penyandian posisi spasial untuk
Encoding Transformer.
fieienvtiybrid | (83, 84, ES) | Pased multi | Agregas fur mult-skafa yang
Encoder scale efisen
Query Selection | Fused features | Q(N_query x | Seleksl query kandidat TOT aware)
D)
Transformer Dar | Carey | —Penyempurnaan query beringkar
Decoder (L) D)
TPredicton T Kotak “Kelas | Predikat end-to-end (anpa NIS pada
Head inferensi: one-to-one matching saat
‘ralning)

Penelitian ini menggunakan tiga varian kapasitas RT-DETRv2, yaitu S

(small), M (medium), dan L (large), yang dipadankan dengan tiga kelas kapasitas
pada YOLOv9. Seluruh varian dilatih dan dievaluasi pada resolusi input yang sama,
dengan prosedur evaluasi yang identik. Rincian varian model RT-DETRV2 yang
diuji disajikan pada Tabel 3.8.

Tabel 3.8 Tipe Model RT-DETRv2 yang Diuji

Tipe Jumlah Parameter (dalam juta)
REDETRD-S 20
RT-DETRY2-M 31
RT-DETRY2L 22

Optimisasi RT-DETRv2 dilakukan menggunakan AdamW dengan linear
warm-up yang diikuti oleh cosine decay. Perbedaan kebutuhan memori antar varian
model diimbangi melalui penerapan gradient accumulation agar effective batch size
tetap sebanding. Proses pencarian learning rate dan batch size dilakukan

menggunakan Optuna dengan early stopping.

Tabel 3.9 Hyperparameter Tuning Model RT-DETRV2
Parameter Nilal
‘Optimizer Adam.

33

PERBANDINGAN METODE DAN.

ARKAN SYAFIQ ATTAOY


## Halaman 67

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Parameter Nila
Learning Rate [o,00008; 0.00061
Batch Size 26: 321
‘etal 09
BetaZ 0,999,
Weight Decay 100001: 0,001]
Gradient Clip Norm 1
‘Scheduler Cosine Annealing
Epoch 500
Tmage Size 0x64
Random Seed a2

3.3.5 Model Performance Evaluation

Perbandingan kinerja YOLOv9 dan RT-DETRv2 mempertimbangkan
dimensi akurasi serta efisiensi waktu dengan pendekatan Pareto Frontier pada
perangkat keras, resolusi masukan, dan prosedur preprocessing yang seragam.
Evaluasi dilakukan pada skenario deteksi multiobjek sesuai format anotasi COCO.
Prosedur evaluasi dirumuskan sebagai berikut.
1. Pengumpulan metrik akurasi dan waktu inferensi

Setiap model dievaluasi pada test set yang identik untuk memperoleh metrik
akurasi berupa mAP50-95 dan mAPSO sesuai standar evaluasi pada format COCO.
Selain akurasi, penelitian ini juga mengukur efisiensi inferensi untuk menilai
“kemampuan model dalam memproses citra secara real-time. Waktu inferensi diukur
pada batch size 1 dengan warm-up singkat, kemudian dihitung rata-rata waktu
pemrosesan per citra (latensi). Pengukuran dilakukan minimal pada 100 iterasi
“untuk memperoleh estimasi yang stabil, tanpa memasukkan waktu pemuatan data.
Selain nilai rata-rata, dilaporkan juga nilai median (PSO) dan persentil ke-95 (P95)
untuk menggambarkan kestabilan waktu inferensi.

Sebagai indikator throughput sistem, penelitian ini juga melaporkan Frames

Per Second (FPS) yang menunjukkan jumlah citra yang dapat diproses model dalam
satu detik. FPS dihitung berdasarkan nilai latensi rata-rata sebagaimana dirumuskan
pada Persamaan (3.1).

1000

Ba en GAS

Gu)

Pelaporan latensi dan FPS secara bersamaan memberikan gambaran yang lebih
komprehensif mengenai efisiensi model, karena latensi menunjukkan waktu

54
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 68

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

pemrosesan satu citra, sedangkan FPS merepresentasikan kapasitas pemrosesan
berkelanjutan dalam skenario real-time. Selain itu, sebagai indikator kompleksitas
komputasi, dicatat pula jumlah parameter model dan Floating Point Operations
(FLOPs). Dengan pendekatan ini, evaluasi performa tidak hanya
mempertimbangkan akurasi deteksi, tetapi juga efisiensi komputasi yang relevan
‘untuk implementasi sistem pada lingkungan nyata.
2. Pembentukan Pareto Frontier

Berdasarkan hasil pengujian, pasangan nilai mAP dan latensi pada resolusi
640x640 diplot untuk membentuk Pareto Frontier. Frontier menandai konfigurasi
yang Pareto-optimal, yakni kombinasi yang memberikan keseimbangan terbaik
antara akurasi dan waktu inferensi dibandingkan alternatif lainnya.
3. Analisis Perbandingan

Konfigurasi yang berada pada frontier dikategorikan sebagai solusi Pareto-
optimal. Apabila dua konfigurasi menghasilkan nilai mAP yang sebanding,
prioritas diberikan pada konfigurasi dengan latensi lebih rendah. Sebaliknya,
apabila latensi relatif setara, konfigurasi dengan nilai mAP lebih tinggi dipilih.
Konfigurasi di luar frontier dianggap kurang efisien karena terdapat alternatif lain
yang lebih unggul pada setidaknya satu dimensi, yaitu akurasi atau latensi.
Kesetaraan kondisi eksperimen dijaga melalui penggunaan resolusi inferensi
640x640, skema augmentasi dan normalisasi yang seragam, presisi komputasi yang
sama, serta penggunaan seed tetap guna menjamin reprodusibilitas hasil
33.6 Web App Implementation

Implementasi Implementasi prototipe aplikasi weh pada penelitian ini
dikembangkan dalam bentuk sistem bernama Visual Intelligence for Car Damage
Detection (VIDI). VIDI merupakan prototipe aplikasi berbasis computer vision
yang dirancang untuk melakukan deteksi kerusakan kendaraan secara otomatis
melalui citra digital. Sistem ini memanfaatkan model deep learning berbasis object
detection untuk mengidentifikasi dan melokalisasi berbagai jenis kerusakan
kendaraan, yaitu dent, scratch, crack, glass shatter, lamp broken, dan tire flat.
Pengembangan VIDI bertujuan menyediakan antarmuka interaktif yang

memungkinkan pengguna non-teknis melakukan analisis kondisi kendaraan secara

55
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 69

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

otomatis melalui unggahan citra kendaraan. Sistem dirancang untuk mendukung
proses inspeksi awal berbasis visual yang berpotensi membantu teknisi bengkel,
(perusahaan asuransi, serta lembaga pembiayaan kendaraan dalam mengidentifikasi
kerusakan kendaraan secara cepat dan konsisten. Proses pengembangan prototipe
mengacu pada tahapan model prototipe sebagaimana ditunjukkan pada Gambar
2.19, yang mencakup lima fase utama yaitu communication, quick plan, modeling,

construction, serta deployment, delivery, dan feedback,

3.3.6.1 Communication

Tahap Communication berfokus pada pengumpulan kebutuhan dan
pemahaman konteks penggunaan sistem melalui identifikasi masalah utama,
ekspektasi pengguna, serta batasan teknis yang berpengaruh pada rancangan. Hasil
tahap ini berupa daftar kebutuhan fungsional dan non-fungsional sebagai dasar
pengembangan prototipe. Sasaran utama prototipe adalah sistem deteksi kerusakan
mobil pada enam kelas (dent, scratch, crack, glass shatter, lamp broken, dan tire
flat) dengan dua arsitektur model, yaitu YOLOV9 berbasis CNN dan RT-DETRV2
berbasis hybrid CNN-Transformer. Karakteristik pengguna mencakup teknisi
bengkel, petugas asuransi, dan lembaga pembiayaan kendaraan. Antarmuka
dirancang agar sederhana, mudah dioperasikan oleh pengguna non-teknis, dan
mampu menyajikan hasil deteksi yang informatif. Kesetaraan kondisi uji terhadap
distribusi data training CarDD dijaga guna meminimalkan domain shifi. Pengguna
diwajibkan mengunggah citra kendaraan dari empat sisi utama, yaitu sisi depan,
belakang, kanan, dan kiri. Ketentuan tersebut memastikan area kerusakan yang
terdeteksi bersifat representatif serta mengurangi potensi occlusion maupun variasi
sudut pandang ekstrem. Rincian kebutuhan fungsional yang menjadi dasar

rancangan sistem ditunjukkan pada Tabel 3.10.
Tabel 3.10 Kebutuhan Fungsional Prototipe

No Fitur Fungsional:
1 | Navigasi Beranda via Logo | Pengguna dapat menekan logo untuk Kembali ke halaman
beranda,
2 | Mom Daftar Kelas | Pengguna dapat membuka mena “Daftar Kelas
Kerusakan” Kerusakan” untuk melihat ringkasan enam kelas yang
digunakan.
3 | Unggah Citra pada Halaman | Pengguna dapat membuka menu “Deteksi Kerusakan”
Deteksi ‘kemudian mengunggah empat cita sisi depan, belakang,
56

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 70

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Ne Tiar Fungsional
Kiri, dan kanan) kendaraan berformat JPG pada halaman
deteksi

© | Tombol “Deteksi| Pengguna dapat mengklik tombol “Deteksi Kerusakan™

Kerusakan" ‘untuk memulai proses deteksi kerusakan mobil

ST Tampilan Hasil Dersksi Pengguna dapat melihat hasil deteksi berupa Satu atau
lebih hounding bor, label kelas, serta skor kepercayaan,

@ | Undah Hasit Pengguna dapat mengunduh hasil dalam bentuk gambar
'beranotasi dalam format JPG.

336.2 Quick Plan

Tahap Quick Plan bertujuan menyusun rencana kerja awal berdasarkan hasil
komunikasi dan analisis kebutuhan. Perencanaan dilakukan untuk menetapkan
prioritas fitur, urutan pengembangan modul, serta estimasi iterasi pengujian.
Rencana pengembangan difokuskan pada tiga komponen utama yang saling
berkaitan, yaitu fungsi input, deteksi, dan ouput. Tahap pertama mencakup
mekanisme unggah citra kendaraan dengan validasi format dan ukuran berkas untuk
memastikan kesesuaian data masukan dengan spesifikasi sistem. Tahap berikutnya
berfokus pada integrasi model terlatih dalam format siap pakai (ready-to-use
inference) yang memungkinkan proses deteksi berjalan otomatis tanpa memerlukan
interaksi teknis dari pengguna. Sementara itu, tahap keluaran mencakup
perancangan tampilan hasil deteksi yang menyajikan bounding box, label kelas,
serta skor kepercayaan, disertai dengan fitur unduhan hasil dalam format JPG agar
pengguna dapat menyimpan keluaran deteksi secara langsung. Seluruh perencanaan
bersifat adaptif dan dilakukan secara iteratif, di mana setiap versi prototipe yang
dihasilkan akan diuji, dievaluasi, dan disempurnakan berdasarkan umpan balik
pengguna.
33.63 Modeling

Tahap Modeling berfokus pada penerjemahan hasil analisis kebutuhan dan
perencanaan kerja menjadi rancangan konseptual sistem. Perancangan ini
mencakup dua aspek utama, yaitu logika alur kerja sistem dan tampilan antarmuka
pengguna. Pada aspek logika, disusun flowchart sistem yang menggambarkan
'hubungan antar-komponen mulai dari unggahan citra hingga proses inferensi dan

penyajian hasil deteksi. Flowchart tersebut ditampilkan pada Gambar 3.2.

57
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 71

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Gambar 3.2 Cara Kerja Sistem

Selain alur logika, tahap ini juga menghasilkan rancangan antarmuka
menggambarkan struktur tampilan halaman aplikasi web. Rancangan ini disusun
untuk memastikan kemudahan navigasi, konsistensi antarhalaman, dan kejelasan
informasi yang disajikan. Gambar 3.3 hingga Gambar 3.5 menampilkan rancangan
konseptual dari tiga halaman utama aplikasi, yaitu halaman beranda, daftar kelas
kerusakan, dan halaman deteksi kendaraan.

Gambar 3.3 Halaman Utama

58
SKRIPSI PERBANDINGAN METODE DAN... 'ARKAN SYAFIQ ATTAOY


## Halaman 72

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Gambar 3.3 memberikan gambaran umum tujuan aplikasi serta petunjuk
singkat agar pengguna memahami alur kerja prototipe.

: =

Gambar 3.4 Halaman Daftar Kelas Kerusakan
Gambar 3.4 menyajikan ringkasan enam kelas kerusakan utama disertai

deskripsi ringkas untuk membantu pengguna mengenali hasil keluaran model

Gambar 3.5 Halaman Deteksi Kerusakan
Gambar 3.5 pengguna dapat mengunggah citra kendaraan, menekan tombol
Deteksi, kemudian memperoleh hasil visual hounding box, label kelas, dan skor
kepercayaan. Tersedia pula tombol unduh untuk menyimpan gambar beranotasi
dalam format JPG.
33.64 Construction of Prototype
Tahap Construction of Prototype merupakan fase implementasi rancangan
konseptual menjadi prototipe sistem yang dapat dijalankan. Implementasi
dilakukan berdasarkan rancangan alur logika dan antarmuka pengguna yang telah
disusun pada tahap Modeling (Gambar 3.3-3.5). Tahap ini mencakup proses
integrasi komponen fungsional utama, yaitu frontend antarmuka berbasis Streamlit,

59

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 73

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

backend inferensi model YOLOv9 dan RT-DETRv2, serta manajemen data
masukan dan keluaran. Model deteksi YOLOv9 dan RT-DETRv2 disiapkan dalam
format ready-to-use inference agar dapat dipanggil secara langsung melalui
antarmuka web. Integrasi dilakukan dengan mengonversi model ke format ringan
(exported weights) dan menautkannya ke fungsi inferensi Streamlit menggunakan
(pustaka pendukung seperti torch dan openev. Pipeline inferensi disusun dalam tiga
tahap utama: (1) pemuatan model dan inisialisasi session, (2) praproses citra
meliputi resize, normalisasi, dan konversi ke tensor, serta (3) pemanggilan model
untuk menghasilkan prediksi berupa hounding box, label kelas, dan skor
kepercayaan.

Antarmuka pengguna diimplementasikan untuk menampilkan empat area
“unggahan citra kendaraan (depan, belakang, kanan, kiri) yang disertai validasi
format (JPG) dan ukuran berkas maksimum. Setelah citra diunggah, sistem secara
otomatis menampilkan pratinjau serta menonaktifkan tombol deteksi apabila
jumlah unggahan kurang dari empat sisi. Hasil inferensi ditampilkan pada bidang
keluaran dalam bentuk gambar beranotasi, di mana setiap deteksi diberi label kelas
dan nilai kepercayaan. Pengguna dapat mengunduh hasil dalam format JPG melalui
tombol “Unduh Hasil”. Setelah seluruh komponen terintegrasi, dilakukan pengujian
internal untuk memastikan stabilitas fungsi, kesesuaian keluaran dengan data
training, serta kecepatan inferensi. Uji coba dilakukan pada beberapa variasi ukuran
berkas dan resolusi untuk menilai waktu pemrosesan rata-rata dan potensi
bottleneck komputasi. Temuan dari pengujian internal digunakan untuk melakukan
optimasi, seperti penyetelan ulang ukuran batch, pengurangan latensi antarmuka,
dan penyempurnaan tampilan hasil agar lebih informatif. Tahap ini menghasilkan
prototipe fungsional yang telah mampu menjalankan proses deteksi kerusakan
kendaraan melalui antarmuka weh secara end-to-end.

33.65 Deployment, Delivery, dan Feedback

Tahap Deployment, Delivery, dan Feedback memfokuskan penyediaan
prototipe kepada pengguna uji, pelaksanaan pengujian terstruktur, serta
pengumpulan dan pemrosesan umpan balik sebagai dasar iterasi berikutnya.
Prototipe yang telah memenuhi kriteria performa pada evaluasi internal

60

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 74

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

didistribusikan dalam bentuk aplikasi berbasis weh disertai panduan singkat
penggunaan. Skenario penggunaan ditetapkan konsisten dengan ketentuan input
empat sisi kendaraan (depan, belakang, kiri, dan kanan) dalam format JPG,
sehingga hasil pengujian dapat dibandingkan secara seragam serta selaras dengan
asumsi data pada tahap perancangan. Pengujian fungsional dilakukan menggunakan
pendekatan black-box testing untuk memverifikasi kesesuaian fungsi sistem
terhadap spesifikasi kebutuhan pengguna tanpa mempertimbangkan struktur
internal model. Rancangan skenario pengujian ditunjukkan pada Tabel 3.11

Tabel 3.11 Tabel Rancang Uji Black Bar

No Pengujian Hasil yang diharapkan

1 | Klikiogo beranda. Sistem kembali ke halaman beranda tanpa galat

2 Buka “Daftar — Kelas | Halaman menampilkan 6 kelas beserta ringkasan

Kerusakan"

3 | Buka“Deteksi Kenusakan” | Halaman deteksi terbuka dan siap menerima
unggahan

4 Unggah citra GPG) Pratinjau citra tampit, format dan ukuran tervalidasi

‘S| dalankan deteksi Citra beranotasi ditampilkan, jika terdapat lebih dari
satu kerusakan, sistem menampilkan seluruh
hounding box “beserta label kelas dan skor
ikepereayaan.

6 Unduh hasil Berkas keluaran (JPG) dapat diunduh dengan benar

Kegunaan (usability) aplikasi weh dievaluasi menggunakan SUS. Instrumen
SUS terdiri dari 10 pernyataan berskala Likert diisi oleh 10 responden. Responden
berasal dari tiga latar belakang profesi dalam proses inspeksi kendaraan, yaitu tiga
(pegawai lembaga pembiayaan kendaraan, tiga pegawai perusahaan asuransi umum,
dan empat teknisi bengkel resmi yang berinteraksi langsung dengan hasil deteksi
kerusakan. Seluruh responden memiliki pengalaman profesional yang berkaitan
dengan inspeksi kendaraan, penilaian klaim asuransi, atau proses perbaikan
kendaraan, sehingga memahami karakteristik kerusakan otomotif yang relevan
dengan konteks penggunaan sistem. Skor SUS dihitung dengan menyesuaikan butir
positif dan negatif sesuai ketentuan, kemudian hasil penjumlahan dikalikan 2,5
sehingga berada pada rentang 0-100. Nilai akhir ditafsirkan untuk menentukan
tingkat kegunaan prototipe. Rancangan butir penilaian dijelaskan pada Tabel 3.12.

61

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 75

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Tabel 3.12 Rancangan Kuesioner System Usability Scale (SUS)

Skala
sis [7s | N ps ss

No Pertanyaan

T | Saya berpotensi sering menggunakan “aplikasi
deteksi kerusakan ini

2 Memurar saya, aplikasi int Terasa terlalu rumit alan
berlebihan fiturnya

3 Aplikasi ini mudah dinavigasi dan dipelajari cara
pakainya

@ (saya memerikan bantuan teknis untuk dapat
‘menggunakan aplikasi ini

itur-itur yang tersedia Terasa dirancang dan

disusun dengan baik:

@ | Saya menemukan adanya keridakkonsistenan pada
tampilan atau Fungsi aplikasi

7 | Kebanyakan orang, menurdi Saya, akan cepat
memahami cara menggunakan aplikasi ini

| Aplikasi ini terasa menyulitkan untuk dijelajahi

9 | Saya merasa percaya diri ketika menggunakan
aplikasi ini

TO | Saya perlu mempelajari banyak hal terlebih dahulu
sebefum dapat menggunakan aplikasi ini

Setelah seluruh responden mengisi kuesioner, nilai SUS per responden
dihitung menggunakan Persamaan (2.18), kemudian nilai akhir SUS kelompok
diperoleh dengan merata-ratakan seluruh nilai responden sesuai Persamaan (2.19).
Nilai akhir tersebut selanjutnya diinterpretasikan pada skema tingkat kegunaan
sebagaimana ditunjukkan pada Gambar 2.21

62
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 76

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

BABIV
HASIL DAN PEMBAHASAN

41 Data Collection

Dataset yang digunakan dalam penelitian ini adalah Car Damage Detection
Dataset (CarDD) yang diperkenalkan oleh CarDD: A New Dataset for Vision-
Based Car Damage Detection. Dataset ini dirancang khusus untuk tugas deteksi
kerusakan kendaraan berbasis computer vision dan telah banyak digunakan sebagai
benchmark pada penelitian deteksi kerusakan otomotif. CarDD terdiri dari 4.000
citra dengan lebih dari 8.000 instance kerusakan yang terbagi dalam enam kelas,
yaitu crack, dent, seratch, glass shatter, lamp broken, dan tire flat. Setiap citra dapat
mengandung lebih dari satu instance kerusakan (multi-object), sehingga satu
gambar dapat memiliki beberapa bounding box dengan kelas yang berbeda. Struktur
anotasi berbasis COCO memungkinkan evaluasi performa model menggunakan

metrik standar deteksi objek seperti mean Average Precision (mAP).

Gambar 4.1 Contoh Citra Dataset CarDD dengan Anotasi Bounding Box

Gambar 4.1 menampilkan contoh citra kendaraan pada dataset CarDD yang
telah dilengkapi anotasi hounding box untuk menandai lokasi kerusakan.
Karakteristik dataset menunjukkan bahwa kerusakan kendaraan umumnya
memiliki ukuran relatif kecil dengan variasi bentuk, tekstur, dan tingkat keparahan

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 77

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

yang berbeda. Variasi kondisi pencahayaan, sudut pengambilan gambar, serta
refleksi permukaan bodi kendaraan juga menjadi tantangan tersendiri dalam proses
deteksi objek
42 Data Splitting

Tahap data splitting dilakukan untuk membagi dataset ke dalam subset data
train, data validation, dan data testing guna mendukung proses pelatihan serta
evaluasi model secara objektif. Pembagian dataset ini mengikuti struktur
pembagian yang disediakan dalam dataset CarDD, dengan proporsi sekitar 70%
data rain, 20% data validation, dan 10% data test. Ringkasan jumlah citra dan
jumlah instance kerusakan pada masing-masing subset ditunjukkan pada Tabel 4.1.
Tabel 4.1 Jumlah Cita dan Instance Kerusakan pada Subset Dataset CarDD.

‘Subset Data Jumlah Citra Jumlah Instance (Bounding Box)
Train 2816 6211

Validation So Tad
Test 374 785
Total 4.000 E740,

Berdasarkan Tabel 4.1, data train memiliki jumlah citra dan instance terbesar,
sehingga cukup representatif untuk proses pembelajaran model. Data validation
digunakan untuk memantau kinerja model selama pelatihan, sedangkan data testing
digunakan untuk mengevaluasi performa akhir model pada data yang belum pernah

dilihat sebelumnya.

Distribusi Jumlah Citra per Split Dataset

2000
7
2 00

Gambar 4.2 Distribusi Jumlah Citra per Split Dataset
Gambar 4.2 memperlihatkan distribusi jumlah citra pada masing-masing
subset dataset. Terlihat bahwa data train mendominasi dengan 2.816 citra (70%

dari total dataset), diikuti oleh validation sebanyak 810 citra (#2074) dan test

64

SKRIPSI PERBANDINGAN METODE DAN... 'ARKAN SYAFIQ ATTAOY


## Halaman 78

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

sebanyak 374 citra (4109). Proporsi ini sesuai dengan praktik umum pada
pelatihan model deep learning karena menyediakan data yang cukup besar untuk
proses pembelajaran sekaligus mempertahankan data independen untuk validasi
dan pengujian.

Distribusi Jumlah Instance per Split Dataset

umah nsance(ownding Bo)

Train Voteration “Test

Gambar 4.3 Distribusi Jumlah fnstanee per Split Dataset

Gambar 4.3 memperlihatkan distribusi jumlah instance pada masing-masing
subset dataset. Terlihat bahwa jumlah instance pada data train mencapai 6.211,
sedangkan pada data validation dan test masing-masing berjumlah 1.744 dan 785
instance. Jumlah instance yang lebih besar dibandingkan jumlah citra menunjukkan
bahwa satu citra dapat mengandung lebih dari satu objek kerusakan kendaraan yang
direpresentasikan melalui beberapa anotasi bounding box.

istibusi instance per kelas

§

Jumiahinsance tbewneng bani

Gambar 44 Distribusi Jumlah Instance per Kelas
Gambar 4.4 memperlihatkan distribusi jumlah instance kerusakan pada setiap

kelas untuk seluruh subser dataset. Secara umum terlihat bahwa kelas scratch dan

6s

SKRIPSI PERBANDINGAN METODE DAN... 'ARKAN SYAFIQ ATTAOY


## Halaman 79

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

dent memiliki jumlah instance paling dominan dibandingkan kelas lainnya pada
seluruh subset, Sebaliknya, kelas tire flat memiliki jumlah instance yang relatif
lebih sedikit sehingga dapat dianggap sebagai kelas minoritas. Distribusi kelas pada
subset validation dan fest menunjukkan pola yang relatif konsisten dengan subset
train, di mana kelas yang dominan pada data pelatihan tetap memiliki
kecenderungan dominan pada data validasi dan pengujian. Konsistensi distribusi ini
menunjukkan bahwa proses pembagian dataset dilakukan secara proporsional
sehingga karakteristik data pada masing-masing subset tetap representatif terhadap
(keseluruhan dataset.

Secara kuantitatif, rasio antara kelas dengan jumlah instance terbesar dan
terkecil berada pada kisaran lebih dari tiga kali lipat, yang mengindikasikan adanya
ketidakseimbangan kelas pada tingkat moderat. Kondisi ini umum dijumpai pada
(permasalahan deteksi kerusakan kendaraan di dunia nyata, di mana beberapa jenis
kerusakan seperti seratch dan dent lebih sering terjadi dibandingkan kerusakan
lainnya. Kondisi distribusi data tersebut menunjukkan bahwa dataset memiliki
karakteristik yang cukup representatif untuk pelatihan model deteksi objek,
meskipun terdapat ketidakseimbangan kelas pada beberapa kategori kerusakan.
Oleh karena itu, proses pelatihan dan evaluasi model pada penelitian ini dilakukan
dengan mempertimbangkan karakteristik distribusi data tersebut agar performa
model dapat dievaluasi secara lebih objektif.

43 Data Preprocessing

Tahap data preprocessing dilakukan untuk memastikan data siap digunakan
dalam proses pelatihan model deteksi objek. Preprocessing difokuskan pada
penyesuaian format data, pemeriksaan anotasi, serta penerapan augmentasi data
untuk meningkatkan variasi data train. Dataset CarDD digunakan dalam format
COCO dengan anotasi hounding box. Setiap citra dapat memiliki lebih dari satu
bounding box, dengan rata-rata sekitar dua instance kerusakan per citra. Ringkasan
statistik jumlah bounding box per citra ditunjukkan pada Tabel 4.2.

Tabel 4.2 Statistik Jumlah Bounding Bax per Citra pada Dataset CarDD.

‘Subset Data | Rata-rata Bounding Box Median Maksimam
Training 221 2 13
Validation 215 2 12
Testing 2.10 2 13
66

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 80

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Teknik augmentasi data diterapkan pada data train untuk meningkatkan
kemampuan generalisasi model dan mengurangi risiko overfitting. Augmentasi
dilakukan dengan mempertahankan kesesuaian antara citra dan anotasi bounding
box. Teknik yang digunakan meliputi horizontal flipping, HSV, serta penyesuaian
kecerahan dan kontras. Augmentasi hanya diterapkan pada data train, sedangkan
data validation dan data test digunakan dalam kondisi asli. Contoh hasil penerapan
data augmentation ditunjukkan pada Gambar 4.5.

Gambar 4.5 Contoh Hasil Penerapan Data Augmentation pada Citra CarDD.

Berdasarkan Gambar 4.5(a), terlihat bahwa penerapan horizontal flipping
menghasilkan citra dengan orientasi terbalik secara horizontal tanpa mengubah
posisi relatif hounding box terhadap objek kerusakan. Transformasi ini
meningkatkan variasi spasial data pelatihan, khususnya terhadap posisi kerusakan
pada sisi kiri dan kanan kendaraan. Dengan augmentasi ini, model diharapkan tidak

4.S(b), ditunjukkan hasil transformasi warna melalui penyesuaian komponen HSV

serta perubahan kecerahan dan kontras. Augmentasi ini menghasilkan variasi
intensitas warna dan pencahayaan tanpa menghilangkan karakteristik visual utama
kerusakan. Transformasi ini penting untuk meningkatkan ketahanan model
terhadap variasi kondisi pencahayaan, refleksi cahaya, serta perbedaan kualitas citra
yang umum terjadi pada data lapangan. Secara keseluruhan, kedua teknik
augmentasi tersebut bertujuan untuk memperkaya keragaman visual data pelatihan
tanpa mengubah anotasi bounding box secara semantik. Dengan demikian, model
diharapkan mampu mempelajari fitur kerusakan yang lebih robust terhadap variasi
posisi dan kondisi pencahayaan, sehingga mengurangi risiko overfitting dan

meningkatkan kemampuan generalisasi pada data test.

67

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 81

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

44 Model Training

Bagian ini menyajikan hasil proses pelatihan model deteksi kerusakan
kendaraan menggunakan dua arsitektur, yaitu YOLOv9 dan RT-DETRv2. Seluruh
eksperimen dilakukan menggunakan dataset CarDD dengan konfigurasi pelatihan
yang konsisten untuk menjaga keadilan perbandingan. Optimisasi kyperparameter
dilakukan menggunakan Optuna dengan pendekatan Bayesian Optimization.
Evaluasi selama pelatihan difokuskan pada perkembangan nilai Joss serta metrik
mAPSO dan mAPS50-95 pada data validation. Konfigurasi terbaik dari masing-
masing arsitektur dipilih berdasarkan performa validasi tertinggi dan selanjutnya
dianalisis melalui kurva pelatihan untuk mengamati stabilitas dan konvergensi
model. Reproduksibilitas eksperimen dijaga dengan penggunaan random seed 42
dengan jumlah epoch maksimum 500. Arsitektur YOLOv9 menggunakan optimizer
Stochastic Gradient Descent (SGD) dengan cosine learning rate schedule,
sedangkan RT-DETRv2 menggunakan AdamW dengan linear warm-up diikuti
cosine decay. Seluruh eksperimen dijalankan pada resolusi input 640x640 piksel
dengan konfigurasi augmentasi yang diseragamkan antar arsitektur. Optimisasi
hyperparameter pada setiap varian model dilakukan menggunakan Optuna dengan
jumlah 30 trial sebagai kompromi antara luas eksplorasi ruang hyperparameter dan
efisiensi biaya komputasi, mengingat setiap trial memerlukan proses pelatihan
'hingga mendekati kondisi konvergensi.
4.4.1 YOLOv9

Pelatihan YOLOv9 dilakukan pada tiga varian model, yaitu YOLOv9-S,
YOLOV9-M, dan YOLOv9-C. Setiap varian terlebih dahulu dilatih menggunakan
konfigurasi dasar, kemudian dilakukan optimis

si Ayperparameter untuk
memperoleh performa terbaik. Proses optimisasi hyperparameter dilakukan
menggunakan Optuna dengan pendekatan Bayesian Optimization. Hyperparameter
tuning difokuskan pada parameter yang memiliki pengaruh paling signifikan
terhadap stabilitas konvergensi dan performa model, yaitu learning rate, bateh size,
momentum, dan weight decay. Learning rate mengontrol besar langkah pembaruan
parameter model, sedangkan batch size mempengaruhi stabilitas estimasi gradien
dan efisiensi komputasi. Pada arsitektur berbasis CNN, momentum membantu

68
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 82

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

mempercepat konvergensi, sementara weight decay berfungsi sebagai regularisasi
untuk mengurangi overfitting. Pembatasan jumlah hyperparameter yang dituning
bertujuan menjaga ruang pencarian tetap terkontrol sehingga interpretasi hasil
eksperimen menjadi lebih jelas serta memastikan perbandingan yang adil antar
arsitektur.
4.4.1.1 YOLOV9-S

Model YOLOv9-S digunakan sebagai varian berkapasitas kecil untuk
merepresentasikan konfigurasi ringan dalam YOLOv9. Pelatihan awal dilakukan
menggunakan konfigurasi default tanpa optimisasi hyperparameter untuk
memperoleh performa baseline sebagai pembanding. Hasil evaluasi pada data
validation disajikan pada Tabel 4.3.
Tabel 4.3 Hasil Baseline Model untuk YOLOV9-S

Konfigurasi MmAPSO mAPS095
YOLOv9-S 0,65652, 0.52426,
Hasil baseline menunjukkan bahwa YOLOv9-S mampu mencapai mAP30-95

sebesar 0,52426 pada data validation. Nilai tersebut menunjukkan performa deteksi
yang cukup stabil untuk model berkapasitas kecil, namun masih terdapat ruang
peningkatan. Selanjutnya dilakukan optimisasi hyperparameter sebanyak 30 trial
menggunakan Optuna. Ringkasan lima konfigurasi terbaik berdasarkan nilai
MAPS0-95 pada data validation disajikan pada Tabel 4.4, sedangkan hasil seluruh
trial dapat dilihat pada Lampiran 1

Tabel 4.4 Hasil Hyperparameter Tuning dengan Optuna untuk YOLOV9-S

Baich | Tearnin WAPSO- | Train | Validation
Bek | Inah | iste. tae | APSO | Ss Loss | Loss
1 2s 32 00027 | 0.66952 | 053013 | 035350 | 0.61920
2 13 32 | 0,00084_| 0.67322 | o,s3aas | 0,35680 | 0,62340
3 18 32 | 0,00298 | 0.68649 | 0.54936 | 0,34890 | 0,62410
4 15 32 | 0,00383_| 0.68547 | 0.54204 | 0,35940 | 0,62K90
5 9 32__|o,o0211_[ 0.65913 0,52881 | 036120 | 0,62980

Berdasarkan Tabel 4.4, konfigurasi dengan peringkat pertama menghasilkan
nilai mAPSO sebesar 0,66952 dan mAPSO-95 sebesar 0,53914. Dibandingkan
dengan baseline, terjadi peningkatan sebesar 0,01488 pada metrik mAPS0-95.
Peningkatan ini menunjukkan bahwa penyesuaian hyperparameter memberikan
kontribusi terhadap peningkatan performa deteksi pada model berkapasitas kecil.
Meskipun terdapat trial lain yang menghasilkan nilai mAP50-9$ lebih tinggi,

69
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 83

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

pemilihan konfigurasi akhir mempertimbangkan keseimbangan antara performa
dan kestabilan validation loss. Trial 25 menunjukkan nilai validation loss yang
relatif lebih baik dan stabil dibandingkan konfigurasi lainnya, sehingga dipilih
sebagai model optimal. Pendekatan ini memastikan bahwa model yang terpilih
tidak hanya unggul secara numerik, tetapi juga menunjukkan pola pembelajaran
yang stabil serta kemampuan generalisasi yang lebih baik pada data validation.

i. sory Ma
os
os

En En

(Gambar 4.6 Kurva Hasil Pelatihan Model YOLOv9-S

Gambar 4.6 menampilkan kurva hasil pelatihan model YOLOv9-S
menggunakan konfigurasi Ayperparameter terpilih. Kurva training loss
menunjukkan penurunan yang konsisten seiring bertambahnya epoch, dari nilai
awal sebesar 1 pada epoch pertama hingga mencapai sekitar 0,3530 pada akhir
pelatihan. Penurunan ini mengindikasikan bahwa proses pembelajaran berlangsung
secara stabil dan parameter model mampu menyesuaikan diri dengan baik terhadap
data latih. Penurunan Joss yang relatif cepat terjadi pada fase awal pelatihan,
kemudian laju penurunannya menjadi lebih lambat pada epoch-epoch selanjutnya,
yang mencerminkan bahwa model mulai mendekati kondisi konvergensi. Pada sisi
validation, kurva validation loss juga menunjukkan pola penurunan yang cukup
signifikan pada tahap awal pelatihan, dari nilai awal sebesar 1 hingga mencapai
nilai minimum sekitar 0,61920 pada epoch ke-11. Setelah titik tersebut, nilai
vatidation loss menunjukkan fluktuasi ringan dengan nilai akhir sekitar 0,66732,
yang mengindikasikan bahwa model telah mencapai titik pembelajaran optimal
terhadap data validasi dan pelatihan lanjutan tidak memberikan peningkatan yang
signifikan terhadap kemampuan generalisasi model. Sejalan dengan pola tersebut,
metrik evaluasi deteksi objek menunjukkan peningkatan performa yang cukup pesat

70

SKRIPSI PERBANDINGAN METODE DAN... 'ARKAN SYAFIQ ATTAOY


## Halaman 84

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

(pada tahap awal pelatihan. Pada epock ke-1 1, model mencapai nilai mAPSO sebesar
0,695 dan mAP50-95 sebesar 0,5391, yang menandai titik performa optimal pada
data validasi. Pada akhir proses pelatihan, nilai metrik meningkat sedikit menjadi
MAPS0 sebesar 0,6828 dan mAP50-95 sebesar 0,5468, namun peningkatan tersebut
relatif kecil sehingga kurva metrik cenderung menunjukkan pola plateau. Kondisi
ini menunjukkan bahwa model telah mencapai performa yang stabil pada rentang
epoch tersebut dan proses pelatihan selanjutnya tidak memberikan peningkatan
performa yang signifikan.
441.2 YOLOv9-M

Model YOLOv9-M digunakan sebagai varian berkapasitas menengah dalam
YOLOV9. Pelatihan awal dilakukan menggunakan konfigurasi default dengan
ukuran citra 640x640 tanpa optimisasi hyperparameter untuk memperoleh
performa baseline sebagai pembanding. Hasil evaluasi pada data validation

disajikan pada Tabel 4.5
Tabel 4.5 Hasil Baseline Model untuk YOLOW9-M.

Konfigurasi mAPSO THAPSO-95
YOLOv?-M 0.67805 0.54055
Hasil baseline menunjukkan bahwa YOLOv9-M menghasilkan performa

yang lebih tinggi dibandingkan YOLOV9-S baseline, dengan mAPS0-95 sebesar
0,54055. Peningkatan ini menunjukkan bahwa kapasitas model yang lebih besar

memberikan kemampuan representasi fitur yang lebih baik dalam mendeteksi
kerusakan kendaraan. Selanjutnya dilakukan optimisasi Ayperparameter sebanyak
30 trial menggunakan Optuna. Ringkasan lima konfigurasi terbaik disajikan pada
Tabel 4.6, sedangkan hasil lengkap seluruh tia! dapat dilihat pada Lampiran 2.
Tabel 4.6 Hasil Hyperparameter Tuning dengan Optuna untuk YOLOV9-M

‘Batch | Learal WAPS0- | Train | Validation
Rank | Telat | Sice ‘gue mars | Se Loss | Loss
1 26 16 1 0.00273 | 0,70320 | 056235 | 0.32690] 0.74010
2 12 32 000178 | 00281 | 0.57438 | 0.33840 | _0,744K0
3 4 32 | 0.00194 | 0,68352 | 0,54900_| 0.35280 | 0.74860
4 4 321 000167 | _0,70227 | _0,55900_| 034120 | _0,75290
3 i 32 | 0,00100 | 0,69840 | _0,55200_| 0.35560 | 0.75410

Berdasarkan Tabel 4.6, konfigurasi dengan peringkat pertama menghasilkan
nilai mAPSO sebesar 0,70329 dan mAPSO-95 sebesar 0,56235. Dibandingkan
dengan baseline, terjadi peningkatan sebesar 0,02180 pada metrik mAPS0-95.

n

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 85

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Peningkatan ini menunjukkan bahwa penyesuaian hyperparameter memberikan
kontribusi terhadap peningkatan performa deteksi pada model berkapasitas
menengah. Meskipun terdapat tria! lain yang menghasilkan nilai mAPSO-95 lebih
tinggi, pemilihan konfigurasi akhir mempertimbangkan keseimbangan antara
performa dan kestabilan validation loss. Trial 26 menunjukkan nilai validation loss
yang lebih rendah dibandingkan konfigurasi lainnya, sehingga dipilih sebagai
model optimal. Pendekatan ini memastikan bahwa model yang terpilih tidak hanya
unggul secara numerik pada satu metrik, tetapi juga menunjukkan pola
pembelajaran yang stabil serta kemampuan generalisasi yang lebih baik pada data
validation.

tes

Gambar 4.7 Kurva Hasil Pelatihan Model YOLOW-M

Gambar 4.7 menampilkan kurva hasil pelatihan model YOLOv9-M
menggunakan konfigurasi Ayperparameter terpilih. Kurva training loss
menunjukkan penurunan yang konsisten seiring bertambahnya epoch pelatihan,
dari nilai awal sebesar 1 hingga mencapai sekitar 0,32690 pada akhir proses
pelatihan. Penurunan ini menunjukkan bahwa proses pembelajaran model
berlangsung secara stabil dan parameter model secara bertahap mampu
menyesuaikan diri dengan karakteristik data latih. Pola penurunan oss yang relatif
bertahap dibandingkan model YOLOv9-S mencerminkan kapasitas model
YOLOV9-M yang lebih besar, sehingga proses pembelajaran berlangsung lebih
gradual sebelum mencapai kondisi konvergensi. Pada sisi validation, kurva
vatidation loss menunjukkan penurunan yang cukup signifikan pada fase awal
pelatihan, dari nilai awal sebesar 1 hingga mencapai nilai minimum sekitar 0,74010

pada epoch ke-13. Setelah titik tersebut, nilai validation loss cenderung

n
SKRIPSI PERBANDINGAN METODE DAN... 'ARKAN SYAFIQ ATTAOY


## Halaman 86

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

menunjukkan fluktuasi ringan dengan nilai akhir sekitar 0,80116, yang
mengindikasikan bahwa model telah mencapai titik pembelajaran optimal terhadap
data validasi. Kondisi ini menunjukkan bahwa pelatihan tambahan setelah epoch
tersebut tidak memberikan peningkatan yang signifikan terhadap kemampuan
generalisasi model. Sejalan dengan pola tersebut, metrik evaluasi deteksi objek
menunjukkan peningkatan performa yang cukup pesat pada tahap awal pelatihan.
Pada epoch ke-13, model mencapai nilai mAPSO sebesar 0,7035 dan mAPSO-95
sebesar 0,5616. Pada akhir pelatihan, performa model meningkat sedikit menjadi
MAPS0 sebesar 0,7242 dan mAP50-95 sebesar 0,5720, namun peningkatan tersebut
relatif kecil sehingga kurva metrik cenderung berada pada kondisi plateau. Hal ini
menunjukkan bahwa model telah mencapai performa yang stabil pada rentang
epoch tersebut dan proses pelatihan selanjutnya tidak memberikan peningkatan
performa yang signifikan.
4413 YOLOv9-C

YOLOv9-C digunakan sebagai varian dengan kapasitas terbesar dalam
YOLOV9. Pelatihan awal dilakukan menggunakan konfigurasi default untuk
memperoleh performa baseline sebagai pembanding sebelum optimisasi
'hyperparameter, Hasil evaluasi pada data validation disajikan pada Tabel 4.7.

Tabel 4.7 Hasil Baseline Model untuk YOLOV-C

Konfigurasi APSO APSO
YOLOV9-C. 0.69997, (0.53800.
Hasil baseline menunjukkan bahwa YOLOv9-C mencapai mAP50-95 sebesar

0,55800, sedikit lebih tinggi dibandingkan YOLOv9-M baseline. Namun,
(peningkatan tersebut relatif terbatas meskipun kapasitas parameter model lebih

besar. Hal ini mengindikasikan bahwa konfigurasi default belum sepenuhnya
memaksimalkan potensi representasi fitur pada model berkapasitas besar.
Selanjutnya dilakukan optimisasi hyperparameter sebanyak 30 trial menggunakan
Optuna. Ringkasan lima konfigurasi terbaik disajikan pada Tabel 4.8, sedangkan
hasil lengkap seluruh ria! dapat dilihat pada Lampiran 3.

3
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 87

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Tabel 4.8 Hasil Hyperparameter Tuning dengan Optuna untuk YOLOv9-C

Batch | Learn MAPSO- | Train | Validation
Rank | Tent | “se | “mae | APSO | Mpg Loss_| Loss
1 28 32 | -o0orer | 071771 | 056807_[0,34200 | 0.66160
2 12 32 | 0.00179 [0.72684 [0,56677_[031980 [0.66410
3 19 32 | 0.00124 [0.71938 056275 (032340 | 0,66540
4 2 32 [0.00266 [0.72334 T 0.56059 [0.35680 | 0,66890
9 32 — 000211 [0.72068 0,57825 [0,30170 | 007140

Berdasarkan Tabel 4.8, konfigurasi dengan peringkat pertama menghasilkan
nilai mAPSO sebesar 0.71771 dan mAP50-95 sebesar 0,56807. Dibandingkan
dengan baseline, terjadi peningkatan sebesar 0,01007 pada metrik mAPS0-95.
Peningkatan ini menunjukkan bahwa optimisasi hyperparameter tetap memberikan
kontribusi terhadap peningkatan performa, meskipun dampaknya relatif lebih kecil
dibandingkan varian YOLOv9-M. Meskipun terdapat trial lain yang menunjukkan
nilai mAPSO-95 lebih tinggi, pemilihan konfigurasi akhir mempertimbangkan
keseimbangan antara performa dan kestabilan validation loss. Trial 28
menunjukkan nilai validation loss yang lebih baik dan stabil dibandingkan
konfigurasi lainnya, sehingga dipilih sebagai model optimal. Pendekatan ini
memastikan bahwa model yang terpilih tidak hanya unggul secara numerik, tetapi
juga memiliki pola pembelajaran yang konsisten serta kemampuan generalisasi

yang lebih baik pada data validation.

pe

wan co

Gambar 4.8 Kurva Hasil Pelatihan Model YOLOv9-C
Gambar 4.8 menampilkan kurva hasil pelatihan model YOLOv9-C
menggunakan konfigurasi Ayperparameter terpilih. Kurva training loss
menunjukkan penurunan yang konsisten sepanjang proses pelatihan, dari nilai awal
sebesar 1 pada epoch pertama hingga mencapai sekitar 0,34200 pada akhir

pelatihan. Penurunan ini menunjukkan bahwa proses pembelajaran model

4

SKRIPSI PERBANDINGAN METODE DAN... 'ARKAN SYAFIQ ATTAOY


## Halaman 88

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

berlangsung secara stabil dan parameter model secara bertahap mampu
menyesuaikan diri dengan karakteristik data latih. Pola penurunan Joss yang relatif
lebih bertahap dibandingkan varian YOLOv9-S dan YOLOv9-M mencerminkan
kapasitas model YOLOv9-C yang lebih besar, sehingga proses optimisasi
parameter berlangsung secara lebih gradual sebelum mencapai kondisi
konvergensi. Pada sisi validation, kurva validation loss menunjukkan penurunan
yang cukup signifikan pada tahap awal pelatihan, dari nilai awal sebesar 1 hingga
mencapai nilai minimum sekitar 0,66160 pada epoch ke-8. Setelah titik tersebut,
nilai validation loss menunjukkan fluktuasi ringan dengan nilai akhir sekitar
0,7287, yang mengindikasikan bahwa model telah mencapai titik pembelajaran
optimal terhadap data validasi dan pelatihan tambahan tidak memberikan
peningkatan yang signifikan terhadap kemampuan generalisasi model. Sejalan
dengan pola tersebut, metrik evaluasi deteksi objek menunjukkan peningkatan
performa yang cukup pesat pada fase awal pelatihan. Pada epoch ke-8, model
mencapai nilai mAPSO sebesar 0,7031 dan mAP50-95 sebesar 0,5681. Pada akhir
proses pelatihan, performa model meningkat sedikit menjadi mAPSO sebesar
0,717 dan mAP50-95 sebesar 0,5840, namun peningkatan tersebut relatif kecil
sehingga kurva metrik cenderung berada pada kondisi plateau. Hal ini
menunjukkan bahwa model telah mencapai performa yang stabil pada rentang
epoch tersebut dan pelatihan lanjutan tidak memberikan peningkatan performa yang
signifikan.
4.4.2 RT-DETRV2

Pelatihan RT-DETRV2 dilakukan pada tiga varian model, yaitu RT-DETRv2-
S, RT-DETRv2-M, dan RT-DETRv2-L. Setiap varian terlebih dahulu dilatih
menggunakan konfigurasi dasar, kemudian dilakukan optimisasi hyperparameter
untuk memperoleh performa terbaik. Proses optimisasi hyperparameter dilakukan
menggunakan Optuna dengan pendekatan Bayesian Optimization. Hyperparameter
tuning difokuskan pada learning rate dan batch size karena optimizer AdamW pada
arsitektur Transformer sangat sensitif terhadap perubahan learning rate dan
mempengaruhi stabilitas proses konvergensi. Parameter lain seperti beta, weight

decay, serta scheduler mengikuti konfigurasi referensi dari implementasi resmi

7s

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 89

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

untuk menjaga stabilitas pelatihan dan konsistensi dengan baseline arsitektur.
Pembatasan ruang pencarian hyperparameter dilakukan untuk memastikan
perbandingan yang adil dengan pendekatan CNN serta menghindari eksplorasi
berlebihan yang berpotensi meningkatkan risiko overfitting terhadap data validasi.
442.1 RT-DETRv2-S

RT-DETRv2-S digunakan sebagai varian berkapasitas kecil dalam keluarga
RT-DETRV2. Pelatihan awal dilakukan menggunakan konfigurasi default untuk
memperoleh performa baseline sebagai pembanding sebelum proses optimisasi.

Hasil evaluasi pada data validation disajikan pada Tabel 4.9.
Tabel 4.9 Hasil Baseline Model untuk RT-DETRV2-S

[ Konfigurasi ‘mAPSO r ‘mAPSU-95 |
RT-DETRv2-S, 0,56672 1 045520 )
Hasil baseline menunjukkan bahwa RT-DETRv2-S menghasilkan mAP50-95

sebesar 0,43520 pada data validation. Nilai tersebut mengindikasikan bahwa
konfigurasi default belum mampu memaksimalkan performa deteksi, terutama pada
kelas kerusakan dengan ukuran kecil dan karakteristik visual kompleks.
Selanjutnya dilakukan optimisasi hyperparameter sebanyak 30 trial menggunakan
Optuna. Ringkasan lima konfigurasi terbaik disajikan pada Tabel 4.10, sedangkan
hasil lengkap seluruh érial dapat dilihat pada Lampiran 4.

Tabel 4.10 Hasil Hyperparameter Tuning dengan Optuna untuk RT-DETRV2-S

Bateh | Learning MAPSO- | Train | Validation

Rank | Teal | “sie | Rate | APSO | 95 Loss | Loss
T T 16 | 0,000267 | 0025p | osisat | 036720 | 0.47660
2 © 16 | 0,000170_| 0,62428 | 0,52339_| 0.37240 | 0.47980
3 a 16 | 0,000200 | 0,61402_|~0,52115 [037410 | 0.48060
4 25 16 | 0,000215 | 0,62147_|0,47585_| 037680 | 0.48640
5 3 32 10000333 0017561 050603 1 035850 | 049090

Berdasarkan Tabel 4.10, konfigurasi dengan peringkat pertama
menghasilkan nilai mAPSO sebesar 0,60239 dan mAPSO-95 sebesar 0,51541

Dibandingkan dengan haseline, terjadi peningkatan sebesar 0,08021 pada metrik
MAPS0-95. Peningkatan ini menunjukkan bahwa RT-DETRV2-S cukup responsif
terhadap penyesuaian hyperparameter, khususnya pada pengaturan learning rate
dan batch size. Meskipun terdapat trial lain yang menghasilkan nilai mAPSO-95
lebih tinggi, pemilihan konfigurasi akhir mempertimbangkan keseimbangan antara

performa dan kestabilan validation loss. Trial 1 menunjukkan nilai validation loss

76

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 90

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

yang relatif lebih baik dan stabil dibandingkan konfigurasi lainnya, sehingga dipilih
sebagai model optimal. Pendekatan ini memastikan bahwa model yang terpilih
tidak hanya unggul secara numerik, tetapi juga menunjukkan pola pembelajaran

yang konsisten serta kemampuan generalisasi yang lebih baik pada data validation.

vv ty SoH mager

is Sea
os af i ss
oa all : Cut Sonne Te

Gambar 4.9 Kurva Hasil Pelatihan Model RT-DETRv2-S
Gambar 4.9 menampilkan kurva hasil pelatihan model RT-DETRv2-S

menggunakan konfigurasi hyperparameter terpilih. Kurva training loss
menunjukkan penurunan yang signifikan sepanjang proses pelatihan, dari nilai awal
sebesar 1 pada epoch pertama hingga mencapai 0,36720 pada akhir pelatihan.
Penurunan ini menunjukkan bahwa model secara bertahap mampu mempelajari
representasi fitur dari data latih sehingga kesalahan prediksi semakin berkurang
seiring bertambahnya epoch. Pada sisi validation, kurva validation loss mengalami
penurunan dari nilai awal sebesar 1 hingga mencapai nilai minimum sekitar 0,47660
pada epoch ke-20, yang menunjukkan titik pelatihan terbaik berdasarkan kinerja
pada data validasi. Setelah epoch tersebut, nilai validation loss menunjukkan
perubahan yang relatif kecil dengan nilai akhir sebesar 0,50142, sehingga
mengindikasikan bahwa proses pembelajaran model telah mendekati kondisi
konvergensi. Sejalan dengan pola tersebut, metrik evaluasi deteksi objek juga
menunjukkan peningkatan performa selama proses pelatihan. Pada epoch ke-20,
model mencapai nilai mAPSO sebesar 0,6024 dan mAPS0-95 sebesar 0,4636. Pada
akhir pelatihan, performa model meningkat menjadi mAPSO sebesar 0,6501 dan
mAP30-95 sebesar 0,5132. Meskipun peningkatan metrik masih terjadi pada epoch-
epoch akhir, laju peningkatan tersebut relatif kecil sehingga kurva metrik cenderung

memasuki fase plateau. Hal ini menunjukkan bahwa model telah mencapai

1
SKRIPSI PERBANDINGAN METODE DAN... 'ARKAN SYAFIQ ATTAOY


## Halaman 91

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

performa yang cukup stabil dan tambahan epoch pelatihan tidak memberikan
peningkatan performa yang signifikan.
4422 RT-DETRV2-M

RT-DETRV2-M digunakan sebagai varian berkapasitas menengah dalam

PTRv2, Pelatihan awal dilakukan menggunakan konfigurasi default

keluarga RT-DI
untuk memperoleh performa baseline sebagai pembanding sebelum. proses

optimisasi hyperparameter, Hasil evaluasi pada data validation disajikan pada

Tabel 4.11
Tabel 4.11 Hasil Baseline Model untuk RT-DETRV2-M
Konfiguras TmAPSO TAPS0.95
RT-DETRV2-M 0.64875 0.50995

Hasil baseline menunjukkan bahwa RT-DETRy2-M mencapai mAP50-95
sebesar 0,50995 pada data validation. Nilai ini lebih tinggi dibandingkan RT-
DETRV2-S baseline, yang menunjukkan bahwa peningkatan kapasitas model
memberikan kontribusi terhadap kualitas deteksi. Namun demikian, performa
tersebut masih membuka peluang untuk peningkatan melalui optimisasi
hyperparameter. Selanjutnya dilakukan optimisasi hyperparameter sebanyak 30
trial menggunakan Optuna. Ringkasan lima konfigurasi terbaik disajikan pada

Tabel 4.12, sedangkan hasil lengkap seluruh trial dapat dilihat pada Lampiran 5

Tabel 4.12 Hasil Hperparameter Tuning dengan Optuna untuk RT-DETRV2-M_
‘Batch | Learning mAPSO- | Train | Validation

Rank | Trial | "size Rare | MAPSO 5 Loss | Loss
T 3 16 | 0.000225 | 0.68374 | 0.53478 | 034720 | 0.42530
2 1 16 | 0,000267_|_0,69088 | 0.53520 | 0,34980 | 0.42810
3 1 16 | 0,000291_| 0,66592 | 0.30970 | 0.35140 | 0.42960
4 22 16 | 0,000201 | 0.67843 | 0.52432 | 0.35290 | 0.43020
3 10 16 [0.000150 | 0.65668 | 0.54067 | 0.35480 [0.43110

Berdasarkan Tabel 4.12, konfigurasi dengan peringkat pertama
menghasilkan nilai mAP50 sebesar 0,68374 dan mAPSO-95 sebesar 0,53478.
Dibandingkan dengan baseline, terjadi peningkatan sebesar 0,02483 pada metrik
mAP50-95. Peningkatan ini menunjukkan bahwa RT-DETRv2-M tetap responsif
terhadap penyesuaian hyperparameter, meskipun peningkatannya tidak sebesar
yang terjadi pada RT-DETRv2-S. Meskipun terdapat trial lain yang menunjukkan
nilai mAPSO-95 lebih tinggi, pemilihan konfigurasi akhir mempertimbangkan

keseimbangan antara performa dan kestabilan validation loss. Trial 9 menunjukkan

78
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 92

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

nilai validation loss yang lebih rendah dan stabil dibandingkan konfigurasi lainnya,
sehingga dipilih sebagai model optimal. Pendekatan ini memastikan bahwa model
yang terpilih tidak hanya unggul secara numerik, tetapi juga memiliki pola
pembelajaran yang konsisten serta kemampuan generalisasi yang baik pada data

validation.

ST TS TE, 58

Gambar 4.10 Kurva Hasil Pelatihan Model RT-DETRV2:M

Gambar 4.10 menampilkan kurva hasil pelatihan model RT-DETRv2-M
menggunakan konfigurasi hyperparameter terpilih. Kurva training loss
menunjukkan penurunan yang signifikan sepanjang proses pelatihan, dari nilai awal
sebesar 1 pada epoch pertama hingga mencapai sekitar 0,34720 pada akhir
pelatihan. Penurunan ini menunjukkan bahwa model secara bertahap mampu
mempelajari representasi fitur dari data latih sehingga kesalahan prediksi semakin
berkurang seiring bertambahnya epoch. Pada sisi validation, kurva validation loss
mengalami penurunan dari nilai awal sebesar 1 hingga mencapai nilai minimum
sekitar 042530 pada epoch ke-19, yang menunjukkan titik pelatihan terbaik
berdasarkan kinerja pada data validasi. Setelah epoch tersebut, nilai validation loss
menunjukkan perubahan yang relatif kecil dengan nilai akhir sebesar 0,44632,
sehingga mengindikasikan bahwa proses pembelajaran model telah mendekati
kon

konvergensi. Sejalan dengan pola tersebut, metrik evaluasi deteksi objek
juga menunjukkan peningkatan performa selama proses pelatihan. Pada epoch ke-
19, model mencapai nilai mAPSO sebesar 0,7035 dan mAPSO-95 sebesar 0,5616.
Pada akhir pelatihan, performa model meningkat menjadi mAPSO sebesar 0,7242
dan mAP50-95 sebesar 0,5720. Meskipun peningkatan metrik masih terjadi pada
epoch-epoch akhir, laju peningkatan tersebut relatif kecil sehingga kurva metrik

79
SKRIPSI PERBANDINGAN METODE DAN... 'ARKAN SYAFIQ ATTAOY


## Halaman 93

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

cenderung memasuki fase plateau. Hal ini menunjukkan bahwa model telah
mencapai performa yang cukup stabil dan tambahan epoch pelatihan tidak
memberikan peningkatan performa yang signifikan.
4423 RT-DETRV2-L

RT-DETRV2-L digunakan sebagai varian dengan kapasitas terbesar dalam
keluarga RT-DETRV2. Pelatihan awal dilakukan menggunakan konfigurasi default
untuk memperoleh performa baseline sebagai pembanding sebelum proses

optimisasi hyperparameter. Hasil evaluasi pada data validation disajikan pada

Tabel 4.13.
"Tabel 4.13 Hasil Baseline Model untuk RT-DETRV2-L
Konfigurasi TmAPSO MAPSO2S
RI-DETRV2-L 0,66072 0.54528
Hasil baseline menunjukkan bahwa RT-DETRv2-L mencapai mAP30-95

sebesar 0,54528 pada data validation. Nilai ini lebih tinggi dibandingkan RT-
DETRv2-M baseline, yang menunjukkan bahwa peningkatan kapasitas model
memberikan kontribusi terhadap kualitas deteksi. Namun demikian, konfigurasi
default belum sepenuhnya memaksimalkan potensi representasi fitur yang dimiliki
model berkapasitas besar. Selanjutnya dilakukan optimisasi hyperparameter
sebanyak 30 trial menggunakan Optuna. Ringkasan lima konfigurasi terbaik
disajikan pada Tabel 4.14, sedangkan hasil lengkap seluruh ria! dapat dilihat pada

Lampiran 6,
Tabel 4.14 Hasil Hyperparameter Tuning dengan Optuna untuk RT-DETRv2-L.
sat | Bateh | Learning MAPSO- | Tram | Validation

Rank | Trial | “size | Rate | APS | 95 Loss | Loss
T T 16 | 0,000267 | 0.68391 | 050051 | 0.35840 | 00010
2 29 16 | o.00018t_| 0,69318 | 0.50075 | 0.35020 | o.50140
3 4 16 | 0,000428 | 0.67144 |_0.55107_| 0.35810 | 0.50480
4 3 16 | 0,000200 | 0.69313 | 0.56794 | 0.32970 | 0.50560
5 10 16 | 0.000150 | 0,67642 | 056250 | 0.35940 | 0.50670.

Berdasarkan Tabel 4.14, Konfigurasi dengan peringkat pertama
menghasilkan nilai mAPS0 sebesar 0,68391 dan mAPS0-95 sebesar 0,56951
gkatan sebesar 0,04423 pada metrik
mAPS0-95. Peningkatan ini menunjukkan bahwa RT-DETRv2-L cukup responsif

Dibandingkan dengan baseline, terjadi pei

terhadap penyesuaian hyperparameter, meskipun peningkatannya tidak sebesar
RT-DETRv2-S. Meskipun terdapat ia! lain yang menunjukkan nilai mAP50-95

80

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 94

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

yang kompetitif, pemilihan konfigurasi akhir mempertimbangkan keseimbangan
antara performa dan kestabilan validation loss. Trial 1 memiliki nilai validation loss
yang paling rendah dan stabil dibandingkan konfigurasi lainnya, sehingga dipilih
sebagai model optimal. Pendekatan ini memastikan bahwa model yang terpilih
tidak hanya unggul secara numerik, tetapi juga menunjukkan pola pembelajaran

yang konsisten serta kemampuan generalisasi yang baik pada data validation,

Scr Moge

(Gambar 4.11 Kurva Hasil Pelatihan Model RT-DETRv2-L

Gambar 4.11 menampilkan kurva hasil pelatihan model RT-DETRV2-L
menggunakan konfigurasi hyperparameter terpilih. Kurva training loss
menunjukkan penurunan yang signifikan sepanjang proses pelatihan, dari nilai awal
sebesar 1 pada epoch pertama hingga mencapai sekitar 0,22380 pada akhir
pelatihan. Penurunan ini menunjukkan bahwa model secara bertahap mampu

mempelajari representasi fitur dari data latih sehingga kesalahan prediksi semakin
berkurang seiring bertambahnya epoch. Pada sisi validation, kurva validation loss
mengalami penurunan dari nilai awal sebesar 1 hingga mencapai nilai minimum
sekitar 0,50020 pada epoch ke-21, yang menunjukkan titik pelatihan terbaik
berdasarkan kinerja pada data validasi. Setelah epock tersebut, nilai validation loss
menunjukkan perubahan yang relatif kecil dengan nilai akhir sebesar 0,52130,

sehingga mengindikasikan bahwa proses pembelajaran model telah mendekati

kondisi konvergensi. Sejalan dengan pola tersebut, metrik evaluasi deteksi objek
juga menunjukkan peningkatan performa selama proses pelatihan. Pada epoch ke-
21, model mencapai nilai mAPSO sebesar 0,6839 dan mAP50-95 sebesar 0,5267.
Pada akhir pelatihan, performa model meningkat menjadi mAPSO sebesar 0,7096

81

SKRIPSI PERBANDINGAN METODE DAN... 'ARKAN SYAFIQ ATTAOY


## Halaman 95

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

dan mAP50-95 sebesar 0,5643. Meskipun peningkatan metrik masih terjadi pada
epoch-epoch akhir, laju peningkatan tersebut relatif kecil sehingga kurva metrik
cenderung memasuki fase plateau. Hal ini menunjukkan bahwa model telah
mencapai performa yang cukup stabil dan tambahan epoch pelatihan tidak
memberikan peningkatan performa yang signifikan.
45 Model Performance Evaluation

Evaluasi performa model dilakukan menggunakan data test CarDD untuk
menilai kinerja akhir masing-masing arsitektur. Model yang diuji merupakan
konfigurasi terbaik hasil optimisasi hyperparameter pada setiap varian. Seluruh
pengukuran latensi inferensi dilakukan menggunakan GPU NVIDIA RTX A6000
untuk mensimulasikan skenario deployment real-time berbasis server. Evaluasi
difokuskan pada metrik akurasi deteksi, yaitu mAPSO dan mAPSO-95, serta
efisiensi komputasi melalui pengukuran latensi inferensi yang dirangkum
menggunakan metrik latensi PSO, latensi P9S, dan Frames Per Second (FPS).
Ringkasan hasil evaluasi disajikan pada Tabel 4.15.
Tabel 4.15 Ringkasan Performa Model Terbaik YOLOV dan RT-DETRV2

Latensi PSO | Latensi P9S | Frames Per

maa temani nanas (ms) (ms) Second (FPS)
Youows | age pose | as 1197 TO
Youow-M “oma [05730 [10,76 1439 32.98
‘youov.c Tori | ose40 [10.91 15.26 91,66
RT-DETRW2-S poso os? | ni 22,92 90,01
RI-DETRv2M | 0.6659 | 0.5349 | 13,07 29.80, 7651
RT-DETRv | 0.7124 | _os664 [16.57 3533 60.33,

Berdasarkan Tabel 4.15, YOLOv9-C menghasilkan nilai mAP50-95 tertinggi
sebesar 0.5840 dengan latensi P50 sebesar 10,91 ms atau setara dengan 91,66 FPS,
yang masih memenuhi kebutuhan implementasi sistem real-time. YOLOv9-M
menunjukkan latensi terendah sebesar 10,76 ms dengan throughput 92,94 FPS dan
akurasi yang tetap kompetitif, sehingga merepresentasikan kompromi yang efisien
antara performa deteksi dan kecepatan inferensi. Pada arsitektur RT-DETRV2,
peningkatan kapasitas model cenderung diikuti peningkatan latensi yang lebih
signifikan, yang berdampak pada penurunan nilai FPS. Meskipun RT-DETRv2-L
mampu mencapai mAPS0-95 sebesar 0,5664, nilai latensi P9S sebesar 35,33 ms
atau 60,33 FPS menunjukkan kebutuhan komputasi yang lebih tinggi dibandingkan
varian YOLOv9. Secara keseluruhan, seluruh model masih berada pada kisaran di

2

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 96

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

atas 60 FPS yang umumnya dianggap memadai untuk skenario real-time. Namun,
YOLOv9 menunjukkan keseimbangan yang lebih optimal antara akurasi deteksi
dan efisiensi inferensi dibandingkan RT-DETRv2 pada dataset CarDD.
4.5.1 Analisis Perbandingan Model Terbaik

Analisis komparatif dilakukan untuk memahami perbedaan karakteristik
performa antara pendekatan Convolutional Neural Network (CNN) dan
Transformer, dilakukan analisis komparatif terhadap model terbaik dari masing-
masing arsitektur, yaitu YOLOv9-C dan RT-DETRv2-L. Kedua model dipilih
berdasarkan nilai mAPS0-95 tertinggi pada masing-masing kelompok arsitektur
sebagaimana ditunjukkan pada Tabel 4.15. Selain membandingkan metrik agregat
berupa akurasi deteksi dan efisiensi inferensi, analisis juga dilakukan terhadap
distribusi kesalahan prediksi antar kelas untuk mengidentifikasi karakteristik

deteksi masing-masing pendekatan secara lebih komprehensif.

:
| senarar
tam broker .
sie at on is
ec | =

snitch

foam
a
—

Gambar 4.12 Confision Maris YOLOV9-C

Gambar 4.12 menunjukkan confision matrix dari model YOLOV9-C pada
data test. Nilai pada diagonal utama merepresentasikan proporsi prediksi benar
(recall) untuk masing-masing kelas kerusakan. Terlihat bahwa kelas glass shatter

83

SKRIPSI PERBANDINGAN METODE DAN... 'ARKAN SYAFIQ ATTAOY


## Halaman 97

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

(0,96), tire lat (0,90), dan lamp broken (0,81) memiliki nilai recal! yang tinggi. Hal
ini menunjukkan bahwa kerusakan dengan pola visual yang jelas, kontras tinggi,
serta struktur objek yang tegas relatif mudah dikenali oleh model. Sebaliknya, kelas
dent (0,55), scratch (0,58), dan crack (049) menunjukkan nilai recall yang lebih
rendah, yang mengindikasikan bahwa kerusakan dengan tekstur halus, pola linear
tipis, atau ukuran relatif kecil masih menjadi tantangan dalam proses deteksi.
Ditinjau dari sisi precision, model YOLOv9-C menunjukkan performa yang tinggi
pada kelas glass shatter sebesar 0,94 dan tire flat sebesar 0,91, yang menunjukkan
bahwa prediksi model pada kelas tersebut relatif stabil dan jarang menghasilkan
false positive. Kelas lamp broken memiliki precision sebesar 0,79 yang masih
menunjukkan konsistensi prediksi yang baik. Sebaliknya, kelas scrateh memiliki
precision sebesar 0,52, diikuti oleh dent sebesar 0,59 dan crack sebesar 0,61. Nilai
precision yang relatif lebih rendah pada kelas-kelas tersebut menunjukkan bahwa
model masih menghasilkan prediksi tambahan pada arca yang memiliki kemiripan
visual dengan kerusakan. Pola ini mengindikasikan bahwa deteksi kerusakan
berukuran kecil sangat dipengaruhi oleh kemampuan model dalam

mempertahankan detail spasial lokal selama proses ekstraksi fitur.
Confusion Matrix Normalized

ag SS) =
5
[= | at va

Predicted Class

tie fat -

“01

Gambar 4.13 Confusion Matrix RT-DETRV2-L.

84
SKRIPSI PERBANDINGAN METODE DAN... 'ARKAN SYAFIQ ATTAOY


## Halaman 98

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Gambar 4.13 menunjukkan confusion matrix dari model RT-DETRV2-L pada
data uji. Nilai pada diagonal utama merepresentasikan proporsi prediksi benar
(recall) untuk masing-masing kelas kerusakan. Terlihat bahwa kelas glass shatter
(0,86), tire flat (0,83), dan lamp broken (0,65) memiliki nilai recal! yang relatif
tinggi. Nilai recall yang tinggi menunjukkan bahwa kerusakan dengan struktur
visual yang jelas dan kontras tinggi relatif lebih mudah dikenali oleh model.
Sebaliknya, kelas dent (0,35), seratch (0,37), dan crack (0,24) menunjukkan nilai
recall yang lebih rendah, yang mengindikasikan bahwa kerusakan dengan tekstur
halus dan ukuran kecil masih menjadi tantangan dalam proses deteksi. Ditinjau dari
sisi precision, model RT-DETRv2-L menunjukkan nilai precision sebesar 0,98
pada kelas glass shatter, 0,85 pada kelas tire flat, dan 0,84 pada kelas lamp broken.
Nilai precision yang tinggi menunjukkan bahwa prediksi model relatif stabil dan
jarang menghasilkan false positive. Sebaliknya, kelas dent memiliki precision
sebesar 0,57, scratch sebesar 0,58, dan crack sebesar 0,46. Nilai precision yang
relatif lebih rendah menunjukkan bahwa model masih menghasilkan prediksi
tambahan pada area yang memiliki kemiripan visual dengan kerusakan.

Secara umum, pola distribusi kesalahan menunjukkan bahwa RT-DETRv2-L
memiliki performa yang sangat baik pada objek dengan struktur kerusakan yang
jelas dan kontras tinggi, namun masih menghadapi keterbatasan dalam mendeteksi
kerusakan berukuran kecil dan bertekstur halus. Mekanisme selfatention global
memungkinkan model memahami hubungan spasial secara luas, tetapi cenderung
(kurang optimal dalam mempertahankan detail lokal beresolusi tinggi. Karakteristik
tersebut menyebabkan sebagian instance kerusakan kecil tidak terdeteksi dan
diklasifikasikan sebagai background. Temuan ini konsisten dengan karakteristik
dataset CarDD yang bersifat damage-centric, di mana sebagian besar objek
kerusakan memiliki ukuran relatif kecil terhadap keseluruhan citra kendaraan.
Analisis berbasis confusion matrix menunjukkan pola kesalahan pada tingkat kelas
(class-level). Pemahaman distribusi kesalahan deteksi pada tingkat instance,
diperdalam melalui analisis jumlah True Positive (TP), False Positive (FP), dan
False Negative (FN) sebagaimana ditunjukkan pada Tabel 4.16.

85

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 99

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Tabel 416 Distribusi Error Instance pada Data Test
Komponen YOLOW-C REDETRL
True Positive (TP) S10 1097
False Positive (EP) 303 1552
False Negative (ENY. 215 596
Precision (REA aan
Recall 497% 64.80%

Berdasarkan Tabel 4.16, kedua model menunjukkan nilai recall yang relatif
sebanding, yaitu 64,97% pada YOLOv9-C dan 64,80% pada RT-DETRV2-L. Hal
ini menunjukkan bahwa kedua arsitektur memiliki kemampuan yang relatif serupa
dalam menemukan sebagian besar instance kerusakan pada data uji. Perbedaan
yang signifikan terlihat pada nilai precision, di mana YOLOV9-C mencapai
precision sebesar 62,73%, sedangkan RT-DETRv2-L hanya mencapai 41,41%.
Perbedaan precision yang cukup besar disebabkan oleh jumlah False Positive yang
jauh lebih tinggi pada RT-DETRV2-L, yaitu sebanyak 1552 prediksi tambahan yang
tidak sesuai dengan anotasi ground truth. Sebaliknya, YOLOv9-C menghasilkan
303 False Positive, yang menunjukkan bahwa prediksi model lebih stabil dan tidak
terlalu sensitif terhadap pola visual yang menyerupai kerusakan. Tingginya jumlah
False Positive pada RT-DETRV2-L menunjukkan bahwa pendekatan Transformer
cenderung lebih sensitif terhadap pola visual global seperti refleksi cahaya,
bayangan, maupun garis panel kendaraan yang secara visual menyerupai kerusakan.
Jumlah False Negative pada RT-DETRv2-L juga lebih tinggi dibandingkan
YOLOV9-C, yang menunjukkan bahwa sebagian instance kerusakan tidak berhasil
terdeteksi. Kondisi ini terutama terjadi pada objek berukuran kecil dengan kontras
rendah terhadap permukaan kendaraan. Dalam konteks dataset CarDD yang
didominasi kerusakan kecil dan bertekstur halus, kemampuan mempertahankan
detail spasial lokal menjadi faktor penting dalam meningkatkan performa deteksi.
Perbedaan distribusi kesalahan ini memperkuat indikasi bahwa CNN memiliki
keunggulan dalam mempertahankan informasi spasial lokal melalui operasi
konvolusi berjenjang, sedangkan Transformer lebih menekankan hubungan global
antar area citra. Pemahaman karakteristik kesalahan secara lebih konkret disajikan
melalui beberapa contoh kesalahan prediksi pada data uji sebagaimana ditunjukkan
pada Gambar 4.14.

86
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 100

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Gambar 414 Con Kesthan Peis! YOLOW-€ pata Dan Ui: ( Masato,
(False Negative, (&) False Positive, (8) Localization Error

Berdasarkan Gambar 4.14(a), terlihat adanya kesalahan klasifikasi antara

kelas seratch dan dent pada kondisi kerusakan majemuk. Model berhasil

mendeteksi sebagian objek, namun terjadi pertukaran label dan prediksi tambahan
(pada area yang tidak sesuai dengan anotasi ground truth. Pola ini menunjukkan
keterbatasan model dalam membedakan karakteristik deformasi struktural (dent)
dan perubahan tekstur linear (serateh) ketika keduanya muncul secara bersamaan.
Pada Gambar 4.14(b), ditunjukkan kasus false negative, di mana beberapa objek
kerusakan tidak terdeteksi sama sekali. Kondisi ini umumnya terjadi pada
kerusakan berukuran kecil atau berdekatan satu sama lain, sehingga model
cenderung menggabungkan atau mengabaikan sebagian instance. Gambar 4.14(c)
memperlihatkan kasus false positive, yaitu munculnya bounding box tambahan
(pada area yang tidak memiliki anotasi kerusakan. Fenomena ini sering terjadi akibat
ambiguitas tekstur dan refleksi cahaya pada permukaan bodi kendaraan, yang
secara visual menyerupai pola kerusakan. Sementara itu, pada Gambar 4.14(d)
terlihat kesalahan lokalisasi (localization error), di mana kelas yang diprediksi
sudah benar namun posisi bounding box tidak sesuai dengan objek sebenarnya.
Ketidaktepatan spasial ini berpotensi menurunkan nilai ToU dan secara langsung
mempengaruhi mAP50-95 meskipun secara visual model telah mengenali

87

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 101

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

keberadaan kerusakan. Pola kesalahan tersebut menunjukkan bahwa karakteristik
visual objek, khususnya ukuran objek, berpotensi menjadi faktor utama yang
mempengaruhi tingkat kesulitan deteksi. Oleh karena itu, dilakukan analisis

distribusi ukuran objek pada data test sebagaimana disajikan pada Tabel 4.17.
Tabel 4.17 Distribusi Ukuran Objek pada Data Test

‘Kelas Kerusakan ‘Small (%) ‘Medium (a) Large Ca
dent 1144 454 43.22,
Seratoh 16,94 4756, 35,50
rack 62,86 3143 sm
lass shatter 0 BA 9155
lamp broken 8.70 23.19 6.12
tire lat 0 938 9062

Ukuran objek dikelompokkan menjadi tiga kategori berdasarkan rasio luas
bounding box terhadap luas citra, yaitu small (<2%), medium (210%), dan large
(1096). Hasil analisis menunjukkan bahwa kelas crack didominasi oleh objek
berukuran small dengan proporsi sebesar 62,86, jauh lebih tinggi dibandingkan
kelas lainnya. Sebaliknya, kelas glass shatter dan tire flat didominasi oleh objek
berukuran large dengan proporsi masing-masing sebesar 91,55% dan 90,62%.
Distribusi ukuran objek ini konsisten dengan hasil confusion matrix dan nilai recall
per kelas pada kedua model, di mana kelas crack menunjukkan performa terendah.
Dominasi objek berukuran kecil menyebabkan detail spasial kerusakan berpotensi
berkurang selama proses downsampling pada feature extraction sehingga
meningkatkan kemungkinan terjadinya /alse negative. Dalam kondisi ini, CNN
cenderung menunjukkan kemampuan yang lebih stabil dalam mempertahankan
representasi fitur lokal melalui operasi konvolusi berjenjang, sedangkan
Transformer yang menekankan hubungan global antar area citra cenderung kurang
optimal dalam mempertahankan detail lokal berukuran sangat kecil.

4.5.2 Analisis Pareto Frontier

Analisis Pareto Frontier digunakan untuk mengidentifikasi konfigurasi
model yang bersifat Pareto-optimal, yaitu model yang tidak dapat ditingkatkan
pada satu metrik tanpa mengorbankan metrik lainnya. Pada penelitian ini, dua
metrik yang dianalisis adalah mAP50-95 sebagai indikator akurasi dan latensi
inferensi P50 sebagai indikator efisiensi komputasi.

8

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 102

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Pareto Frontier of YOLOv9 and REOETRV2

an Semen
Ampemas

i =

Amorman

(Gambar 4.15 Pareto Frontier antara mAPS0-9S dan Latensi Inferensi

Gambar 4.15 menampilkan visualisasi Pareto Frontier yang
merepresentasikan hubungan antara akurasi deteksi (mAP50-95) dan latensi
inferensi (P50) dari seluruh model terbaik yang diuji. Titik-
menunjukkan konfigurasi model yang bersifat Pareto-optimal, yaitu model yang

tik pada kurva Pareto

tidak dapat didominasi oleh model lain secara simultan baik dari sisi akurasi
maupun efisiensi inferensi. Berdasarkan visualisasi tersebut, terlihat bahwa dua
model berada pada kurva Pareto-optimal, yaitu YOLOv9-M dan YOLOv9-C.
YOLOv9-M merepresentasikan konfigurasi dengan latensi inferensi terendah
sekaligus mempertahankan tingkat akurasi yang tinggi, sehingga sesuai untuk
skenario aplikasi yang menuntut respons cepat. Sementara itu, YOLOv9-C
menempati ekstrem akurasi dengan nilai mAP50-95 tertinggi, dengan latensi
inferensi yang sedikit lebih tinggi namun masih berada dalam batas yang dapat
diterima untuk aplikasi real-time.

Model lain seperti YOLOv9-S, RT-DETRv2-S, RT-DETRv2-M, dan RT-
DETRv2-L berada di luar kurva Pareto karena bersifat terdominasi, baik oleh
YOLOv9-M maupun YOLOv9-C. Hal ini menunjukkan bahwa peningkatan
kapasitas atau kompleksitas model tidak selalu menghasilkan kombinasi akurasi

dan efisiensi yang optimal. Berdasarkan hasil analisis Pareto Frontier, terdapat dua

model yang memenuhi kriteria Pareto-optimal, yaitu YOLOV9-M dan YOLOv9-C.

89
SKRIPSI PERBANDINGAN METODE DAN... 'ARKAN SYAFIQ ATTAOY


## Halaman 103

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

YOLOV9-M menunjukkan latensi inferensi terendah sebesar 10,76 ms (92,94 FPS),
sedangkan YOLOv9-C menghasilkan nilai mAPS0-95 tertinggi sebesar 0,5840
dengan latensi 10,91 ms (91,66 FPS). Selisih latensi antara kedua model relatif
kecil, yaitu sekitar 0,15 ms atau 1,394, sehingga tidak memberikan perbedaan
signifikan terhadap performa real-time sistem.

Pemilihan model utama dalam penelitian ini mempertimbangkan tujuan
sistem sebagai alat bantu inspeksi kerusakan kendaraan yang memerlukan tingkat
ketelitian deteksi yang tinggi. Dalam konteks aplikasi seperti dokumentasi klaim
asuransi, estimasi biaya perbaikan, dan evaluasi kondisi kendaraan, kesalahan
deteksi dapat berdampak pada ketidaktepatan penilaian kerusakan. Oleh karena itu,
peningkatan akurasi memiliki nilai praktis yang lebih penting dibandingkan
(perbedaan latensi yang sangat kecil. Dengan mempertimbangkan bahwa YOLOv9-
C tetap mampu mencapai kecepatan 91,66 FPS yang masih berada dalam kategori
real-time, model YOLOv9-C dipilih sebagai model utama karena memberikan
akurasi tertinggi tanpa mengorbankan kelayakan implementasi sistem berbasis web.
Meskipun selisih nilai mAP50-95 antara YOLOv9-C dan RT-DETRV2-L relatif
kecil, interpretasi hasil penelitian tidak difokuskan pada klaim superioritas absolut
salah satu arsitektur. Sebaliknya, analisis diarahkan pada keseimbangan antara
akurasi deteksi dan efisiensi komputasi melalui pendekatan Pareto Frontier. Dalam
implementasi sistem real-time, perbedaan latensi yang cukup signifikan
menunjukkan bahwa YOLOv9-C memberikan keuntungan praktis dalam hal
efisiensi inferensi tanpa mengorbankan akurasi deteksi.

4.6 Web App Implementation

Implementasi prototipe aplikasi weh pada penelitian ini dikembangkan
sebagai sarana implementasi model deteksi kerusakan kendaraan yang telah dipilih
berdasarkan hasil evaluasi performa sebelumnya dengan mempertimbangkan
keseimbangan antara akurasi deteksi dan efisiensi inferensi. Model terbaik
kemudian diintegrasikan ke dalam sistem aplikasi sebagai backend untuk
memproses citra masukan dan menghasilkan keluaran berupa hasil deteksi
kerusakan kendaraan dalam bentuk bounding box beserta label kelas kerusakan
yang teridentifikasi. Aplikasi weh ini dirancang untuk memudahkan pengguna

90

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 104

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

dalam melakukan analisis kondisi kendaraan secara otomatis melalui unggahan
citra kendaraan. Selain menampilkan hasil prediksi model, aplikasi juga
menyediakan visualisasi hasil deteksi sehingga pengguna dapat memahami lokasi
serta jenis kerusakan yang terdeteksi secara lebih jelas. Dengan demikian, prototipe
tidak hanya berfungsi sebagai alat prediksi, tetapi juga sebagai media pendukung
dalam interpretasi hasil deteksi kerusakan kendaraan. Pengujian awal terhadap
prototipe dilakukan menggunakan metode Black Box Testing untuk memastikan
bahwa seluruh fungsi utama aplikasi berjalan sesuai dengan kebutuhan sistem dan
tidak mengalami kesalahan fungsional. Selanjutnya, prototipe aplikasi di-deploy
menggunakan framework Streamlit agar dapat diakses dengan mudah melalui
antarmuka web. Pada tahap akhir, dilakukan evaluasi menggunakan System
Usability Seale (SUS) untuk mengukur tingkat kegunaan aplikasi berdasarkan
penilaian pengguna terhadap kemudahan penggunaan dan kenyamanan antarmuka.
4.6.1 Pengembangan Prototipe

Pengembangan prototipe dilakukan sebagai tahap implementasi dari model
deteksi kerusakan kendaraan yang telah ditentukan pada tahap eksperimen.
Prototipe ini merepresentasikan integrasi model deteksi ke dalam sistem aplikasi
berbasis web yang memungkinkan pengguna melakukan prediksi secara langsung
melalui antarmuka grafis. Model deteksi berperan sebagai inti sistem klasifikasi dan
pelokalan objek, yang diintegrasikan melalui komponen backend aplikasi. Keluaran
model divisualisasikan dalam bentuk citra beranotasi sehingga lokasi dan jenis
kerusakan dapat diamati secara langsung. Perancangan antarmuka difokuskan pada
(kesederhanaan struktur navigasi dan kemudahan interaksi pengguna.
a. Halaman Utama

Halaman utama berfungsi sebagai titik awal interaksi pengguna dengan
sistem. Gambar 4.16 memperlihatkan tampilan halaman utama prototipe aplikasi
Visual Intelligenee for Car Damage Detection (VIDI). Halaman ini memuat
deskripsi singkat mengenai tujuan pengembangan sistem sebagai solusi deteksi
kerusakan kendaraan berbasis computer vision. Informasi tersebut memberikan

konteks mengenai fungsi aplikasi dalam mendukung proses inspeksi visual

1
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 105

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

kendaraan secara otomatis. Petunjuk penggunaan disajikan secara ringkas untuk

Vv

VIDI

vor

menjelaskan alur kerja system.

get i ea yak paman nm

Formats
‘ara marggunaan Aptian

MMA kt den Aga AL en gn

nang doa mera Wae

Gambar 4.16 Tampilan Halaman Utama Prototipe
Navigasi antarmuka direpresentasikan dalam bentuk tombol menuju halaman

Daftar Kerusakan dan halaman Prediksi Kerusakan. Struktur navigasi yang

sederhana menjadikan halaman utama sebagai pusat akses seluruh fitur sistem.

b. Halaman Daftar Kerusakan

Halaman Daftar Kerusakan menyajikan enam kelas kerusakan yang
digunakan dalam sistem deteksi, yaitu dent, scratch, crack, glass shatter, lamp
broken, dan tire flat. Gambar 4.17 memperlihatkan tampilan halaman tersebut pada
prototipe VIDI. Setiap kelas ditampilkan dalam bentuk citra ilustratif disertai
deskripsi singkat mengenai karakteristik visual dan dampaknya terhadap kondisi
kendaraan. Penyajian ini mendukung pemahaman pengguna terhadap kategori
kerusakan yang diidentifikasi oleh model.

92
SKRIPSI PERBANDINGAN METODE DAN... 'ARKAN SYAFIQ ATTAOY


## Halaman 106

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Gambar 4.17 Tampilan Halaman Daftar Kerusakan Prototipe
Halaman Daftar Kerusakan Prototipe berperan sebagai referensi konseptual

yang membantu pengguna menginterpretasikan hasil prediksi model berdasarkan

karakteristik kerusakan yang ditampilkan.
Halaman Prediksi Kerusakan

Halaman Prediksi Kerusakan merupakan komponen utama prototipe aplikasi.
Pengguna dapat memasukkan citra kendaraan dari empat sisi, yaitu depan,
belakang, kiri, dan kanan. Sistem kemudian melakukan proses inferensi berbasis
deep learning menggunakan model YOLOv9-C sebagai model terpilih untuk
mengidentifikasi serta melokalisasi kerusakan kendaraan secara otomatis. Model
YOLOV9-C dipilih berdasarkan hasil evaluasi eksperimen yang menunjukkan
(keseimbangan terbaik antara akurasi deteksi dan efisiensi komputasi. Contoh citra
yang digunakan pada fitur demonstrasi aplikasi merupakan gambar kendaraan nyata
yang diperoleh di luar dataset penelitian, sehingga skenario penggunaan
merepresentasikan kondisi implementasi sistem pada lingkungan aktual. Sistem
mendukung dua mekanisme akuisisi citra, yakni unggah berkas dari penyimpanan
lokal serta pengambilan gambar secara langsung melalui kamera berbasis browser.

93
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 107

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Fitur ini memungkinkan sistem diakses melalui perangkat desktop maupun
perangkat bergerak sehingga meningkatkan fleksibilitas penggunaan dalam
berbagai kondisi.

Prediksi Kerusakan Kendaraan

ota dengan ntah Gambar

gah / Ambil Citra Kendaraan

(© mination | mutetaan

agro a oe pec ee

meta

Meat 01 2 meee

Status elngkapn Gambar

og ents

Gambar 4.18 Tampilan Halaman Prediksi Kerusakan Prototipe

Gambar 4.18 memperlihatkan tampilan awal halaman prediksi sebelum
proses unggah dilakukan. Antarmuka menyediakan area input citra untuk empat sisi
kendaraan, yaitu depan, belakang, kiri, dan kanan, serta tombol aksi untuk
menjalankan proses deteksi. Sistem dirancang secara fleksibel sehingga pengguna
dapat mengunggah satu atau lebih citra sesuai kebutuhan. Setiap citra akan diproses
secara independen oleh model untuk mengidentifikasi kerusakan pada sisi
kendaraan yang tersedia. Meskipun sistem mendukung input parsial, penggunaan
empat sisi kendaraan secara lengkap dianjurkan untuk memperoleh gambaran
kondis

kendaraan yang lebih komprehensif. Setelah citra berhasil dimasukkan,

sistem menampilkan pratinjau gambar pada masing-masing sisi kendaraan

94

SKRIPSI PERBANDINGAN METODE DAN... 'ARKAN SYAFIQ ATTAOY


## Halaman 108

SKRIPSI

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

sebagaimana ditunjukkan pada Gambar 4.19. Pratinjau ini memungkinkan
pengguna melakukan verifikasi visual terhadap citra yang diunggah sebelum proses
deteksi dijalankan.

Unggah ite Kendaraan

os

Gambar 4.19 Tampilan Halaman Prediksi Setelah Mengunggah Gambar
Gambar 4.19 menampilkan kondisi antarmuka setelah citra berhasil diunggah.
Pada tahap ini, sistem telah menerima input dan siap menjalankan proses inferensi.
Tidak terdapat anotasi pada citra karena proses deteksi belum dilakukan. Setelah
(pengguna menekan tombol deteksi, setiap citra diproses secara independen melalui
tahapan preprocessing, inferensi model, dan postprocessing untuk menghasilkan
prediksi lokasi serta kelas kerusakan. Hasil akhir sistem ditampilkan setelah seluruh
proses inferensi selesai dijalankan. Gambar 4.20 menunjukkan keluaran berupa

visualisasi kerusakan pada masing-masing sisi kendaraan.

95

PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 109

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Hasil Deteksi

Frant ack

oration Buscateateens
tt ight

Gambar 4.20 Tampilan Halaman Prediksi Setelah Mendeteksi Gambar

Setiap kerusakan direpresentasikan dalam bentuk bounding box yang
menunjukkan lokasi objek terdeteksi. Label kelas kerusakan serta nilai confidence
score ditampilkan pada setiap anotasi sebagai indikator tingkat keyakinan model
terhadap prediksi yang dihasilkan. Visualisasi ini memungkinkan pengguna
mengamati jenis dan posisi kerusakan secara langsung pada citra kendaraan,
sehingga mendukung proses identifikasi kerusakan secara cepat dan intuitif.
4.6.2 Evaluasi Prototipe

Evaluasi prototipe dilakukan untuk memastikan bahwa aplikasi web yang
dikembangkan telah berfungsi sesuai dengan kebutuhan sistem serta memiliki
tingkat kegunaan yang baik dari sisi pengguna. Evaluasi ini mencakup pengujian
fungsionalitas aplikasi dan penilaian tingkat kegunaan antarmuka pengguna.
Metode evaluasi yang digunakan dalam penelitian ini meliputi Black Box Testing

96

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 110

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

untuk menguji fungsi utama aplikasi dan System Usability Scale (SUS) untuk
mengukur tingkat usability prototipe berdasarkan persepsi pengguna.
a. Black Box Testing

Black Box Testing digunakan sebagai metode pengujian fungsionalitas pada
prototipe aplikasi weh yang dikembangkan. Pengujian ini dilakukan dengan
berfokus pada keluaran sistem berdasarkan masukan yang diberikan, tanpa
memperhatikan struktur internal atau proses implementasi sistem. Tujuan dari
pengujian ini adalah untuk memastikan bahwa seluruh fitur utama aplikasi dapat

berjalan sesuai dengan fungsi yang diharapkan.
Tabel 4.18 Hasil Pengujian Black Box System Pada Prototipe Aplikasi

Nof Pengujian | Masilyang Diharapkan | Hasil Pengujian | Keterangan
1 [Klik — logo] Sistem kembali ke | Sistem — berhasil
beranda halaman beranda kembali ke halaman) Sesuai
beranda
2 | Buka menu] Halaman menampilkan | Enam Kelas
“Daftar Kelas| enamkelaskerusakan | kerusakan” tampil| Sesuai
Kerusakan" “dengan deskripsi
3 | Buka halaman Halaman siap menerima | Mataman deteksi |g
deteksi sungeahan citra terbuka tanpa galat
4 | Unggah —citra Pratinjaucitra tampilkan | Pratinjau cial
‘kendaraan (PG) berhasil ditampilkan
SJ dalankan deteksi | Bounding bor, Tabel, dan | Hasil deteksi
confidence muncul ditampilkan sesuai | Sesuai
cita:
© | Unduhhasil | File IPG beranotasi dapat | File berhasil diunduh soa
diunduh

Hasil pengujian Black Box Testing yang disajikan pada Tabel 418
menunjukkan bahwa seluruh skenario pengujian yang dilakukan menghasilkan
keluaran yang sesuai dengan hasil yang diharapkan. Setiap fungsi utama aplikasi,
mulai dari navigasi halaman, proses unggah citra kendaraan, hingga penampilan
hasil deteksi kerusakan, dapat dijalankan tanpa mengalami kesalahan fungsional.
Hal ini menunjukkan bahwa integrasi model deteksi dengan antarmuka weh telah
berjalan dengan baik serta memenuhi kebutuhan fungsional sistem.

b. System Usability Seale (SUS)

Evaluasi kegunaan dilakukan menggunakan instrumen System Usability Scale
(SUS) yang terdiri dari 10 pernyataan dengan skala Likert lima tingkat. Kuesioner
disebarkan secara daring kepada 10 responden yang telah mencoba menggunakan
prototipe aplikasi. Responden yang terlibat memiliki pemahaman praktis terkait

”
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 111

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

kondisi kerusakan kendaraan, baik melalui pengalaman profesional maupun
keterlibatan langsung dalam proses inspeksi kendaraan. Data jawaban responden
secara lengkap disajikan pada Lampiran 7, sedangkan hasil perhitungan skor SUS
masing-masing responden disajikan pada Lampiran 8. Perhitungan skor SUS
dilakukan menggunakan Persamaan (2.18) untuk memperoleh skor tiap responden,
kemudian dirata-ratakan menggunakan Persamaan (2.19) untuk memperoleh nilai
usability keseluruhan sistem. Berdasarkan hasil perhitungan, diperoleh skor rata-
rata SUS sebesar 81,55. Mengacu pada interpretasi standar SUS, nilai tersebut
termasuk dalam kategori Acceptable pada Acceptability Range, berada pada Grade
Scale B, serta memiliki Adjective Rating yang dikategorikan sebagai Good. Skor
ini menunjukkan bahwa prototipe aplikasi memiliki tingkat kegunaan yang baik,
mudah dipahami, serta dapat digunakan secara efektif oleh pengguna. Penilaian
responden secara umum menunjukkan persepsi positif terhadap kemudahan
navigasi, konsistensi antarmuka, serta kejelasan informasi yang disajikan.
4.7 Diskusi

Dataset CarDD memiliki karakteristik damage-centric dan bersifat single-
view, di mana sebagian besar citra berfokus pada area kerusakan tertentu dengan
dominasi objek berukuran kecil, tekstur halus, serta pantulan bodi kendaraan yang
menyerupai pola kerusakan. Distribusi visual ini menyebabkan informasi lokal
menjadi faktor utama dalam proses deteksi, sementara konteks global kendaraan
memiliki kontribusi yang relatif terbatas. Karakteristik tersebut berimplikasi
langsung terhadap performa arsitektur yang diuji. Model berbasis CNN, khususnya
YOLOV9-C, menunjukkan nilai mAPS0-95, precision, dan recall tertinggi pada
data uji. Keunggulan ini dapat dijelaskan oleh mekanisme konvolusi berjenjang
yang mempertahankan detail spasial lokal melalui representasi fitur hierarkis.
Sebaliknya, pendekatan Transformer pada RT-DETRv2 yang mengandalkan self.
attention global tidak memperoleh keuntungan signifikan pada dataset ini karena
relasi antar-area citra bukan faktor dominan dalam distribusi data CarDD.

Peningkatan kapasitas model pada YOLOv9 dari varian S ke M dan C secara
umum diikuti oleh peningkatan akurasi. Peningkatan tersebut tidak sepenuhnya
sebanding dengan kompleksitas komputasi yang dibutuhkan. YOLOv9-C

98

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 112

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

menghasilkan akurasi tertinggi, tetapi dengan latensi inferensi yang lebih besar
dibandingkan YOLOv9-M. Selisih akurasi antara YOLOv9-M dan YOLOv9-C
relatif kecil, sementara perbedaan latensi cukup signifikan. Hal ini menunjukkan
adanya trade-off nyata antara akurasi dan efisiensi komputasi. YOLOv9-M lebih
rasional digunakan pada kebutuhan respons cepat atau potensi implementasi real-
time berbasis web. YOLOV9-C lebih sesuai pada skenario yang memprioritaskan
akurasi maksimum, seperti dokumentasi klaim asuransi atau evaluasi kerusakan
bernilai tinggi. Pada arsitektur Transformer, peningkatan kapasitas RT-DETRv2
dari varian kecil hingga besar meningkatkan nilai AP, namun disertai kenaikan
latensi yang signifikan. Peningkatan akurasi yang diperoleh tidak sebanding dengan
tambahan kompleksitas model, yang mengindikasikan bahwa kompleksitas global
modeling belum sepenuhnya termanfaatkan pada dataset yang berfokus pada detail
lokal seperti CarDD. Dengan demikian, pada distribusi data yang menekankan
objek kecil dan tekstur spesifik, arsitektur CNN terbukti lebih efisien dalam
memanfaatkan kapasitas parameter model.

Dataset CarDD menunjukkan distribusi jumlah instance antar kelas yang
tidak sepenuhnya seimbang, di mana kelas seperti serateh dan dent memiliki jumlah
instance lebih banyak dibandingkan kelas seperti tire flat atau glass shatter.
Ketidakseimbangan kelas merupakan kondisi umum pada permasalahan deteksi
objek di dunia nyata karena frekuensi kemunculan objek tidak selalu merata. Dalam
penelitian ini, teknik augmentasi diterapkan secara konsisten pada seluruh data
training tanpa secara khusus menargetkan kelas minoritas. Pendekatan ini sejalan
dengan praktik umum pada penelitian computer vision, di mana augmentasi lebih
difokuskan pada peningkatan keragaman representasi visual daripada mengubah
distribusi kelas secara artifisial. Transformasi geometrik dan fotometrik seperti
flipping, resizing, rotasi, serta penyesuaian intensitas warna diketahui mampu
meningkatkan robustness model terhadap variasi orientasi objek, pencahayaan, dan
kualitas citra tanpa memodifikasi distribusi label secara langsung (Shorten dan
Khoshgoftaar, 2023; X. Wang dkk, 2023). Selain itu, pendekatan dynamic
augmentation pada arsitektur deteksi modern menunjukkan bahwa augmentasi

berperan dalam menjaga keseimbangan antara eksplorasi variasi data dan stabilitas

99
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 113

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

proses konvergensi model selama pelatihan (Lv dkk, 2024). Penerapan
oversampling secara khusus pada kelas minoritas berpotensi menghasilkan
distribusi data yang kurang realistis serta meningkatkan risiko model mempelajari
pola yang terlalu spesifik pada jumlah sampel terbatas (Shorten dan Khoshgoftaar,
2023). Oleh karena itu, augmentasi generik dipilih untuk mempertahankan
karakteristik distribusi dataset yang realistis sekaligus menjaga konsistensi skenario
eksperimen pada perbandingan arsitektur CNN dan Transformer. Dengan
pendekatan ini, performa model yang dihasilkan tetap merefleksikan kemampuan
deteksi pada kondisi dunia nyata, di mana ketidakseimbangan kelas merupakan
karakteristik yang sulit dihindari dalam data kerusakan kendaraan (X. Wang dkk,
2023).

Selain mempertimbangkan distribusi kelas dan strategi augmentasi,
pemahaman terhadasp pola kesalahan prediksi juga menjadi penting untuk
menjelaskan kemampuan generalisasi model secara lebih komprehensif. Nilai
metrik agregat seperti mAP, precision, dan recall memberikan gambaran umum
performa deteksi, namun belum sepenuhnya merepresentasikan karakteristik
kesalahan yang terjadi pada tingkat instance. Pada kasus deteksi kerusakan
kendaraan, kesalahan prediksi umumnya berkaitan dengan ukuran objek yang
relatif kecil, tekstur kerusakan yang halus, serta kemiripan visual antara kerusakan
dan pantulan permukaan bodi kendaraan. Variasi kondisi citra tersebut
menyebabkan model menghadapi kesulitan dalam mempertahankan konsistensi
representasi fitur antara data pelatihan dan data pengujian. Analisis kesalahan
memungkinkan identifikasi lebih rinci terhadap jenis kegagalan deteksi, seperti
objek yang tidak terdeteksi (false negative), prediksi tambahan pada area non-
kerusakan (false positive), maupun ketidaktepatan posisi hounding bor
(localization error). Contoh karakteristik kesalahan tersebut ditunjukkan pada
Gambar 4.16, yang memperlihatkan bahwa sebagian kegagalan deteksi terjadi pada
kerusakan berukuran kecil atau area dengan pola visual yang menyerupai tekstur
kerusakan. Temuan ini menunjukkan bahwa performa model tidak hanya
dipengaruhi oleh perbedaan arsitektur, tetapi juga oleh tingkat kesulitan visual
objek yang menuntut sensitivitas tinggi terhadap detail spasial berukuran kecil.

100
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 114

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Analisis lebih lanjut menunjukkan bahwa perbedaan skala objek antara data
pelatihan dan skenario implementasi turut berkontribusi terhadap munculnya
kesalahan prediksi. Citra pada dataset CarDD umumnya bersifat damage-centric,
di mana area kerusakan direkam dalam jarak dekat sehingga detail tekstur terlihat
jelas. Sebaliknya, pada implementasi sistem, citra kendaraan cenderung diambil
dari jarak yang lebih jauh untuk menangkap keseluruhan
area kerusakan menempati proporsi piksel yang lebih kecil setelah proses resizing
ke resolusi input 640x640. Perbedaan distribusi skala objek ini meningkatkan

i kendaraan, sehingga

potensi terjadinya false negative, khususnya pada kerusakan berukuran kecil seperti
scratch dan crack, karena informasi visual yang tersedia menjadi lebih terbatas
dibandingkan kondisi pelatihan. Perbandingan karakteristik citra antara dataset
pelatihan dan skenario implementasi ditunjukkan pada Gambar 4.21.

©
Gambar 4.21 Contoh Implementasi Sistem Inspeksi Kerusakan Kendaraan

Gambar 4.21(a) merepresentasikan citra pada CarDD yang bersifat single
view dan terfokus pada area kerusakan tertentu. Gambar 4.21(b) menunjukkan
implementasi sistem yang menerima unggahan citra kendaraan dari empat sisi
secara terpisah. Perbedaan karakteristik ini menyebabkan ukuran kerusakan pada
citra implementasi relatif lebih kecil dibandingkan citra pada dataset pelatihan,
sehingga dapat mempengaruhi sensitivitas model dalam mendeteksi kerusakan
berukuran kecil. Meskipun demikian, perbedaan skenario penggunaan ini tidak
mengubah kecenderungan umum performa komparatif antar arsitektur, melainkan
menegaskan pentingnya representasi fitur multi-skala dalam meningkatkan
kemampuan deteksi pada kondisi penggunaan nyata.

Secara keseluruhan, hasil penelitian menunjukkan bahwa kesesuaian antara
"mekanisme ekstraksi fitur dan distribusi visual data merupakan faktor utama yang

101

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 115

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

menentukan performa model deteksi objek. Pada dataset damage-centric seperti
CarDD, informasi lokal berperan lebih dominan dibandingkan relasi global antar
area citra, sehingga pendekatan CNN menunjukkan efisiensi representasi yang
lebih baik dibandingkan Transformer. Temuan ini menegaskan bahwa keunggulan
arsitektur modern berbasis attention tidak bersifat universal, melainkan bergantung
(pada karakteristik visual data yang dianalisis. Kontribusi penelitian ini terletak pada
bukti empiris bahwa pada skenario inspeksi kerusakan kendaraan dengan dominasi
objek kecil dan tekstur spesifik, peningkatan kompleksitas global modeling tidak
selalu menghasilkan peningkatan performa yang sebanding. Implikasi praktis dari
hasil ini menunjukkan bahwa pemilihan arsitektur deteksi objek sebaiknya
mempertimbangkan karakteristik distribusi objek, kebutuhan latensi inferensi, serta
konteks implementasi sistem, sehingga pemanfaatan model menjadi lebih efisien

dan tepat guna dalam lingkungan operasional nyata.

102
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 116

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

BAB V
KESIMPULAN DAN SARAN

54 Kesimpulan
Berdasarkan hasil dan pembahasan penelitian yang telah dilakukan,

kesimpulan dapat diambil sebagai berikut:

IL Proses pembangunan model deteksi kerusakan kendaraan menggunakan
arsitektur YOLOv9 dan RT-DETRv2 dilakukan melalui tahapan
preprocessing data, penerapan augmentasi yang seragam, pelatihan model
dengan resolusi input 640x640 piksel, serta optimisasi hyperparameter
menggunakan Optuna. Pengaturan eksperimen dilakukan secara konsisten
antar arsitektur untuk menjaga keadilan perbandingan performa. Hasil
pelatihan menunjukkan bahwa kedua arsitektur mampu mempelajari pola
kerusakan kendaraan pada dataset CarDD, meskipun memiliki karakteristik
konvergensi dan sensitivitas parameter yang berbeda.

2. Hasil perbandingan performa menunjukkan bahwa YOLOv9 menghasilkan
kinerja yang lebih optimal dibandingkan RT-DETRv2 berdasarkan metrik
akurasi deteksi dan efisiensi komputasi. Varian YOLOV9-C mencapai nilai
MAPS0-95 tertinggi sebesar 0,5840 dengan latensi inferensi 10,91 ms (91,66
FPS), sedangkan RT-DETRv2-L mencapai mAPS0-95 sebesar 0,5664
dengan latensi yang lebih tinggi sebesar 16,57 ms (60,33 FPS). Analisis
Pareto Frontier menunjukkan bahwa YOLOv9-M dan YOLOv9-C
merupakan model Pareto-optimal, di mana YOLOv9-M memiliki latensi
terendah dan YOLOv9-C memiliki akurasi tertinggi. Dengan
mempertimbangkan bahwa selisih latensi antara kedua model relatif kecil,
YOLOv9-C dipilih sebagai model terbaik karena memberikan akurasi deteksi
yang lebih tinggi tanpa mengurangi kelayakan implementasi real-time. Hasil
ini menunjukkan bahwa arsitektur Convolutional Neural Network (CNN)
lebih efektif dalam mengekstraksi fitur lokal pada dataset damage-centric
seperti CarDD dibandingkan pendekatan Transformer.

3. Implementasi prototipe aplikasi weh deteksi kerusakan kendaraan
menggunakan model YOLOv9-C menunjukkan kinerja fungsional dan

103

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 117

SKRIPSI

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

usability yang baik. Hasil pengujian Black Box Testing menunjukkan bahwa
seluruh fungsi utama aplikasi berjalan sesuai spesifikasi, mulai dari proses
“unggah citra, pelaksanaan inferensi, hingga visualisasi hasil deteksi. Evaluasi
menggunakan System Usability Scale (SUS) menghasilkan skor rata-rata
81,55 yang termasuk kategori Acceptable dengan Grade B. Hasil ini
menunjukkan bahwa sistem mampu digunakan secara efektif sebagai alat
bantu pra-inspeksi kerusakan kendaraan berbasis citra.

52 Saran
Penelitian ini masih memiliki beberapa keterbatasan, antara lain penggunaan

dataset tunggal (CarDD), pendekatan citra single-view, serta keterbatasan jumlah

data pada beberapa kelas kerusakan. Oleh karena itu, beberapa saran pengembangan
yang dapat dilakukan pada penelitian selanjutnya adalah sebagai berikut:

1. Pengembangan dataset dengan anotasi multi-view perlu dilakukan untuk
merepresentasikan satu kendaraan dari beberapa sisi, yaitu depan, belakang,
kiri, dan kanan, Pendekatan ini bertujuan untuk menyelaraskan distribusi data
pelatihan dengan kebutuhan sistem inspeksi kendaraan yang menilai kondisi
kendaraan secara menyeluruh, sehingga model dapat mempelajari relasi
antar-sisi secara lebih konsisten.

2. Pengembangan metode agregasi prediksi lintas sisi dapat dipertimbangkan
untuk meningkatkan stabilitas hasil deteksi pada sistem inspeksi empat sisi
Integrasi pada tingkat fitur atau tingkat keputusan berpotensi menghasilkan
penilaian kerusakan yang lebih representatif terhadap kondisi kendaraan
secara keseluruhan.

3. Peningkatan sensitivitas terhadap objek kecil seperti scratch, dent, dan crack
dapat dilakukan melalui optimasi representasi multi-skala, penyesuaian
resolusi input, atau penerapan mekanisme perhatian spasial yang tetap
mempertahankan efisiensi inferensi agar sistem tetap layak digunakan pada
aplikasi berbasis web.

104
PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 118

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

DAFTAR PUSTAKA

ASEAN Automotive Federation. (2024). ASEAN automotive statisties (as at
November 2024). ASEAN Automotive Federation. https://www.asean-
antofed.com/files/AAP. Statistics ytd nov2024.pdf

Amalia, C. R. P., & Mahyuddin. (2023). Perancangan sistem pakar untuk
mendiagnosa tingkat stres belajar pada siswa SMA dengan menggunakan
metode” forward”) chaining. Design Journal, I(1), 38-54.
Ihttps://doi.org/10.58477/dj.v1i1.27

Arkin, E., Yadikar, N., Xu, X., Aysa, A, & Ubul, K. (2022). A survey: Object
detection methods ftom CNN to transformer. Multimedia Tools and
Applications, 82(14), 21353-21383. https://doi.org/10.1007/s1 1042-022
13801-3

Bangor, A., Kortum, P. T., & Miller, J. T. (2008). An Empirical Evaluation of the
System Usability Scale. International Journal of Human-Computer
Interaction, 24(6), 574-594. https://doi.org/10.1080/10447310802205776

Bangor, A., Kortum, P., & Miller, J. (2009). Determining what individual SUS
scores mean: Adding an adjective rating scale. Journal of Usability Studies,
43), 114-123.

Bergstra, J, & Bengio, Y. (2012). Random search for hyper-parameter
optimization. Journal of Machine Learning Research, 13, 281-305.

Bochkovskiy, A., Wang, C., & Liao, H. M. (2020). YOLOv4: Optimal Speed and
Accuracy of Object Detection. arXiv preprint arXiv:2301016SI.
Ittps://arxiv.org/abs/2301.01651

Brooke, J. (1996). SUS: A quick and dirty usability scale. In P. W. Jordan, B.
‘Thomas, B. A. Weerdmeester, & I. L. MeClelland (Eds.), Usability evaluation
in industry (pp. 189-194). — Taylor = & — Prancis
hhttps://doi.org/10.1201/9781498710411-35

Cacciola, M., Frangioni, A., Asgharian, M., Ghaffari, A., Nia, V. P., & Montreal,
P. (2023). On the convergence of stochastic gradient descent in low-precision
number formats. arXiv preprint arXiv:2301.01651.
Ittps://arxiv.org/abs/2301.01651

Carion, N., Massa, F., Synnaeve, G., Usunier, N., Kirillov, A., & Zagoruyko, S.
(2020). End-to-end object detection with transformers. atXiv preprint
arXiv:2005.12872. https://arxiv.org/abs/2005.12872

Chaudhuri, M. (2023). Deep-learning apps for image processing made easy: A step-
by-step guide. In S. Advocates (Ed.), Streamlit Blog (Advocate Posts).
Streamlit Inc. Diakses 8 Oktober 2025, dari https://blog.streamlit.io/deep-
leamning-apps-for-image-processing-made-easy/

105

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 119

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Chicco, D., & Jurman, G. (2020). The advantages of the Matthews correlation
coefficient (MCC) over FI score and accuracy in binary classification
evaluation. BMC Genomics, 21(6). https://doi.org/10.1186/s12864-019-6413-
7

Chua, E. 9. Y., & Tan, J. H. (2025). RT-DETRv2 explained in 8 illustrations. atXiv
preprint arXiv:2509.01241. https://arxiv.org/abs/2509.01241

Dalal, N., Triggs, B., & Europe, D. (2005). Histograms of Oriented Gradients for
Human Detection. In Proceedings of the 2005 IEEE Computer Society
Conference on Computer Vision and Pattern Recognition (CVPR'05) (Vol. 1,
pp. 886-893). IEEE. https://doi.org/10.1109/CVPR.2005.177

Deb, K. (2011). Multi-objective optimisation using evolutionary algorithms: An
introduction. In L. Wang, A. Ng, & K. Deb (Eds.) Multi-objective evolutionary
optimisation for product design and manufacturing (pp. 1-24). Springer.
https://doi.org/10.1007/978-0-85729-652-8 1

Diwan, T., Anirudh, G., & Tembhurne, J. V. (2023). Object detection using YOLO:
Challenges, architectural successors, datasets and applications. Multimedia
Tools and Applications, 82(12), 9243-9275. https:/Idoi.org/10.1007/511042-
022-13644-y

Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner,
T., Dehghani, M., Minderer, M., Heigold, G., Gelly, S., Uszkoreit, J., &
Houlsby, N. (2021). An image is worth 16x 16 words: Transformers for image
recognition at scale. — atXiv preprint — arXiv:2010.11929.
hittps://arxiv.org/abs/2010.11929

GAIKINDO. (202Sa). GAIKINDO production data January-August 2025.
Gabungan Industri Kendaraan Bermotor Indonesia. Diakses 19 September
2025, dari https-//www.gaikindo.or.id/indonesian-automobile-industry-data/

GAIKINDO. (2025b). GAIKINDO wholesales data January-August 2025.
Gabungan Industri Kendaraan Bermotor Indonesia. Diakses 19 September
2025, dari https-//www.gaikindo.or.id/indonesian-automobile-industry-data/

Girshick, R. (2015). Fast R-CNN. arXiv preprint arXiv:1504.08083.
https://arxiv.org/abs/1504.08083

Girshick, R., Donahue, J., Darrell, T., Malik, J, & Berkeley, U. C. (2014). Rich
feature hierarchies for accurate object detection and semantic segmentation.
arXiv preprint arXiv:1311.2524. https://arxiv.org/abs/1311.2524

Goodfellow, L, Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press.
Diakses 9 September 2025, dari https://www.deeplearingbook.org

Gonzilez-Heméndez, D., Lopez-Martinez, F., & Rodriguez-Timénez, R. (2025). An
analysis of YOLO models versus RT-DETR applied to industrial vision.
International Journal of Advanced Robotic Systems, 221), 1-15.
'https://doi.org/10.61467/2007.1558.2025.1613.778

106
SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 120

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Grandini, M., Bagli, E., & Visani, G. (2020). Metrics for multi-class classification:
An overview. arXiv preprint arXiv:2008.05756.
https://arxiv.org/abs/2008.05756

Hasan, M. J., Nguyen, C. K., Boo, Y. L., Jahani, H., & Ong, K-L. (2025). Vehicle
damage detection using artificial intelligence: A systematic literature review.
WIREs Data Mining and Knowledge Discovery, 15(2), €70027.
hittps://doi.org/10.1002/vidm. 70027

He, K., Zhang, X., Ren, S., & Sun, J. (2016). Deep residual learning for image
recognition. In Proceedings of the IEEE Conference on Computer Vision and
Pattern Recognition (CVPR) (pp. 710-778). IEEE,
hittps://doi.org/10.1109/CVPR.2016.90

Hidayatullah, P., & Tubagus, R. (2024). YOLOv9 architecture explained. In
Stunning Vision — Al.” Diakses 6 Oktober 2025, dari
https://article.stunningvisionai.com/yolov9-architecture

Jain, V., Kavitha, H., & Kumar, S. M. (2022). Credit card fraud detection web
application using Streamlit and machine learning. 2022 IEEE International
Conference on Data Science and Information System (ICDSIS). TEE
https://doi.org/10.1109/ICDSIS55133.2022.9915901

Jocher, G., Chaurasia, A., & Qiu, J. (2023). YOLO hy Uttralptics. Ultralytics.
Diakses 1 September 2025, dari https://doos.ultralyties.com/

Jocher, G., Chaurasia, A., Stoken, A., Borovec, J, NanoCode012, Kwon, Y.,
TaoXie, Fang, J., Imyhxy, Michael, K., Lorna, V, A., Montes, D., Nadar, J.
Laughing, Tkianai, YxNONG, Skalski, P., Wang, Z., & Hogan, A. (2022).
ultralyties/yolovS: v6.1 - TensorRT, TensorFlow Edge TPU and Open VINO
Export and Inference. Zenodo. https:i/doi.org/10.5281/zenodo.6222936

Kementerian Koordinator Bidang Perekonomian Republik Indonesia. (2022).
Tumbuh signifikan dan miliki kontribusi besar ke PDB, sektor otomotif dukung
era elektrifikasi menjadi masa depan sistem transportasi Indonesia. Diakses 3
Oktober 2025, dari https//www.ekon.go.id/publikasi/detail/4744/tumbuh-
signifikan-dan-miliki-kontribusi-besar-ke-pdb-sektor-otomotif-dukung-era-
elektrifikasi -menjadi-masa-depan-sistem-transportasi-indonesia

Keskar, N. S., Mudigere, D., Nocedal, J., Smelyanskiy, M., & Tang, P. T. P. (2017).
On large-batch training for deep learning: Generalization gap and sharp
minima. arXiv preprint arXiv:1609.04836. https'//arxiv.org/abs/1609.04836

Khan, S., Naseer, M., Hayat, M., & Zamir, S. W. (2022). Transformers in vision :
A survey. ACM Computing | Surveys, 54(108), Article 200.
https://doi.org/10.1145/3505244

Khanam, R, & Hussain, M. (2024a). YOLOvII: An overview of the key
architectural enhancements. atXiv preprint — arXiv:2410.17725.
'https://doi.org/10.48550/arXiv.2410.17725

107

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 121

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Khanam, R., & Hussain, M. (2024b). What is YOLOvS: A deep look into the internal
features of the popular object detector. atXiv preprint arXiv:2407.20892.
https://arxiv.org/abs/2407.20892.

Krizhevsky, A., Sutskever, L, & Hinton, G. B. (2017). ImageNet classification with
deep convolutional neural networks. Communications of the ACM, 60(6), 84-
90. https:#/doi.org/10.1145/3065386

LeCun, Y., Boser, B., Denker, J. S., Henderson, D., Howard, R. E., Hubbard, W.,
& Jackel, L. D. (1989). Backpropagation applied to handwritten zip code
recognition. Neural Computation, 14), 541-551
https://doi.org/10.1162/neco.1989.1.4.541

Lewis, LR. (2018) Measuring Perceived Usability: The CSUQ, SUS, and
UMUX. International Journal of Human-Computer Interaction, 34(12),
1148-1156. https://doi.org/10.1080/10447318.2017.1418805

Li, X, Wang, W., Wu, L,, Chen, S., Hu, X., Li, J., Tang, J., & Yang, J. (2020).
Generalized focal loss: Learning qualified and distributed bounding boxes for
dense object detection.” arXiv preprint — arXiv:2006.04388.
https:/Jarxiv.org/abs/2006.04388

Li, Z, Liu, F., Yang, W., Peng, S., & Zhou, J. (2021). A survey of convolutional
neural networks: Analysis, applications, and prospects. JEEE Transactions on
Neural Networks and Learning Systems, 33(12), 6999-7019.
https://doi.org/10.1109/TNNLS.2021.3084827

Lin, T.-Y., Goyal, P., Girshick, R., He, K., & Dollir, P. (2018). Focal loss for dense
object detection. arXiv preprint arXiv:1708.02002.
https://arxiv.org/abs/1708.02002.

Liu, L., Guo, W., Huang, S., Li, C., & Shen, X. (2024). From COCO to COCO-
FP: A deep dive into background false positives for COCO detectors. atXiv
preprint arXiv:2409.07907. https://arxiv.org/abs/2409.07907

Liu, W., Anguelov, D., Ethan, D., Szegedy, C., Reed, S., Fu, C., & Berg, A. C.
(2016). SSD : Single shot multibox detector. In B. Leibe, J. Matas, N. Sebe, &
M. Welling (Eds.), Computer Vision - ECCV 2016 (LNCS, Vol. 9905, pp. 21-
37). Springer. https://doi.org/10.1007/978-3-319-46448-0 2

Liu, Z., Lin, ¥., Cao, Y., Hu, H., Wei, Y., Zhang, Z., Lin, S., & Guo, B. (2021).
Swin transformer: Hierarchical vision transformer using shifted windows. In
Proceedings of the IEEE/CVF International Conference on Computer Vision
(ICcy) (pp. 9992-10002). TEE.
https://doi.org/10.1109/TCCV48922.2021.00986

Loshchilov, L, & Hutter, F. (2019). Decoupled weight decay regularization. arXiv
preprint arXiv:171 1.05101. https://arxiv.org/abs/1711.05101

Lowe, D. G. (2004). Distinctive image features from scale-invariant keypoints.
International Journal of. Computer Vision, 60, 91-110.

108

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 122

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

‘ttps://doi.org/10. 1023/B: VISI.0000029664.99615.94

Ly, W., Zhao, Y., Chang, Q., Huang, K., Wang, G., & Liu, Y. (2024). RT-DETRv2:
Improved baseline with bag-of-freebies for real-time detection transformer.
arXiv preprint arXiv:2407.17140. https://arxiv.org/abs/2407.17140

Masters, D., & Luschi, C. (2018). Revisiting small hatch training for deep neural
networks, arXiv preprint arXiv:1804,07612. https://arxiv.org/abs/1804,07612

Masum, M., Shahriar, HL, Haddad, H., Faruk, J. H., & Valero, M. (2022). Bayesian
'hyperparameter optimization for deep neural network-based network intrusion
detection. In 2021 IEEE International Conference on Big Data (Big Data) (pp.
5413-5419). IEEE. htps://doi.org/10.1109/BigDataS2589.2021.9671576

‘Moraes, A. M., Pugliese, L. F., Santos, R. F. dos, Vitor, G. B., Braga, R. A. da S.,
& Silva, F. R. da. (2025). Effectiveness of YOLO Architectures in Tree
Detection: Impact of Hyperparameter Tuning and SGD, Adam, and AdamW
Optimizers. Standards, 5(), 9. MDPI.
Inttps://doi.org/10.3390/standards5010009

Muhammad, M., Ullah, H., Iqbal, S., Alghobiri, M., Igbal, T., & Fayyaz, M. (2023).
Deep learning in news recommender systems: A comprehensive survey,
challenges and future trends. Neurocomputing, 562, 126881
Inttps://doi.org/10.1016/j.neucom.2023.126881

Mulyono, H., & Ardhiyani, R. P. (2018). Analisis dan perancangan sistem informasi
pariwisata berbasis web sebagai media promosi pada Kabupaten Tebo. Jurnal
Manajemen Sistem Informasi, 3(1), 1-10.

O'Shea, K., & Nash, R. (2015). An introduction to convolutional neural networks.
arXiv preprint arXiv:1511.08458. https://arxiv.org/abs/151 1.08458

Pérez-Zarate, S. A., Corzo-Garcia, D., Pro-Martin, J. L., Alvarez-Garcia, J. A.,
Martinez-del-Amor, M. A., & Fernfndez-Cabrera, D. (2024). Automated car
damage assessment using computer vision: insurance company use case.
Applied Sciences, 14(20), 9560. https://doi.org/10.3390/app14209560

Phung, V. H., & Rhee, E. J. (2018). A deep learning approach for classification of
cloud image patches on small datasets. Journal of Information and
Communication Convergence — Engineering, — 168), 173-198.
'https://doi.org/10.6109/jicce.2018.16.3.173

Powers, D. M. W. (2020). Evaluation: From precision, recall and F-measure to
ROC, informedness, markedness & correlation. arXiv preprint
arXiv:2010.16061. https://arxiv.org/abs/2010.16061

Pressman, R. S., & Maxim, B. R. (2015). Software engineering: A practitioner's
approach (8th ed.). MeGraw-Hill Education.

Ramazhan, M. R. S., Bustamam, A., Buyung, R. A. (2025). Smart car damage
assessment using enhanced YOLO algorithm and image processing

109

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 123

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

techniques. Information, 16(3), 211. https://doi.org/10.3390/info16030211

Redmon, J., Divvala, S., Girshick, R., & Farhadi, A. (2016). You only look once:
Unified, real-time object detection. atXiv preprint arXiv:1506.02640.
'https://arxiv.org/abs/1506.02640

Redmon, J. & Farhadi, A. (2016). YOLO9000: Better, faster, stronger. arXiv
preprint arXiv:1612.08242. https:/arxiv.org/abs/1612.08242

Redmon, J, & Farhadi, A. (2018). YOLOv3: An incremental improvement.
arXiv:1804.02767. https://arxiv.org/abs/1804.02767

Ren, S., He, K., Girshick, R., & Sun, J. (2016). Faster R-CNN : Towards real-time
object detection with region proposal networks. arXiv _ preprint
arXiv:1506.01497. https://arxiv.org/abs/1506.01497

Rezatofighi, H., Tsoi, N., Gwak, J., Sadeghian, A., Reid, T., & Savarese, S. (2019).
Generalized intersection over union: A metric and a loss for bounding box
regression. arXiv preprint arXiv:1902.09630.
'https://arxiv.org/abs/1902.09630

Ruby, A. U,, Theerthagiri, P., Jacob, I. J., & Vamsidhar, Y. (2020). Binary cross
entropy with deep learning technique for Image classification. International
Journal of Advanced Trends in Computer Science and Engineering, 9(4),
5393-5397. https://doi.org/10.30534/ijatese/2020/175942020

Salih, Y., & Saefullah, R. (2024). Black Box testing on website-based guestbook
registration applications, International Journal of Mathematics, Statistics, and
Computing, 2(2), 44-49. https://doi.org/10.46336/ijmse.v2i2.96

Sari, M. (2021). Implementasi framework Codelgniter 3 dalam marketplace
showroom Dp Dua Putri dengan model prototyping. Jurnal Transformatika,
18(2), 115-123.

Sarath, P., Soorya, M., Shaik Abdul Rahman, A., Kumar, S. S., & Devaki, K.
(2020). Assessing car damage using Mask R-CNN. arXiv preprint
arXiv:2004.14173. https://arxiv.org/abs/2004.14173

Sauro, J., & Lewis, J. R. (2012). Quantifying the user experience: Practical
statistics for user research. Morgan — Kaufimann.
'https://doi.org/10.1016/C2010-0-65192-3

Shorten, C., & Khoshgoftaar, T. M. (2019). A survey on image data augmentation
for deep learning. Journal of Big Data, 6(60). https://doi.org/10.1186/540537-
019-0197-0

Smith, L. N. (2017). Cyelical learning rates for training neural networks. In 2017
IEEE Winter Conference on Applications of Computer Vision (WACV) (pp.
464-472). IEEE. https://doi.org/10.1109/WACV.2017.58

Sommerville, 1. (2016). Software Engineering (10th ed.). Pearson Education.

110

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 124

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Suvittawat, N., Kurniawan, C., Datephanyawat, J., Tay, J., Liu, Z., Soh, D. W., &
Ribeiro, N. A. (2025). Advances in aircraft skin defect detection using
computer vision: A survey and comparison of YOLOv9 and RT-DETR
performance. Aerospace, 12(4), 356,
https://doi.org/10.3390/aerospace12040356

Tharwat, A. (2021). Classification assessment methods. Applied Computing and
Informatics, 17(1), 168-192. https://d0i.org/10.1016/).aci.2018.08.003

Tian, Z., Ye, M., & Doermann, D. (2025). YOLOv12: An attention-centric real-time

object detector. arXiv preprint arXiv:2502.12524.
https://arxiv.org/abs/2502.12524
Tullis, ——T. Ss, & Stetson, I N. (2004).

A comparison of questionnaires for assessing website usability. Proceedings
of the Usability Professionals Association (UPA) Conference, Minneapolis,
USA.

Umam, S.N,, Sumantri, R. B. B., dan Setiawan, R. A. (2023). Usability testing pada
PUSADBOT menggunakan black-box dan System Usability Scale (SUS).
Prosiding SENAPAS, 1(1), 156-162.

Vanathi, B., A, R., & Lekhasri, S. (2025). Damage detection using YOLOv8 AT
for vehicle assessment. International Journal of Innovative Seience and
Research Technology. https:/idoi.org/10.38124/ijistt/25mar567

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N.,
Kaiser, E., & Polosukhin, T. (2023). Attention is all you need. arXiv preprint
arXiv:1706.03762. https://arxiv.org/abs/1706.03762.

Viola, P., Way, O. M., & Jones, M. J. (2004). Robust real-time face detection.
International Journal of Computer Vision, 37(2), 137-154.
https://doi.org/10.1023/B:VTSI.0000013087.49260.fb

Voulodimos, A., Doulamis, N., Doulamis, A., & Protopapadakis, E. (2018). Deep

earning for computer vision: A brief review. Computational Intelligence and
‘Neuroscience, 7068349. https://doi.org/10.1155/2018/7068349

Wang, B. (2022). A parallel implementation of computing mean average precision.
arXiv preprint arXiv:2206.09504. https://arxiv.org/abs/2206.09504

Wang, C-Y,, Yeh, I-HL, & Liao, HL-¥, M. (2024). YOLOv9: Learning what you
want 10 learn using programmable gradient information. atXiv preprint
arXiv:2402.13616. https://arxiv.org/abs/2402.13616

Wang, C.-Y., Bochkovskiy, A., & Liao, H.-Y. M. (2024b). YOLOv/0: Real-time
end-to-end object detection. arXiv preprint atXiv:2405.14458.
https://arxiv.org/abs/2405.14458

Wang, M., & Wu, L. (2024). 4 theoretical analysis of noise geometry in stochastic
gradient descent. arXiv preprint — arXiv:2310.00602.

1

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 125

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

hhttps://arxiv-org/abs/2310.00692

Wang, X., Li, W., & Wu, Z. (2023). CarDD: A new dataset for vision-based car
damage detection. IEEE Transactions on Intelligent Transportation Systems,
24(7), 7202-7214, https://doi.org/10.1109/TITS.2023.3258480

Watanabe, S. (2025). Tree-structured Parzen estimator: Understanding its
algorithm components and their roles for better empirical performance. atXiv
preprint arXiv:2304.11127. https://arxiv.org/abs/2304,11127

Wiley, V., & Lucas, T. (2018). Computer vision and image processing: A paper
review. International Journal of Artificial Intelligence Research, 2(1), 28-36.
Inttps://doi.org/10.29099/ijair.v2il 42

Yaghini, M., Liu, P.-Y., Boenisch, F., & Papemot, N. (2023). Learning with
impartiality to walk on the Pareto frontier of fairness, privacy, and utility
arXiv preprint arXiv:2302,09183. hitps://arxiv.org/abs/2302.09183

Ye, R, Chen, L., Liao, W., Zhang, L, & Ishibuchi, FI. (2024). Data-driven
preference sampling for Pareto front learning. atXiv preprint
arXiv:2404.08397. https://arxiv.org/abs/2404.08397

Yu, H., Wan, C., Dai, X., Liu, M., Chen, D., Xiao, B., Huang, Y., Lu, Y., & Wang,

L. (2025). Real-time image segmentation via hybrid convolutional-transformer
architecture search (HyCTAS). arXiv preprint arXiv:2403.07431

‘Yu, J, Jiang, Y., Wang, Z., Cao, Z., & Huang, T. (2016). UnitBox: An advanced
object detection network. arXiv preprint arXiv:1608.01471
https://arxiv.org/abs/1608.01471

Zhang, H., Cisse, M., Dauphin, Y. N., & Lopez-paz, D. (2018). mixup: Beyond
empirical risk minimization. arXiv preprint _arXiv:1710.09412.
https://arxiv.org/abs/1710.09412.

Zhao, Y., Lv, W., Xu, S., Wei, I, Wang, G., Dang, Q., Liu, Y., & Chen, J. (2024).
DETRs beat YOLOs on real-time object detection. arXiv preprint
arXiv:2304.08069. https://arxiv.org/abs/2304.08069

Zheng, Z., Wang, P., Liu, W., Li, J., Ye, R., & Ren, D. (2019). Distance-IoU loss:
Faster and better learning for bounding box regression. arXiv preprint
arXiv:191 1.08287. https://arxiv.org/abs/191 1.08287

Zhu, C., Ping, W., Xiao, C., Shoeybi, M., & Goldstein, T. (2021). Long-short
Transformer : Efficient Transformers for language and vision. arXiv preprint
arXiv:2107.02192. https://arxiv.org/abs/2107.02192.

Zhu, X., Su, W., Lu, L., Li, B., Wang, X., & Dai, J. (2021). Deformable DETR:
Deformable Transformers for end-to-end object detection. arXiv preprint
arXiv:2010.04159. https://arxiv.org/abs/2010.04159

12

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 126

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

LAMPIRAN
Lampiran 1. Hasil Hyperparameter Tuning untuk YOLOV9-S
Batch | Learning mAPS0- | Train | Validation
Rank | Telat | "Se "Rate | MAPSO 7 tos pa
1 25 32 000278 | 0,66952 | 0.53914 | 0.35350 | 061920
z 13 32 ‘0.00054 | 0673227 0.53448 | 0.35680 | 0.62340,
3 18 32 000298 | 0,6%649 | 0.54936 | 0,34890| oe2410
4 1s 32 000383 | 0,68547 |_0,54204_| o,3so0| 0.62890.
5 9 32 000211 | oes913 | O,s2ssi | 0,36420 | 0.62980.
6 14 32 000275 | 061822) 0.54119 | 0,36170| 063390
a u 32 0.00100 067805 | 0.53563 | 0.36640 | 0.63620.
8 2 32 000291 | oenisi | 0.54025 | 0.36910 | 0.63940.
9 27 32 000245 0,67964 |_ 0.54319 | 0.37180 | 064210
10 22 32 000295 | 0,67622 | 0,s3s1o | 0,37490| 0.64560.
1 12 32 000179 | oe73sa| 0.53436 | 0,37720| 061820
12 4 32 0.00167 | 0673227 0.53755 _| 0.37940 | 0.65130.
13 0 16 ‘0.00056 | 0.67414 | 0.53457 | 0,38210| 0.65480.
14 17 32 0.00494 | 066754) 0,53178 | 0,38450 | 0.65890.
15 6 16 0.00164 | 0,66994 | 0.52840 | 0,38760| 0.66140
16 20 32 0.00098 [0.665% | 0.52611 | 0,39120 | 0.66490.
17 5 32 0.00372 | 0,653K6 | 0.52034 | 0.39480 | 0.66850.
18 23 32 000629 | 0,66163 | 0.52269 | 0,39920 | oer210
19 24 32 000119 | 066328) o,s2428 | 0,40350 | 061540
20 26 16 000075 | 0,65926 | 0,s2178 | 0.40790 | 061890
21 3 32 000023 [0.64990 | 0.51954 | 0,41230 | 0.68280.
22 7 16 ‘0.00414 [0.65412 | 0.51497 | 0.41610 | 0.68610.
23 1 32 000020 | ocasi9 | o,stosi | 0.42050 | 068920
24 z 16 000011 | 064349 | 0,51307_| 0,42470 | 069210
25 8 16 000017 | 062557 | 0,s0390 | 0,42960 | 0.69580.
26 10 32 000842 | 0,639x% | O,s0400 | 0.43480 | 0,69920
27 16 32 0.00919 [0.63270 | 0.49860 | 0,44090 | “070310
28 19 32 ‘0.00590 | 0,66402 | 0,53059 | 0,38620 | 070580
29 28 32 000379 | 0,67854 | o,sa1i6 | 0,36080 | 070890
30 29 16 000039 | 0.61003 | 0.49234 | 0.45270 0.71430.
113

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 127

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

(Lampiran 2. Hasil Hyperparameter Tuning untuk YOLOV9-M

“Learning MAPSO- | Train | Validation
Rank | Triat | Batch "Rate | MAPSO mi toe pai
1 26 16 000275 | 070220 | 0.56235 | 0,32690 | 04010
2 12 32 000178 [0,70281 | 0,57438 | 0,33840 |" 0,74480,
3 14 32 0.00194 | 0683527 0,54900 | 0,35280 | “074860
4 4 32 000167 | 070227) 0,55900_| 0,34120 |" 0,75290,
5 in 32 10,0100 | 0,69840 | 0,ss200 | o3ss6o| 07410
6 29 16 0.00066 | 0.69574 | 0.55139 | 0.36480 | 0.75980.
7 24 32 000053 | 067008 | 0,53sa7 | 0,35970 | 076290
5 3 32 0.00060 | 067271 | 0,s37a1 | 0,360 | “076640
9 2 16 ‘0.00011 | 066375 | 0,52642 | 0,36290 | 0,76920,
10 15 32 0oooss | 068075 | 0,s4258 | 0,37150 | 0,77360
1 1 32 000020 | o67m5 | 0,53536 | 0,38040 | 078120
12 8 16 000017 _[0,68021 | 0,54463 | 0,38710 | 0.78540,
3 3 32 000025 0,67066 | 0.53239 | 0,38490 | “078620
14 0 16 0.00056 | 068883 | 0.55468 | 0.37860 | 0,78810,
15 22 32 10,0266 | o6s260| O,5s6s6 | 0,39270 | o,79040
16 2 32 000125 | oeusos| 0,ssass | 0,39020 | “0,79420
17 23 32 000153 | 071023) o,se1s6 | 0,39710 | o9sio
18 5 32 000172 | 0,69792 | 055551 |odorso| “079640
19 16 32 10,0350 | 069930 | o,ssan6 |odiaso| 0,79830
20 9 32 000211 | 060990 o,ssss2 | 0,38950 | 0,79910
21 27 16 0.00274 | 0,69660 | 0,5s203 | 0,43170| os0120
22 19 32 0.00288 | 069725 | o,sssos | od2reo| o,80370
2 18 32 0.00426 [0.70748 | 0.56059 | odisa0| “ososa0
24 10 32 000815 | 068252 | 0.55324 | 0,41260 | 0.81090,
25 20 32 0.00615 | 0,65667 | 0,s2025 | 0,42510 | o,sor60
26 28 16 0.00560 | 0,6897% | 0.54923 | 0.43490 | 0.80970,
27 25 32 000619 | o6r4s0| 0,54579 | 0.42860 | o,s1280
28 6 16 0.00164 067522) 0.53935 | 0.40590 | 0.81560.
29 7 16 000414 | 066572 | 0,53320 | odos7o| o,82430
30 17 32 0.00906 | 0,56912 042647 | 0.45880 [0.89690
114

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 128

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

“Lampiran 3. Hasil Hyperparameter Tuning untuk YOLOV9-C

Batch | Learning WAPSO- | Train | Validation
Rank Trial Size: prin “S| mapso ai tae py
T P3 32 | aoe Pori | oseso7 | 0.34200] 0.66160
2 12 32 | oooro | 0.72684 | 0.5667 [0.31980 | ~0,66410
3 19 32 [0.00124 | o,71938 | 0.56273 [0.32340 | 0.66540
4 Pi 32 0.00266 | 0,72334 | 0.56059 | 0,3s680 | _0,66890
3 9 32__|0,00211_|_0,72068 | 0.57825 [0.30170 | 0.67140.
6 4 32 | ooo1e7 Fotos | o.s7s40[ 0.39590 | 0.67320
T if 32 | 0.00195 | 0.71439 | 0.57152 | 0,32610 | 0.67450
8 16 32 | 0.00350 | 072762 | 0.57623 | 0,32970 | 0.67630,
° 2 32 00025 | 0.71290 | 0.57513 [0.32910 | 0.67740
10 1 32 00010 |_0,71802_| 057551 | 0.32480 | _0,67#20
n 26 16 | 0.00237 [0.71074 | 0.57379 | 0.30860 | 0.67960.
12 [33 321 0.00134 | 0,71240 | 0,57422, | 0.32850 | 0.68020
3 20 32_| 0.00299 | 0.70606 | o.s6715 [0.33100 | 0.68270
14 Fa 16 | 000010 | 0:70409-| 055857 | 0.31040 | 0,68390)
15 15 32 | 0.00085 |_0,7067# | 0.85931 [0.32560 | _0,68510
16 1 32 | 0.00060 | ogosrs | 0.85665 | 0.37710 | osenao
17 2 32 | 0.00517 | 0,69570 | 0,55418 | o3sasof 0.69010
18 27 32 000077 | 069623 | 0.55188 | 0,33080| 0,69120
19 3 32 [0.00023 | 0,69100 | 0.85044 [0.32390 | ~0,69210
20 5 32 0002 _|_0,6#296 | osaso | 0525201 _0,69370
21 2 16 | -oooon (065257 asasos | 0.30740 | 0,69420
22 1 32 | 0.00020 | o,6a16 | o,s4611 [0.32790 | _0,69560
2 7 16 | ooona [0.68346 | ass | 0.30790 | 0.69640.
2 Fa 32 0.00040 | ossoso | 058175 | 0538801 070020
25 6 16 | o00sa [0.71151 | 056256 | 0,30810 [0.70350
26 2s 32 |0.00587 | 0.70682 | 0.56232 [0.30930 | 0.70560
27 10 32 | ogosis | ag9os1 | 056057 [0.32450 | o7unao
P3 a 16 | o0oos [0.71348 |0,56970_| 0.30720 | 0.71080.
29 0 16 | 0.00056 | 0.69919 |_o,s6111_| 020750 omp10:
30 17 32 0.00861 | 0,59614 045427 | 0,52000| 076000
115

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 129

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

Lampiran 4, Hasil Hyperparameter Tuning untuk RT-DETRV2-S

Learni ‘mAPS0- Train | Validation

Rank | Telat | Baen | Carsing | mapso | MARS Tania | Vee
1 1 1G | Ooooze7 | 0.60030 051511 | 036720 | 0.47660
z Oo 16 Lo0no17o| 0621281 0.52339 | 037240 | 0.47980
3 A 16 | 0.000200 | 0,61402 | 0.52115 | 0.37410 | 0.48060.
4 25 16 | 0.000215 | 0.62147 | 0.67585 | 0.37680 | 0.48640
3 3 32 0000333 | 0,61796 | 0,50603_|_0.35890 | _0,49090
6 2 16 | 0.000089 | 059845 | 05018 | 038170 | 0.49690.
7 23 16 | 0,000321 | 0ss9s7 | 041425 | 0.38820 | 0.49880.
5 9 16 10000225 | 0546821 039712 | 030140 | 0.50560.
9 19 16 | 0,000250 | 0.54163 | 0.38538 | 0.39460 | 0.50740.
10 21 16 | 0,000268 | 0.55241 | 039599 | 035700 | 0.50960
1 13 16 | 0.000148 | 0.53694 | 038035 | 0.40070 | 0.51110
12 15 16 | 0,000203 [0.53871 | 038366 | 0.40380 | 0.51340.
13 12 16 | 0.000291 | 054895 039101 | 0.40620 | 0.51780.
1 28 16 | 0,000282 [0.53462 | 037846 | 0.40950 | 0.51870
15 27 16 | 0,000179 | 0.52684 | 036869 | 0.41240 | 0.51990
15 22 16 (0000237 | 0523171 036525 | 0.41560 | 0.52140.
17 4 16 | 0,000428 | 0501927 0.35046 | 0.41890 | 0.52480
1s 24 16 — 0.000421 | 051948 036152 | 0.42170 | 0.52810
19 17 16 | 0.000184 [0.47385 | 032549 | 0.42590 | 0.54860.
20 20 16 | 0.000166 | 0.48971 | 033838 | 0.43010 | 0.55320
21 10 16 | 0.000150 | 0.47236 032192 | 0.43480 | 0.55040.
22 14 16 | 0.000339 | 0.41874 | 026885 | 0.43890 | 0.56010
23 18 32_| 0.000362 | 0.43301 | 028277 | 0.44280 | 0.56280
24 11 16 | 0.000158 | 0.45162 | 0.30044 | 0.44610 | 0.56670
25 2 16 —Lo0oooe | 04138 026255 | o.4s020 | 0.57490
26 16 16 | 0.000123 | 0.42187 | 0.27180 | 0.45480 | 0.58960.
27 6 32__| 0000191 | 0.33684 | 0,18224 | 0.45890 | _0,60120
28 26 32 | 0.000138 | 0.28653 | 0,12403 | 0.46370 | 062550
29 7 32 -—L 0,000105 | 0.24168 | 009630 | 0.46890 | _0,64730
30 5 32 0000116 (023642 | 009195 T 47500 | _0,66000

116

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 130

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

“Lampiran 5. Hasil Hyperparameter Tuning untuk RT-DETRV2-M

Learni MAPSO- Train | Validation
Rank | Telat | Baten | Cearsing | mapsy | MARS Tee ar
1 Oi Te | 0000225 | 0.6374 | Ossa7s | 034720 | 0.42530
z 1 16 | 0,000257 [0.69088 | 0553520 | 034980 | 0.42810
3 12 16 | 0.000291 | 066502 | 0.50079 | 035140 | 0.42960.
4 22 16 [0.000201 | 0675451 0552432 | 035290 | 0.43020
3 10 16 |_0,000150 | oesess | 0.54067 | 035480 | 03110
6 27 16 | 0.000218 | 0.63087 | 0.48701 | 035570 | 0.43340.
7 23 16 | 0.000163 [0.67614 | 0.53907 | 035590 | 0.43430
5 0 16 | 0.000170 | 0.6361 | 0.54932 | 034080 | 0.43560.
9 4 16 | 0,000428 [0.67038 | 0.53041 1 035890 | 0.43680
10 1 16 [0.000158 |_0,66072 osi981 | 035710 | 0.43840
1 21 16 | 0.000185 | o,¢s084 | 0.50721 | 036080 | 0.44190.
12 13 16 | 0.000148 | oes2s7 | 0.54560 | 033860 | 0.44260
13 15 16 | 0.000123 [0.67548 | 0.59707 | 036520 | 0.44410.
1 8 16 Looooz0o| Oe6e79 | 0.54221 | 0.34690 | 0.44780
1s 29 16 | 0.000247 |_0,63093 | 0.46983 | 036980 | 0.45260
15 3 32 | 0.000333 | 0,64062 | 0.52208 | 0.37140 | 0.45570
17 2g 16 100002527 062081 | 0.47731 | 037420 | 0.45690
1s 1 16 | 0.000234 [0.61054 | 0.46825 | 037860 | 0.47020.
19 2 16 | 0.000089 [0.65048 | 0553542 | 035630 | 0.46980.
20 3 32 | 0.000116 | 0,64092 | 052286 | 035970 | _0,46890
21 20 16 | 0.000130 | 0.61073 | o.eass | 0.38050 | 0.47380.
22 1 16 | 0.000143 | oeo0saT 0.46221 | 038310 | 0.47510
23 28 16 | 0.000143 |0,s9x42 | 0.45639 | 038560 | 0.47640.
24 17 16 | 0.000089 [0.58053 | 0.43746 | 030370 | 0.48990
25 25 16 | 0.000349 [0.39084 | 0.44204 | 030920 | 0.49730
25 6. 32_| 0.000191 | 0.55063 | 0.40283 | 0.39680 | 0.49540
27 15 16 | 0.000562 | 0.35091 | 039974 | 0.41060 | 0.51480
28 18 32— 0.000179 | 0.52061 | 0.39031 | 0.40580 | 0.52890
29 25 32 | o0o0os | 050083 | 0,32904_| 0.40820 0,s5340
30 7 321 0000105 | 0,46078 | 031015 | 042000 | 0.35000
117

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 131

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

(Lampiran 6, Hasil Hyperparameter Tuning untuk RT-DETRV2-L

Learni MAPSO- | Train | Validation
Rank | Telat | Baten | Cearsing | mapsy | MAT Tee ar
1 1 Té | 0.000267 | 0.6391 | Os6osi | 035340 | 0,s0010
2 29 16 [0.000181 | 0.69318 | 0.56073 | 035520 | 0.50140
3 4 16 | 0.000428 [0.67144 | ossto7 | 035810 | 0.s04x0.
4 5 16 | 0.000200 [0.69313 | 0.56704 | 032970 | 0.50560
3 10 16 |0,000150 | 0,67642 | 0.56256 | 035940 | 0.50670
6 20 16 | 0.000121 | 0.68752 | 0.56784 | 036120 | 0.50830
7 0 16 | 0.000170 [0.68286 | 0.57080 | 0.34780 | 0.50960
5 21 16 | 0.000180 | 0.65138 | o,sisa6 | 035490 | 0.51020.
9 16 16 | 0.000142 [0.66982 | 0.58171 | 035760 | os1170
10 25 16 |_0,000160 |0,6H664 | 0.57579 | 033840 | 0.51280
1 28 16 | 0.000137 | 0.66211 | 0.52481 | 035260 | 0.51560.
12 9 16 100002257 0661251 052558 | 035130 | 051720
13 1 16 | 0.000166 | 0.68491 | 0.56669 | 0.34720 | O.SI8I0
1 19 16 | 0.000124 | 069733 | 0.57045 | 031190 | 0.51900
1s 3 321 0000333 | 0,67594 | 055362 | 035640 | o,s2000
15 ar 16 | 0.000273 | oe12a7 | 0.49425 | 036000 | 0.53010
17 17 16 Lo00o2se | oe1183T 0.49252 | 036210 | 0.53280
1s 1 16 | 0.000283 [0.61201 | 0.49260 | 036150 | 0.53560.
19 2 16 | 0.000089 | e7e21 | 0.56607 | 0.34540 | 053500
20 23 16 100001327 es77a| 02520 | 0.34890 | 053740
21 24 16 | 0.000099 | 0.64013 | 0.49523 | 036580 | 0.56070.
22 27 16 100001227 oe42saT 0.49790 | 036820 | 0.56510
23 3 32— 0000115 | 0,67352 | 0.ss418 | 0.37240 | 0.57320
24 22 16 | 0.000085 | 061587 | 0.47170 | 037510 | 0.60840
25 12 16 | 0.000445 |[0,39326 | 0.44678 | 038050 | 0.61290
25 18 32—1 0000229 | ossaro | 0.4383 | 0.38480 | 063060
27 6 32 [0.000191 | 0,58632 | 0440281 038970 | _0,65020
28 26 '32 | o,000160_| 0.57144 | 0.42745 | 0.39340 | 0.65640
29 15 16 [0.000370 [0.54081 | 039037 | 040190 | _0,68030
30 7 321 0000105 | 0,53622 | 038875 | 0.41000 | _0,70000
118

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 132

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

(Lampiran 7. Hasil Form Sysiem Usability Seale (SUS)

mw | 1 | g2 | 93 | o4 | os | oe] oF | 8 | @ | O10
1 4 1 5 F3 4 2 | 1 4 vi
PEN DN NS NK DN DES DS NE ND DE DE
aps TN DN ND KS NS BE 52
EN DNS NS KS DT DS DS ES NA DE ME
ES NS NS DS TT KS NE NK NT ES
CN NE NG DN DN DN NS NT DE
KN KS DN DK DS KS ES DE NS NE 3
EN NE TN DN DD AS tes AT BE 2
CN NS TN DK DES KS ND DE DT ES 3
wf>4at2t4t2t4¢f2,4)f2)s 2
119

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


## Halaman 133

IR - PERPUSTAKAAN UNIVERSITAS AIRLANGGA

(Lampiran 8, Hasil Perhitungan System Usability Seale (SUS)

aw {ot | 92 | 93 | 4 | 95 [96 | Q7 | 8 | 09 | gio] sm | Sus
rhafirsta2taf2fsa tifa ta tf xo
alatas take hahaha Le
EN DA DA DA BE DI DE DA SS BSA ES BEI
ahaters bae saos
ES DD DP DE ED NE DES SA NE PA [34 [aso
CE DE DE DE NE ES DE DE GE DA [34 [sso
nista late tanah batas
ES DE DP DE ED DE ED BE [aso
o>s}[2]4}214{[i1,4}i1}4[2)% as

PN DS DE ES te ts DER DIET

120

SKRIPSI PERBANDINGAN METODE DAN. ARKAN SYAFIQ ATTAOY


