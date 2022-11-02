pesan = input("Masukan Kalimat : ").upper()
l = int(input("Mau berapa hurup per kata : "))

def r_space(kalimat):
    return kalimat.replace(" ","")

def potong(text):
    hasil = []
    w = []
    lebar = l
    for i,t in enumerate(text):
        if i % lebar == 0 and i != 0:
            hasil.append(w)
            w = []
        w.append(t)
    hasil.append(w)
    return hasil

def see_sandi():
    y = potong(r_space(pesan))
    print("Sandinya adalah ",end=(""))
    for index,item in enumerate(y):
        if index % 2 == 0:
            [print(j,end=("")) for j in item]
        else:
            item.reverse()
            [print(j,end=("")) for j in item]
        print(" ",end=(""))
                
see_sandi()