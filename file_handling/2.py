with open("file_handling\data.txt","r") as data:
    nama = data.readline()
    print(nama)
    print(f"Apakah file sudah ditutup = {data.closed}")

print(f"Apakah file sudah ditutup = {data.closed}")