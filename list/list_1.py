print(" Colection Type Data ".center(50,"="))

# ======== list ========
# Kumpulan angka
numbers = [1,2,3]

# Kumpulan string
strings = ["ucup","otong","odah"]

# Kumpulan boolean
bools = [True,False,True]

# kumpulan Campuran
campurans = [1,"ucup",True]

print(f"""
{" list ".center(40,"=")}
list number       {numbers}
list string       {strings}
list boolean      {bools}
list campuran     {campurans}""")

# data range
# range(start,stop,step)
data_range = range(0,10,2)
data_list = list(data_range)
print(f"""
Data range                  {data_range}
angka range tersebut ialah  {data_list}""")

# membuat list dengan for, list comphrehensif
list_for = [i for i in range(0,10)]
list_for_kuadrat = [i**2 for i in range(0,10)]
list_for_if = [i for i in range(0,10) if i != 5]
list_genap = [i for i in range(0,10,2)] # range(mulai,akhir,beda)

print(f"""
{" membuat list dengan for ".center(40,"=")}
for         {list_for}
for kuadrat {list_for_kuadrat}
for not 5   {list_for_if}
for & beda  {list_genap}""")

# ============ list mathod ============
# index  0(-3)   1(-2)    2(-1)
data = ["Ucup","Otong","Dudung"]

# mengambil data list pertama --> Ucup
data_first = data[0] # Index pertama dari depan
data_last = data[-1] # index terakhir dari belakang

# mengetahui total data 
data_total = len(data)

print(f"""
{" list method ".center(40,"=")}
data             : {data}
get data first   : {data_first}
get data last    : {data_last}
lenght data      : {data_total}""")

# memanipulasi data list
data = ["Ucup","Otong","Dudung"]
data_1 = ["Ujang","Usop","Dodi"]

# [1] menambah item sesuai posisi --> list_name.insert(index_posisi,item)
data.insert(2,"Ahmad")
# [2] menambah di akhir list --> list_name.append(item)
data.append("Dodi")
# [3] menggabungkan list data_1 ke list data
data.extend(data_1)


# merubah data list

data[2] = "Dinda"

# menghapus data list sesuai nama itemnya
data.remove("Ucup")

# menghapus data list terakhir
data.pop()
data_yang_dihapus = data.pop()


# =========== Operasi List =========== 

num = [2,3,4,5,3,2,5,4,6,2,6,8,7]

# count data number
jml_data_5 = num.count(5) # out --> 2

# mengambil posisi data (index)
data = ["Ucup","Otong","Dudung"]
p_dudung = data.index("Dudung") # out --> 2

# mengurutkan list
num.sort() # dari angka kecil ke besar
data.sort() # dari a - z

# membalikan urutan list
# !!! ini akan bekerja jika kita sebelumnya sudah melakukan sort pada listnya
num.reverse() # dari angka besar ke kecil
data.reverse() # dari z - a