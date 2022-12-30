from pytube import YouTube
link = "https://www.youtube.com/watch?v=mfjRsAbs6Ms"
yt = YouTube(link)
for i in yt.streams:
    print(i.itag, i.mime_type, i.resolution, i.fps)