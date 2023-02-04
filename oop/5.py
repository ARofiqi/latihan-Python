# getter dan setter default

class Hero:

    def __init__(self, name, hp):
        self.__name = name
        self.__hp = hp
        # self.info = f"{self.__name} : {self.__hp}"

    @property
    def info(self):
        return f"{self.__name} : {self.__hp}"

    @property
    def hp(self):
        pass

    @hp.getter
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, input):
        self.__hp = input

    @hp.deleter
    def hp(self):
        self.__hp = None

rofiqi = Hero("Rofiqi", 100)
# print(rofiqi.info)

print(rofiqi.hp)

rofiqi.hp = 200

print(rofiqi.hp)

print(rofiqi.__dict__)
del rofiqi.hp
print(rofiqi.__dict__)