daftar_barang = {
    "Mouse": 90000,
    "Ram": 300000,
    "Keyboard": 200000,
    "Meja": 500000,
    "Headset": 250000,
    "ssd": 400000,
}
print("*** Berikut adalah daftar barang yang tersedia: ***")
print("")
for nama_barang in daftar_barang.keys():
    print(nama_barang)

print("")
#Pemilihan Barang
print("*** Pemilihan Barang ***")
print("")
pilihan_barang = []
while len(pilihan_barang) < 2:
    pilihan = input("Pilih barang (ketik 'selesai' jika sudah selesai): ")
    if pilihan.lower() == "selesai":
        break
    elif pilihan in daftar_barang:
        pilihan_barang.append(pilihan)
    else:
        print("Barang tidak ditemukan. Coba lagi.")

# Menghitung total harga
print("")
print("*** Proses Perhitungan Harga ***")
print("")
total_harga = sum(daftar_barang[barang] for barang in pilihan_barang)
bayar = total_harga
diskon1 = 0
diskon2 = 0 
if total_harga >= 318000:
    print("Pembelian Anda lebih dari 318000")
    print("Kamu mendapatkan diskon 27%")

    # hitung diskonnya
    diskon1 = total_harga * 27 / 100 
    bayar = total_harga - diskon1

if bayar >= 120000 :
        print("Pembelian Anda lebih dari 120000")
        print("Anda Mendapatkan diskon 5%")
        diskon2 = bayar * 5 / 100
        bayar = bayar - diskon2 
# Menampilkan pilihan dan total pembayaran
for barang in pilihan_barang:
    print(f"{barang} - Harga: Rp {daftar_barang[barang]:}")

print(f"Total Harga: Rp {total_harga:}")
print(f"Diskon 318000 adalah : Rp {diskon1:}")
print(f"Diskon 120000 adalah : Rp {diskon2:}")
print(f"Total Pembayaran: Rp {bayar:}")


print("")
print("*** Selesai ***")

