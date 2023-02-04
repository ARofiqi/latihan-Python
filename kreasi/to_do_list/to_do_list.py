from os import system

list_todo = []


def write_todo(text):
    list_todo.append(text)


def remove_todo(no):
    list_todo.pop(no)


def see_todo(list):
    print("To do list :")
    for index, item in enumerate(list):
        print(f"{index+1}. {item}")


def menu():
    print("Aplikasi To Do list Sederhana ")
    print("---------------------------------")
    print("1. Buat Baru")
    print("0. Keluar")


def buat():
    system("cls")
    nama_file = input("Masukan Nama file : ")
    deskripsi_file = input("Masukan Deskripsi Todo List : ")

    while True:
        system("cls")
        print("Membuat File To Do List Baru")
        print("---------------------------------")
        print(f"Nama File      : {nama_file}")
        print(f"Deskripsi File : {deskripsi_file}")
        see_todo(list_todo)
        todo = input("\nMasukan list : ")
        if todo == "":
            continue
        else:
            write_todo(todo)
            isQuit = input("\nMau lagi (y/n) : ")
            if isQuit == 'n' or isQuit == "N":
                break
    try:
        with open(f"./kreasi/to_do_list/{nama_file}.txt", "a") as file:
            file.writelines(deskripsi_file.upper().center(50, "-"))
            for list in list_todo:
                file.write(f"\n+ {list}")
            system("cls")
            input("File berhasil Dibuat Terima Kasih")
    except:
        input("file tidak dapat dibuat")


while True:
    system("cls")

    print("Aplikasi To Do list Sederhana ")
    print("---------------------------------")
    print("1. Buat Baru")
    print("0. Keluar")

    user_option = input("\nPilih : ")

    match user_option:
        case "1": buat()
        case "0": break
