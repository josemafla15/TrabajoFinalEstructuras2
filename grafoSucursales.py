class GrafoSucursales:
    def __init__(self):
        self.sucursales = {}  # Almacena las sucursales como nodos
        self.conexiones = {}  # Almacena las conexiones como diccionario de distancias

    def agregar_sucursal(self, nombre):
        if nombre not in self.sucursales:
            self.sucursales[nombre] = nombre
            self.conexiones[nombre] = {}
            return True
        return False

    def conectar_sucursales(self, sucursal1, sucursal2, distancia):
        if sucursal1 in self.sucursales and sucursal2 in self.sucursales:
            self.conexiones[sucursal1][sucursal2] = distancia
            self.conexiones[sucursal2][sucursal1] = distancia
            return True
        return False

    def obtener_conexiones(self):
        return self.conexiones