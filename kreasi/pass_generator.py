import random

def pasw():
    jml = int(input("Berapa huruf : "))

    abjad = "aAbBcCdDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    simbol = "@#$%^&*()-+|\{>}?<.,-_]`;:"
    number = "1234567890"

    print("Your pasw : ",end=(""))
    for i in range(jml):
        print(random.choice(abjad)+random.choice(simbol)+random.choice(number),end=(""))     

pasw()