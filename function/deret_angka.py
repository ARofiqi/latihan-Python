print("""
=========================
    Jumlah Deret Angka
=========================""")

def deret(n_max):
    hasil = 0
    for i in range(n_max+1):
        hasil+=i
    print("Rata-rata =",hasil)

i = int(input("Masukan angka :"))
deret(i)