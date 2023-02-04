# membuat class abstrak
# ABC = Abstrak Base Class

from abc import ABC, abstractmethod

class Button(ABC):

    @abstractmethod
    def klik(self):
        print("Button klik")
    
    def say(self):
        print("Hallo")

class PushButton(Button):
    
    def klik(self):
        return super().klik()

# tombol1 = Button()
# tombol1.klik()

tombol2 = PushButton()
tombol2.klik()
tombol2.say()

# help(tombol2)