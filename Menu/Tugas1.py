# NIM : 102022300118
# Nama : Deazard Muhammad Arrayyan

makanan_0118 = {"Nasi Goreng": 30000, "Mie Goreng": 30000, "Ayam Goreng": 45000, "Sate Ayam": 60000, "Nasi Campur": 25000}
minuman_0118 = {"Es Teh": 15000, "Es Jeruk": 20000, "Kopi Hitam": 20000, "Jus Alpukat": 20000, "Air Mineral": 8000}

keranjang_0118 = []

while True:
    print("\n||   *Menu*   ||")
    print("|| 1. Makanan ||")
    print("|| 2. Minuman ||")
    print("|| 3. Selesai ||")

    kategori_0118 = input("Pilih kategori (1/2/3): ")

    if kategori_0118 == '1':
        menu_0118 = makanan_0118
        jenis_menu_0118 = "Makanan"
    elif kategori_0118 == '2':
        menu_0118 = minuman_0118
        jenis_menu_0118 = "Minuman"
    elif kategori_0118 == '3':
        break
    else:
        print("Input tidak valid. Silakan pilih kategori yang benar.")

    print("\nMenu", jenis_menu_0118 + ":")
    for item_0118, harga_0118 in menu_0118.items():
        print(item_0118 + ":", "Rp.", harga_0118)

    pilihan_0118 = input("\nPilih " + jenis_menu_0118 + " : ")

    if pilihan_0118.lower() == 'selesai':
        break

    if pilihan_0118 in menu_0118:
        jumlah_0118 = int(input("Masukkan jumlah " + pilihan_0118 + ": "))
        keranjang_0118.append({"jenis": pilihan_0118, "jumlah": jumlah_0118, "harga": menu_0118[pilihan_0118] * jumlah_0118})
    else:
        print("Menu tidak valid. Silakan pilih menu yang benar.")

print("\nHasil Pemesanan:")
total_harga_0118 = 0
for item_0118 in keranjang_0118:
    print(item_0118['jenis'] + " -", str(item_0118['jumlah']) + " pcs: Rp.", item_0118['harga'])
    total_harga_0118 += item_0118['harga']
print("Total Harga: Rp.", total_harga_0118)

diskon_0118 = 0
if total_harga_0118 > 500000:
    diskon_0118 = 0.25
    print("Selamat Anda Mendapatkan Diskon 25%")
elif total_harga_0118 > 250000:
    diskon_0118 = 0.15
    print("Selamat Anda Mendapatkan Diskon 15%")
   
elif total_harga_0118 > 100000:
    diskon_0118 = 0.10
    print("Selamat Anda Mendapatkan Diskon 10%")

total_akhir_0118 = total_harga_0118 - (total_harga_0118 * diskon_0118)

nim_0118 = input("\nMasukkan NIM: ")
nama_0118 = input("Masukkan Nama: ")

print("\n*** Struk Pembelian ***")
print("Total Harga: Rp.", total_harga_0118)
print("Diskon:", str(diskon_0118 * 100) + "%")
print("Total Akhir: Rp.", total_akhir_0118)
nominal_pembayaran_0118 = int(input("Masukkan nominal pembayaran: "))

while nominal_pembayaran_0118 < total_akhir_0118:
    print("Uang tidak cukup. Total Akhir:", total_akhir_0118)
    nominal_pembayaran_0118 = int(input("Masukkan nominal pembayaran yang mencukupi: "))

print("\nPembayaran dari", nama_0118 + " (" + nim_0118 + "): Rp.", nominal_pembayaran_0118)
kembalian_0118 = nominal_pembayaran_0118 - total_akhir_0118
print("Kembalian: Rp.", kembalian_0118)

