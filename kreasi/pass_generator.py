import random
def pasw():
    all_pass = []
    abjad = "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM"
    simbol = "@#$%^&*()-+|\{>}?<.,-_]`;:"
    number = "1234567890"

    print("Your pasw : ",end=(""))
    new_pass = [random.choice(abjad)+random.choice(number)+random.choice(abjad)+random.choice(number)+random.choice(abjad)+random.choice(simbol)+random.choice(abjad)+random.choice(number)]
    all_pass.append(new_pass)

    print(new_pass)
    return all_pass

while True:
    pasw()
    exit = input("\nLagi (y/n) : ")
    if exit == 'y':
        continue
    else:
        print(pasw())
        break