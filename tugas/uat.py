# 2. Buatlah sebuah sistem kalkulator untuk menghitung beberapa rumus luas dan keliling ruang 
# datar serta luas dan volume ruang bangun dengan ketentuan:
# a. Buatlah menu untuk memilih rumus yang harus dihitung
# b. Buatlah perulangan ketika sudah selesai melakukan proses apakah ingin mengulang 
# kembali menu atau tidak
# c. Ruang Datar: Persegi, Persegi Panjang, Jajar Genjang, Segitiga, Belah Ketupat, Layang-Layang, Trapesium, Lingkaran
# d. Ruang Bangun: Kubus, Balok, Prisma Segitiga, Limas Segiempat, Limas Segitiga, Tabung, 
# Kerucut, dan Bola

import os

abjad = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
abjad_low = abjad.lower()
name_creator = abjad[0]+abjad_low[7]+abjad_low[12]+abjad_low[0]

def menu():
    print(f"""{" Kalkulator Rumus ".center(40," ")}
{" Dibuat oleh Ahmad Rofiqi ".center(40," ")}
{"-"*40}
[1] Ruang Datar
[2] Ruang Bangun
[0] Exit""")

# Fungsi Ruang datar

rumus_bangun_datar = [
    "Persegi",
    "Persegi Panjang",
    "Jajar Genjang",
    "Segitiga",
    "Belah Ketupat",
    "Layang-Layang",
    "Trapesium",
    "Lingkaran"
]

# menu bangun datar
def menu_rd():
    print(f"""{" Luas dan Keliling Ruang Datar ".center(40," ")} \n{"-"*40}""")
    for i,n in enumerate(rumus_bangun_datar):
        print(f"[{i+1}] {n}")
    print("[0] Back")

# Rumus Persegi
# luas = s x s
# keliling = s x 4
def persegi():
    print(" Persegi ".center(40," "))
    print("-"*40)
    s = float(input("Masukan Sisi : "))
    print(f"""\n{" Hasil ".center(40,"-")}
Persegi dengan Sisinya adalah {s}, maka :
Luas      = {s*s}
Keliling  = {s*4}""")

# Rumus Persegi Panjang
# luas = p x l
# Keliling = 2(p + l)
def persegi_panjang():
    print(" Persegi Panjang ".center(40," "))
    print("-"*40)
    p = float(input("Masukan Panjang : "))
    l = float(input("Masukan Lebar   : "))
    print(f"""\n{" Hasil ".center(40,"-")}
Persegi panjang dengan panjangnya adalah {p}
dan lebarnya adalah {l}, maka :
Luas      = {p*l}
Keliling  = {2*(p + l)}""")

# Rumus Jajar Genjang
# Luas = alas x tinggi
# Keliling = 2(alas + sisi miring)
def jajar_genjang():
    print(" jajar Genjang ".center(40," "))
    print("-"*40)
    a = float(input("Masukan Alas        : "))
    t = float(input("Masukan Tinggi      : "))
    s_m = float(input("Masukan Sisi Miring : "))
    print(f"""\n{" Hasil ".center(40,"-")}
Jajar genjang dengan alasnya adalah {a},
tingginya adalah {t} dan sisi miringnya
adalah {s_m}, maka :
Luas      = {a*t}
Keliling  = {2*(a + s_m)}""")

# Rumus Segitiga
# luas = alas x tinggi / 2
# keliling = s1 + s2 + s3
def segitiga():
    print(" Segitiga ".center(40," "))
    print("-"*40)
    a = float(input("Masukan Alas     : "))
    t = float(input("Masukan Tinggi   : "))
    s1 = float(input("Masukan Sisi 1   : "))
    s2 = float(input("Masukan Sisi 2   : "))
    s3 = float(input("Masukan Sisi 3   : "))
    print(f"""\n{" Hasil ".center(40,"-")}
Segitiga dengan alasnya adalah {a},
tingginya adalah {t} dan sisi-sisinya 
adalah {s1},{s2},{s3}, maka :
Luas      = {(a*t)/2}
Keliling  = {s1 + s2 + s3}""")

