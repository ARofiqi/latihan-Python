from os import system

def pengubah_ke_int(x):
    try:
        return int(x)
    except:
        return x

while True:
    system("cls")
    hitung = input("Masukan Hitungan : ")
    operator = ["+","-","/","x"]
    potongan = list(filter(lambda x : x!=" ", hitung))

    for i in operator:
        if i in potongan:
            hitung_ubah = hitung.replace(i," "+i+" ")

    hitung_potongan = hitung_ubah.split(" ")
    hitung_list = list(map(lambda x : pengubah_ke_int(x), hitung_potongan))

    for i in hitung_list:
        if "" in hitung_list: 
            hitung_list.remove("")

    for i in hitung_list:
        print(i)
        match i:
            case "-":
                hasil = hitung_list[hitung_list.index(i)-1] - hitung_list[hitung_list.index(i)+1]
            case "+":
                hasil = hitung_list[hitung_list.index(i)-1] + hitung_list[hitung_list.index(i)+1]
            case "x":
                hasil = hitung_list[hitung_list.index(i)-1] * hitung_list[hitung_list.index(i)+1]
            case "/":
                hasil = hitung_list[hitung_list.index(i)-1] / hitung_list[hitung_list.index(i)+1]

    print("Hasil : " + str(hasil))

    isQuit = input("\nApakah Mau Lagi : ")
    if isQuit == "n" or isQuit == "N":break