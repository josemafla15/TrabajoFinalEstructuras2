class NodoServicio:
    def __init__(self, nombre: str, descripcion: str):
        self.nombre = nombre
        self.descripcion = descripcion
        self.subservicios = []

    def agregar_subservicio(self, subservicio):
        self.subservicios.append(subservicio)


class ArbolServicios:
    def __init__(self):
        self.servicios = []

    def agregar_servicio(self, servicio: NodoServicio):
        self.servicios.append(servicio)