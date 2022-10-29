print("-"*20,"Kalkulator","-"*20)

num_1 = int(input("Masukan number pertama   : "))
operator = input("Pilih operator           : " )
num_2 = int(input("Masukan number kedua     : "))

print("- "*15)
if operator=='+':
    print(num_1," + ",num_2," = ",num_1+num_2)
elif operator=='-':
    print(num_1," - ",num_2," = ",num_1-num_2)
elif operator=='*':
    print(num_1," x ",num_2," = ",num_1*num_2)
elif operator=='/':
    print(num_1," / ",num_2," = ",num_1/num_2)
print("- "*15)