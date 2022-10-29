# Tugas 6
name = input("Masukan nama : ")
skor = int(input("Masukan Skor (0-100) : "))
if (skor >= 90 and skor <= 100):
    nilai = "A"
    predikat = "Dengan Pujian"
elif (skor >= 80 and skor < 90):
    nilai = "B"
    predikat = "Sangat Memuaskan"
elif (skor >= 70 and skor < 80):
    nilai = "C"
    predikat = "Memuaskan"
elif (skor >= 60 and skor < 70):
    nilai = "D"
    predikat = "Tidak Memuaskan"
elif (skor >= 0 and skor < 60):
    nilai = "E"
    predikat = "Tidak Lulus"
else:
    print("Harap Masukan skor dari 0 - 100")
    nilai = "none"
    predikat = "none"

print(f"""\n============== Nilai ==============
nama     = {name}
nilai    = {nilai}
predikat = {predikat}
""")