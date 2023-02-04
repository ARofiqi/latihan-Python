# override method

class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def showInfo(self):
        print(f"{self.name} : {self.hp}")


class Hero_intelegent(Hero):
    def __init__(self, name):
        super().__init__(name, 100)
    
    # override method
    def showInfo(self):
        print(f"{self.name} : {self.hp} : Type Inteligent")


class Hero_strength(Hero):
    def __init__(self, name):
        super().__init__(name, 200)


rofiqi = Hero_strength("Rofiqi")
ucup = Hero_intelegent("Ucup")

rofiqi.showInfo()
ucup.showInfo()
