import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Evento Boton')
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        my_btn = wx.Button(panel, label='Ingresar')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            print("Es necesario ingresar algun texto")
        else:
            print("El texto ingresado fue {}".format(value))


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
