class GrafoSucursales:
    def __init__(self):
        self.sucursales = {}  # Almacena las sucursales como nodos
        self.conexiones = {}  # Almacena las conexiones como diccionario de distancias

    def append_branch(self, name):
        if name not in self.sucursales:
            self.sucursales[name] = name
            self.conexiones[name] = {}
            return True
        return False

    def conect_branches(self, sucursal1, sucursal2, distancia):
        if sucursal1 in self.sucursales and sucursal2 in self.sucursales:
            self.conexiones[sucursal1][sucursal2] = distancia
            self.conexiones[sucursal2][sucursal1] = distancia
            return True
        return False

    def get_conections(self):
        return self.conexiones