biodata_temp = {
    "nama":"nama kalian",
    "prodi":"prodi kalian",
    "kelas":"kelas kalian",
    "ipk":"ipk kalian"
}

mhs = {
    "Rofiqi":{
        "nama":"Ahmad Rofiqi",
        "prodi":"Teknik Informatika",
        "kelas":"TI22E",
        "ipk":"4.0"
        },

}

def buat_bio(bio_utama):
    print("List data".ljust(17))
    print("="*17)
    for index,i in enumerate(bio_utama):
        print(index+1,":",i)

def see_bio(bio):
    print(f"Biodata Mahasiswa")
    print("-"*17)
    for i in bio:
        print(i.ljust(7),"=",bio[i].ljust(10))

# buat_bio(mhs)
# print("")
# see_bio(mhs["Rofiqi"])

def tambah(x=0,y=0):
    return x + y

def kuadrat(x=0):
    return x**2

def akar(x=0):
    for i in range(x):
        if i**2 == x:
            return i

# print("Hasilnya :",tambah(8,20))
# print("Hasilnya :",kuadrat(20))
# print("Hasilnya :",akar(144))

# print("Hasilnya :",tambah())
# print("Hasilnya :",kuadrat())
# print("Hasilnya :",akar())

import os


def kotak():
    while True:    
        os.system("cls")
        sisi = int(input("Tentukan Sisinya : "))
        os.system("cls")
        for i in range(sisi):
            print(" = "*sisi)
kotak()