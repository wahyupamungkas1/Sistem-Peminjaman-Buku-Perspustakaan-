## Program Peminjaman Buku di Perpustakaan

Program ini adalah sebuah program sederhana untuk sistem peminjaman buku di perpustakaan. Program ini menggunakan konsep *Association* antara dua kelas utama yaitu `Buku` dan `AnggotaPerpustakaan`.

### Kelas `Buku`

Kelas `Buku` merepresentasikan buku dengan atribut berikut:
- `judul`: String yang menyimpan judul buku.
- `pengarang`: String yang menyimpan nama pengarang buku.
- `tersedia`: Boolean yang menunjukkan status ketersediaan buku.

Kelas ini memiliki dua metode:
- `pinjam()`: Meminjam buku. Jika buku tersedia, status ketersediaan diubah menjadi `False`.
- `kembalikan()`: Mengembalikan buku. Status ketersediaan diubah menjadi `True`.

### Kelas `AnggotaPerpustakaan`

Kelas `AnggotaPerpustakaan` merepresentasikan anggota perpustakaan dengan atribut berikut:
- `nama`: String yang menyimpan nama anggota.
- `buku_dipinjam`: List yang menyimpan daftar buku yang sedang dipinjam oleh anggota.

Kelas ini memiliki dua metode:
- `pinjam_buku(buku)`: Meminjam buku. Jika buku tersedia, buku ditandai sebagai dipinjam dan ditambahkan ke daftar buku yang dipinjam oleh anggota.
- `kembalikan_buku(buku)`: Mengembalikan buku. Jika buku ada dalam daftar buku yang dipinjam oleh anggota, buku ditandai sebagai tersedia dan dihapus dari daftar buku yang dipinjam.

### Alur Program

1. Daftar buku yang tersedia diinisialisasi sebagai objek `Buku` dalam `buku_list`.
2. Pengguna diminta untuk memasukkan nama anggota perpustakaan.
3. Objek `AnggotaPerpustakaan` dibuat dengan menggunakan nama anggota yang dimasukkan.
4. Program memasuki perulangan utama untuk menampilkan menu dan menerima input pengguna.
5. Jika pengguna memilih menu "Pinjam Buku":
   - Program menampilkan daftar buku yang tersedia.
   - Pengguna diminta untuk memilih nomor buku yang ingin dipinjam.
   - Jika pilihan valid, buku dipinjam oleh anggota perpustakaan.
6. Jika pengguna memilih menu "Kembalikan Buku":
   - Program menampilkan daftar buku yang sedang dipinjam oleh anggota.
   - Pengguna diminta untuk memilih nomor buku yang ingin dikembalikan.
   - Jika pilihan valid, buku dikembalikan oleh anggota perpustakaan.
7. Jika pengguna memilih menu "Selesai", program keluar dari perulangan utama.
8. Setelah keluar dari perulangan utama, program menampilkan daftar buku yang dipinjam oleh anggota perpustakaan.

### Menjalankan Program

1. Jalankan program di lingkungan Python.
2. Program akan meminta Anda untuk memasukkan nama anggota perpustakaan.
3. Pilih menu "Pinjam Buku" atau "Kembalikan Buku" sesuai kebutuhan.
4.

 Ikuti instruksi yang ditampilkan di layar untuk memilih buku yang ingin dipinjam atau dikembalikan.
5. Untuk keluar dari program, pilih menu "Selesai".
6. Setelah keluar dari program, daftar buku yang dipinjam akan ditampilkan.

Pastikan Anda telah memasukkan nama anggota perpustakaan dengan benar dan mengikuti instruksi yang ditampilkan untuk memilih buku yang ingin dipinjam atau dikembalikan.

Selamat menggunakan program peminjaman buku di perpustakaan!
