print("""================================
      kalkulator sederhana      
================================""")

x = float(input("masukan angka pertama : "))
y = float(input("masukan angka kedua   : "))
operator = int(input("""masukan operatornya 
[1] tambah
[2] kurang
[3] kali
[4] bagi
pilih : """))

if operator==1:
    print(f"{x} + {y} = {x+y}")
elif operator==2:
    print(f"{x} - {y} = {x-y}")
elif operator==3:
    print(f"{x} x {y} = {x*y}")
elif operator==4:
    print(f"{x} / {y} = {x/y}")
else:
    print("masukan yang benar")