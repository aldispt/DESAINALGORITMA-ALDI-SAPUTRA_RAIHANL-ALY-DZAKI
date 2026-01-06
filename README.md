# Optimasi Penggunaan Perangkat Elektronik Kamar Kos  
## 0/1 Knapsack Problem Menggunakan Algoritma Backtracking

## 📌 Deskripsi Proyek
Proyek ini merupakan tugas mata kuliah **Desain dan Analisis Algoritma** yang membahas penerapan **algoritma 0/1 Knapsack Problem** dengan pendekatan **Backtracking** untuk mengoptimalkan penggunaan daya listrik di kamar kos mahasiswa.

Permasalahan berangkat dari kondisi nyata di mana mahasiswa kos memiliki **keterbatasan daya listrik (MCB 900 Watt)**, sementara terdapat banyak perangkat elektronik dengan tingkat kepentingan yang berbeda-beda. Tujuan utama adalah memilih kombinasi perangkat yang memberikan **nilai kepentingan maksimum** tanpa melebihi kapasitas daya listrik.

---

## 🎯 Tujuan
- Menerapkan algoritma **0/1 Knapsack Problem**
- Mengimplementasikan **Backtracking dengan pruning**
- Membandingkan efisiensi **Brute Force vs Backtracking**
- Menentukan kombinasi perangkat elektronik yang optimal dan aman

---

## ⚙️ Spesifikasi Masalah
- **Jumlah perangkat (n)**: 10
- **Kapasitas daya maksimum (M)**: 900 Watt
- **Jenis masalah**: 0/1 Knapsack Problem
- **Metode penyelesaian**: Backtracking

---

## 📦 Data Perangkat

| No | Nama Perangkat        | Konsumsi Daya (Watt) | Nilai Kepentingan |
|----|----------------------|----------------------|-------------------|
| 1  | Laptop Gaming        | 200                  | 95                |
| 2  | Rice Cooker          | 350                  | 90                |
| 3  | AC Portable          | 400                  | 85                |
| 4  | Kipas Angin          | 50                   | 60                |
| 5  | Lampu Belajar LED    | 10                   | 40                |
| 6  | Dispenser (Hot)      | 300                  | 50                |
| 7  | Setrika Listrik      | 300                  | 45                |
| 8  | Speaker Monitor      | 40                   | 30                |
| 9  | Charger HP           | 25                   | 70                |
| 10 | Teko Listrik         | 450                  | 20                |

---

## 🧮 Model Matematis

### Fungsi Tujuan
Memaksimalkan total nilai kepentingan:
\[
\text{Max } Z = \sum_{i=1}^{n} p_i x_i
\]

### Kendala Kapasitas
\[
\sum_{i=1}^{n} w_i x_i \leq 900
\]

### Variabel Keputusan
\[
x_i \in \{0,1\}
\]

---

## 🌳 Algoritma Backtracking
Algoritma Backtracking membangun **pohon ruang status (state space tree)** secara dinamis.  
Setiap node merepresentasikan keputusan **mengambil (1)** atau **tidak mengambil (0)** suatu perangkat.

### Pruning
Cabang pencarian akan dipangkas apabila:
\[
\sum w_i x_i > 900
\]

Dengan teknik ini, algoritma tidak perlu mengevaluasi seluruh kemungkinan solusi.

---

## ⚖️ Perbandingan Brute Force dan Backtracking

| Aspek | Brute Force | Backtracking |
|-----|------------|--------------|
| Jumlah Node | \(2^{10} = 1024\) | Sebagian node |
| Pemeriksaan Kendala | Di akhir lintasan | Di tengah proses |
| Efisiensi | Rendah | Tinggi |
| Pohon Pencarian | Penuh | Tidak penuh (pruning) |

---

## ✅ Hasil Optimasi
Berdasarkan hasil eksekusi program, diperoleh kombinasi optimal sebagai berikut:

- **Perangkat Aktif**:  
  Laptop Gaming, Rice Cooker, Kipas Angin, Lampu Belajar LED, Charger HP, dan AC Portable
- **Total Konsumsi Daya**: 885 Watt
- **Total Nilai Kepentingan (Z)**: 440
- **Sisa Kapasitas**: 15 Watt
- **Status**: Aman (MCB Tidak Jepret)

---

## 💻 Implementasi Program
Program diimplementasikan menggunakan **bahasa Python** dengan pendekatan rekursif untuk membangun state space tree dan menerapkan pruning.

Struktur program meliputi:
- Inisialisasi data perangkat
- Fungsi rekursif Backtracking
- Evaluasi kapasitas dan profit
- Penentuan solusi optimal

---

## 👨‍💻 Anggota Kelompok
- **ALDI SAPUTRA** (105841115923)  
- **RAIHAN ALIDZAKY** (105841115323)

---

## 🏫 Institusi
Program Studi Informatika  
Fakultas Teknik  
Universitas Muhammadiyah Makassar  
Tahun 2026

---

## 📄 Lisensi
Proyek ini dibuat untuk keperluan **akademik dan pembelajaran**.
