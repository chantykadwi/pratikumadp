print("\n")
print("=== PROGRAM HITUNG JARAK TITIK ===")
print("----------------------------------")
print("Format input: x,y (contoh: 3,4 atau 1.5,-2)")


while True:
    try:
        n = int(input("\nMasukkan jumlah titik (n): "))
        if n < 1:
            print("Harus lebih dari 0!")
            continue
        break
    except:
        print("Input harus angka!")


titik = []


print("\nMasukkan koordinat titik:")
for i in range(n):
    while True:
        try:
            x, y = map(float, input(f"Titik ke-{i+1}: ").split(','))
            titik.append([x, y])
            break
        except:
            print("Format salah! Contoh: 2,3 atau 1.5,-4")


print("\n=== HASIL ===")
print("Jarak dari (0,0):")
for i in range(n):
    x, y = titik[i]
    jarak = (x**2 + y**2)**0.5
    print(f"Titik {i+1}: {jarak:.3f}")


print("\nJarak antar titik:")
for i in range(n):
    for j in range(i+1, n):
        x1, y1 = titik[i]
        x2, y2 = titik[j]
        jarak = ((x2-x1)**2 + (y2-y1)**2)**0.5
        print(f"Titik {i+1} ke {j+1}: {jarak:.3f}")

print("\n===SELESAI===")