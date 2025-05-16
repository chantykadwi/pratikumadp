data_mahasiswa = []  

def tampilkan_menu():
    print("\n=== PROGRAM MANAJEMEN NILAI MAHASISWA ===")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampilkan Data (Urut Nilai)")
    print("4. Keluar")
    print("======================================")

def tambah_data():
    print("\n-- Tambah Data --")
    nomor = input("Nomor Mahasiswa: ")
    nama = input("Nama Mahasiswa: ")
    
    while True:
        try:
            nilai = float(input("Nilai (0-100): "))
            if 0 <= nilai <= 100:
                break
            print("Nilai harus 0-100!")
        except:
            print("Harus angka!")
    
    data_mahasiswa.append([nomor, nama, nilai])
    print(f"Data {nama} ditambahkan!")

def hapus_data():
    if not data_mahasiswa:
        print("\nDatabase kosong!")
        return
    
    print("\n-- Hapus Data --")
    for i, mhs in enumerate(data_mahasiswa):
        print(f"{i+1}. {mhs[0]} - {mhs[1]} - {mhs[2]}")
    
    nomor = input("Nomor yang akan dihapus: ")
    for i in range(len(data_mahasiswa)):
        if data_mahasiswa[i][0] == nomor:
            del data_mahasiswa[i]
            print("Data dihapus!")
            return
    print("Nomor tidak ditemukan!")

def tampilkan_data():
    if not data_mahasiswa:
        print("\nDatabase kosong!")
        return
    
    
    salinan = [mhs.copy() for mhs in data_mahasiswa]
    
    
    n = len(salinan)
    for i in range(n):
        for j in range(0, n-i-1):
            if salinan[j][2] < salinan[j+1][2]:
                
                salinan[j][0], salinan[j+1][0] = salinan[j+1][0], salinan[j][0]
                salinan[j][1], salinan[j+1][1] = salinan[j+1][1], salinan[j][1]
                salinan[j][2], salinan[j+1][2] = salinan[j+1][2], salinan[j][2]
    
    print("\nData Terurut:")
    print("No.\tNama\t\tNilai")
    print("-"*30)
    for mhs in salinan:
        print(f"{mhs[0]}\t{mhs[1]}\t{mhs[2]}")


while True:
    tampilkan_menu()
    pilih = input("Pilihan (1-4): ")
    
    if pilih == '1':
        tambah_data()
    elif pilih == '2':
        hapus_data()
    elif pilih == '3':
        tampilkan_data()
    elif pilih == '4':
        print("\nProgram selesai")
        break
    else:
        print("\ninput salah")

    input("\ntekan enter")