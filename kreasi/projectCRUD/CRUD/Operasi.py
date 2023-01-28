import random
import string
import time
from . import Database
from . import utility


def create_first_data():
    penulis = input("Penulis : ")
    judul = input("Judul : ")
    while (True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun Harus Angka, silahkan masukan tahun lagi(yyyy)")
        except:
            print("Tahun Harus Angka, silahkan masukan tahun lagi(yyyy)")

    data = Database.TEMPLATE.copy()

    data["pk"] = utility.random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    try:
        with open(f"kreasi\projectCRUD\{Database.DB_NAME}", "w") as file:
            file.write(data_str)
    except:
        print("error")


def read(**kwargs):

    try:
        with open(f"kreasi\projectCRUD\{Database.DB_NAME}","r") as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return content[index_buku]
            else:
                return content
    except:
        print("ERROR")
        return False

def create(tahun,judul,penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = utility.random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    try:
        with open(f"kreasi\projectCRUD\{Database.DB_NAME}", "a") as file:
            file.write(data_str)
        print("Data Berhasil Ditambahkan")
    except:
        print("data tidak dapat ditambahkan")

def update(no_buku,pk,date_add,tahun,judul,penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = date_add
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}'
    data_len = len(data_str)

    try:
        with open(f"kreasi\projectCRUD\{Database.DB_NAME}","r+") as file:
            file.seek(data_len*(no_buku-1))
            file.write(data_str)
    except:
        print("Error dalam update data")

def delete(no_buku):
    try:
        with open(f"kreasi\projectCRUD\{Database.DB_NAME}","r") as file:
            data = file.readlines()
            with open(f"kreasi\projectCRUD\{Database.DB_NAME}","w") as file:
                for index,i in enumerate(data):
                    if index == (no_buku-1):
                        continue
                    else:
                        file.write(i)
    except:
        print("Error dalam menghapus database")