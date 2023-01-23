from os import system

list_todo = []

def write_todo(text):
    list_todo.append(text)

def remove_todo(no):
    list_todo.pop(no)

def see_todo(list):
    print(' To do list : ')
    [print(f"{index+1}. {i}") for index,i in enumerate(list)]
    print('')

def menu():
    print(f"""===============================
 Aplikasi To Do list Sederhana 
===============================
[1] Buat To Do List Baru
[0] Exit
""")

while True:
    system("cls")
    menu()
    opt = input("Pilih : ")
    if opt == '1':
        nama_file = input("Masukan nama file : ")
        judul = input("Masukan Judul Todo List : ")
        while True:
            system("cls")
            menu()
            todo = input("Masukan Todo list : ")
            if todo=="":continue
            else:
                write_todo(todo)
                see_todo(list_todo)
                quit = input("Mau lagi (y/n) : ")
                if quit == 'n': break
        try:
            with open(f"./kreasi/to_do_list/{nama_file}.txt","a") as td:
                td.writelines(judul.upper().center(50,"-"))
                for i in list_todo:
                    td.write(f"\n+ {i}")
                system("cls")
                input("File berhasil Dibuat Terima Kasih")
        except:
            input("file tidak dapat dibuat")
    if opt == '0':
        break