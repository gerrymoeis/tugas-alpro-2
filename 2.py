"""
    Nama: Gerry Moeis M.D.P
    NIM: 23091397164
    Kelas: 2023E
    Prodi: D4 Manajemen Informatika
"""

import math

data = input("Masukan nilai awal, nilai akhir, dan bunga (pisahkan spasi):\n")
[nilai_awal, nilai_akhir, bunga] = [int(number) for number in data.strip().split(" ")]

ratio_nilai = nilai_akhir // nilai_awal
tahun = math.ceil(math.log(ratio_nilai, 1 + bunga/100))

print(f"Dengan modal Rp {nilai_awal} Dibutuhkan {tahun} tahun untuk mencapai minimal Rp {nilai_akhir}")