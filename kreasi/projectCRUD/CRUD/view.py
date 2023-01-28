from . import Operasi


def read_console():
    data_file = Operasi.read()

    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # Header
    print("="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)

    # Data
    for index, data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{(index+1):4} | {judul:.40} | {penulis:.40} | {tahun:5}", end="")

    # Footer
    print("\n", "="*100)


def create_console():
    print("="*100)
    print("Silahkan tambah data buku")
    penulis = input("Penulis\t: ")
    judul = input("Judul\t: ")
    while (True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun Harus Angka, silahkan masukan tahun lagi(yyyy)")
        except:
            print("Tahun Harus Angka, silahkan masukan tahun lagi(yyyy)")

    Operasi.create(tahun, judul, penulis)
    read_console()


def update_console():
    read_console()
    while (True):
        print("Silahkan Pilih nomor buku yang akan di update")
        no_buku = int(input("Nomor Buku : "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            break
        else:
            print("Nomor tidak valid")
    data_break = data_buku.split(",")
    pk = data_break[0]
    date_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    while (True):
        print("\n", "="*100)
        print("Silahkan Pilih Data yang akan diubah")
        print(f"1. Judul\t:{judul:.40}")
        print(f"2. Penulis\t:{penulis:.40}")
        print(f"3. Tahun\t:{tahun:4}")
        print(f"0. Selesai")

        user_option = input("Pilih Opsi :")
        match user_option:
            case "0": break
            case "1": judul = input("Judul\t: ")
            case "2": penulis = input("Penulis\t: ")
            case "3":
                while (True):
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print(
                                "Tahun Harus Angka, silahkan masukan tahun lagi(yyyy)")
                    except:
                        print("Tahun Harus Angka, silahkan masukan tahun lagi(yyyy)")
            case _: print("Index Tidak Cocok")

        Operasi.update(no_buku, pk, date_add, tahun, judul, penulis)
        print("\n", "="*100)

def delete_console():
    read_console()
    while (True):
        print("Silahkan Pilih nomor buku yang akan di delete")
        no_buku = int(input("Nomor Buku : "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            is_done = input("Apakah Yakin akan dihapus(y/n)?")
            if is_done == "y" or is_done == "Y":
                Operasi.delete(no_buku)
                break
        else:
            print("Nomor tidak valid")
    print("data berhasil dihapus")
            
