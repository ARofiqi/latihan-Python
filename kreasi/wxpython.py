import wx
import os

# 1. Membuat Kotak Pesan

# class MyApp(wx.App):
#     def OnInit(self):
#         wx.MessageBox("Hallo Ini Siapa","Pemberitahuan")
#         return True

# if __name__ == "__main__":
#     app = MyApp(False)
#     MyApp.MainLoop()


# 2. Membuat Kotak Frame

# class MyFrame(wx.Frame):
#     def __init__(self):
#         wx.Frame.__init__(self,None,title="Ahmad Rofiqi")
#         self.Show()
# if __name__ == "__main__":
#     app = wx.App(False)
#     frame = MyFrame()
#     app.MainLoop()

# 3. Menampilkan Gambar pada Frame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None,title="Menampilkan Gambar PNG")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True
    
class MyFrame(wx.Frame):
    def __init__(self, parent,id=wx.ID_ANY,title="",pos=wx.DefaultPosition,size=wx.DefaultSize,style=wx.DEFAULT_FRAME_STYLE,name="MyFrame"):
        super(MyFrame,self).__init__(parent,id,title,pos,size,style,name)
        # Atribut
        self.panel = wx.Panel(self)
        img_path = os.path.abspath(r"D:\umaru.png")
        bitmap = wx.Bitmap(img_path,type=wx.BITMAP_TYPE_PNG)
        self.bitmap = wx.StaticBitmap(self.panel,bitmap=bitmap)

if __name__=="__main__":
    app = MyApp(False)
    app.MainLoop()

# 4. 