# Latihan List
# Program daftar buku
data_buku = []

add = input("Tambah buku (y/n): ")
if add == 'y':add = True
if add == 'n':add = False
while add == True:
    judul = input("masukan judul buku : ")
    penulis = input("masukan penulisnya : ")
    buku = [judul,penulis]
    data_buku.append(buku)
    print(f"""\n========= list Buku =========""")
    [print(f"judul : {buku[0]} \npenulis : {buku[1]}\n") for buku in data_buku ]
    add = input("\nTambah buku lagi (y/n): ")
    if add == 'y':add = True