# Rumus Belah Ketupat
# luas = d1 x d2 / 2
# keliling = sisi x 4
def belah_ketupat():
    print(" Belah Ketupat ".center(40," "))
    print("-"*40)
    d1 = float(input("Masukan diagonal 1   : "))
    d2 = float(input("Masukan diagonal 2   : "))
    s = float(input("Masukan sisi         : "))
    print(f"""\n{" Hasil ".center(40,"-")}
Belah Ketupat dengan diagonal 1-nya adalah {d1}
dan sisinya adalah {s}, maka :
Luas      = {(d1*d2)/2}
Keliling  = {s*4}""")

# Rumus Layang Layang
# Luas = d1 x d2 / 2
# keliling = 2 x (s1 + s2)
def layang_layang():
    print(" Layang-Layang ".center(40," "))
    print("-"*40)
    d1 = float(input("Masukan diagonal 1   : "))
    d2 = float(input("Masukan diagonal 2   : "))
    s1 = float(input("Masukan sisi 1       : "))
    s2 = float(input("Masukan sisi 2       : "))
    print(f"""\n{" Hasil ".center(40,"-")}
Layang Layang dengan diagonal 1, diagonal 2
secara berturut-turut adalah {d1},{d2} dan
sisi 1, sisi 2 secara berturut-turut adalah 
{s1},{s2} , maka :
Luas      = {(d1*d2)/2}
Keliling  = {2*(s1+s2)}""")

# Rumus Trapesium
# luas = ((sisi atas + sisi bawah) x t )/ 2
# keliling = sisi atas + sisi bawah + sisi miring + tinggi
def trapesium():
    print(" Trapesium ".center(40," "))
    print("-"*40)
    s_a = float(input("Masukan sisi atas     : "))
    s_b = float(input("Masukan sisi bawah    : "))
    s_m = float(input("Masukan sisi miring   : "))
    t = float(input("Masukan tinggi        : "))
    print(f"""\n{" Hasil ".center(40,"-")}
Trapesium dengan sisi atas, sisi bawah, 
dan sisi miring secara berturut-turut adalah 
{s_a},{s_b},{s_m} dan tingginya adalah {t}, maka :
Luas      = {((s_a + s_b)*t)/2}
Keliling  = {s_a + s_b + s_m + t}""")

# Rumus Lingkarang
# Luas = pi x r x r
# keliling = 2 x pi x r
def lingkaran():
    print(" Lingkaran ".center(40," "))
    print("-"*40)
    r = float(input("Masukan jari-jari  : "))
    pi = 3.14
    print(f"""\n{" Hasil ".center(40,"-")}
Lingkaran dengan jari-jarinya adalah {r}, maka :
Luas      = {pi*r**2}
Keliling  = {2*pi*r}""")

# Fungsi Ruang Bangun
rumus_bangun_ruang = [
    "Kubus",
    "Balok",
    "Prisma Segitiga",
    "Limas Segiempat",
    "Limas Segitiga",
    "Tabung",
    "Kerucut",
    "Bola"
]
def menu_rb():
    print(f"""{" Luas dan Volume Ruang Bangun ".center(40," ")} \n{"-"*40}""")
    for i,n in enumerate(rumus_bangun_ruang):
        print(f"[{i+1}] {n}")
    print("[0] Back")


# Rumus Kubus
# luas = 6 x R x R
# Volume = R x R x R
def kubus():
    print(" Kubus ".center(40," "))
    print("-"*40)
    R = float(input("Masukan rusuk : "))
    print(f"""\n{" Hasil ".center(40,"-")}
Kubus dengan rusuk-rusuknya adalah {R} , maka :
Luas      = {6*R**2}
Volume    = {R**3}""")

# Rumus Balok
# luas = (2 x p x l) + (2 x p x t) + (2 x l x t)
# volume = p x l x t
def balok():
    print(" Balok ".center(40," "))
    print("-"*40)
    p = float(input("Masukan panjang : "))
    l = float(input("Masukan lebar   : "))
    t = float(input("Masukan tinggi  : "))
    print(f"""\n{" Hasil ".center(40,"-")}
Balok dengan panjangnya adalah {p}, lebarnya adalah {l},
dan tingginya adalah {t} , maka :
Luas      = {(2*p*l)+(2*p*t)+(2*l*t)}
Volume    = {p*l*t}""")

