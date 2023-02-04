class Hero:
    def __init__(self, name, hp, power, armor) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.armor = armor

    def serang(self, lawan):
        lawan.hp -= lawan.hp // self.power
        print(self.name + " Menyerang " + lawan.name)
        lawan.diserang(self)

    def diserang(self, lawan):
        print(self.name + " Diserang " + lawan.name)
        print("sisa darah " + self.name + " = " + str(self.hp))
    
    def healing(self, heal):
        self.hp += heal
        print(self.name + " Melakukan Heal Sebanyak " + str(heal))
        print(self.name + " Memiliki HP Sebanyak " + str(self.hp))
    
    def healing_to(self, heal ,friend):
        friend.hp += heal
        print(self.name + " Melakukan Haeling Ke " + friend.name + " Sebanayak " + str(heal))


rofiqi = Hero("Rofiqi", 100, 20, 30)
ucup = Hero("Ucup", 100, 30, 25)

rofiqi.serang(ucup)
print("")
ucup.serang(rofiqi)
