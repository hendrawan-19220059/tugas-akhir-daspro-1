import pandas as pd     # Import pandas module buat database
from function import *  # Import function.py
from data import *      # Import data.py



# dataframe itu excel
# dataframe = pd.read_excel('data_buku.xlsx', index_col=False) 

dataframe_buku = pd.read_excel('data_perpustakaan.xlsx', 'Data Buku',index_col=False) 
dataframe_anggota = pd.read_excel('data_perpustakaan.xlsx', 'Data Anggota',index_col=False) 
dataframe_buku.set_index('No.', inplace=True) # Remove index default pandas diganti jadi 'No.'


# dataframe_buku = dataframe_buku.reset_index(drop=True)
# print(dataframe_buku)
print(dataframe_anggota)



#Kategori 2 - IPS


#Kategori 3 - IPA & Sains
kategori1JudulBuku = [kategori1_Buku1[0], kategori1_Buku2[0]]







'''
Data Anggota
  Nama
  ID
  Alamat
  No. Telp


Data Buku
  Judul Buku
  Penulis Buku
  Jumlah Halaman
  Penerbit
'''

while(True) :
  printJudulApp()
  print('1. Daftar Isi\n2. Daftar Anggota\n3. Login Administrator')
  pilihanUserMenu = int(input("Silahkan masukan pilihan anda : "))

  if pilihanUserMenu == 1 :  
    
    printJudulApp()
    printKategoriBuku()

    pilihanKategoriBuku = int(input("Silahkan pilih kategori buku : "))

    while (pilihanKategoriBuku == 1) : 
    # if pilihanKategoriBuku == 1 :
      printJudulApp()
      print(dataframe_buku['Judul Buku'])
      # print('\n'.join(kategori1JudulBuku)) #loop isi array buat nampilin list buku
      print("99 - Kembali")
      pilihan_kategori1 = int(input("Silahkan pilih buku yg diinginkan : "))

      if pilihan_kategori1 == 0 :     
        while(True) : 
          judulBukuKategori1 = kategori1_Buku1[0]
          penulisBukuKategori1 = kategori1_Buku1[1]
          jumlahHalamanBukuKategori1 = kategori1_Buku1[2]
          penerbitBukuKategori1 = kategori1_Buku1[3]

          # Print Header 
          printJudulApp()
          printJudulBuku(kategori1_Buku1[0])
          

          # Print Keterangan Buku
          printKeteranganBuku(judulBukuKategori1, penulisBukuKategori1, jumlahHalamanBukuKategori1, penerbitBukuKategori1)
          inputPinjamBuku = input("Ingin pinjam buku ini? (Y/N) ")
          

          # Verifikasi. User mau pinjam buku atau kgk
          while (True) :
            if inputPinjamBuku == "Y" or "y" :
                print("Buku sudah dipinjam")
                break
                #masukin id Anggota -> Klo bener lanjut (Disuruh ke petugas perpustakaan), klo gagal (mau coba lagi atau batal)
            elif inputPinjamBuku == "N" or "n" :
                break    
            else :
                print("Data yang anda masukan tidak valid!\n")
                break          
          break # Exit verifikasi user  
        
      if pilihan_kategori1 == 99 :
        break    
    
    if pilihanKategoriBuku == 2 :
      print("IPA & Sains\n Ini buku Mat")

    if pilihanKategoriBuku == 3 :
      print("Sejarah\n Ini buku Mat")

    if pilihanKategoriBuku == 4 :
      print("Sastra & Bahasa\n Ini buku Mat")




  if pilihanUserMenu == 2 :
    print("Daftar Anggota")
    namaAnggota = input("Nama\t\t: ")
    alamatAnggota = input("Alamat\t\t: ")
    noTelpAnggota = input("No. Telp\t: ")
    emailAnggota = input("Email\t\t:")







