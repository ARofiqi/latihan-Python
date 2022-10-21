nama = input("Hallo, nama Kamu siapa : ")
nim = int(input("emm... kalau NIM Kamu berapa :"))
kelas = input("Kamu dari kelas apa : ")
jurusan = input("Wahhh... Kita satu kelas dong...\nBtw Kamu ngambil jurusan apa :")


print(f"""\n========= BiodataKu =========
Nama    : {nama}
NIM     : {nim}
Jurusan : {jurusan.lower()}
Kelas   : {kelas.upper()}


""")