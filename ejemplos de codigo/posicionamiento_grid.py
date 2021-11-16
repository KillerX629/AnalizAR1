import wx
import wx.lib.inspection


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        panel = wx.Panel(self)

        my_sizer = wx.GridBagSizer(5, 5)

        # Expande el widget a todo el espacio disponible
        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM)

        # Agrega un borde (espacio) a todos los bordes del widget
        ingresar_btn = wx.Button(panel, label='Ingresar')
        my_sizer.Add(ingresar_btn, pos=(1, 1))

        # Centra el widget
        salir_btn = wx.Button(panel, label='Salir')
        my_sizer.Add(salir_btn, pos=(2, 2))

        cancelar_btn = wx.Button(panel, label='Cancelar')
        my_sizer.Add(cancelar_btn, pos=(3, 3))

        acerca_btn = wx.Button(panel, label='Acerca')
        my_sizer.Add(acerca_btn, pos=(4, 4))

        # Se configura el sizer a utilizar
        panel.SetSizer(my_sizer)
        my_sizer.Fit(self)

        wx.lib.inspection.InspectionTool().Show()

        self.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
