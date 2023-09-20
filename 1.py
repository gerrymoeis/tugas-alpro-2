# beli = True
# while beli:
#     data = input("Masukan emas, harga beli, harga jual (pisahkan spasi):\n")
#     [emas, harga_beli, harga_jual] = [int(number) for number in data.strip().split(" ")]

#     keuntungan = (harga_jual - harga_beli) * emas
#     persentase_untung = round(keuntungan / (harga_beli * emas) * 100)
#     print(f"Keuntungan: Rp {keuntungan} atau {persentase_untung}%")

#     input_user = input("Beli lagi gk? (Y/N)")
#     beli = True if input_user == "Y" else False

"""
    Nama: Gerry Moeis M.D.P
    NIM: 23091397164
    Kelas: 2023E
    Prodi: D4 Manajemen Informatika
"""

total_emas = 0
total_modal = 0
beli = True

while beli:
    data = input("Masukan emas, harga beli, harga jual (pisahkan spasi):\n")
    [emas, harga_beli, harga_jual] = [int(number) for number in data.strip().split(" ")]
    total_emas += emas
    total_modal += emas * harga_beli
    total_jual = total_emas * harga_jual

    keuntungan = total_jual - total_modal
    persentase_untung = round(keuntungan / (total_modal) * 100, 1)
    print(f"Keuntungan: Rp {keuntungan} atau {persentase_untung}%")

    input_user = input("Beli lagi gk? (y/n)\n")
    beli = True if input_user.lower() == "y" else False