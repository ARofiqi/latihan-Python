from tkinter import messagebox
import wx
class MyApp(wx.app):
    def OnInit(self):
        wx.MessageBox("Hallo","wxApp")
        return True

if __name__=="__main__":
    app = MyApp(False)
    app.MainLoop()
