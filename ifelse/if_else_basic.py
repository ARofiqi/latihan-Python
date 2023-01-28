# if else statement
# if kondisi : aksi

print("="*10, " belajar if else ", "="*10)

nama = "rofiqi"
if nama == "rofiqi":
    print("hallo", nama)

# if and else

# if kondisi-true:
#   aksi-true
# else:
#   aksi-false

nama = "rofiqi"
if nama == "rofiqi":
    print("hallo", nama)
else:
    print("kamu siapa")

# elif = else if

number = int(input("masukan angka :"))
if number % 2 == 0:
    print("kamu memasukan angka genap")
elif number % 2 != 0:
    print("kamu memasukan angka ganjil")
else:
    print("harap masukan angka")