import wx
from anses import TipoDocumento, Usuario


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()

    def InitUI(self):
        panel = wx.Panel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)

        tipos_documento = [
            TipoDocumento(1, 'Documento Unico'),
            TipoDocumento(2, 'Libreta de Enrolamiento'),
            TipoDocumento(3, 'Libreta Civica'),
            TipoDocumento(4, 'Otros'),
        ]

        eleccion = []

        self.ctl_tipo_documento = wx.ComboBox(panel,
                                              size=wx.DefaultSize,
                                              choices=eleccion)

        for tipo in tipos_documento:
            self.ctl_tipo_documento.Append(tipo.nombre, tipo)

        self.txt_tipo_documento = wx.StaticText(panel, label="Tipo de Documento")

        # API: Box.Add(control, proportion, flag, border)
        sizer.Add(self.txt_tipo_documento, 0, wx.EXPAND, 5)
        sizer.Add(self.ctl_tipo_documento, 0, wx.EXPAND, 5)

        self.txt_nro_documento = wx.StaticText(panel, label="Numero de Documento")
        self.ctl_nro_documento = wx.TextCtrl(panel)

        # API: Box.Add(control, proportion, flag, border)
        sizer.Add(self.txt_nro_documento, 0, wx.EXPAND, 5)
        sizer.Add(self.ctl_nro_documento, 0, wx.EXPAND, 5)

        self.ctl_nombre = wx.TextCtrl(panel)

        # API: Box.Add(control, proportion, flag, border)
        sizer.Add(wx.StaticText(panel, label="Nombre"), 0, wx.EXPAND, 5)
        sizer.Add(self.ctl_nombre, 0, wx.EXPAND, 5)

        self.ctl_apellido = wx.TextCtrl(panel)

        # API: Box.Add(control, proportion, flag, border)
        sizer.Add(wx.StaticText(panel, label="Apellido"), 0, wx.EXPAND, 5)
        sizer.Add(self.ctl_apellido, 0, wx.EXPAND, 5)

        lista_sexo_opciones = ['Femenino', 'Masculino']
        self.group_sexo = wx.RadioBox(panel, choices=lista_sexo_opciones)

        sizer.Add(wx.StaticText(panel, label="Sexo"), 0, wx.EXPAND, 5)
        sizer.Add(self.group_sexo, 0, wx.EXPAND, 5)

        self.fecha_nacimiento = wx.TextCtrl(panel)

        # API: Box.Add(control, proportion, flag, border)
        sizer.Add(wx.StaticText(panel, label="Fecha de Nacimiento"), 0, wx.EXPAND, 5)
        sizer.Add(self.fecha_nacimiento, 0, wx.EXPAND, 5)

        self.button_aceptar = wx.Button(panel, label="Consultar")
        sizer.Add(self.button_aceptar, 0, wx.EXPAND)

        panel.SetSizer(sizer)
        sizer.Fit(self)


def main():
    app = wx.App()
    ex = Example(None, title="Constancia de CUIL")
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
