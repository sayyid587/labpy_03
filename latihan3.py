# Saldo awal
saldo = 100_000_000

print("Selamat datang di Mesin ATM!")
print(f"Saldo Anda saat ini: Rp {saldo}")

while True:
    # Menampilkan menu
    print("\nMenu:")
    print("1. Tarik Tunai")
    print("2. Cek Saldo")
    print("3. Keluar")

    # Meminta input dari pengguna
    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == '1':
        # Tarik tunai
        jumlah_tarik = int(input("Masukkan jumlah uang yang ingin ditarik: Rp "))
        
        if jumlah_tarik > saldo:
            print("Jumlah yang diminta melebihi saldo Anda. Silakan coba lagi.")
        elif jumlah_tarik <= 0:
            print("Jumlah penarikan harus lebih dari 0. Silakan coba lagi.")
        else:
            saldo -= jumlah_tarik
            print(f"Anda telah menarik Rp {jumlah_tarik}. Sisa saldo Anda: Rp {saldo}")

    elif pilihan == '2':
        # Cek saldo
        print(f"Saldo Anda saat ini: Rp {saldo}")

    elif pilihan == '3':
        # Keluar
        print("Terima kasih telah menggunakan Mesin ATM. Selamat tinggal!")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")