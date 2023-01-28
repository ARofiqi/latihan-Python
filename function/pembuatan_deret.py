print("""
=========================
    Pembuatan Deret
=========================""")

def buat_deret_ganjil(total):
    print("deret ganjil :")
    for n in range(total):
        print(2*n+1)

def buat_deret_genap(total):
    print("deret genap :")
    for n in range(total):
        print("-",2*n+2)

buat_deret_genap(10)