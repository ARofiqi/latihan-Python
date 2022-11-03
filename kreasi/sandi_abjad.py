pesan = input("Masukan Pesannya : ").upper()

abjad = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
balik = abjad.copy()
balik.reverse()

def see_sandi(text):
    t = []
    print("your pass : ",end=(""))
    [t.append(i) for i in text]
    for i in t:
        if i == " ":
            print(" ",end=(""))
            continue
        print(balik[abjad.index(i)],end=(""))

see_sandi(pesan)