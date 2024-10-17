import time  # Mengimpor modul waktu untuk manipulasi waktu
import random  # Mengimpor modul acak untuk pemilihan pesan selamat datang secara acak

# Inisialisasi variabel
kendaraan_parkir = {}  # Dictionary untuk menyimpan informasi parkir kendaraan
tarif_parkir = 10000  # Tarif parkir default per menit
maks_waktu_parkir = 240  # Batas waktu parkir tanpa denda (dalam menit)
batas_denda_1 = 240  # Batas waktu parkir untuk denda level 1 (dalam menit)
batas_denda_2 = 360  # Batas waktu parkir untuk denda level 2 (dalam menit)
tarif_denda_1 = 0.1  # Tarif denda level 1 (10% dari biaya parkir)
tarif_denda_2 = 0.25  # Tarif denda level 2 (25% dari biaya parkir)
pin_admin = "1234"  # PIN admin untuk otorisasi

# Tarif parkir berdasarkan zona
tarif_parkir_zona = {'a': 12000, 'b': 10000, 'c': 10000}

# Informasi anggota parkir dengan diskon
anggota_parkir = {'D1234AF': {'nama': 'Ijat', 'diskon': 0.1}}

# Pesan selamat datang yang dipilih secara acak
pesan_selamat_datang = [
    "Selamat datang di Aplikasi Parkir! Nikmati layanan kami.",
    "Salam parkir! Semoga perjalanan Anda menyenangkan.",
    "Halo, pengguna parkir cerdas! Mari parkir dengan nyaman.",
]
print(random.choice(pesan_selamat_datang))  # Mencetak pesan selamat datang secara acak

# Fungsi untuk menambahkan member baru
def tambah_member():
    # Input informasi member baru
    id_member_baru = input("Masukkan ID keanggotaan baru: ")  # Meminta pengguna untuk memasukkan ID member baru
    nama_member_baru = input("Masukkan nama member baru: ")  # Meminta pengguna untuk memasukkan nama member baru
    diskon_member_baru = float(input("Masukkan diskon untuk member baru (0.1 untuk 10%): "))  # Meminta pengguna untuk memasukkan diskon member baru

    # Menambahkan member baru ke dalam dictionary anggota_parkir
    if id_member_baru in anggota_parkir:  # Memeriksa apakah ID member sudah ada
        print("Member dengan ID tersebut sudah ada.")
    else:
        anggota_parkir[id_member_baru] = {'nama': nama_member_baru, 'diskon': diskon_member_baru}  # Menambahkan member baru ke dictionary anggota_parkir
        print(f"Member baru {nama_member_baru} (ID: {id_member_baru}) ditambahkan dengan diskon {diskon_member_baru * 100}%.")  # Memberikan konfirmasi penambahan member baru

# Fungsi untuk menampilkan daftar member
def tampilkan_member():
    print("\n=== Daftar Member ===")  # Menampilkan judul daftar member
    for id_member, info_member in anggota_parkir.items():  # Meloop melalui setiap item di dictionary anggota_parkir
        print(f"ID: {id_member}, Nama: {info_member['nama']}, Diskon: {info_member['diskon'] * 100}%")  
        # Menampilkan informasi setiap member, termasuk ID, nama, dan diskon dalam persentase
    print("=====================\n")  # Menampilkan pemisah setelah semua member ditampilkan

# Fungsi untuk menghitung biaya parkir berdasarkan waktu dan zona
def hitung_biaya_parkir(waktu_masuk, waktu_keluar, zona_parkir):
    # Menghitung durasi parkir dalam detik
    durasi_parkir_detik = waktu_keluar - waktu_masuk

    # Mengubah penggunaan waktu UTC ke waktu UTC+7
    waktu_masuk = time.gmtime(waktu_masuk)
    waktu_keluar = time.gmtime(waktu_keluar)

    # Menampilkan waktu masuk dalam format jam:menit:detik UTC+7
    print(f"Waktu Masuk: {time.strftime('%H:%M:%S', waktu_masuk)} UTC+7")
    
    # Menampilkan waktu keluar dalam format jam:menit:detik UTC+7
    print(f"Waktu Keluar: {time.strftime('%H:%M:%S', waktu_keluar)} UTC+7")

    # Tarif parkir berdasarkan zona
    tarif_parkir_zona = {'a': 12000, 'b': 10000, 'c': 10000}
    tarif_parkir = tarif_parkir_zona[zona_parkir]

    # Pembulatan waktu parkir ke menit terdekat (60 detik)
    durasi_parkir_menit = max(1, round(durasi_parkir_detik / 60))  # Durasi minimal 1 menit

    # Pembulatan waktu parkir sesuai dengan aturan (maksimal 240 detik)
    if durasi_parkir_menit > 4:
        durasi_parkir_menit = 4

    # Menghitung biaya per menit
    biaya_parkir = durasi_parkir_menit * tarif_parkir

    return biaya_parkir

