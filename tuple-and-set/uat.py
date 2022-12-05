# Soal esay dasar pemmrograman dasar
# Buatlah program sederhana dengan dilengkapi menu pilihan  untuk menghitung studi kasus berikut:
# a. Menghitung umur saat ini
# b. Menghitung sisa tahun cicilan
# c. Menghitung BMI berat badan
# d. Quit
# hint : Gunakan Statment Percabangan dan Looping
# Kirim link video (video tidak boleh sama, yang sama otomatis nilai 0 )

while True:
    print(f"""{" Menu ".center(40,"-")}
[1] Menghitung umur saat ini
[2] Menghitung sisa tahun cicilan
[3] Menghitung BMI berat badan
[4] Quit""")
    opt = input("Pilih : ")
    if opt == "1":
        tahun_lahir = int(input("\nMasukan Tahun lahir kamu (YYYY): "))
        tahun_sekarang = int(input("Masukan Tahun Sekarang   (YYYY): "))
        print(f"""\n{" Hasil ".center(40,"-")}
Tahun Lahir Kamu : {tahun_lahir}
Tahun Sekarang   : {tahun_sekarang}
{"-"*40}
Umur Kamu sekarang yaitu {tahun_sekarang - tahun_lahir} Tahun\n""")
    elif opt == "2":
        cicilan = int(input("\nTotal cicilan untuk berapa tahun     : "))
        lunas = int(input("Cicilan yang lunas sudah berapa tahun : "))
        print(f"""\n{" Hasil ".center(40,"-")}
Anda mempunyai cicilan untuk {cicilan} tahun,
dan Anda sudah melunasi untuk {lunas} tahun. maka,
Anda mempunyai waktu {cicilan - lunas} tahun lagi untuk melunasinya.
Semangat Yah...\n""")
    elif opt == "3":
        berat_badan = int(input("\nMasukan Berat Badan Anda  : "))
        tinggi_badan = int(input("Masukan Tinggi Badan Anda : "))
        bmi = berat_badan/(tinggi_badan**2)
        print("")
        if bmi < 18.5:
            print("Sepertinya Anda Kekurangan Berat Badan")
            print("Jangan Lupa Makan Yang Banyak Yah ^^")
        elif bmi >= 18.5 and bmi < 24.5:
            print("Wah Berat Anda Normal")
            print("Sepertinnya Anda suka olahraga yah")
        elif bmi >= 25 and bmi < 29.9:
            print("Sepertinya Anda Kelebihan Berat Badan Nih...")
            print("Jangan lupa diet, olah raga dan tidur tepat waktu Yah...")
        else:
            print("Sepertinya Anda Kegemukan/obesitas")
            print("Anda sebaiknya periksakan diri ke dokter")
            print("supaya tidak ada penyakit yang serius")
        print("")
    elif opt == "4":
        while True:
            quit = input("\nApakah Anda Ingin Keluar (y/n) : ")
            if quit == 'y' or quit == 'n':break
            else:print("\nHarap masukan pilihan yang tepat")
        if quit == 'y':
            print("="*40)
            print("Terima Kasih".center(40))
            print("="*40)
            break