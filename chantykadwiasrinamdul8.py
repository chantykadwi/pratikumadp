def validasi_nilai(prompt):
    while True:
        try:
            nilai = float(input(prompt))
            if 0 <= nilai <= 100:
                return nilai
            else:
                print("Nilai harus antara 0-100. Silakan coba lagi.")
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")


def input_data_praktikan():
    daftar_praktikan = []
    jumlah = int(input("Berapa banyak praktikan dalam shift ini? "))
    print("\n" + "="*50)
    
    for i in range(jumlah):
        print(f"\nData Praktikan ke-{i+1}")
        nama = input("Nama Praktikan: ").title()
        nim = input("NIM: ")
        
        print("\nMasukkan Nilai Praktikan:")
        pretest = validasi_nilai("Pretest (0-100): ")
        postest = validasi_nilai("Postest (0-100): ")
        tugas = validasi_nilai("Tugas/Makalah (0-100): ")
        bonus = validasi_nilai("Bonus (0-10): ")
        
       
        nilai_akhir = (0.25 * pretest + 0.25 * postest + 0.5 * tugas) + bonus
        
        
        nilai_akhir = min(nilai_akhir, 100)
        
        daftar_praktikan.append({
            'nama': nama,
            'nim': nim,
            'pretest': pretest,
            'postest': postest,
            'tugas': tugas,
            'bonus': bonus,
            'nilai_akhir': nilai_akhir
        })
        print("-"*30)
    
    return daftar_praktikan


def hitung_rata_rata(daftar_praktikan):
    if not daftar_praktikan:
        return None
    
    total = {
        'pretest': 0,
        'postest': 0,
        'tugas': 0,
        'nilai_akhir': 0
    }
    
    for praktikan in daftar_praktikan:
        total['pretest'] += praktikan['pretest']
        total['postest'] += praktikan['postest']
        total['tugas'] += praktikan['tugas']
        total['nilai_akhir'] += praktikan['nilai_akhir']
    
    jumlah = len(daftar_praktikan)
    return {
        'pretest': total['pretest'] / jumlah,
        'postest': total['postest'] / jumlah,
        'tugas': total['tugas'] / jumlah,
        'nilai_akhir': total['nilai_akhir'] / jumlah
    }


def urutkan_dan_beri_peringkat(daftar_praktikan):
    
    daftar_terurut = sorted(daftar_praktikan, key=lambda x: x['nilai_akhir'], reverse=True)
    
    
    for i, praktikan in enumerate(daftar_terurut):
        praktikan['peringkat'] = i + 1
    
    return daftar_terurut


def tampilkan_hasil(daftar_praktikan, rata_rata):
    
    print("\n" + "="*65)
    print("| {:<20} | {:<15} | {:<12} | {:<8} |".format(
        "NAMA", "NIM", "NILAI AKHIR", "RANKING"))
    print("="*65)
    
      
    for praktikan in daftar_praktikan:
        print("| {:<20} | {:<15} | {:<12.2f} | {:<8} |".format(
            praktikan['nama'],
            praktikan['nim'],
            praktikan['nilai_akhir'],
            praktikan['peringkat']))
    
    
    print("="*65)
    print("| {:<20} | {:<15} | {:<12.2f} | {:<8} |".format(
        "", "RATA-RATA", rata_rata['nilai_akhir'], ""))
    print("="*65)


def tampilkan_statistik(rata_rata):
    print("\nSTATISTIK NILAI PRAKTIKAN")
    print("="*30)
    print(f"Rata-rata Pretest : {rata_rata['pretest']:.2f}")
    print(f"Rata-rata Postest : {rata_rata['postest']:.2f}")
    print(f"Rata-rata Tugas   : {rata_rata['tugas']:.2f}")
    print("="*30)


def main():
    print("\n" + "="*50)
    print(" SISTEM PENGOLAHAN NILAI PRAKTIKAN ".center(50, '='))
    print("="*50)
    
    
    data_praktikan = input_data_praktikan()
    
    
    statistik = hitung_rata_rata(data_praktikan)
    
    
    data_terurut = urutkan_dan_beri_peringkat(data_praktikan)
    
    
    tampilkan_hasil(data_terurut, statistik)
    tampilkan_statistik(statistik)
    
    print("\nProgram selesai. Data berhasil diproses!")

main()