# Fungsi untuk menghitung denda berdasarkan durasi parkir dalam menit
def hitung_denda(durasi_parkir_menit):
    # Menentukan denda berdasarkan aturan tertentu
    if durasi_parkir_menit >= 4 and durasi_parkir_menit < 6:
        denda = 0.1  # Denda level 1 (10% dari biaya parkir)
    elif durasi_parkir_menit >= 6:
        denda = 0.25  # Denda level 2 (25% dari biaya parkir)
    else:
        denda = 0  # Tidak ada denda jika durasi parkir kurang dari 4 menit

    return denda

# Fungsi untuk mencetak semua transaksi parkir
def cetak_semua_transaksi():
    # Memeriksa apakah ada transaksi parkir atau tidak
    if not kendaraan_parkir:
        print("Belum ada transaksi parkir.")
    else:
        # Menampilkan header untuk seluruh transaksi parkir
        print("\n=== Seluruh Transaksi Parkir ===")
        
        # Iterasi melalui setiap transaksi dan mencetak detailnya
        for plat, info in kendaraan_parkir.items():
            cetak_transaksi_parkir(plat, info['waktu_masuk'], info['waktu_keluar'], info['biaya_parkir'], info['denda'], info['jenis_kendaraan'])
        
        # Menampilkan garis pemisah setelah semua transaksi dicetak
        print("=============================\n")

# Fungsi untuk mencetak detail transaksi parkir
def cetak_transaksi_parkir(nomor_kendaraan, waktu_masuk, waktu_keluar, biaya_parkir, denda, jenis_kendaraan):
    # Memeriksa apakah kendaraan sudah keluar (waktu_keluar tidak None)
    if waktu_keluar is not None:  
        # Menampilkan header transaksi parkir
        print("\n--- Transaksi Parkir ---")
        
        # Menampilkan nomor kendaraan
        print(f"Nomor Kendaraan: {nomor_kendaraan}")
        
        # Menampilkan jenis kendaraan (Mobil atau Motor)
        print(f"Jenis Kendaraan: {'Mobil' if jenis_kendaraan == '1' else 'Motor'}")
        
        # Menampilkan waktu masuk dalam format jam:menit:detik UTC+7
        print(f"Waktu Masuk: {time.strftime('%H:%M:%S', time.gmtime(waktu_masuk))}")
        
        # Menampilkan waktu keluar dalam format jam:menit:detik UTC+7
        print(f"Waktu Keluar: {time.strftime('%H:%M:%S', time.gmtime(waktu_keluar))}")
        
        # Menghitung durasi parkir dalam menit dan detik
        durasi_parkir_detik = waktu_keluar - waktu_masuk
        durasi_parkir_menit = int(durasi_parkir_detik / 60)
        durasi_parkir_detik_sisa = int(durasi_parkir_detik % 60)

        # Menampilkan durasi parkir
        print(f"Durasi Parkir: {durasi_parkir_menit} menit {durasi_parkir_detik_sisa} detik")
        
        # Menampilkan biaya parkir dalam format mata uang
        print(f"Biaya Parkir: Rp {biaya_parkir:,.0f}")

        # Menampilkan denda jika ada, dalam format mata uang
        if denda > 0:
            print(f"Denda: Rp {denda * biaya_parkir:,.0f}")
        else:
            print("Denda: Tidak ada")

        # Menampilkan total bayar (biaya parkir + denda) dalam format mata uang
        print(f"Total Bayar: Rp {(1 + denda) * biaya_parkir:,.0f}")
        
        # Menampilkan garis pemisah setelah mencetak satu transaksi
        print("------------------------")
        
        # Menampilkan garis pemisah setelah mencetak satu transaksi (format ekstra)
        print("=============================\n")

