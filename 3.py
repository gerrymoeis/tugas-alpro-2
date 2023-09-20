"""
    Nama: Gerry Moeis M.D.P
    NIM: 23091397164
    Kelas: 2023E
    Prodi: D4 Manajemen Informatika
"""

data = input("Masukan nilai awal, jangka waktu/tahun, dan bunga (pisahkan spasi):\n")
[nilai_awal, tahun, bunga] = [int(number) for number in data.strip().split(" ")]

nilai_akhir = round(nilai_awal * (1 + bunga/100)**tahun)

print(f"Dengan modal {nilai_awal} dan jangka waktu {tahun} tahun akan menghasilkan Rp {nilai_akhir}")