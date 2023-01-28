def luas_segitiga(alas=0, tinggi=0):
    return (0.5*alas*tinggi)


def jenis(n):
    num = int(n)
    if num % 2 == 0:
        return "genap"
    else:
        return "Ganjil"


def luas_persegi_panjang(panjang=0, lebar=0):
    return (panjang*lebar)


while True:
    print("========== kalkulator ==========")
    print("1. Luas segitiga")
    print("2. Luas persegi empat")
    print("3. Menentukan ganjil / genap")
    print("4. Quit\n")

    opt = input("Pilih Opsi : ")

    if opt == 1:
        a = int(input("Masukan Alas   : "))
        t = int(input("Masukan Tinggi : "))
        hasil = luas_segitiga(a, t)
        print(f"Hasil = {hasil}")
    elif opt == 2:
        p = int(input("Masukan Panjang   : "))
        l = int(input("Masukan lebar     : "))
        hasil = luas_persegi_panjang(p, l)
        print(f"Hasil = {hasil}")
    elif opt == 3:
        num = int(input("Masukan Angka : "))
        hasil = jenis(num)
        print(f"Hasil = {hasil}")
    elif opt == 4:
        quit = input("Apakah kamu ini keluar (y/n) : ")
        if quit == 'y':
            break
    else:
        print("Harap memasukan nilai yang benar")