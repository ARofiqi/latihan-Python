# class

class Hero:
    # Class Variabel
    # variabel static
    jumlah = 0

    # Fungsi yang akan dijalankan ketika menjalankan class
    def __init__(self, name, power, health, vitality):
        # instance Variable
        self.name = name
        self.power = power
        self.health = health
        self.vitality = vitality
        Hero.jumlah += 1

    # Method tanpa return
    def say(self):
        print(f"Hallo, {self.name}")
    
    # mathod dengan argumen
    def healing(self,heal):
        self.health += heal
    
    def hit(self, damage):
        self.health -= damage

    # Method dengan return
    def getHealth(self):
        return self.health
    


# Membuat Object
hero1 = Hero("Rofiqi", 100, 2000, 3000)
data_hero1 = hero1.__dict__

print(" ")
for i in data_hero1:
    print(i,"    \t=", data_hero1[i])
# print(Hero.jumlah)

print(" ")
hero1.say()
print(" ")

hero1_health = hero1.getHealth()
print(f"hero 1 health = {hero1_health}\n")

print(f"{hero1.name} health = {hero1.health}")
hero1.healing(20)
hero1.hit(200)
hero1.healing(20)
print(f"{hero1.name} health = {hero1.health}")

hero2 = Hero("Ucup", 200, 2500, 5000)
data_hero2 = hero2.__dict__

hero2_health = hero2.getHealth()
print(f"\nhero 2 health = {hero2_health}\n")

for i in data_hero2:
    print(i,"    \t=", data_hero2[i])
print(" ")

# print(Hero.jumlah)
hero2.say()

# Method
# 1. method interaktif dengan user
# 2. method interaktif dengan objek
