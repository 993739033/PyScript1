import wx

class App(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent = None, title = "第一个窗口程序")
        frame.show()
        return True

if __name__ =="__mian__":
    app = wx.App()
    frame = wx.Frame(title="Window")
    frame.show()
    app.MainLoop()
