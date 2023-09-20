"""
    Nama: Gerry Moeis M.D.P
    NIM: 23091397164
    Kelas: 2023E
    Prodi: D4 Manajemen Informatika
"""

JANGKA_KERJA = 5

def budi_gabut(gaji, jam_per_minggu):
    pendapatan_kotor = gaji * jam_per_minggu * JANGKA_KERJA
    pendapatan_bersih = pendapatan_kotor - pendapatan_kotor * 14//100
    shopping = pendapatan_bersih * 10//100
    alat_tulis = pendapatan_bersih * 1//100
    sisa_pendapatan = pendapatan_bersih - (shopping + alat_tulis)
    sedekah = sisa_pendapatan * 25//100
    anak_yatim = sedekah // 1000 * (1000 * 30//100)
    kaum_dhuafa = sedekah - anak_yatim

    print(f"""
          a. Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak: Rp {pendapatan_kotor}
          b. Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak: Rp {pendapatan_bersih}
          c. Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris: Rp {shopping}
          d. Jumlah uang yang akan Budi habiskan untuk membeli alat tulis: Rp {alat_tulis}
          e. Jumlah uang yang akan Budi sedekahkan: Rp {sedekah}
          f. Jumlah uang yang akan diterima anak yatim: Rp {anak_yatim}
          g. Jumlah uang yang akan diterima kaum dhuafa: Rp {kaum_dhuafa}""")


data = input("Masukan gaji dan jam kerja per minggu untuk Budi (pisahkan spasi):\n")
[gaji, jam_per_minggu] = [int(number) for number in data.strip().split(" ")]
budi_gabut(gaji, jam_per_minggu)