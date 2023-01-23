with open("./kreasi/hitung_huruf/text.txt","r") as text:
    txt = text.read()

    y = [i for i in txt]
    y.sort()

    t = {}

    abj_min, abj_max = [],[]
    for i in y:
        if i == " ":
            t.update({"space":y.count(i)})
        else:
            t.update({i:y.count(i)})


    jml_abj = [t[i] for i in t]
    abj = [i for i in t]

    for i in t:
        print(i,":",t[i])
        if t[i] == 1:
            abj_min.append(i)
        if t[i] == max(jml_abj):
            abj_max.append(i)


    print("\n")
    print("  ".join(abj_min),":",min(jml_abj))
    print("  ".join(abj_max),":",max(jml_abj))