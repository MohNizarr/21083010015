from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process
x = int(input("Batas perulangan: "))
def tampil(i):
  if i % 2 == 0:
    print(f"{i+1} Ganjil", "- ID proses", getpid())
  elif i % 2 !=0:
    print(f"{i+1} Genap", "- ID proses", getpid())
  else:
    print("selesai")
    sleep(1)
print("\nSekuensial")

# UNTUK MENDAPATKAN WAKTU SEBELUM EKSEKUSI
sekuensial_awal = time()

# PROSES BERLANGSUNG
for i in range(x):
    tampil(i)

# UNTUK MENDAPATKAN WAKTU SETELAH EKSEKUSI
sekuensial_akhir = time()
print("\nKelas Process")

# UNTUK MENAMPUNG PROSES-PROSES
kumpulan_proses = []

# UNTUK MENDAPATKAN WAKTU SEBELUM EKSEKUSI
process_awal = time()

# PROSES BERLANGSUNG
for i in range(x):
    p = Process(target=tampil, args=(i,))
    kumpulan_proses.append(p)
    p.start()

# UNTUK MENGGABUNGKAN PROSES-PROSES AGAR TIDAK LONCAT KE PROSES SEBELUM'NYA
for i in kumpulan_proses:
    p.join()
    
# UNTUK MENDAPATKAN WAKTU SETELAH EKSEKUSI
process_akhir = time()
print("\nKelas Pool")

# UNTUK MENDAPATKAN WAKTU SEBELUM EKSEKUSI
pool_awal = time()

# PROSES BERLANGSUNG
pool = Pool()
pool.map(tampil, range(x))
pool.close()

# UNTUK MENDAPATKAN WAKTU SEBELUM EKSEKUSI
pool_akhir = time()
print("\nSekuensial :", sekuensial_akhir - sekuensial_awal, "detik")
print("Kelas Process :", process_akhir - process_awal, "detik")
print("Kelas Pool :", pool_akhir - pool_awal, "detik")
