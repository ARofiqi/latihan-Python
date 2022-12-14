# Berat badan normal= tinggi badan – 100 
# Wanita: Berat badan ideal= (tinggi badan-100)-((tinggi badan-100) x 15%)
# Pria: Berat badan ideal= (tinggi badan-100)-((tinggi badan-100) x 10%)

def bb_normal(tinggi_badan=0):
    return (tinggi_badan - 100)

def bb_p_ideal(tinggi_badan=0):
    return ((tinggi_badan - 100)-((tinggi_badan - 100)*(15/100)))

def bb_l_ideal(tinggi_badan=0):
    return ((tinggi_badan - 100)-((tinggi_badan - 100)*(10/100)))

while True:
    print("""
Aplikasi penghitung berat badan    
[1] Berat Badan Normal
[2] Berat Badan Ideal Untuk Laki Laki
[3] Berat Badan Ideal Untuk Perempuan
[4] Keluar""")
    opt = input("Pilih : ")
    if opt == '1':
        tb = int(input("\nMasukan Tinggi Badan (cm): "))
        hasil = bb_normal(tb)
        print(f"Berat badan normal kamu ialah {hasil} kg")
    elif opt == '2':
        tb = int(input("\nMasukan Tinggi Badan (cm): "))
        hasil = bb_l_ideal(tb)
        print(f"Berat badan ideal kamu ialah {hasil} kg")
    elif opt == '3':
        tb = int(input("\nMasukan Tinggi Badan (cm): "))
        hasil = bb_p_ideal(tb)
        print(f"Berat badan ideal kamu ialah {hasil} kg")
    elif opt == '4':
        quit = input("\nApakah Kamu Yakin (y/n): ")
        if quit == 'y':break
        