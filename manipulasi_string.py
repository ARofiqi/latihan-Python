print("="*20)
print(" manipulasi string")
print("="*20)

say = "Selamat datang tuan apa kabarnya hari ini"
print("say       = "+say)

# upper()       ==> merubah string ke kapital  -A,B,C,...
say_1 = say.upper()
print("say 1 = "+say_1)

# lower()       ==> merubah srting ke normal   -a,b,c,...
say_2 = say.lower()
print("say 2 = "+say_2)

# isupper()     ==> pengecekan upper case pada string output=boolean
print("\nApakah say 1 upper case : {}".format(say_1.isupper()))
print("Apakah say 2 upper case : {}".format(say_2.isupper()))

# islower()     ==> pengecekan lower case pada string output=boolean
print("\nApakah say 1 lower case : {}".format(say_1.islower()))
print("Apakah say 2 lower case : {}".format(say_2.islower()))

# PENGECEKAN PADA STRING DENGAN BEBERAPA TUJUAN
nama = "Ahmad Rofiqi"
jurusan = "Informatika"
kelas = "TI22E"
ipk = "4"
quote = """Selalu bersyukur
dan selalu tenang
--aro"""

print("\nnama \t : {}\njurusan  : {}\nkelas \t : {}\nipk \t : {}\nquote \t : {}".format(nama,jurusan ,kelas, ipk, quote))

# isalpha()     ==> full abjad
print("\nMengecek jurusan dengan isalpha() \t : {}".format(jurusan.isalpha()))

# isalnum()     ==> abjad + number
print("Mengecek kelas dengan isalnum() \t : {}".format(kelas.isalnum()))

# isdescimal()  ==> number
print("Mengecek ipk dengan isdecimal() \t : {}".format(ipk.isdecimal()))

# isspace()     ==> spaci, tab, newline \n
print("Mengecek quote dengan isscpace() \t : {}".format(quote.isspace()))

# istitle()     ==> semua kata dimulai dengan huruf kapital
print("Mengecek nama dengan istitle() \t\t : {}\n".format(nama.istitle()))

# startswith() , endwith()  ==> mengecek komponen kata awal atau akhir dari string
print("Mengecek komponen quote dengan startswith() : {}".format(quote.startswith("Selalu")))
print("Mengecek komponen quote dengan endswith()   : {}\n".format(quote.endswith("--aro")))

# print("mengecek kata awal dari quote : {}".format(quote.startswith())

# join(), split()           ==> menggabungkan dan memisahkan string pada list
hobi = ["ngoding","nonton yt","main minecraft"]
print("hobi =",hobi)

hobi_1 = "-".join(hobi)
print("Menampilkan list hobi dengan join() : {}".format(hobi_1))
print("Menampilkan list hobi dengan split() : {}".format(hobi_1.split("-")))

# rjust(), ljust(), center()==> alokasi karakter
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(10)
print("'"+tengah+"'")

ngaran = "rofiqi".center(20,"-")
print("'"+ngaran+"'")

# strip()                   ==> kebalikan
ngaran = ngaran.strip("-")
print("'"+ngaran+"'")

























