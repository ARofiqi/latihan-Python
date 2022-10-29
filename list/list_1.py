print("-"*10,"Colection Type Data","-"*10)

# ======== list ========
print("\n============ list ============")

# Kumpulan angka
numbers = [1,2,3]
print(f"list number \t {numbers}")

# Kumpulan string
strings = ["ucup","otong","odah"]
print(f"list string \t {strings}")

# Kumpulan boolean
bools = [True,False,True]
print(f"list boolean \t {bools}")

# kumpulan Campuran
campurans = [1,"ucup",True]
print(f"list campuran \t {campurans}")

# data range
# range(start,stop,step)
data_range = range(0,10,2)
print(f"Data range \t {data_range}")
data_list = list(data_range)
print(f"angka range tersebut ialah {data_list}")

# membuat list dengan for, list comphrehensif
list_for = [i for i in range(0,10)]
list_for_kuadrat = [i**2 for i in range(0,10)]
list_for_if = [i for i in range(0,10) if i != 5]
list_genap = [i for i in range(0,10,2)] # range(mulai,akhir,beda)
print(f"""\n============ membuat list dengan for ============
list for dengan range 0 - 10 \n {list_for}
list for kuadrat dengan range 0 - 10 \n {list_for_kuadrat}
list for dengan if \n {list_for_if}
list for dengan beda \n {list_genap}
""")

# ============ list mathod ============
print("=============== list mathod ===============")
# index  0(-3)   1(-2)    2(-1)
data = ["Ucup","Otong","Dudung"]

# mengambil data list pertama --> Ucup
data_first = data[0] # Index pertama dari depan
data_last = data[-1] # index terakhir dari belakang

print(f"""data \t {data}
mengambil data pertama   : {data_first}
mengambil data terakhir  : {data_last}""")

# mengetahui total data 
data_total = len(data)
print(f"jumlah item pada list data ialah : {data_total}")

# memanipulasi data list

# menambah item sesuai posisi --> list_name.insert(index_posisi,item)
print("\n============ memanipulasi data list ============")
print(f"data awal : {data}")
data.insert(2,"Ahmad")
print(f"[1] Menambah Ahmad pada index ke-2 : \n    {data}")

# menambah di akhir list --> list_name.append(item)
data.append("Dodi")
print(f"[2] Menambah Dodi pada index terakhir : \n    {data}")

# menggabungkan list data_1 ke list data
data_1 = ["Ujang","Usop","Dodi"]
print(f"[3] Menggabungkan list data : \n    {data} \n   , dengan list data_1 : {data_1}")
data.extend(data_1)
print(f"    Hasilnya : \n    {data}")

# merubah data list

data[2] = "Dinda"

# menghapus data list sesuai nama itemnya
# data.remove("Ucup")

# menghapus data list terakhir
# data.pop()
# data_yang_dihapus = data.pop()


# =========== Operasi List =========== 

# num = [2,3,4,5,3,2,5,4,6,2,6,8,7]

# count data number
# jml_data_5 = num.count(5) # out --> 2

# mengambil posisi data (index)
# data = ["Ucup","Otong","Dudung"]
# p_dudung = data.index("Dudung") # out --> 2

# mengurutkan list
# num.sort() # dari angka kecil ke besar
# data.sort() # dari a - z

# membalikan urutan list
# !!! ini akan bekerja jika kita sebelumnya sudah melakukan sort pada listnya
# num.reverse() # dari angka besar ke kecil
# data.reverse() # dari z - a

# 