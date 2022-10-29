# ======== teknik menduplikat list / references list ========

a = ["ucup","otong","dudung"]

# List b akan dibuat dan list b memiliki address yang sama
# jika item di list b diubah maka list a juga akan berubah juga
# address = 0x14cba372a80
b = a
# print(f"address a = {hex(id(a))}")
# print(f"address b = {hex(id(b))}")

# menduplikat list dengan copy
# list c akan dibuat dengan address yang berbeda
# jika item di list c diubah maka list a tidak akan berubah
c = a.copy()
# print(f"address a = {hex(id(a))}") # 0x15a7f6d2a80
# print(f"address c = {hex(id(c))}") # 0x15a7f6c73c0 

# ============== nested list / list bersarang ==============
data_1 = [1,2]
data_2 = [3,5]

list_2d = [data_1,data_2]
# output --> [[1, 2], [3, 5]]
# print(list_2d)

# dengan reference
# jika kita mengubah isi data_1/data_2 maka tidak akan mengubah item di list_copy
list_copy = list_2d.copy()

# mengambil data di nested list
num = list_2d[0] # out --> [1,2]
num_1 = list_2d[0][1] # out --> 2

# ============  copy for nesting list ============ 

# list_2d_copy akan dibuat dan menghasilkan isi list yang sama persis dengan list_2d dengan address yang beda pula
list_2d_copy = list_2d.copy()
# print(f"address list_2d = {hex(id(list_2d))}") 
# out --> 0x23d6706cd00
# print(f"address list_2d_copy = {hex(id(list_2d_copy))}")
# out --> 0x23d6706cf00

# tetapi jika item list yang dicopy merupakan type list maka yang dicopy hanya addressnya
# print(f"address data_1 asli = {hex(id(list_2d[0]))}")
# print(f"address data_1 copy = {hex(id(list_2d_copy[0]))}")
# dengan hanya mengcopy addressnya maka jika kita mengubah list aslinya maka list copy-an nya juga akan berubah

# print(f"list_2d      = {list_2d}")
# print(f"list_2d_copy = {list_2d_copy}")
list_2d[0][0] = 4 # mengubah list_2d asli angka 1 dengan 4
# print(f"list_2d      = {list_2d}")
# print(f"list_2d_copy = {list_2d_copy}")
# kita mengubah list yang asli tetapi list copy-an nya juga ikut berubah
# jika kita menggunakan copy() untuk list nested maka item yang merupakan type list tidak benar benar tercopy hanya addressnya saja yang tercopy
# solusinya ialah menggunakan deepcopy()
from copy import deepcopy
list_2d = [data_1,data_2]
list_2d_deepcopy = deepcopy(list_2d)

# print(f"list_2d          = {list_2d}")
# print(f"list_2d_deepcopy = {list_2d_deepcopy}")
# # addressnya listnya akan berbeda
# print(f"address list_2d          = {hex(id(list_2d))}")
# print(f"address list_2d_deepcopy = {hex(id(list_2d_deepcopy))}")
# # dan address item list nya juga akan berbeda
# print(f"address list_2d          = {hex(id(list_2d[0]))}")
# print(f"address list_2d_deepcopy = {hex(id(list_2d_deepcopy[0]))}")

# kita coba ubah item nya
print("list awal")
print(f"list_2d          = {list_2d}")
print(f"list_2d_deepcopy = {list_2d_deepcopy}")

list_2d_deepcopy[0][0] = 9 # merubah item 1 di list_2d_deepcopy menjadi 9
print("list akhir")
print(f"list_2d          = {list_2d}")
print(f"list_2d_deepcopy = {list_2d_deepcopy}")