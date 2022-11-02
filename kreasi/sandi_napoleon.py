kalimat = "Tolong Aku Disekap dadiracun"

box = []
for i in kalimat:
    if i == ' ':continue
    box.append(i)


w = len(box)
# k = 0
# print("w =",w)
# # for i in range(w):
# #     if i**2 == w:
# #         k = i**2
# #         break
# #     elif i**2 < w:
# #         w -= 1
# #     else:
# #         w += 1
# i = 0
# while True:
#     if i**2 == w:
#         k = i**2
#         break
#     elif i**2 < w:
#         w -= 1
#     else:
#         w += 1
#     i += 1

# print("K =",k)

for i in range(w):
    if (i + 1)**2 == w:
        lebar = i + 1

hasil = []
l = int(len(box)/lebar)

for i in range(l):
    sub_box = []
    x = l*i
    y = l*(i+1)
    for i in range(x,y):
        sub_box.append(box[i])
    hasil.append(sub_box)

for index,i in enumerate(hasil):
    if index % 2 != 0: i.reverse()

for i in hasil:
    for j in i:
        print(j,end=(''))
    print(" ",end=(""))