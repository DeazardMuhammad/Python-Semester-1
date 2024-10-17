import time
import random 

kendaraan_parkir = {}  
tarif_parkir = 10000  
maks_waktu_parkir = 240  
batas_denda_1 = 240  
batas_denda_2 = 360  
tarif_denda_1 = 0.1   
tarif_denda_2 = 0.25  
pin_admin = "1234"  

tarif_parkir_zona = {'a': 12000, 'b': 10000, 'c': 10000}
anggota_parkir = {'D1234AF': {'nama': 'Ijat', 'diskon': 0.1}}

pesan_selamat_datang = [
    "Selamat datang di Aplikasi Parkir! Nikmati layanan kami.",
    "Salam parkir! Semoga perjalanan Anda menyenangkan.",
    "Halo, pengguna parkir cerdas! Mari parkir dengan nyaman.",
]
print(random.choice(pesan_selamat_datang))

def tambah_member():
    id_member_baru = input("Masukkan ID keanggotaan baru: ")
    nama_member_baru = input("Masukkan nama member baru: ")
    diskon_member_baru = float(input("Masukkan diskon untuk member baru (0.1 untuk 10%): "))

    if id_member_baru in anggota_parkir:
        print("Member dengan ID tersebut sudah ada.")
    else:
        anggota_parkir[id_member_baru] = {'nama': nama_member_baru, 'diskon': diskon_member_baru}
        print(f"Member baru {nama_member_baru} (ID: {id_member_baru}) ditambahkan dengan diskon {diskon_member_baru * 100}%.")

def tampilkan_member():
    print("\n=== Daftar Member ===")
    for id_member, info_member in anggota_parkir.items():
        print(f"ID: {id_member}, Nama: {info_member['nama']}, Diskon: {info_member['diskon'] * 100}%")
    print("=====================\n")

def hitung_biaya_parkir(waktu_masuk, waktu_keluar, zona_parkir):
    durasi_parkir_detik = waktu_keluar - waktu_masuk

    # Mengubah penggunaan waktu UTC ke waktu UTC+7
    waktu_masuk = time.gmtime(waktu_masuk)
    waktu_keluar = time.gmtime(waktu_keluar)

    print(f"Waktu Masuk: {time.strftime('%H:%M:%S', waktu_masuk)} UTC+7")
    print(f"Waktu Keluar: {time.strftime('%H:%M:%S', waktu_keluar)} UTC+7")

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



def hitung_denda(durasi_parkir_menit):
    if durasi_parkir_menit >= 4 and durasi_parkir_menit < 6:
        denda = 0.1
    elif durasi_parkir_menit >= 6:
        denda = 0.25
    else:
        denda = 0

    return denda

def cetak_semua_transaksi():
    if not kendaraan_parkir:
        print("Belum ada transaksi parkir.")
    else:
        print("\n=== Seluruh Transaksi Parkir ===")
        for plat, info in kendaraan_parkir.items():
            cetak_transaksi_parkir(plat, info['waktu_masuk'], info['waktu_keluar'], info['biaya_parkir'], info['denda'], info['jenis_kendaraan'])
        print("=============================\n")

        
def cetak_transaksi_parkir(nomor_kendaraan, waktu_masuk, waktu_keluar, biaya_parkir, denda, jenis_kendaraan):
    if waktu_keluar is not None:  
        print("\n--- Transaksi Parkir ---")
        print(f"Nomor Kendaraan: {nomor_kendaraan}")
        print(f"Jenis Kendaraan: {'Mobil' if jenis_kendaraan == '1' else 'Motor'}")
        print(f"Waktu Masuk: {time.strftime('%H:%M:%S', time.gmtime(waktu_masuk))}")
        print(f"Waktu Keluar: {time.strftime('%H:%M:%S', time.gmtime(waktu_keluar))}")
        
        durasi_parkir_detik = waktu_keluar - waktu_masuk
        durasi_parkir_menit = int(durasi_parkir_detik / 60)
        durasi_parkir_detik_sisa = int(durasi_parkir_detik % 60)

        print(f"Durasi Parkir: {durasi_parkir_menit} menit {durasi_parkir_detik_sisa} detik")
        print(f"Biaya Parkir: Rp {biaya_parkir:,.0f}")

        if denda > 0:
            print(f"Denda: Rp {denda * biaya_parkir:,.0f}")
        else:
            print("Denda: Tidak ada")

        print(f"Total Bayar: Rp {(1 + denda) * biaya_parkir:,.0f}")
        print("------------------------")
        print("=============================\n")



