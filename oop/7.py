# seper inhertence

class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class Hero_intelegent(Hero):
    def __init__(self, name):
        # Hero.__init__(self,name,100)
        super().__init__(name,100)

class Hero_strength(Hero):
    def __init__(self, name):
        Hero.__init__(self,name,200)
    
rofiqi = Hero("Rofiqi", 1000)
ucup = Hero_intelegent("Ucup")
rudi = Hero_strength("Rudi")

print(rofiqi.__dict__)
print(ucup.__dict__)
print(rudi.__dict__)