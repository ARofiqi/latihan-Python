print("""
----------------------
    Koneversi Suhu
----------------------""")

def dari_celsius():
    celsius = int(input("Masukan suhu dalam Celcius :"))
    fahrenheit = 9/5*celsius+32
    print(celsius,"Celsius = ",fahrenheit,"Fahrenheit")

dari_celsius()