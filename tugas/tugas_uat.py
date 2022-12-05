# Soal esay dasar pemmrograman dasar
# Buatlah program sederhana dengan dilengkapi menu pilihan  untuk menghitung studi kasus berikut:
# a. Menghitung umur saat ini
# b. Menghitung sisa tahun cicilan
# c. Menghitung BMI berat badan
# d. Quit
# hint : Gunakan Statment Percabangan dan Looping
# Kirim link video (video tidak boleh sama, yang sama otomatis nilai 0 )

def hitung_umur():
    tahun_lahir = int(input("Masukan Tahun Lahir    (YYYY) : "))
    tahun_sekarang = int(input("Masukan Tahun Sekarang (YYYY) : "))
    hitung = tahun_sekarang - tahun_lahir
    print(f"""
{" Hasil ".center(40)}
{"-"*40}
Tahun Kamu Lahir adalah {tahun_lahir}
Tahun Sekarang adalah {tahun_sekarang}
{"-"*40}
Umur Kamu Sekarang Adalah {hitung}
""")

def sisa_cicilan():
    total_cicilan = int(input("Total Cicilan untuk berapa tahun       : "))
    cicilan_lunas = int(input("Cicilan yang sudah lunas berapa tahun  : "))
    hitung = total_cicilan - cicilan_lunas
    print(f"""
{" Hasil ".center(40)}
{"-"*40}
Kamu Memiliki Cicilan Untuk {total_cicilan} tahun dan
Kamu Telah Melunasi cicilan selama {cicilan_lunas} tahun
maka, Kamu memiliki sisa {hitung} tahun untuk membayar cicilan. 
""")

def bmi_bb():
    berat_badan = int(input("Masukan berat badan  (kg): "))
    tinggi_badan = int(input("Masukan tinggi badan (cm): "))
    bmi = berat_badan/((tinggi_badan / 100)**2)
    if bmi < 18.5:
        print("""
Kamu Sepertinya Kekurangan Berat Badan
Jangan Lupa Makan Yang Banyak Yah...
dan olahraga yang teratur biar kondisi badan 
Kamu membaik ^ ^
""")
    elif bmi >= 18.5 and bmi <= 24.5:
        print("""
Kamu memiliki kondisi badan yang normal
sepertinya Kamu rajin menjaga kesehatan 
Badan Kamu Yah... Jangan lupa untuk dipertahankan ^ ^   
""")
    elif bmi >= 25 and bmi <= 29.9:
        print("""
Kamu Punya Masalah nih, Kamu Kelebihan Berat badan
Suka Makan Boleh Tapi, Jangan Lupa Untuk Menjaga
Pola Makannya Juga Yah ... ^ ^
""")
    else:
        print("""
Wahh... Kamu Kegemukan / obesitas, Segeralah 
Pergi Ke Dokter dan Minta Obat Penurun Berat Badan
Agar Gak Ada Penyakit Yang Serius Yang Terjangkit 
Pada Kamu ... ^ ^
""")

while True:
    print(f"""{" Kalkulator Sederhana ".center(40)}
{" Dibuat Oleh Ahmad Rofiqi ".center(40)}
{"-"*40}
[1] Menghitung Umur Saat Ini
[2] Menghitung sisa tahun cicilan
[3] Menghitung BMI berat badan
[4] Quit""")
    opt = input("Pilih : ")
    print("")
    if opt == '1':hitung_umur()
    elif opt == '2':sisa_cicilan()
    elif opt == '3':bmi_bb()
    elif opt == '4':
        while True:
            quit = input("Apakah Kamu Yakin (y/n) : ")
            if quit == 'y' or quit == 'n':break
            else: print("ERROR : Harap Masukan Pilihan Yang Tersedia Dalam Daftar")
        if quit == 'y':
            print("-"*40)
            print(" Terima Kasih ".center(40))
            print("-"*40)
            break
    else:
        print("ERROR : Harap Masukan Pilihan Yang Tersedia Dalam Daftar")
    input("")
