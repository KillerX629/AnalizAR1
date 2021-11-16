import wx


class ExampleToolbar(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title='Evento Boton')

        self.timer = None
        # self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        client = wx.Panel(self)
        client.SetBackgroundColour(wx.WHITE)

        tb = wx.ToolBar(client)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(tb, 0, wx.EXPAND)
        client.SetSizer(sizer)

        self.CreateStatusBar()

        tsize = (24, 24)
        new_bmp = wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR, tsize)
        open_bmp = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, tsize)
        copy_bmp = wx.ArtProvider.GetBitmap(wx.ART_COPY, wx.ART_TOOLBAR, tsize)
        paste_bmp = wx.ArtProvider.GetBitmap(wx.ART_PASTE, wx.ART_TOOLBAR, tsize)

        tb.SetToolBitmapSize(tsize)

        # tb.AddTool(10, new_bmp, "New", "Long help for 'New'")
        tb.AddTool(10, "New", new_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "New", "Long help for 'New'", None)

        # tb.AddTool(20, open_bmp, "Open", "Long help for 'Open'")
        tb.AddTool(20, "Open", open_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "Open", "Long help for 'Open'", None)

        tb.AddSeparator()
        tb.AddTool(30, "Copy", copy_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "Copy", "Long help for 'Copy'", None)

        tb.AddTool(40, "Paste", paste_bmp, wx.NullBitmap, wx.ITEM_NORMAL, "Paste", "Long help for 'Paste'", None)

        tb.AddSeparator()

        tb.AddSeparator()
        cbID = wx.NewIdRef()

        tb.AddControl(
            wx.ComboBox(
                tb, cbID, "", choices=["Elegir...", "Esto", "es un", "wx.ComboBox"],
                size=(150, -1), style=wx.CB_DROPDOWN
            ))

        tb.AddStretchableSpace()

        # Final thing to do for a toolbar is call the Realize() method. This
        # causes it to render (more or less, that is).
        tb.Realize()


def main():
    app = wx.App()
    ex = ExampleToolbar()
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
