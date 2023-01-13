
# Variabel untuk menampung pesanan
pesanan = {}

# Variabel untuk menampung harga total dari pelanggan
harga_total = 0

# Variabel penampung data menu yang tersedia
menu = {
    "Jus Mangga":13000,
    "Jus Alpukat":14000,
    "Jus Jambu":15000,
    "Jus Jeruk":12000,
    "Jus Sirsak":10000
}

# Variabel untuk menampung list menu
menu_key = [i for i in menu]

# perulangan menu yang akan tampil di layar
while True:
    print("""Selamat Datang Di Warung ARO
Berikut Adalah Menu Dari Kami :""")

    # Perulangan Untuk menampilkan item menu dari variabel menu
    for index,m in enumerate(menu):
        print(f"[{index+1}] {m}\t\t:Rp.{menu[m]:,}")
    
    # Perulangan untuk melakukan pemesanan
    while True:
        try:
            # opt --> option pelanggan terhadap menu
            opt = int(input("\nPilih Menu     : "))
            # jml --> jumlah item yang di pesan
            jml = int(input("Jumlah Pesanan : "))

            # Pengkondisian dalam menentukan jumlah pesanan
            if menu_key[opt-1] in [i for i in pesanan]:
                pesanan[menu_key[opt-1]]+=jml
            else:
                pesanan.update({menu_key[opt-1]:jml})
            
            # menambahkan harga ke daftar pesanan
            harga = menu[menu_key[opt-1]] * jml
            harga_total += harga

            # Menampilkan pesanan yang baru dipesan
            print(f"\nAnda Memesan {jml} {menu_key[opt-1]} Rp.{harga:,}")

            quit = input("Pesan Lagi [y/n] : ")
            if quit == 'n': break
        except:
            print("Pesanan tidak ada")
            continue
    # Mengambil nilai uang dari pelanggan
    uang = int(input("\nMasukan Uang : "))

    # menuliskan nota ke layar menggunakan print yang berulang
    print("Nota Pemesanan : ")
    for i in pesanan:
        print(f"-{i}\tJumlah : {pesanan[i]}\tRp.{menu[i]:,} x {pesanan[i]}")
    print(f"""Uang        : Rp.{uang:,}
Harga Total : Rp.{harga_total:,}
Kembalian   : Rp.{uang-harga_total:,}""")

    # Menuliskan nota ke file nota.txt di folder tugas
    with open("./tugas/nota.txt","a") as nota:
        nota.write("\nNota Pemesanan : ")
        for i in pesanan:
            nota.write(f"\n-{i.ljust(15)} Jumlah : {pesanan[i]} \tRp.{menu[i]:,} x {pesanan[i]}")
        nota.write(f"""
Uang        : Rp.{uang:,}
Harga Total : Rp.{harga_total:,}
Kembalian   : Rp.{uang-harga_total:,}
""")
