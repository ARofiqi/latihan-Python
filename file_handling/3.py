# 1. mode write akan mereset isi file ketika dibuka dan dapat menuliskan ulang filenya
with open(r"file_handling\3.txt", "w") as file:
    file.write("Mode Write 1\n")

with open(r"file_handling\3.txt", "w") as file:
    pass

# 2. mode append akan menambahkan isi file dan tidak mereset isi file sebelumnya
with open(r"file_handling\3.txt", "a") as file:
    file.write("Mode append \n")

with open(r"file_handling\3.txt", "a") as file:
    file.write("Mode append1\n")
    file.write("Mode append2\n")
    file.write("Mode append3\n")
    file.write("Mode append4\n")


# 3. mode read+ : gabungan antara mode write (mode write disini akan menimpa tulisan yang sudah ada sesuai dengan panjang data) sama mode read
with open(r"file_handling\3.txt", "r+") as file:
    file.write("Mode read + line 1\n")
    file.write("Mode read + line 2")