# Fungsi untuk masuk ke mode admin dengan memasukkan PIN
def masuk_mode_admin():
    # Meminta pengguna untuk memasukkan PIN Admin Parkir
    pin_dimasukkan = input("Masukkan PIN Admin Parkir: ")

    # Memeriksa apakah PIN yang dimasukkan sesuai dengan PIN Admin yang benar
    if pin_dimasukkan == pin_admin:
        # Menampilkan pesan selamat datang jika PIN benar
        print("\n=== Selamat datang, Admin Parkir ===")

        # Memanggil fungsi menu_admin untuk menampilkan menu admin
        menu_admin()
    else:
        # Menampilkan pesan kesalahan jika PIN salah
        print("PIN salah. Kembali ke menu utama.")

# Fungsi untuk mencetak kendaraan yang belum keluar dari area parkir
def cetak_kendaraan_belum_keluar():
    # Menggunakan list comprehension untuk mendapatkan plat kendaraan yang belum keluar
    belum_keluar = [plat for plat, info in kendaraan_parkir.items() if info['waktu_keluar'] is None]

    # Memeriksa apakah tidak ada kendaraan yang belum keluar
    if not belum_keluar:
        print("Semua kendaraan telah keluar dari area parkir.")
        print("==============================================\n")
    else:
        # Menampilkan header untuk kendaraan yang belum keluar
        print("\n=== Kendaraan Belum Keluar ===")

        # Iterasi melalui setiap kendaraan yang belum keluar dan mencetak informasinya
        for plat in belum_keluar:
            info = kendaraan_parkir[plat]
            print(f"Nomor Kendaraan: {plat}")
            print(f"Waktu Masuk: {time.strftime('%H:%M:%S', time.gmtime(info['waktu_masuk']))}")
            print("------------------------")

        # Menampilkan garis pemisah setelah mencetak kendaraan yang belum keluar
        print("=============================\n")

