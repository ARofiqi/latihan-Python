# Tugas 10 - Buat To do list menggunakan list
activitys = []

def see_todo(list):
    print("\nTo do list : ")
    [print((index+1),":", item) for index,item in enumerate(list)]

while True:
    print(f"""
Aplikasi To do list sederhana :
[1] Lihat To do list
[2] Tambah kegiatan
[3] Hapus Kegiatan
[4] Keluar""")
    opt = input("Masukan Pilihan (ex : 1,2,3 or 4): ")
    if opt == '1':
        see_todo(activitys)
    elif opt == '2':
        see_todo(activitys)
        while True:    
            new_act = input("\nMasukan kegiatannya : ")
            activitys.append(new_act)
            see_todo(activitys)
            lagi = input("\nApakah mau tambah lagi (y/n): ")
            if lagi == 'n':break
    elif opt == '3':
        see_todo(activitys)
        while True:
            no = int(input("\nHapus list ke : "))
            no-=1
            activitys.pop(no)
            see_todo(activitys)
            lagi = input("\nApakah mau hapus lagi (y/n): ")
            if lagi == 'n':break
    elif opt == '4':
        lagi = input("\nApakah kamu yakin (y/n): ")
        if lagi == 'y':
            print("Terima Kasih")
            break
    else:
        print("\nERROR - Mohon masukan pilihan yang benar")