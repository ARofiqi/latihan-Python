import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name
    match sistem_operasi:
        case "nt": os.system("cls")
        case "posix": os.system("clear")
    print("SELAMAT DATANG DI PERPUSTAKAAN ROFIQI")
    print("DATABASE PERPUSTAKAAN")
    print("========================================")

    CRUD.init_console()

    while True:
        match sistem_operasi:
            case "nt": os.system("cls")
            case "posix": os.system("clear")

        print("SELAMAT DATANG DI PERPUSTAKAAN ROFIQI")
        print("DATABASE PERPUSTAKAAN")
        print("========================================")
        print("1. Read Data")
        print("2. Create Data")
        print("3. Update Data")
        print("4. Delete Data\n")

        user_option = input("Masukan Opsi : ")

        print("\n========================================\n")

        match user_option:
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": CRUD.delete_console()

        print("\n========================================\n")

        is_done = input("Apakah Lanjut(y/n)?")
        if is_done == "y" or is_done == "Y":
            break
    print("Program Berakhir Terima kasih")
