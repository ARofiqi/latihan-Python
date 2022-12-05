import random

subjek = ["Aku", "Kamu", "Dia", "Saya", "Mereka"]
predikat = ["menyapu", "mengepel", "menjilat", "membeli", "merusak"]
object = ["rumah", "kantor", "sekolah", "mainan"]

kalimat = 4
[print(random.choice(subjek),random.choice(predikat),random.choice(object)) for n in range(kalimat)]