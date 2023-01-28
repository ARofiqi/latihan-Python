def hitung(*numbers, **operasi):
    hasil = 0
    if operasi["pilih"] == "tambah":
        for i in numbers:
            hasil += i
        print(f"Hasilnya : {hasil}")
    elif operasi["pilih"] == "kurang":
        for i in numbers:
            hasil -= i
        print(f"Hasilnya : {hasil}")
    elif operasi["pilih"] == "kali":
        hasil = 1
        for i in numbers:
            hasil *= i
        print(f"Hasilnya : {hasil}")
    else:
        print("Error")


# hitung(1,2,3,4,54,pilih="tambah")
# hitung(1,2,3,4,54,pilih="kali")
# hitung(1,2,3,4,54,pilih="kurang")

def mhs(**data):
    for i in data:
        print(i.ljust(8), data[i].ljust(20))

mhs(nama="Ahmad Rofiqi",jrs="Informatika")
