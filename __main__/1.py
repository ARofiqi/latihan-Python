# __main__ = Top level code enviroment

# __name__ == "__main__" akan terjadi jika ad di file program utama
# __name__ pada file program utama
print(f"nilai __name __ pada 1.py = {__name__}")

# __name__ pada program external
import fungsi

# contoh penggunaan __main__

# deklarasi
def tambah(x,y):
    return (x+y)

# fungsi utama 
if __name__ == "__main__":
    a = 5
    b = 2
    hasil = tambah(a,b)
    print(hasil)

# import package
import package