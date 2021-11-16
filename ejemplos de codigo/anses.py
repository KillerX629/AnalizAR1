import datetime


class TipoDocumento:
    """ Los posibles tipos de documentos que se admiten """

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre


class Usuario:
    """ Modela una entidad de Usuario inscripto en el sistema """

    def __init__(self, nombre, apellido, fecha_nacimiento):
        self.tipo_documento = TipoDocumento(1, 'DNI')
        self.numero_documento = None
        self.nombre = nombre
        self.apellido = apellido
        self.sex = 'F'  # <- es buen modelado este??
        self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%d/%m/%y')

