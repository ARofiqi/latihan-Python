# inheritence / Pewarisan

class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class Hero_intelegent(Hero):
    pass


rofiqi = Hero("Rofiqi",100)
ucup = Hero_intelegent("Ucup",200)

print(rofiqi.__dict__)
print(ucup.__dict__)
print(help(ucup))
