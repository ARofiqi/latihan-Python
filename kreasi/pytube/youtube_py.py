from pytube import YouTube
link = input("Masukan Link : ")
yt = YouTube(link)
stream = yt.streams.get_by_itag(140)
stream.download()