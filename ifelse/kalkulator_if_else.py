print("-"*20 + " Kalkulator " + "-"*20)

number_1 = int(input("Masukan number pertama   : "))
operator = int(input("""Pilih operator : [1] Tambah
                 [2] Kurang
                 [3] Kali
                 [4] Bagi
pilih : """))
number_2 = int(input("Masukan number kedua     : "))

match operator:
    case 1:print(number_1, " + ", number_2, " = ", number_1+number_2)
    case 2:print(number_1, " - ", number_2, " = ", number_1-number_2)
    case 3:print(number_1, " x ", number_2, " = ", number_1*number_2)
    case 4:print(number_1, " / ", number_2, " = ", number_1/number_2)

# if operator == 1:
#     print(number_1, " + ", number_2, " = ", number_1+number_2)
# elif operator == 2:
#     print(number_1, " - ", number_2, " = ", number_1-number_2)
# elif operator == 3:
#     print(number_1, " x ", number_2, " = ", number_1*number_2)
# elif operator == 4:
#     print(number_1, " / ", number_2, " = ", number_1/number_2)
