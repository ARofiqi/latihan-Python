def rata_rata1(*nilai):
    hasil = 0
    for i in list(nilai):
        hasil += i
    hasil /= len(nilai)
    return hasil

mean = rata_rata1(20,30,40,50,20,20,30,40)
print(f"Nilai rata rata Matematika kelas 12 = {mean}")
