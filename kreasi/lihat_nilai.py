daftar_nilai = {
    "Rofiqi":{"nilai":80},
    "Gunawan":{"nilai":90},
    "dosi":{"nilai":70},
    "kopjo":{"nilai":99},
    "adit":{"nilai":59}
}

def tampil_nilai():
    print("""======================================
            Daftar Nilai
======================================""")
    i=0
    for n in daftar_nilai:
        if daftar_nilai[n]["nilai"]>=90:
            daftar_nilai[n].update({"scor":"A"})
        elif daftar_nilai[n]["nilai"]>=70 and daftar_nilai[n]["nilai"]<90:
            daftar_nilai[n].update({"scor":"B"})
        elif daftar_nilai[n]["nilai"]>=60 and daftar_nilai[n]["nilai"]<70:
            daftar_nilai[n].update({"scor":"C"})
        elif daftar_nilai[n]["nilai"]>=50 and daftar_nilai[n]["nilai"]<60:
            daftar_nilai[n].update({"scor":"D"})
        elif daftar_nilai[n]["nilai"]<50:
            daftar_nilai[n].update({"scor":"E"})
        i+=1
        print(i,n," \t Nilai =",daftar_nilai[n]["nilai"]," \t score =",daftar_nilai[n]["scor"])

def add_nilai():
    new_name = input("Masukan nama siswa :")
    new_nilai = int(input("Masukan nilai siswa :"))
    daftar_nilai.update({new_name:{"nilai":new_nilai}})
    tampil_nilai()

tampil_nilai()