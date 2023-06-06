class Hero:
    def __init__(self, name):
        self.hp_pool = [0, 100, 200, 300, 400, 500]
        self.attPower_pool = [0, 10, 20, 30, 40, 50]
        self.armor_pool = [0, 1, 2, 3, 4, 5]

        self.__name = name
        self.__exp = 0
        self.__level = 1

    def showInfo(self):
        print(f"{self.__name} Level {self.__level} \n\t: Hp = {self.__hp} \n\t: Attack Power = {self.__attPower} \n\t: Armor = {self.__armor}")

    @property
    def hp_pool(self):
        pass

    @property
    def attPower_pool(self):
        pass

    @property
    def armor_pool(self):
        pass

    @property
    def levelUp(self):
        pass

    @property
    def gainExp(self):
        pass

    @hp_pool.setter
    def hp_pool(self, input):
        self.__hp_pool = input

    @attPower_pool.setter
    def attPower_pool(self, input):
        self.__attPower_pool = input

    @armor_pool.setter
    def armor_pool(self, input):
        self.__armor_pool = input

    @gainExp.setter
    def gainExp(self, input):
        self.__exp = input
        if (self.__exp == 100):
            self.levelUp = self.__exp//100
            self.__exp %= 100
    
    @levelUp.setter
    def levelUp(self,input):
        self.__level += input
        self.__hp = self.__hp_pool[self.__level]
        self.__attPower = self.__attPower_pool[self.__level]
        self.__armor = self.__armor_pool[self.__level]

class Hero_intelligent(Hero):

    def __init__(self, name):
        super().__init__(name)
        self.hp_pool = [0, 50, 100, 150, 200, 250]
        self.attPower_pool = [0, 20, 40, 60, 80, 100]
        self.armor_pool = [0, 0.5, 1, 1.5, 2, 2.5]
        self.levelUp = 1


class Hero_strangeth(Hero):

    def __init__(self, name):
        super().__init__(name)
        self.hp_pool = [0, 200, 300, 400, 500, 600]
        self.attPower_pool = [0, 20, 40, 60, 80, 100]
        self.armor_pool = [0, 2, 4, 6, 8, 10]
        self.levelUp = 1


rofiqi = Hero_intelligent("Rofiqi")
ucup = Hero_strangeth("Ucup")

rofiqi.showInfo()
ucup.showInfo()

rofiqi.gainExp = 200
ucup.gainExp = 300

rofiqi.showInfo()
ucup.showInfo()