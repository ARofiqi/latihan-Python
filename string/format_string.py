print("="*10,"format string","="*10)

# string
hurup = "Ahmad Rofiqi"
format_str = f"Hallo, {hurup}"
print(format_str)

# number
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"Bilangan bulat : {angka}"
print(format_str)

# bilangan ribuan dengan ordo ribuan
angka = 1000000000
format_str = f"Bilangan ribuan : {angka:,}"
print(format_str)

# bilangan decimal
angka = 2005.58374234
format_str = f"Bilangan decimal : {angka:.2f}"
print(format_str)

# leading zero
angka = 1534.3412423
format_str = f"Bilangan decimal : {angka:09.3f}"
print(format_str)

# tanda plus minus
angka_plus = 15
angka_minus = -15
format_str_plus = f"Bilangan bulat : {angka_plus:+d}"
format_str_min = f"Bilangan bulat : {angka_minus:+d}"
print(format_str_plus)
print(format_str_min)

# formating persen
persen = 0.32
format_persen = f"persen = {persen:.2%}"
print(format_persen)

# melakukan operasi aritmatika didalam placeholder
harga = 20000
jml = 3

format_str = f"harga total = Rp{harga*jml:,}"
print(format_str)

# format angka lain(binary, oktal, hexadecimal)
angka = 255

format_binary = f"binary = {bin(angka)}"
format_oktal = f"oktal = {oct(angka)}"
format_hexa = f"hexa = {hex(angka)}"

print(format_binary)
print(format_oktal)
print(format_hexa)





















