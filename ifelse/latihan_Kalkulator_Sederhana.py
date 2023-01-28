print("================================")
print("      kalkulator sederhana      ")
print("================================")

x = float(input("masukan angka pertama : "))
y = float(input("masukan angka kedua   : "))

print("""Masukan operatornya 
[1] tambah
[2] kurang
[3] kali
[4] bagi""")
operator = input("pilih oparator : ")

if operator == '1':
    print(f"{x} + {y} = {x+y}")
elif operator == '2':
    print(f"{x} - {y} = {x-y}")
elif operator == '3':
    print(f"{x} x {y} = {x*y}")
elif operator == '4':
    print(f"{x} / {y} = {x/y}")
else:
    print("masukan yang benar")
