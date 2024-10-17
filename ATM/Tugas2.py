# NIM : 102022300118
# Nama : Deazard Muhammad Arrayyan

nim_0118 = input("Masukkan NIM Anda: ")
nama_0118 = str(input("Masukkan Nama Anda: "))
NoRek_0118 = int(input("Masukkan Nomor Rekening Anda: "))
saldo_0118 = 0
pin_0118 = nim_0118[-6:]
login_0118 = False

while not login_0118:
    pin_masuk_0118 = input("Masukkan PIN (6 digit dari NIM): ")
    login_0118 = pin_masuk_0118 == pin_0118

    if not login_0118:
        print("PIN yang dimasukkan salah. Silakan coba lagi.")


while True:
    print("")
    print("===     ATM     ===")
    print("|                 |")
    print("|  1. Cek Saldo   |")
    print("|                 |")
    print("|  2. Tarik Uang  |")
    print("|                 |")
    print("|  3. Setor Uang  |")    
    print("|                 |")
    print("|  4. Selesai     |")
    print("|                 |")
    print("===================")
    print("")
    kategori_0118 = input("Pilih Menu (1/2/3/4): ")

    if kategori_0118 =="1":
        print("|--- Cek Saldo ---|")
        print("NIM:", nim_0118)
        print("Nama:", nama_0118)
        print("No. Rek:", NoRek_0118)
        print("Saldo:", saldo_0118)
        print("|-----------------|")
        print("")
   
    elif kategori_0118 =="2":
        print("|---- Tarik Uang ----|")
        nominal_0118 = int(input("Masukkan nominal yang akan ditarik: "))
        if nominal_0118 > 0 and nominal_0118 <= saldo_0118:
            saldo_0118 -= nominal_0118
            print("Tarik uang berhasil. Saldo akhir:", saldo_0118)
        else:
            print("Nominal tidak valid atau saldo tidak mencukupi.")
    elif kategori_0118 =="3":
        print("|---- Setor Uang ----|")
        nominal_0118 = int(input("Masukkan nominal yang akan disetor: "))
        if nominal_0118 > 0:
            saldo_0118 += nominal_0118
            print("Setor uang berhasil. Saldo akhir:", saldo_0118)
        else:
            print("Nominal tidak valid.")
    elif kategori_0118 =="4":
        print("")
        cetak_struk_0118 = input("Apakah Anda ingin mencetak struk transaksi? (ya/tidak): ")
        if cetak_struk_0118.lower() == "ya":
            print("|----- Histori Transaksi -----|")
            print("NIM:", nim_0118)
            print("Nama:", nama_0118)
            print("No. Rek:", NoRek_0118)
            print("Saldo Awal:", saldo_0118 + nominal_0118) 
            print("Nominal Transaksi:", nominal_0118)
            print("Saldo Akhir:", saldo_0118)
            print("|-----------------------------|")
            print("")
            print("||== Terima Kasih, Sampai Jumpa ==||")
            print("")
            break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")