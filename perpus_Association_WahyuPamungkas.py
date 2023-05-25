class Buku:
    def __init__(self, judul, pengarang, tersedia=True):
        self.judul = judul
        self.pengarang = pengarang
        self.tersedia = tersedia
    
    def pinjam(self):
        if self.tersedia:
            self.tersedia = False
            print("Buku {} telah dipinjam.".format(self.judul))
        else:
            print("Maaf, buku {} sedang tidak tersedia.".format(self.judul))
    
    def kembalikan(self):
        self.tersedia = True
        print("Buku {} telah dikembalikan.".format(self.judul))


class AnggotaPerpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.buku_dipinjam = []
    
    def pinjam_buku(self, buku):
        if buku.tersedia:
            buku.pinjam()
            self.buku_dipinjam.append(buku)
        else:
            print("Maaf, buku {} sedang tidak tersedia.".format(buku.judul))
    
    def kembalikan_buku(self, buku):
        if buku in self.buku_dipinjam:
            buku.kembalikan()
            self.buku_dipinjam.remove(buku)
        else:
            print("Anda tidak meminjam buku {}.".format(buku.judul))


# Daftar buku
buku_list = [
    Buku("Laskar Pelangi", "Andrea Hirata"),
    Buku("Bumi Manusia", "Pramoedya Ananta Toer"),
    Buku("Pulang", "Leila S. Chudori"),
    Buku("Perahu Kertas", "Dee Lestari"),
    Buku("Cinta dalam Gelas", "Andrea Hirata")
]
# Input nama anggota perpustakaan
nama_anggota = input("Masukkan nama anggota perpustakaan: ")

# Membuat objek anggota perpustakaan
anggota = AnggotaPerpustakaan(nama_anggota)

while True:
    print("\nMenu: ")
    print("1. Pinjam Buku")
    print("2. Kembalikan Buku")
    print("0. Selesai")
    
    pilihan = input("\nMasukkan pilihan menu: ")
    
    if pilihan == '1':
        # Pinjam buku
        while True:
            print("\nDaftar Buku Tersedia:")
            for index, buku in enumerate(buku_list):
                if buku.tersedia:
                    print("{}. {}".format(index+1, buku.judul))
            
            pilihan_buku = input("\nMasukkan nomor buku yang ingin dipinjam atau '0' untuk selesai: ")
            
            if pilihan_buku == '0':
                break
            
            try:
                index_buku = int(pilihan_buku) - 1
                buku_dipilih = buku_list[index_buku]
                
                if buku_dipilih.tersedia:
                    anggota.pinjam_buku(buku_dipilih)
                else:
                    print("Buku tidak tersedia.")
            
            except (ValueError, IndexError):
                print("Pilihan tidak valid. Silakan coba lagi.")
    
    elif pilihan == '2':
        # Kembalikan buku
        while True:
            if len(anggota.buku_dipinjam) == 0:
                print("\nAnda belum meminjam buku apapun.")
                break
            
            print("\nDaftar Buku yang Dipinjam oleh {}: ".format(nama_anggota))
            for index, buku in enumerate(anggota.buku_dipinjam):
                print("{}. {}".format(index+1, buku.judul))
            
            pilihan_buku = input("\nMasukkan nomor buku yang ingin dikembalikan atau '0' untuk selesai: ")
            
            if pilihan_buku == '0':
                break
            
            try:
                index_buku = int(pilihan_buku) - 1
                buku_dikembalikan = anggota.buku_dipinjam[index_buku]
                
                anggota.kembalikan_buku(buku_dikembalikan)
            
            except (ValueError, IndexError):
                print("Pilihan tidak valid. Silakan coba lagi.")
    
    elif pilihan == '0':
        break
    
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

# Menampilkan daftar buku yang dipinjam
print("\nDaftar Buku yang Dipinjam oleh {}: ".format(nama_anggota))
if len(anggota.buku_dipinjam) > 0:
    for index, buku in enumerate(anggota.buku_dipinjam):
        print("{}. {}".format(index+1, buku.judul))
else:
    print("Tidak ada buku yang dipinjam.")
