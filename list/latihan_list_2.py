# membuat matrix

x_2x2 = [[8,6],[4,2]]
print("========= matriks 2x2 =========")
[print(f"|{i[0]}  {i[1]}|") for i in x_2x2]
print("  +")

y_2x2 = [[4,6],[9,1]]
[print(f"|{i[0]}  {i[1]}|") for i in y_2x2]

print("  =")

# a = x_2x2[0][0] + y_2x2[0][0]
# b = x_2x2[0][1] + y_2x2[0][1]
# c = x_2x2[1][0] + y_2x2[1][0]
# d = x_2x2[1][1] + y_2x2[1][1]
# hasil = [[a,b],[c,d]]
# [print(f"|{i[0]}  {i[1]}|") for i in hasil]

row_1 = []
row_2 = []
hasil = [row_1,row_2]

for i in range(2):
    row_1.append(x_2x2[i] + y_2x2[i])

print(hasil)
# a = 2
# b = 4
# c = 4
# d = 2
# e = 5
# f = 8
# g = 9
# h = 8
# matriks_3x3 = [[a,b,c],[c,d,e],[f,g,h]]
# print("\n========= matriks 3x3 =========")
# [print(f"|{i[0]}  {i[1]}  {i[2]}|") for i in matriks_3x3]

i = 0

x = 0

while i < 4:

    x+=i

    i+=1

print(x)

