def rata_rata():
    num = input("Masukan angka : ")
    hasil = 0
    r = []
    for i in num:
        if i == " ":continue
        hasil += int(i)
        r.append(int(i))
    num.replace(" ","")
    print(hasil//len(r))

rata_rata()