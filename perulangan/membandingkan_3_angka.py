print("""=========================
    Bandinkan 3 angka
=========================""")

lagi = True
while lagi:
    angka = []
    angka.append(input("masukan angka pertama :"))
    angka.append(input("masukan angka kedua   :"))
    angka.append(input("masukan angka ketiga  :"))
    
    print("+"*10)
    
    print(angka.sort())
    
    print("+"*10)
    
    ulang = input("lagi(y/n) :")
    if ulang=="n":
        lagi=False
        print("="*5,"Terima Kasih","="*5)
