print("""=========================
    Bandinkan 2 angka
=========================""")

lagi = True
while lagi:
    x = int(input("masukan angka pertama :"))
    y = int(input("masukan angka kedua   :"))
    
    print("+"*10)
    if x>y:
        print(x,">",y)
    elif x<y:
        print(x,"<",y)
    else:
        print(x,"=",y)
    print("+"*10)
    
    ulang = input("lagi(y/n) :")
    if ulang=="n":
        lagi=False
        print("="*5,"Terima Kasih","="*5)