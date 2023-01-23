import random
from os import system

pilihan = ["Gunting","Kertas","Batu"]

while True:
    system("cls")
    player_input = int(input(f"""Pilih 
[1] Gunting
[2] Kertas
[3] Batu 
: """))

    try:
        bot = random.choice(pilihan)
        player = pilihan[player_input-1]

        print(f"""{"Kamu".center(10)} Vs {"Bot".center(10)}
{player.center(10)}    {bot.center(10)}
""")

        if bot == player:
            hasil = "Seri"
        elif bot == "Gunting" and player == "Batu":
            hasil = "Menang"
        elif bot == "Kertas" and player == "Gunting":
            hasil = "Menang"
        elif bot == "Batu" and player == "Kertas":
            hasil = "Menang"
        else:
            hasil = "Kalah"
        
        print(f"Kamu {hasil}")
    
        with open(".\kreasi\gkb\hasil.txt","a") as skor:
            txt = f"""
========================
{"Kamu".center(10)} Vs {"Bot".center(10)}
{player.center(10)}    {bot.center(10)}
========================
Hasil = {hasil}
"""
            skor.write(txt)

    except IndexError:
        print("MOHON UNTUK PILIH PILIHAN YANG ADA DI MENU")
    input("")