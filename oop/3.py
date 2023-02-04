# Encapsulasi

class Hero:
    # Membuat semua variabel menjadi private
    def __init__(self, name, hp):
        self.__name = name
        self.__hp = hp

    # getter
    def getName(self):
        return self.__name

    def getHp(self):
        return self.__hp

    # setter
    def hit(self, damage):
        self.__hp -= damage

# Awal game
rofiqi = Hero("Rofiqi",100)
print(rofiqi.__dict__)

name_hero1 = rofiqi.getName()
print(name_hero1)

# Game Berjalan
print(rofiqi.getHp())
rofiqi.hit(20)
print(rofiqi.getHp())