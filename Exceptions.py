# try:
#     x = int(input("Masukan x : "))
#     y = int(input("Masukan y : "))
#     print(x/y)
# except ZeroDivisionError:
#     print("Tidak Dapat Membagi dengan nilai 0")

# num = int(input("masukan angka : "))
# if num < 0:
#     raise ValueError("Angka yang dimasukan tidak boleh negatif")

try:
    x = 1/0
except:
    print("ERROR")
    raise