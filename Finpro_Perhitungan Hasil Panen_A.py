print(50*'=')
print('''
              	PERHITUNGAN HASIL 
                    PANEN BUAH
''')
print(50*'=')
print('''
    ---------------------------------------------
    |                DAFTAR BUAH                |
    ---------------------------------------------
    |NO|    NAMA BUAH     |    HARGA PER KILO   |
    ---------------------------------------------
    |1.|    PISANG        |     Rp. 20000       |
    |2.|    APEL          |     Rp. 24000       | 
    |3.|    MANGGA        |     Rp. 30000       |
    |4.|    JERUK         |     Rp. 25000       |
    |5.|    JAMBU         |     Rp. 25000       |
    ---------------------------------------------
''')
while True:
    nomor = int(input("Pilih nomor dari daftar buah :"))
    jmlpanen = int(input("Masukkan jumlah buah yg akan dipanen (Kg) :"))
    modal = int(input("Masukkan modal yang akan digunakan : Rp."))
    print('''
=============== HASIL PERHITUNGAN ===============
''')

    if nomor == 1:
      total = 20000 * jmlpanen
      nama = "PISANG"
      keuntungan = total - modal
      print ("Nama buah :", nama, "\njumlah panen pisang (Kg) :",jmlpanen, "\ntotal pendapatan : Rp.", total, "\nkeuntungan yang didapat : Rp.", keuntungan)
    elif nomor == 2:
      total = 24000 * jmlpanen
      nama = "APEL"
      keuntungan = total - modal
      print ("Nama buah :", nama, "\njumlah panen apel (Kg) :",jmlpanen, "\ntotal pendapatan : Rp.", total, "\nkeuntungan yang didapat : Rp.", keuntungan)
    elif nomor == 3:
      total = 30000 * jmlpanen
      nama = "MANGGA"
      keuntungan = total - modal
      print ("Nama buah :", nama, "\njumlah panen mangga (Kg) :",jmlpanen, "\ntotal pendapatan : Rp.", total, "\nkeuntungan yang didapat : Rp.", keuntungan)
    elif nomor == 4:
      total = 25000 * jmlpanen
      nama = "JERUK"
      keuntungan = total - modal
      print ("Nama buah :", nama, "\njumlah panen jeruk (Kg) :",jmlpanen, "\ntotal pendapatan : Rp.", total, "\nkeuntungan yang didapat : Rp.", keuntungan)
    elif nomor == 5:
      total = 25000 * jmlpanen
      nama = "JAMBU"
      keuntungan = total - modal
      print ("Nama buah :", nama, "\njumlah panen jambu (Kg) :",jmlpanen, "\ntotal pendapatan : Rp.", total, "\nkeuntungan yang didapat : Rp.", keuntungan)
    else:
      print ("Pilihan tidak ada di daftar, coba lagi")

    print('''
=================================================''')
   
    if (total > modal):
      print('''
    ---------------------------------------------
    |        Panen anda sukses lanjutkan !      |
    ---------------------------------------------
    ''')
    elif (total == modal):
      print('''
    ---------------------------------------------
    |         Panen anda balik modal            |
    ---------------------------------------------
    ''')
    elif (total < modal):
      print('''
    ---------------------------------------------
    |       Panen anda tidak menghasilkan       |
    |         Coba lagi dengan cara baru!       |
    ---------------------------------------------
    ''')
    else:
      print ("Pilihan tidak ada di daftar, coba lagi")

    lanjut = input("lanjut perhitungan(y/t) : ")
    if lanjut == "t":
        print("")
        break
