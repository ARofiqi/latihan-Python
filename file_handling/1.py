print("="*3," Membaca File External ","="*3)

data = open("file_handling\data.txt",mode="r")

print(f"status read : {data.readable()}")
print(f"status write : {data.writable()}")

# baca seluruh file
# print(data.read())

# baca per baris
# print(data.readline()) # baris 1
# print(data.readline()) # baris 2
# print(data.readline()) # baris 3

# Membaca file seluruh baris
# data_seluruh_baris = data.readlines()
# for i in data_seluruh_baris:
#     print(i,end=(""))

print(f"\napakah file sudah di close : {data.closed}")
data.close()
print(f"\napakah file sudah di close : {data.closed}")
