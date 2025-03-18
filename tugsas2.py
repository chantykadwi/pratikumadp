print("mari hitung probalitas distribusi poisson.")
lamda_t= float(input("masukan nilai lambda*t: "))
m=int(input("masukan nilai m: "))

e=2.71828

print(f"\n masukan lambda={lamda_t} dan m={m}.")
print("berikut adalah hasil perhitungan probalitasn untuk n=0 sampai n = m:\n")
for n in range(m+1):

    faktorial=1
    for i in range(1, n+1):
        faktorial*=i

    probalitas=(e**(-lamda_t))*((lamda_t**n)/ faktorial)

    print(f"untuk n = {n}:")
    print(f"faktorial({n})={faktorial}")
    print(f"probalias p(N(t) = {n}) = {probalitas:.6f}")
    print("-"*30)


print("\n selesai")

