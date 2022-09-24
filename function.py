#Function Section

def printJudulApp () :
    '''Function untuk menampilkan judul app'''
    print("==============================\n\tPerpustakaan Ini\n==============================")

def printKategoriBuku ():
    # print("1. Matematika\n2. IPS\n3. IPA & Sains\n4. Sejarah\n5. Sastra Bahasa\n6. Novel & Komik")
    print("1. Matematika")
    print("2. IPS")
    print("3. IPA & Sains")
    print("4. Sejarah")
    print("5. Sastra & Bahasa")
    print("6. Novel & Komik")


def printJudulBuku (judulBuku) :
    '''Function untuk print judul buku'''
    print(judulBuku,"\n==============================")

def printKeteranganBuku (judulbuku, penulisBuku, jumlahHalaman, penerbit) :
    # print("Judul Buku\t: ", judulBukuKategori1, "\nPenulis Buku\t: ", penulisBukuKategori1, "\nJumlah Halaman\t: ", jumlahHalamanBukuKategori1,"halaman", "\nPenerbit\t: ", penerbitBukuKategori1)
    print("Judul Buku\t:", judulbuku)
    print("Penulis Buku\t:", penulisBuku)
    print("Jumlah Halama\t:", jumlahHalaman, "halaman")
    print("Penerbit\t:", penerbit)
# Function untuk menampilkan detail buku


# Function untuk verifikasi peminjaman buku
# def verifikasiPinjamBuku(i) :
#     while (True) :
#       if i == "Y" or "y" :
#         print("Buku sudah dipinjam")
#         break
#         #masukin id Anggota -> Klo bener lanjut (Disuruh ke petugas perpustakaan), klo gagal (mau coba lagi atau batal)
#       elif i == "N" or "n" :
#         break    
#       else :
#         print("Data yang anda masukan tidak valid!\n")
#         break          
