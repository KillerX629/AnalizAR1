import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)

        my_sizer = wx.BoxSizer(wx.VERTICAL)

        # Expande el widget a todo el espacio disponible
        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 0, wx.EXPAND, 5)

        # Agrega un borde (espacio) a todos los bordes del widget
        ingresar_btn = wx.Button(panel, label='Ingresar')
        my_sizer.Add(ingresar_btn, 0, wx.ALL, 5)

        # Centra el widget
        salir_btn = wx.Button(panel, label='Salir')
        my_sizer.Add(salir_btn, 0, wx.RIGHT, 5)

        cancelar_btn = wx.Button(panel, label='Cancelar')
        my_sizer.Add(cancelar_btn, 0, wx.ALIGN_RIGHT)

        acerca_btn = wx.Button(panel, label='Acerca')
        my_sizer.Add(acerca_btn, 0, wx.EXPAND)

        # Se configura el sizer a utilizar
        panel.SetSizer(my_sizer)
        self.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()


print("Hola)")