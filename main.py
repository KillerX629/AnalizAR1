# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent = None, title="AnalizAR"):
            wx.Frame.__init__(self, parent=parent, title=title, size=(800,600))
            self.control= wx.TextCtrl(self,style=wx.TE_MULTILINE)
            self.CreateStatusBar()





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
