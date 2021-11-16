import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='TextEntry y Button')
        panel = wx.Panel(self)

        self.text_ctrl = wx.TextCtrl(panel, pos=(5, 5))
        my_btn = wx.Button(panel, label='Ingresar', pos=(5, 55))

        self.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
