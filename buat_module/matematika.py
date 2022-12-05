def tambah(*value):
    hasil = 0
    for i in value:
        hasil += i
    return hasil

def kali(*value):
    hasil = 1
    for i in value:
        hasil *= i
    return hasil

def pangkat(n:int):
    return lambda angka:angka**n