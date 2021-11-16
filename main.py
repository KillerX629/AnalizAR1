import wx
import numpy as np
import pandas as pd
import os
import glob


class MyFrame(wx.Frame):
    def __init__(self, parent=None, title="AnalizAR"):
        wx.Frame.__init__(self, parent=parent, title=title)
        self.empresas = []
        self.empresaCargada = None
        self.init_empresas()
        self.initUI()

    def init_empresas(self):
        os.chdir("./empresas")
        for archivo in glob.glob("*.csv"):
            self.empresas.append(archivo)

    def initUI(self):
        panel1 = wx.Panel(self)  # Panel1 vendría a ser toda la ventana

        self.comboboxEmpresas = wx.ComboBox(panel1, choices=self.empresas, size=wx.DefaultSize)
        self.comboboxEmpresas.Bind(wx.EVT_COMBOBOX, self.cargarEmpresa)
        sizerPanel1 = wx.BoxSizer(wx.VERTICAL)

        sizerMedio = wx.GridSizer(rows=2, cols=2, hgap=3, vgap=5)
        sizerArriba = wx.BoxSizer(wx.HORIZONTAL)
        sizerAbajo = wx.BoxSizer(wx.HORIZONTAL)
        sizerFecha = wx.BoxSizer(wx.HORIZONTAL)

        botonGuardar = wx.Button(panel1, label="Guardar")
        botonCargar = wx.Button(panel1, label="Cargar")

        #Elegida la empresa, debe tener una opción donde se pueda elegir una fecha y mostrar el valor promedio de ese dia (media aritmética entre precio de cierre y precio de apertura)
        #También debe tener otra opción que calcule y muestre el promedio ANUAL (o sea, teniendo en cuenta todos los datos del archivo) del precio de Cierre
        #Debe mostrar el Precio histórico más alto y el más bajo
        #Debe permitir grabar en otro archivo de texto el resumen con la info, conteniendo: promedio anual de precio de apertura, promedio anual de precio de cierre, valor mas alto historico, valor más bajo historico

        self.precioAlto = wx.StaticText(panel1,label="Precio mas alto:")
        self.precioBajo = wx.StaticText(panel1,label="Precio mas bajo:")
        self.promedioAnual = wx.StaticText(panel1, label="Promedio anual:")
        self.promDia = wx.StaticText(panel1,label="Promedio del dia:")

        self.fecha = wx.TextCtrl(panel1)

        sizerFecha.Add(self.fecha, flag=wx.EXPAND )
        sizerAbajo.Add(self.comboboxEmpresas, 1, wx.ALIGN_CENTER)


        sizerArriba.Add(botonGuardar, 1, wx.LEFT)
        sizerArriba.Add(botonCargar, 1, wx.RIGHT)

        sizerMedio.Add(self.precioAlto)
        sizerMedio.Add(self.precioBajo)
        sizerMedio.Add(self.promedioAnual)
        sizerMedio.Add(self.promDia)


        sizerPanel1.Add(sizerArriba, flag=wx.EXPAND | wx.TOP | wx.CENTER, border=2)
        sizerPanel1.Add(sizerMedio, flag=wx.EXPAND | wx.CENTER)
        sizerPanel1.Add(sizerAbajo, flag=wx.EXPAND | wx.BOTTOM | wx.CENTER, border=2)
        sizerPanel1.Add(sizerFecha, flag= wx.BOTTOM)

        panel1.SetSizer(sizerPanel1)


        self.Show()



    def cargarEmpresa(self, event):
        empresa = self.comboboxEmpresas.GetValue()
        if  self.comboboxEmpresas.IsEmpty():
            pass
        else:
            self.empresaCargada= empresa
            self.actualizarTextos(empresa)


    def actualizarTextos(self, empresa):
        df = pd.read_csv("../empresas/"+ empresa)
        print(df)
        alto = df['High'].max()
        bajo = df['Low'].min()
        promAn = df['Close'].median()
        self.precioAlto.SetLabel("Precio mas alto: {}".format(alto))
        self.precioBajo.SetLabel("Precio mas bajo: {}".format(bajo))
        self.promedioAnual.SetLabel("Promedio anual: {}".format(promAn))



if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
