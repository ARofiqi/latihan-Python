# Contoh Penerapan copy()
fruit = ["Mangga","Anggur","Apel","Pepaya"]
copy = fruit.copy()
print(f"""
List fruit = {fruit}
List copy = {copy}
""")

# Contoh penerapan count()
num = [1,2,3,3,4,5,5,4,4,4,3,2,2]
print(f"""
List num = {num}
jumlah angka 1 ada {num.count(1)}
jumlah angka 2 ada {num.count(2)}
jumlah angka 3 ada {num.count(3)}
jumlah angka 4 ada {num.count(4)}
jumlah angka 5 ada {num.count(5)}
""")

# Contoh penerapan extend()
buah_asam = ["Lemon","Kedongdong","Markisa"]
buah_manis = ["Apel","Semangka","Mangga"]
buah = []
buah.extend(buah_asam)
buah.extend(buah_manis)
print(f"""
List buah asam = {buah_asam}
list buah manis = {buah_manis}
list semua buah = {buah}
""")