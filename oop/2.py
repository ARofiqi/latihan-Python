class Hero:
    # Class Variabel
    # variabel static
    jumlah = 0

    # Fungsi yang akan dijalankan ketika menjalankan class
    def __init__(self, name, hp):
        # instance Variable
        self.name = name
        self.hp = hp
        Hero.jumlah += 1

        # Variabel instance private
        self.__private = "private"

        # variable instance protected
        self._protected = "protected"

rofiqi = Hero("Rofiqi",100)

print(rofiqi.__dict__)
# print(rofiqi.__private)
print(rofiqi._protected)