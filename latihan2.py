def hitung_keuntungan(modal_awal, laba_per_bulan):
    total_keuntungan = 0
    laba_bulanan = []

    # Menghitung laba untuk setiap bulan
    for bulan in range(len(laba_per_bulan)):
        laba = modal_awal * laba_per_bulan[bulan]
        laba_bulanan.append(laba)
        total_keuntungan += laba
        print(f"Bulan {bulan + 1}: Laba = Rp.{laba:.0f} ")

    return total_keuntungan, laba_bulanan

def main():
    # Modal awal
    modal_awal = 100_000_000  # 100 juta IDR

    # Persentase laba per bulan
    laba_per_bulan = [0, 0, 0.01, 0.01, 0.05, 0.05, 0.05, 0.02]

    # Menghitung total keuntungan
    total_keuntungan, laba_bulanan = hitung_keuntungan(modal_awal, laba_per_bulan)

    # Menampilkan total keuntungan
    print(f"\nTotal keuntungan selama 8 bulan: Rp.{total_keuntungan:.0f} ")

if __name__ == "__main__":
    main()