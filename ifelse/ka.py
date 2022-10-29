print("-"*20,"Kalkulator","-"*20)

num_1 = int(input("Masukan number pertama   : "))
operator = int(input("""Pilih operator : [1] Tambah
                 [2] Kurang
                 [3] Kali
                 [4] Bagi
pilih : """))
num_2 = int(input("Masukan number kedua     : "))

if operator==1:
    print(num_1," + ",num_2," = ",num_1+num_2)
elif operator==2:
    print(num_1," - ",num_2," = ",num_1-num_2)
elif operator==3:
    print(num_1," x ",num_2," = ",num_1*num_2)
elif operator==4:
    print(num_1," / ",num_2," = ",num_1/num_2)