class Hero:
    __jumlah = 0

    def __init__(self, name, hp, attackPower, armor):
        self.__name = name
        self.__hpBase = hp
        self.__attackPowerBase = attackPower
        self.__armorBase = armor
        self.__level = 1
        self.__exp = 0

        self.__hpMax = self.__hpBase * self.__level
        self.__attackPower = self.__attackPowerBase * self.__level
        self.__armor = self.__armorBase * self.__level

        self.__hp = self.__hpMax
        Hero.__jumlah += 1

    @property
    def info(self):
        return f"{self.__name}\tLevel= {self.__level}\n\thp={self.__hp}/{self.__hpMax}\n\tattack={self.__attackPower}\n\tarmor={self.__armor}"

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(self.__name + " Level Up")
            self.__level += 1
            self.__exp -= 100

            self.__hpMax = self.__hpBase * self.__level
            self.__attackPower = self.__attackPowerBase * self.__level
            self.__armor = self.__armorBase * self.__level
    
    def attack(self, enemy):
        self.gainExp = 50


rofiqi = Hero("Rofiqi", 100, 5, 20)
ucup = Hero("Ucup", 100, 5, 20)

