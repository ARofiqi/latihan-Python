with open("./kreasi/hitung_huruf/text.txt","r") as file:
    kalimat = file.read()

    list_huruf = list(map(lambda x: x,kalimat))
    list_huruf.sort()

    kumpulan_teks = {}

    abjad_mininal =  []
    abjad_maksimal = []
    
    for huruf in list_huruf:
        if huruf == " ":
            kumpulan_teks.update({"space":list_huruf.count(huruf)})
        else:
            kumpulan_teks.update({huruf:list_huruf.count(huruf)})


    jumlah_abjad = list(kumpulan_teks[i] for i in kumpulan_teks)

    for teks in kumpulan_teks:
        print(teks,":",kumpulan_teks[teks])
        if kumpulan_teks[teks] == 1:
            abjad_mininal.append(teks)
        if kumpulan_teks[teks] == max(jumlah_abjad):
            abjad_maksimal.append(teks)


    print("\n")
    print("  ".join(abjad_mininal),":",min(jumlah_abjad))
    print("  ".join(abjad_maksimal),":",max(jumlah_abjad))