def masuk_mode_admin():
    pin_dimasukkan = input("Masukkan PIN Admin Parkir: ")
    if pin_dimasukkan == pin_admin:
        print("\n=== Selamat datang, Admin Parkir ===")
        menu_admin()
    else:
        print("PIN salah. Kembali ke menu utama.")

def cetak_kendaraan_belum_keluar():
    belum_keluar = [plat for plat, info in kendaraan_parkir.items() if info['waktu_keluar'] is None]
    
    if not belum_keluar:
        print("Semua kendaraan telah keluar dari area parkir.")
        print("==============================================\n")

    else:
        print("\n=== Kendaraan Belum Keluar ===")
        for plat in belum_keluar:
            info = kendaraan_parkir[plat]
            print(f"Nomor Kendaraan: {plat}")
            print(f"Waktu Masuk: {time.strftime('%H:%M:%S', time.gmtime(info['waktu_masuk']))}")
            print("------------------------")
        print("=============================\n")

def menu_admin():
    while True:
        print("\nMenu Admin Parkir:")
        print("1. Cetak Seluruh Transaksi")
        print("2. Kendaraan Belum Keluar")
        print("3. Tambah Member")
        print("4. Tampilkan Member")
        print("5. Kembali ke Menu Utama")
        opsi = input("Pilih menu (1/2/3/4/5): ")

        if opsi == "1":
            cetak_semua_transaksi()
        elif opsi == "2":
            cetak_kendaraan_belum_keluar()
        elif opsi == "3":
            tambah_member()
        elif opsi == "4":
            tampilkan_member()
        elif opsi == "5":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def masuk_parkir():
    print("Masukkan plat nomor kendaraan:")
    plat_kendaraan = input("Nomor Kendaraan (contoh: D1234AF): ")

    if plat_kendaraan in kendaraan_parkir and kendaraan_parkir[plat_kendaraan]['waktu_keluar'] is None:
        print(f"Kendaraan dengan plat {plat_kendaraan} sudah terdaftar di area parkir.")
        return

    # Rest of the existing masuk_parkir() function remains unchanged
    while True:
        print("Pilih jenis kendaraan:")
        print("1. Mobil")
        print("2. Motor")
        jenis_kendaraan = input("Masukkan nomor jenis kendaraan (1/2): ")

        if jenis_kendaraan not in ["1", "2"]:
            print("Pilihan tidak valid. Silakan coba lagi.")
            continue

        konfirmasi_jenis = input(f"Apakah Anda yakin ingin memilih jenis kendaraan {'Mobil' if jenis_kendaraan == '1' else 'Motor'}? (y/n): ").lower()

        if konfirmasi_jenis == "y":
            break
        else:
            print("Pilihan jenis kendaraan dibatalkan. Kembali ke menu pilihan kendaraan.")
            continue

    while True:
        while True:
            print("Pilih zona parkir:")
            print("a. Zona A")
            print("b. Zona B")
            print("c. Zona C")
            zona_parkir = input("Masukkan pilihan zona parkir (a/b/c): ")

            validasi_zona = (zona_parkir == "a" and jenis_kendaraan == "1") or (zona_parkir in ["b", "c"] and jenis_kendaraan == "2")

            if not validasi_zona:
                print("Pilihan zona dan jenis kendaraan tidak sesuai. Silakan coba lagi.")
                continue

            if zona_parkir not in tarif_parkir_zona:
                print("Zona parkir tidak valid. Silakan coba lagi.")
                continue

            tariff = tarif_parkir_zona[zona_parkir]

            print(f"Tarif parkir untuk zona {zona_parkir}: Rp {tariff:,.0f} per 60 detik")

            konfirmasi_zona = input(f"Apakah Anda yakin ingin memilih zona {zona_parkir}? (y/n): ").lower()

            if konfirmasi_zona == "y":
                break
            else:
                print("Pilihan zona dibatalkan. Kembali ke menu zona.")
                continue
        
        id_anggota = input("Masukkan ID keanggotaan (kosongkan jika tidak ada): ")

        if id_anggota in anggota_parkir:
            diskon = anggota_parkir[id_anggota]['diskon']
            print(f"Selamat datang, {anggota_parkir[id_anggota]['nama']}! Anda mendapatkan diskon {diskon * 100}%.")
            tariff = tariff * (1 - diskon)
        else:
            diskon = 0

        waktu_masuk = time.time() + 7 * 3600  # Tambahkan offset waktu UTC+7
        print(f"Waktu masuk kendaraan dicatat: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(waktu_masuk))} UTC+7")

        kendaraan_parkir[plat_kendaraan] = {'waktu_masuk': waktu_masuk, 'waktu_keluar': None, 'biaya_parkir': None,
                                            'denda': None, 'zona_parkir': zona_parkir, 'diskon': diskon, 'jenis_kendaraan': jenis_kendaraan}
        
        break  # Keluar dari loop utama jika sudah berhasil memilih zona