# Fungsi untuk menampilkan menu admin dan memproses pilihan pengguna
def menu_admin():
    # Melakukan loop tak terbatas untuk menu admin
    while True:
        print("\nMenu Admin Parkir:")
        print("1. Cetak Seluruh Transaksi")
        print("2. Kendaraan Belum Keluar")
        print("3. Tambah Member")
        print("4. Tampilkan Member")
        print("5. Kembali ke Menu Utama")

        # Meminta pengguna untuk memilih opsi menu
        opsi = input("Pilih menu (1/2/3/4/5): ")

        # Memproses pilihan pengguna sesuai dengan opsi yang dipilih
        if opsi == "1":
            cetak_semua_transaksi()
        elif opsi == "2":
            cetak_kendaraan_belum_keluar()
        elif opsi == "3":
            tambah_member()
        elif opsi == "4":
            tampilkan_member()
        elif opsi == "5":
            # Keluar dari loop jika pengguna memilih kembali ke menu utama
            break
        else:
            # Menampilkan pesan kesalahan jika pilihan tidak valid
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi untuk memproses masuk parkir kendaraan
def masuk_parkir():
    # Meminta pengguna untuk memasukkan plat nomor kendaraan
    print("Masukkan plat nomor kendaraan:")
    plat_kendaraan = input("Nomor Kendaraan (contoh: D1234AF): ")

    # Memeriksa apakah kendaraan sudah terdaftar dan belum keluar dari area parkir
    if plat_kendaraan in kendaraan_parkir and kendaraan_parkir[plat_kendaraan]['waktu_keluar'] is None:
        # Menampilkan pesan jika kendaraan sudah terdaftar dan belum keluar
        print(f"Kendaraan dengan plat {plat_kendaraan} sudah terdaftar di area parkir.")
        return

    # Memproses pemilihan jenis kendaraan
    while True:
        # Menampilkan pilihan jenis kendaraan
        print("Pilih jenis kendaraan:")
        print("1. Mobil")
        print("2. Motor")
        jenis_kendaraan = input("Masukkan nomor jenis kendaraan (1/2): ")

        # Memeriksa validitas pilihan jenis kendaraan
        if jenis_kendaraan not in ["1", "2"]:
            print("Pilihan tidak valid. Silakan coba lagi.")
            continue

        # Konfirmasi pemilihan jenis kendaraan
        konfirmasi_jenis = input(f"Apakah Anda yakin ingin memilih jenis kendaraan {'Mobil' if jenis_kendaraan == '1' else 'Motor'}? (y/n): ").lower()

        # Memeriksa konfirmasi pemilihan jenis kendaraan
        if konfirmasi_jenis == "y":
            break
        else:
            print("Pilihan jenis kendaraan dibatalkan. Kembali ke menu pilihan kendaraan.")
            continue

    # Memproses pemilihan zona parkir
    while True:
        while True:
            # Menampilkan pilihan zona parkir
            print("Pilih zona parkir:")
            print("a. Zona A")
            print("b. Zona B")
            print("c. Zona C")
            zona_parkir = input("Masukkan pilihan zona parkir (a/b/c): ")

            # Memeriksa validitas pilihan zona dan jenis kendaraan
            validasi_zona = (zona_parkir == "a" and jenis_kendaraan == "1") or (zona_parkir in ["b", "c"] and jenis_kendaraan == "2")

            # Menampilkan pesan jika pilihan zona dan jenis kendaraan tidak sesuai
            if not validasi_zona:
                print("Pilihan zona dan jenis kendaraan tidak sesuai. Silakan coba lagi.")
                continue

            # Memeriksa validitas zona parkir
            if zona_parkir not in tarif_parkir_zona:
                print("Zona parkir tidak valid. Silakan coba lagi.")
                continue

            # Mendapatkan tarif parkir untuk zona yang dipilih
            tariff = tarif_parkir_zona[zona_parkir]

            # Menampilkan tarif parkir per 60 detik
            print(f"Tarif parkir untuk zona {zona_parkir}: Rp {tariff:,.0f} per 60 detik")

            # Konfirmasi pemilihan zona parkir
            konfirmasi_zona = input(f"Apakah Anda yakin ingin memilih zona {zona_parkir}? (y/n): ").lower()

            # Memeriksa konfirmasi pemilihan zona parkir
            if konfirmasi_zona == "y":
                break
            else:
                print("Pilihan zona dibatalkan. Kembali ke menu zona.")
                continue

        # Memeriksa ID keanggotaan untuk memberikan diskon
        id_anggota = input("Masukkan ID keanggotaan (kosongkan jika tidak ada): ")

        # Memberikan diskon kepada anggota jika ID keanggotaan valid
        if id_anggota in anggota_parkir:
            diskon = anggota_parkir[id_anggota]['diskon']
            print(f"Selamat datang, {anggota_parkir[id_anggota]['nama']}! Anda mendapatkan diskon {diskon * 100}%.")
            tariff = tariff * (1 - diskon)
        else:
            diskon = 0

        # Mendapatkan waktu masuk kendaraan dan menampilkan informasi
        waktu_masuk = time.time() + 7 * 3600  # Tambahkan offset waktu UTC+7
        print(f"Waktu masuk kendaraan dicatat: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(waktu_masuk))} UTC+7")

        # Merekam informasi parkir kendaraan ke dalam dictionary kendaraan_parkir
        kendaraan_parkir[plat_kendaraan] = {'waktu_masuk': waktu_masuk, 'waktu_keluar': None, 'biaya_parkir': None,
                                            'denda': None, 'zona_parkir': zona_parkir, 'diskon': diskon, 'jenis_kendaraan': jenis_kendaraan}

        # Keluar dari loop utama jika sudah berhasil memilih zona
        break

