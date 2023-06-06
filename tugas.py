# 1

# def faktorial(a): 
#     if a == 1: 
#         return (a) 
#     else: 
#         return (a*faktorial(a-1)) 

# bil = int(input("Masukan Bilangan : ")) 
# print("%d! = %d" % (bil, faktorial(bil)))


# 2

# def pangkat(x,y):
#    if y == 0:
#       return 1
#    else:
#       return x * pangkat(x,y-1)

# x = int(input("Masukan Nilai X : "))
# y = int(input("Masukan Nilai Y : "))

# print("%d dipangkatkan %d = %d" % (x,y,pangkat(x,y)))


# # 3

def fibonacci(n):
   if n == 0 or n == 1:
      return n
   else:
      return (fibonacci(n-1) + fibonacci(n-2))

x = int(input("Masukan Batas Deret Bilangan Fibonacci : "))
print("Deret Fibonacci")
for i in range(x):
   print(fibonacci(i),end=' ')
