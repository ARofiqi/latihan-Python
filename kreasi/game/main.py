import os
import random
import GBK

choices = ["GUNTING", "KERTAS", "BATU"]
class Gbk:

    def __init__(self, name, choice) -> None:
        self.__name = name
        self.__choice = choice.upper()

    def getWin(self, enemy):
        if (enemy.__choice == self.__choice):
            result = "Seri"
        elif (enemy.__choice == self.__choices[0] and self.__choice == self.__choices[2]):
            result = "Menang"
        elif (enemy.__choice == self.__choices[1] and self.__choice == self.__choices[0]):
            result = "Menang"
        elif (enemy.__choice == self.__choices[2] and self.__choice == self.__choices[1]):
            result = "Menang"
        else:
            result = "Kalah"
        return f"{self.__name} {result}"
    



def start():
    print("Apakah Mau Bermain Bersama Bot Atau Pemain Lain")
    print("1. Bot")
    print("2. Pemain Lain")
    opt = input("\nPilih : ")
    match opt:
        case "1": pass
        case "2": pass


if __name__ == "__main__":

    while True:
        os_name = os.name
        match os_name:
            case "nt": os.system("cls")
            case "posix": os.system("clear")

        print("SELAMAT DATANG DI GAME GUNTING KERTAS BATU")
        print("=============================================")
        print("1. Start")
        print("2. Option")
        print("0. Exit")
        opt = input("\nMasukan Opsi : ")

        match opt:
            case "1": start()
            case "2": option()
            case "0": exit()

        try:
            with open(".\kreasi\gkb\hasil.txt", "a") as skor:
                txt = ""
                skor.write(txt)
        except IndexError:
            print("MOHON UNTUK PILIH PILIHAN YANG ADA DI MENU")
