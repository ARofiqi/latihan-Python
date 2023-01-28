nilai = 0
def ubah_angka(nilai_baru):
    global nilai # mendapat akses merubah variabel global
    nilai = nilai_baru
print(f"Nilai sebelum diubah : {nilai}" )
ubah_angka(20)
print(f"Nilai sesudah diubah : {nilai}" )

angka_lama = 0
def ubah_angka():
    angka_baru = 20
    return angka_baru

print(f"Angka Sebelum diubah : {angka_lama}")
angka_lama = ubah_angka()
print(f"Angka Sebelum diubah : {angka_lama}")

