from . import Operasi

DB_NAME = "data.txt"
TEMPLATE = {
    "pk": "XXXXXX",
    "date_add": "yyyy-mm-dd",
    "judul": 255*" ",
    "penulis": 255*" ",
    "tahun": "yyyy"
}


def init_console():
    try:
        with open(f"kreasi\projectCRUD\{DB_NAME}", "r") as file:
            print(file.readable())
    except:
        print("Database tidak ditemukan")
        Operasi.create_first_data()
