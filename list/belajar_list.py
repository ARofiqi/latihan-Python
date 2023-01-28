buah = ["mangga", "jeruk", "durian", "semangka", "anggur"]

# menampilkan isi list sesuai dengan nilai index -- list[]
print("Buah ke-index[2] : {}".format(buah[2]))

# menampilkan berapa banyak isi didalam list -- len()
print("Total semuah buah : {} buah".format(len(buah)))

# menampikan semua isi list dengan perulangan
for b in buah:
    print("- buah {}".format(b))

# mengganti nilai list
print("buah pertama : buah {}".format(buah[0]))
buah[0] = "Apel"
print("diganti dengan : buah {}".format(buah[0]))

# prepend(item), menambahkan item dari depan
# append(item),  menambahkan item dari belakang
# insert(index,  item) menambahkan item dari indeks tertentu

buah.append("Dukuh")
print("\nbuah yang ditambah dengan append : buah {}".format(buah[0]))
print(buah)

buah.insert(3, "pisang")
print("\nbuah yang ditambah dengan insert : buah {}".format(buah[3]))
print(buah)

# menghilangkan list item --  del dan remove()

# del --> menghapus list sesuai indexnya syntax del list[index]
print("\nlist buah awal :{}".format(buah))
print(
    "menghapus list ke-2-index dengan del jadi yang akan hilang yaitu {}".format(buah[2]))
del buah[2]
print("list buah akhir : {}".format(buah))

# remove() --> menghapus list sesuai dengan item list syntax list.remove(item)
print("\nlist buah awal       : {}".format(buah))
hapus = "jeruk"
print("menghapus list dengan remove() jadi yang akan hilang yaitu {}".format(hapus))
buah.remove(hapus)
print("list buah akhir      : {}".format(buah))


# memotong list syntax list[index_awal:index_akhir] note: awal <= x < akhir
print("\nlist buah awal                : {}".format(buah))
print("list buah yang telah dipotong : {}".format(buah[1:4]))

# operasi pada list

# penggabungan (+) --> untuk menggabungkan list
hewan = ["kucing", "anjing", "sapi", "Kambing"]
ikan = ["nila", "mujair", "cod", "salmon"]
makhluk_hidup = hewan + ikan

print("\nlist hewan         :", hewan)
print("list ikan          :", ikan)
print("list makhluk hidup :", makhluk_hidup)

# perkalian (*)    --> untuk menduplikasi list
sapa = ["halo", "hai"]
ulang = 4
print("\nlist sapa : {}\ndikali {}".format(sapa, ulang))
print(sapa*ulang)
