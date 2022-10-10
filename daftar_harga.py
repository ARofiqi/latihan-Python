menu = {
    "mie ayam":{
        "harga":2000,
        "diskon":50
    },
    "mie kocok":{
        "harga":8000,
        "diskon":60
    },
    "tahu pedas":{
        "harga":500,
        "diskon":0
    }
}

uang = 10000

def tampil_menu():
    print("-"*30)
    print("Daftar Harga Warung Makan aro")
    print("-"*30)
    for mak in menu:
        print("+",mak," harga : Rp."+str(menu[mak]["harga"])," diskon :",str(menu[mak]["diskon"])+"%")
    print("="*30)
    print("Uang :",uang)

def tambah_menu():
    new_nama = input("masukan nama menu barunya :")
    syarat = new_nama in menu
    if syarat==False:    
        new_harga = int(input("masukan harga :"))
        new_diskon = int(input("masukan diskon :"))
        menu.update({new_nama:{"harga":new_harga,"diskon":new_diskon}})
    else:
        print("Menu Sudah Ada")
    tampil_menu()

def hapus_menu():
    hapus = input("masukan menu yang akan dihapus :")
    syarat = hapus in menu
    if syarat==True:
        menu.pop(hapus)
    else:
        print("Menu Tidak Ada Didaftar/Sudah dihapus")
    tampil_menu()

def ubah_menu():
    opt_menu = input("Pilih menu yang akan diubah :")
    syarat = opt_menu in menu
    if syarat==True:
        print("Apa yang mau diubah :")
        print("[1] harga")
        print("[2] diskon")
        opt = int(input("pilih :"))
        if opt==1:
            menu[opt_menu]["harga"]=input("masukan harga baru :")
        elif opt==2:
            menu[opt_menu]["diskon"]=input("masukan harga baru :")
    else:
        print("Menu tidak ada")
    tampil_menu()

def pesan_menu():
    pesanan = int(input("Pilih Pesanan :"))
    syarat = pesanan in menu
    if syarat==True:
        jml_pesanan = int(input("Mau Berapa :"))
        print("Pesaa")

tampil_menu()