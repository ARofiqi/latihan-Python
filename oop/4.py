# staticmethod dan classmethod

class Hero:
    __jumlah = 0

    def __init__(self, name, hp):
        self.__name = name
        self.__hp = hp
        Hero.__jumlah += 1

    # Method yang hanya berlaku untuk objek
    def getJumlah(self):
        return Hero.__jumlah

    # Method tidak berlaku untuk objek tetapi berlaku untuk Class
    def getJumlah1():
        return Hero.__jumlah

    # Method static (decorator)
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah

# print(Hero.getJumlah())
# print(Hero.getJumlah1())

print(Hero.getJumlah3())

rofiqi = Hero("Rofiqi", 100)
print(rofiqi.getJumlah3())
ucup = Hero("Ucup", 100)

