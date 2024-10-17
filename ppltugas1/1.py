# Membaca dua nilai dari pengguna
nilai1 = int(input("Masukkan nilai pertama: "))
nilai2 = int(input("Masukkan nilai kedua: "))

# Membandingkan nilai
if nilai1 < nilai2:
    print("Nilai pertama lebih kecil dari nilai kedua.")
elif nilai1 > nilai2:
    print("Nilai pertama lebih besar dari nilai kedua.")
else:
    print("Kedua nilai sama besar.")
