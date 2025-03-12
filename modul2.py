



harga_paket_makanan = int(input("silahkan masukan harga paket makanan :"))
paket_makanan =input("silahkan masukan paket makanan :")
if  harga_paket_makanan<25000:
    print("pelanggan tersebut mendapatkan paket a= nasi goreng, es teh")
elif 26000<harga_paket_makanan<29000:
   print('pelangggan tersebut mendapatkan paket b= nasi pecel ayam,es teh')
elif 30000<harga_paket_makanan<32000 :
   print("pelanggan tersebut mendapatka paket c=  nasi pecel lele, es teh")
elif 33000<harga_paket_makanan <36000:
    print("pelanggan tersebut mendapatkan paket d= nasi ayam bakar, es teh")
elif 37000<harga_paket_makanan <39000:
   print("pelanggan tersebut mendapatkan paket e= nasi ayam saus padang, es teh")
else:
   print("maaf, tidak ada paket dengan harga tersebut")

