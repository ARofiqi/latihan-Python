pesanan = {}
harga_total = 0

menu = {
    "Jus Mangga":13000,
    "Jus Alpukat":14000,
    "Jus Jambu":15000,
    "Jus Jeruk":12000,
    "Jus Sirsak":10000
}

menu_key = [i for i in menu]

while True:
    print("""Selamat Datang Di Warung ARO
Berikut Adalah Menu Dari Kami :""")

    for index,m in enumerate(menu):
        print(f"[{index+1}] {m}\t\t:Rp.{menu[m]:,}")
    while True:
        try:
            opt = int(input("\nPilih Menu     : "))
            jml = int(input("Jumlah Pesanan : "))

            if menu_key[opt-1] in [i for i in pesanan]:
                pesanan[menu_key[opt-1]]+=jml
            else:
                pesanan.update({menu_key[opt-1]:jml})
            
            harga = menu[menu_key[opt-1]] * jml
            harga_total += harga
            print(f"\nAnda Memesan {jml} {menu_key[opt-1]} Rp.{harga:,}")
            # print(pesanan)

            quit = input("Pesan Lagi [y/n] : ")
            if quit == 'n': break
        except:
            print("Pesanan tidak ada")
            continue
    uang = int(input("\nMasukan Uang : "))

    print("Nota Pemesanan : ")
    for i in pesanan:
        print(f"-{i}\tJumlah : {pesanan[i]}\tRp.{menu[i]:,} x {pesanan[i]}")
   
    print(f"""Uang        : Rp.{uang:,}
Harga Total : Rp.{harga_total:,}
Kembalian   : Rp.{uang-harga_total:,}""")

    with open("./tugas/nota.txt","a") as nota:
        nota.write("\nNota Pemesanan : ")
        for i in pesanan:
            nota.write(f"\n-{i.ljust(15)} Jumlah : {pesanan[i]} \tRp.{menu[i]:,} x {pesanan[i]}")
        nota.write(f"""
Uang        : Rp.{uang:,}
Harga Total : Rp.{harga_total:,}
Kembalian   : Rp.{uang-harga_total:,}
""")

    input("")
    