# Fungsi untuk memproses keluar parkir kendaraan
def keluar_parkir():
    # Meminta pengguna untuk memasukkan nomor kendaraan
    plat_kendaraan = input("Masukkan nomor kendaraan: ")

    # Memeriksa apakah kendaraan sudah terdaftar di area parkir
    if plat_kendaraan not in kendaraan_parkir:
        # Menampilkan pesan jika kendaraan tidak ditemukan di area parkir
        print("Kendaraan tidak ditemukan di area parkir. Silakan masukkan kendaraan yang benar.")
    elif kendaraan_parkir[plat_kendaraan]['waktu_keluar'] is not None:
        # Menampilkan pesan jika kendaraan sudah keluar dari area parkir
        print("Kendaraan dengan plat", plat_kendaraan, "sudah keluar dari area parkir.")
        # Menghapus entri dari dictionary kendaraan_parkir
        del kendaraan_parkir[plat_kendaraan]
    else:
        # Memproses perhitungan biaya parkir, denda, dan transaksi parkir
        waktu_keluar = time.time() + 7 * 3600
        waktu_masuk = kendaraan_parkir[plat_kendaraan]['waktu_masuk']
        durasi_parkir_detik = waktu_keluar - waktu_masuk
        durasi_parkir_menit = round(durasi_parkir_detik / 60)  # Durasi parkir dalam menit, dibulatkan

        zona_parkir = kendaraan_parkir[plat_kendaraan]['zona_parkir']
        biaya_parkir = hitung_biaya_parkir(waktu_masuk, waktu_keluar, zona_parkir)
        denda = hitung_denda(durasi_parkir_menit)

        diskon = kendaraan_parkir[plat_kendaraan]['diskon']
        biaya_parkir_diskon = biaya_parkir * (1 - diskon)

        jenis_kendaraan = kendaraan_parkir[plat_kendaraan]['jenis_kendaraan']

        # Memperbarui informasi kendaraan_parkir dengan hasil perhitungan
        kendaraan_parkir[plat_kendaraan]['waktu_keluar'] = waktu_keluar
        kendaraan_parkir[plat_kendaraan]['biaya_parkir'] = biaya_parkir_diskon
        kendaraan_parkir[plat_kendaraan]['denda'] = denda

        # Mencetak informasi transaksi parkir
        cetak_transaksi_parkir(plat_kendaraan, waktu_masuk, waktu_keluar, biaya_parkir_diskon, denda, jenis_kendaraan)

        # Memproses pembayaran dan memberikan kembalian
        nominal_pembayaran = float(input("Masukkan nominal pembayaran: Rp "))

        while nominal_pembayaran < (1 + denda) * biaya_parkir_diskon:
            print("Maaf, nominal pembayaran kurang. Silakan masukkan uang yang cukup.")
            print("Jika tidak dapat membayar, silakan menghubungi petugas.")
            nominal_pembayaran = float(input("Masukkan nominal pembayaran: Rp "))

        kembalian = nominal_pembayaran - (1 + denda) * biaya_parkir_diskon

        # Menampilkan kembalian jika ada, jika tidak menampilkan pesan gerbang keluar tertutup
        if kembalian >= 0:
            print(f"Terima kasih! Kembalian Anda: Rp {kembalian:,.0f}")
            print("Gerbang keluar terbuka. Sampai jumpa!")
        else:
            print("Gerbang keluar tetap tertutup.")

            # Menambahkan kendaraan kembali ke daftar kendaraan yang belum keluar
            kendaraan_parkir[plat_kendaraan]['waktu_keluar'] = None
            kendaraan_parkir[plat_kendaraan]['biaya_parkir'] = None
            kendaraan_parkir[plat_kendaraan]['denda'] = None

# Fungsi untuk menjalankan aplikasi parkir
def aplikasi_parkir():
    while True:
        # Menampilkan menu utama
        print("\nMenu Utama:")
        print("1. Masuk Area Parkir")  # Pilihan untuk kendaraan masuk
        print("2. Keluar Area Parkir")  # Pilihan untuk kendaraan keluar
        print("3. Admin Parkir")  # Pilihan untuk masuk ke mode admin
        print("4. Keluar Aplikasi")  # Pilihan untuk keluar dari aplikasi
        
        # Pengguna memilih menu
        pilihan = input("Pilih menu (1/2/3/4): ")

        # Menjalankan fungsi terkait dengan pilihan pengguna
        if pilihan == "1":
            masuk_parkir()  # Panggil fungsi masuk_parkir() jika pilihan adalah 1
        elif pilihan == "2":
            keluar_parkir()  # Panggil fungsi keluar_parkir() jika pilihan adalah 2
        elif pilihan == "3":
            masuk_mode_admin()  # Panggil fungsi masuk_mode_admin() jika pilihan adalah 3
        elif pilihan == "4":
            # Keluar dari loop dan aplikasi
            pesan_perpisahan()  # Panggil fungsi pesan_perpisahan() jika pilihan adalah 4
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def pesan_perpisahan():
    # Pesan perpisahan ditampilkan secara acak dari daftar pesan
    pesan_perpisahan = [
        "Terima kasih telah menggunakan Aplikasi Parkir! Sampai jumpa di kesempatan berikutnya.",
        "Hati-hati di perjalanan Anda! Terima kasih telah memilih layanan parkir kami.",
        "Selamat tinggal! Semoga harimu menyenangkan dan bebas dari masalah parkir.",
    ]
    print(random.choice(pesan_perpisahan))

# Memanggil fungsi aplikasi_parkir() untuk menjalankan aplikasi
aplikasi_parkir()


