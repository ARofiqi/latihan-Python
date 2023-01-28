def get_sandi(massage):
    slice_word = []
    result = ""
    awal = 0
    akhir = 5

    huruf = list(filter(lambda x: x != " ", massage))
    panjang_total_huruf = (len(huruf) // 5) + 1

    for i in range(panjang_total_huruf):
        word = huruf[awal:akhir]
        if i % 2 != 0:
            word.reverse()
        slice_word.append(word)
        awal += 5
        akhir += 5

    for word in slice_word:
        result = result + "".join(word)+"\n"

    return result


pesan = input("Masukan Kalimat : ")
sandi = get_sandi(pesan)
print(sandi)
