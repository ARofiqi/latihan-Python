from pytube import YouTube
from os import system

while True: 
    try:
        yt = YouTube(input("Masukan Link : "))
        system("cls")
        print("\nJudul video = ",yt.title)
        for i in yt.streams:
            print(f"id = {i.itag}   res = {i.resolution} type = {i.type}")
        id = int(input("\nMasukan Id = "))
        while True:
            try:
                system("cls")
                print(f"Judul : {yt.title}\nSedang mengunduh ...")
                yt.streams.get_by_itag(id).download(r"D:\video-youtube")
                print("Selesai\n")
                break
            except:
                input("Video tidak dapat didownload\n")
        quit = input("Apakah Ada Video Yang Ingin Anda Download Lagi (y/n): ")
        if quit == 'n':
            print("Terima Kasih")
            break
    except:
        input("Link Yang Anda Masukan Salah, Harap mengisi link yang benar")
    