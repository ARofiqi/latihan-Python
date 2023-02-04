import random as r

def get_pass(jumlah_huruf):
    ABJAD = "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"
    SIMBOL = "@#$%^&*()-+|\{>}?<.,-_]`;:"
    NUMBER = "1234567890"

    huruf = (ABJAD * 3) + (SIMBOL) + (NUMBER)
    new_pass = list(r.choice(huruf) for i in range(jumlah_huruf))
    hasil = "".join(new_pass)

    return hasil

while True:
    sandi = get_pass(20)
    print("Sandi : " + sandi)
    is_exit = input("\nLagi (y/n) : ")
    if is_exit == 'n' or is_exit == 'N':
        break