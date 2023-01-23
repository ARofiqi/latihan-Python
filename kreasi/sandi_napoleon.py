pesan = input("Masukan Kalimat : ")

def see_sandi(kalimat):
    x = list(filter(lambda x: x!=" ",kalimat))
    potongan_kata = []
    awal = 0
    akhir = 5
    total_huruf = (len(x)//5)+1
    for i in range(total_huruf):
        kata = x[awal:akhir]
        if i%2 != 0:kata.reverse()
        potongan_kata.append(kata)
        awal += 5
        akhir += 5
    hasil = ""
    for i in potongan_kata:
        hasil = hasil + "".join(i)+"\n"
    return hasil


sandi = see_sandi(pesan)
print(sandi)