# Rumus Prisma Segitiga
# Luas = (s1 + s2 + s3) x T + luas segitiga
# volume = 1/2 x Luas alas x T 
def prisma_segitiga():
    print(" Prisma Segitiga ".center(40," "))
    print("-"*40)
    s1 = float(input("Masukan Sisi 1        : "))
    s2 = float(input("Masukan Sisi 2        : "))
    s3 = float(input("Masukan Sisi 3        : "))
    T = float(input("Masukan tinggi prisma : "))
    luas_s = float(input("Masukan luas segitiga : "))
    luas_a = float(input("Masukan luas alas     : "))
    print(f"""\n{" Hasil ".center(40,"-")}
Prisma Segitiga dengan sisi-sisi secara berturut-turut 
adalah {s1},{s2},{s3}, tingginya adalah {T}, 
luas segitiganya adalah {luas_s}, dan luas alasnya 
adalah {luas_a} , maka :
Luas      = {(s1 + s2 + s3)*T+luas_s}
Volume    = {0.5 * luas_a * T}""")

# Rumus Limas Segiempat
# luas = L1 + L2 + L3 + L4 + L5
# volume = 1/3 x l_a x T
def limas_segiempat():
    print(" Limas Segiempat ".center(40," "))
    print("-"*40)
    L1 = float(input("Masukan luas sisi 1   : "))
    L2 = float(input("Masukan luas sisi 2   : "))
    L3 = float(input("Masukan luas sisi 3   : "))
    L4 = float(input("Masukan luas sisi 4   : "))
    L5 = float(input("Masukan luas sisi 5   : "))
    l_a = float(input("Masukan luas alas     : "))
    T = float(input("Masukan tinggi limas  : "))
    print(f"""\n{" Hasil ".center(40,"-")}
Limas Segiempat dengan luas sisi-sisinya secara
berturut-turut adalah {L1},{L2},{L3}, {L4}, {L5},
tingginya adalah {T}, dan luas alasnya adalah {l_a} , maka :
Luas      = {L1 + L2 + L3 + L4 + L5}
Volume    = {1/3 * l_a * T}""")

# Rumus Limas Segitiga
# Luas = L_s1 + L_s2 + L_s3 + L_s4
# volume = 1/6 x L_a x T
def limas_segitiga():
    print(" Limas Segitiga ".center(40," "))
    print("-"*40)
    L1 = float(input("Masukan luas sisi 1   : "))
    L2 = float(input("Masukan luas sisi 2   : "))
    L3 = float(input("Masukan luas sisi 3   : "))
    L4 = float(input("Masukan luas sisi 4   : "))
    l_a = float(input("Masukan luas alas     : "))
    T = float(input("Masukan tinggi limas  : "))
    print(f"""\n{" Hasil ".center(40,"-")}
Limas Segitiga dengan luas sisi-sisiny 
secara berturut-turut adalah {L1},{L2},{L3}, {L4}, 
tingginya adalah {T}, dan luas alasnya adalah {l_a}, 
maka :
Luas      = {L1 + L2 + L3 + L4}
Volume    = {1/6 * l_a * T}""")

# Rumus Tabung
# Luas Selimut = 2 x pi x r x T
# Luas Permukaan = 2 x pi x r x T + 2 x pi x r x r
# volume = pi x r x r x T
def tabung():
    print(" Tabung ".center(40," "))
    print("-"*40)
    r = float(input("Masukan jari-jari : "))
    T = float(input("Masukan tinggi    : "))
    pi = 3.14
    luas_s = 2 * pi * r * T
    luas_p = (2 * pi * r * T) + (2 * pi * r**2)
    vol = pi * r**2 * T
    print(f"""\n{" Hasil ".center(40,"-")}
Tabung dengan jari-jari adalah {r} dan 
tingginya adalah {T}, maka :
Luas selimut     = {luas_s}
Luas permukaan   = {luas_p}
Volume           = {vol}""")

# Rumus Kerucut
# Luas Selimut = 2 x pi x r x s
# Luas Permukaan = 2 x pi x r x s + 2 x pi x r x r
# volume = 1/3 x pi x r x r x T
def kerucut():
    print(" Kerucut ".center(40," "))
    print("-"*40)
    r = float(input("Masukan jari-jari    : "))
    s = float(input("Masukan sisi miring  : "))
    T = float(input("Masukan tinggi       : "))
    pi = 3.14
    luas_s = 2 * pi * r * s
    luas_p = (2 * pi * r * s) + (2 * pi * r**2)
    vol = 1/3 * pi * r * r * T
    print(f"""\n{" Hasil ".center(40,"-")}
Kerucut dengan jari-jarinya adalah {r} dan 
sisi miringnya adalah {s}, maka :
Luas selimut     = {luas_s}
Luas permukaan   = {luas_p}
Volume           = {vol}""")

