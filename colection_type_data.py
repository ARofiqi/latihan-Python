print("-"*10,"Colection Type Data","-"*10)

# ======== list ========

# Kumpulan angka
# numbers = [1,2,3]

# Kumpulan string
# strings = ["ucup","otong","odah"]

# Kumpulan boolean
# bools = [True,False,True]

# kumpulan Campuran
# campurans = [1,"ucup",True]

# data range
# range(start,stop,step)
# data_range = range(0,10,2)
# data_list = list(data_range)

# membuat list dengan for, list comphrehensif
# list_for = [i for i in range(0,10)]
# list_for_kuadrat = [i**2 for i in range(0,10)]
# list_for_if = [i for i in range(0,10) if i != 5]
# list_genap = [i for i in range(0,10,2)] ## range(mulai,akhir,beda)

# ============ list mathod ============
# data = ["Ucup","Otong","Dudung"]

# mengambil data list pertama --> Ucup
# data_first_1 = data[0] # Index pertama dari depan
# data_first_2 = data[-3] # index terakhir dari belakang

# mengambil data list terakhir --> Dudung
# data_last = data[-1] # index pertama dari terakhir

# mengetahui total data 
# data_total = len(data)

# memanipulasi data list

# menambah item sesuai posisi --> list_name.insert(index_posisi,item)
# data.insert(2,"Ahmad")

# menambah di akhir list --> list_name.append(item)
# data.append("Dodi")

# menggabungkan list data_1 ke list data
# data_1 = ["Ujang","Usop","Dodi"]
# data.extend(data_1)

# merubah data list
# data[2] = "Dinda"

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