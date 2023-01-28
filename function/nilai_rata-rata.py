print("""
=========================
    Nilai Rata Rata
=========================""")

def hitung_rata_rata():
    value = 0
    for n in nilai:
        value+=n
    print(nilai)
    print("rata rata :",value/len(nilai))


nilai = [2,3,4,5,6,7]
hitung_rata_rata()