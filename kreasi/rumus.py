def rata_rata(list):
    result = 0
    for i in list:
        result += i
    result /= len(list)
    return result


nilai_matematika = [80, 77, 69, 70, 80, 97, 88, 56, 90, 95]
mean_nilai = rata_rata(nilai_matematika)
print(f"Nilai rata rata Matematika kelas 12 = {mean_nilai}")