def keluar_parkir():
    plat_kendaraan = input("Masukkan nomor kendaraan: ")

    if plat_kendaraan not in kendaraan_parkir:
        print("Kendaraan tidak ditemukan di area parkir. Silakan masukkan kendaraan yang benar.")
    elif kendaraan_parkir[plat_kendaraan]['waktu_keluar'] is not None:
        print("Kendaraan dengan plat", plat_kendaraan, "sudah keluar dari area parkir.")
        # Remove the entry from kendaraan_parkir dictionary
        del kendaraan_parkir[plat_kendaraan]
    else:
        # Rest of the existing keluar_parkir() function remains unchanged
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

        kendaraan_parkir[plat_kendaraan]['waktu_keluar'] = waktu_keluar
        kendaraan_parkir[plat_kendaraan]['biaya_parkir'] = biaya_parkir_diskon
        kendaraan_parkir[plat_kendaraan]['denda'] = denda

        cetak_transaksi_parkir(plat_kendaraan, waktu_masuk, waktu_keluar, biaya_parkir_diskon, denda, jenis_kendaraan)

        nominal_pembayaran = float(input("Masukkan nominal pembayaran: Rp "))

        while nominal_pembayaran < (1 + denda) * biaya_parkir_diskon:
            print("Maaf, nominal pembayaran kurang. Silakan masukkan uang yang cukup.")
            print("Jika tidak dapat membayar, silakan menghubungi petugas.")
            nominal_pembayaran = float(input("Masukkan nominal pembayaran: Rp "))

        kembalian = nominal_pembayaran - (1 + denda) * biaya_parkir_diskon

        if kembalian >= 0:
            print(f"Terima kasih! Kembalian Anda: Rp {kembalian:,.0f}")
            print("Gerbang keluar terbuka. Sampai jumpa!")
        else:
            print("Gerbang keluar tetap tertutup.")

            # Tambahkan kendaraan kembali ke daftar kendaraan yang belum keluar
            kendaraan_parkir[plat_kendaraan]['waktu_keluar'] = None
            kendaraan_parkir[plat_kendaraan]['biaya_parkir'] = None
            kendaraan_parkir[plat_kendaraan]['denda'] = None


def aplikasi_parkir():
    while True:
        print("\nMenu Utama:")
        print("1. Masuk Area Parkir")
        print("2. Keluar Area Parkir")
        print("3. Admin Parkir")
        print("4. Keluar Aplikasi")
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == "1":
            masuk_parkir()
        elif pilihan == "2":
            keluar_parkir()
        elif pilihan == "3":
            masuk_mode_admin()
        elif pilihan == "4":
            pesan_perpisahan()
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def pesan_perpisahan():
    pesan_perpisahan = [
        "Terima kasih telah menggunakan Aplikasi Parkir! Sampai jumpa di kesempatan berikutnya.",
        "Hati-hati di perjalanan Anda! Terima kasih telah memilih layanan parkir kami.",
        "Selamat tinggal! Semoga harimu menyenangkan dan bebas dari masalah parkir.",
    ]
    print(random.choice(pesan_perpisahan))

aplikasi_parkir()
