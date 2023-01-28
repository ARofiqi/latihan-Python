daftar_nilai = {
    "Rofiqi": {"nilai": 80},
    "Gunawan": {"nilai": 90},
    "dosi": {"nilai": 70},
    "kopjo": {"nilai": 99},
    "adit": {"nilai": 59}
}

def tampil_nilai():
    i = 0
    for n in daftar_nilai:
        nama = daftar_nilai[n]
        nilai = nama["nilai"]

        if nilai >= 90:
            nama.update({"scor": "A"})
        elif nilai >= 70 and nilai < 90:
            nama.update({"scor": "B"})
        elif nilai >= 60 and nilai < 70:
            nama.update({"scor": "C"})
        elif nilai >= 50 and nilai < 60:
            nama.update({"scor": "D"})
        elif nilai < 50:
            nama.update({"scor": "E"})
        
        i += 1
        print(i, n, " \t Nilai =",nilai, " \t score =", nama["scor"])


def add_nilai():
    new_name = input("Masukan nama siswa :")
    new_nilai = int(input("Masukan nilai siswa :"))
    daftar_nilai.update({new_name: {"nilai": new_nilai}})
    tampil_nilai()


print("======================================")
print("            Daftar Nilai              ")
print("======================================")

tampil_nilai()
