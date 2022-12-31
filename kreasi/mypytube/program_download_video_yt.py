from pytube import YouTube
import wx
import demo

class myapp(demo.myapp):
    def __init__(self,parent):
        demo.myapp.__init__(self,parent)
    
    def download(self, event):
            id = self.res.GetValue()
            yt = YouTube(self.link.GetValue(),on_progress_callback=progress_down)

            if id == '1':id = 160
            elif id == '2':id = 18
            elif id == '3':id = 22

            global load
            global size
            load = self.loading
            size = yt.streams.get_by_itag(id).filesize
            def progress_down(chunk,bytes_remaining):
                    current = ((size - bytes_remaining)/size)
                    load.SetValue(current)
                    print(size)
            
            self.info.SetValue("")
            load.SetRange(size)
            try:
                yt.streams.get_by_itag(id).download(r"D:\video-youtube")
                load.SetValue(size)

                self.info.SetValue("Sukses")
            except:
                self.info.SetValue("Tidak Sukses")



app = wx.App(False)
frame = myapp(None)
frame.Show(True)
app.MainLoop()

# while True:
#     system("cls")
#     try:
#         print("PROGRAM MENDOWNLOAD VIDEO YOUTUBE")
#         yt = YouTube(input("Masukan Link : "))
#         system("cls")
#         print("Judul video = ",yt.title)
#         print(f" id / resolusi / type ")
#         for i in yt.streams:
#             if i.itag == 17 or i.itag == 18 or i.itag == 22:
#                     print(f" {i.itag} /   {i.resolution}   / {i.type}")
#         while True:
#             try:
#                 id = int(input("\nMasukan Id = "))
#                 yt.streams.get_by_itag(id).download(r"D:\video-youtube")
#                 print(f"\nJudul : {yt.title}\nSedang mengunduh ...")
#                 print("Selesai\n")
#                 break
#             except:
#                 input("Video tidak dapat didownload - id yang anda masukan tidak ada\n")
#         quit = input("Apakah Ada Video Yang Ingin Anda Download Lagi (y/n): ")
#         if quit == 'n':
#             print("Terima Kasih")
#             break
#     except:
#         input("Link Yang Anda Masukan Salah, Harap mengisi link yang benar")

    