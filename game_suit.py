print("""===================
     Game Suit      
===================""")
main = True

while main==True:
    player_name = input("Masukan nama :")
    game_opt = ["Gunting","Kertas","Batu"]
    
    player_opt = input("pilih(kertas,gunting,batu) :")
    
    lagi = input("main lagi(y/n):")
    if lagi=='n':main=False