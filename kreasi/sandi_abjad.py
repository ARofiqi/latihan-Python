pesan = input("Masukan Pesannya : ").upper()

abjad = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
balik = abjad.copy()
balik.reverse()
def see_sandi(text):
    def filter(x):
        if x == " ":
            return " "
        else:
            return balik[abjad.index(x)]
    
    t = list(map(filter,text))
    return ''.join(t)

sandi = see_sandi(pesan)
print(f"sandi saya = {sandi}")
