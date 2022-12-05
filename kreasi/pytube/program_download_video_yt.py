from pytube import YouTube

def download_video():
    link = input("Masukan Link : ")
    yt = YouTube(link)
    print("Judul video = ",yt.title)
    stream = yt.streams
    for i in stream:
        print(f"id = {i.itag}   res = {i.resolution} type = {i.type}")
    id = int(input("\nMasukan Id = "))
    print("Sedang mengunduh ...")
    stream.get_by_itag(id).download(r"D:\video_youtube")
    print("Selesai")

download_video()