from pytube import YouTube
from os import system

while True:
    system("cls")
    try:
        print("PROGRAM MENDOWNLOAD VIDEO YOUTUBE")
        yt = YouTube(input("Masukan Link : "))
        system("cls")
        print("Judul video = ",yt.title)
        print(f" id / resolusi / type ")
        for i in yt.streams:
            if i.itag == 160 or i.itag == 18 or i.itag == 22:
                    print(f" {i.itag} /   {i.resolution}   / {i.type}")
        while True:
            try:
                id = int(input("\nMasukan Id = "))
                yt.set_filename(yt.title) 
                print(f"\nJudul : {yt.title}\nSedang mengunduh ...")
                yt.streams.get_by_itag(id).download(r"D:\video-youtube")
                print("Selesai\n")
                break
            except:
                input("Video tidak dapat didownload - id yang anda masukan tidak ada\n")
        quit = input("Apakah Ada Video Yang Ingin Anda Download Lagi (y/n): ")
        if quit == 'n':
            print("Terima Kasih")
            break
    except:
        input("Link Yang Anda Masukan Salah, Harap mengisi link yang benar")
