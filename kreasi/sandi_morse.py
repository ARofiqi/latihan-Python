pesan = input("Masukan Pesan : ").upper()

def see_pass():
    morse = {
        "A":".-",
        "B":"-...",
        "C":"-.-.",
        "D":"-..",
        "E":".",
        "F":"..-.",
        "G":"--.",
        "H":"....",
        "I":"..",
        "J":".---",
        "K":"-.-",
        "L":".-...",
        "M":"--",
        "N":"-.",
        "O":"---",
        "P":".--.",
        "Q":"--.-",
        "R":".-.",
        "S":"...",
        "T":"-",
        "U":"..-",
        "V":"...-",
        "W":".--",
        "X":"-..-",
        "Y":"-.--",
        "Z":"--..",
        " ":"/"
    }

    print("your pass : ",end=(""))
    for t in pesan:
        if t == " ":
            print("/",end=(""))
            continue
        print(morse[t],end=("/"))
    print("//")

see_pass()