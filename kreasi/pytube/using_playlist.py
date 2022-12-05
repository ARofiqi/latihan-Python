from pytube import Playlist

p = Playlist("https://youtube.com/playlist?list=PLsZXkthdAp7bqIQTNuvXRJU5cD3ZfR3z5")
print(f'Downloading: {p.title}')
for video in p.videos:
    print(video)