# Rumus Bola
# Luas = 4 x pi x r x r
# Volume = 4/3 x pi x r x r x r
def bola():
    print(" Bola ".center(40," "))
    print("-"*40)
    r = float(input("Masukan jari-jari : "))
    print(f"""\n{" Hasil ".center(40,"-")}
Kerucut dengan jari-jarinya adalah {r}, maka :
Luas     = {4*3.14*r**2}
Volume   = {4/3*3.14*r**3}""")

while True:
    laptop = input("Penting!!! \nOperasi sistem apa yang digunakan : \n[1] Windows \n[2] Linux/Mac \n::")
    if laptop=='1':
        laptop="cls"
        break
    elif laptop=='2':
        laptop="clear"
        break
    else:
        print("Harap Memasukan Pilihan Yang Benar")


while True:
    os.system(laptop)
    menu()
    opt = input("Pilih : ")
    if opt == '1' or opt == "Ruang Datar":
        while True:
            os.system(laptop)
            menu_rd()
            opt_1 = input("Pilih : ")
            os.system(laptop)
            if opt_1 == '1' or opt_1 == "Persegi":
                persegi()
            elif opt_1 == '2' or opt_1 == "Persegi Panjang":
                persegi_panjang()
            elif opt_1 == '3' or opt_1 == "Jajar Genjang":
                jajar_genjang()
            elif opt_1 == '4' or opt_1 == "Segitiga":
                segitiga()
            elif opt_1 == '5' or opt_1 == "Belah Ketupat":
                belah_ketupat()
            elif opt_1 == '6' or opt_1 == "Layang-Layang":
                layang_layang()
            elif opt_1 == '7' or opt_1 == "Trapesium":
                trapesium()
            elif opt_1 == '8' or opt_1 == "Lingkaran":
                lingkaran()
            elif opt_1 == '0' or opt_1 == "Back":
                os.system(laptop)
                while True:
                    os.system(laptop)
                    back = input("\nApakah anda yakin (y/n) : ")
                    if back == 'y' or back == 'n':break
                    else:print("ERROR")
                    input("")
                if back == 'y':break
                if back == 'n':continue
            else:
                print("ERROR - Harap masukan pilihan yang ada didalam daftar")
            input("")
    elif opt == '2' or opt == "Ruang Bangun":
        while True:
            os.system(laptop)
            menu_rb()
            opt_2 = input("Pilih : ")
            os.system(laptop)
            if opt_2 == '1' or opt_2 == "Kubus":
                kubus()
            elif opt_2 == '2' or opt_2 == "Balok":
                balok()
            elif opt_2 == '3' or opt_2 == "Prisma Segitiga":
                prisma_segitiga()
            elif opt_2 == '4' or opt_2 == "Limas Segiempat":
                limas_segiempat()
            elif opt_2 == '5' or opt_2 == "Limas Segitiga":
                limas_segitiga()
            elif opt_2 == '6' or opt_2 == "Tabung":
                tabung()
            elif opt_2 == '7' or opt_2 == "Kerucut":
                kerucut()
            elif opt_2 == '8' or opt_2 == "Bola":
                bola()
            elif opt_2 == '0' or opt_2 == "Back":
                os.system(laptop)
                while True:
                    os.system(laptop)
                    back = input("\nApakah anda yakin (y/n) : ")
                    if back == 'y' or back == 'n':break
                    else:print("ERROR")
                    input("")    
                if back == 'y':break
                if back == 'n':continue
            else:
                print("ERROR - Harap masukan pilihan yang ada didalam daftar")
            input("")
    elif opt == '0' or opt == "Exit":
        os.system(laptop)
        while True:
            os.system(laptop)
            back = input("\nApakah anda yakin (y/n) : ")
            if back == 'y' or back == 'n':break
            else:print("ERROR")
            input("")
        if back == 'y':
            os.system(laptop)
            print("-"*40)
            print(" Terima Kasih Banyak ".center(40," "))
            print("-"*40)
            input("")
            os.system(laptop)
            break
    else:
        os.system(laptop)
        print("ERROR - Harap masukan pilihan yang ada didalam daftar")
        input(" ")