import random
def pasw():
    abjad = "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"
    simbol = "@#$%^&*()-+|\{>}?<.,-_]`;:"
    number = "1234567890"
    huruf = abjad*2+simbol+number
    new_pass = list(random.choice(huruf) for i in range(10))
    return "".join(new_pass)

while True:
    sandi = pasw()
    print(sandi)
    exit = input("\nLagi (y/n) : ")
    if exit == 'n':
        break