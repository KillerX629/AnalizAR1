import wx


class FramePrincipal(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = FramePrincipal()
    app.MainLoop()
