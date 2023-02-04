# class abstrak dan decorator

from abc import ABC, abstractmethod


class Button(ABC):

    def __init__(self, set_link):
        self.link = set_link

    @abstractmethod
    def klik(self):
        pass

    @property
    @abstractmethod
    def link(self):
        pass

class PushButton(Button):

    def klik(self):
        print(f"Go To : {self.link}")
    
    @Button.link.setter
    def link(self, input):
        self.__link = input

    @link.getter
    def link(self):
        return self.__link

tombol1 = PushButton("www.rofiqi.id")

tombol1.klik()