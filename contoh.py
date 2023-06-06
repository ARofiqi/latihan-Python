listData = []

no = [78,79,80]
nilai = [
    [76,76,76,76,76,80,80,76,80,80],
    [80,80,80,80,75,80,80,76,80,80],
    [80,82,78,85,78,76,80,80,80,80]
]

# tabel = {
#     78:[76,76,76,76,76,80,80,76,80,80],
#     79:[80,80,80,80,75,80,80,76,80,80],
#     80:[80,82,78,85,78,76,80,80,80,80],
# }

rata = [79, 79, 80, 78]
hasil = []

for i, d in enumerate(rata):
    if d in no:
        p = no.index(d)
        print(i," = ",d," = ",p)
        try:
            hasil.append(nilai[p])
        except:
            print("hehe")
            

print(hasil)
        


for a in hasil:
    for g in a:
        if(a.index(g) == a.length):
            print(f"{g}\t",end=" ")

try:
    with open('D:\\data.txt', 'w') as file:
            for a in hasil:
                for g in a:
                    file.write(f"{g}\t")
    with open('D:\\data.txt', 'r') as file:
        data = file.readlines
        print(data)
except:
    print("error")
