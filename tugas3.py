def tampilkan_kursi():
    print("\n[LAYOUT KURSI]")
    for i in range(6):
        baris = []
        for j in range(5):
            nomor = i*5 + j + 1
            if kursi[nomor-1] == 1:
                baris.append("X")
            else:
                baris.append(str(nomor))
        print(" ".join(baris))

def tentukan_kategori(nomor):
    if 1 <= nomor <= 5:
        return "VVIP", 1000000
    elif 6 <= nomor <= 15:
        return "VIP", 750000
    elif 16 <= nomor <= 25:
        return "Regular", 500000
    else:
        return "Ekonomi", 300000

# Inisialisasi data
kursi = [0] * 30  # 0 = kosong, 1 = terisi

print("=== RESERVASI TIKET KONSER ===")
print("\nKategori Kursi:")
print("1-5: VVIP (Rp1.000.000)")
print("6-15: VIP (Rp750.000)")
print("16-25: Regular (Rp500.000)")
print("26-30: Ekonomi (Rp300.000)")

while True:
    tampilkan_kursi()
    
    try:
        jumlah = int(input("\nMau pesan berapa tiket? (0 untuk keluar) "))
        if jumlah == 0:
            break
    except:
        print("Harap masukkan angka!")
        continue
    
    for i in range(jumlah):
        print(f"\nPEMESANAN KE-{i+1}")
        
        while True:
            try:
                nomor = int(input("Pilih nomor kursi: "))
                if nomor < 1 or nomor > 30:
                    print("Nomor kursi antara 1-30")
                    continue
                if kursi[nomor-1] == 1:
                    print("Kursi sudah terisi!")
                    continue
                break
            except:
                print("Harap masukkan angka!")
        
        nama = input("Nama pemesan: ")
        password = input("Buat password: ")
        
        kategori, harga = tentukan_kategori(nomor)
        kursi[nomor-1] = 1
        
        print("\n[STRUK PEMESANAN]")
        print(f"Nama: {nama}")
        print(f"Kursi: {nomor}")
        print(f"Kategori: {kategori}")
        print(f"Harga: Rp{harga:,}")
        print(f"Password: {password}")
        print("------------------")

print("\nTerima kasih!")