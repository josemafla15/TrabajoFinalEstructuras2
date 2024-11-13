class NodoServicio:
    def __init__(self, nombre, descripcion=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.subservicios = []  # Lista para los subservicios

    def agregar_subservicio(self, subservicio):
        # Evitar duplicados
        for s in self.subservicios:
            if s.nombre == subservicio.nombre:
                return  # No agregar duplicado
        self.subservicios.append(subservicio)

class ArbolServicios:
    def __init__(self):
        self.raiz = NodoServicio("Servicios")
        self.servicios = []

    def agregar_servicio(self, nombre_servicio, descripcion=None):
        # Agregar un servicio a la lista
        nuevo_servicio = NodoServicio(nombre_servicio, descripcion)
        self.servicios.append(nuevo_servicio)
        return nuevo_servicio  # Devuelve el servicio recién creado para poder agregarle subservicios

    def obtener_lista_servicios(self):
        lista_servicios = []
        for servicio in self.servicios:
            lista_servicios.append(servicio.nombre)  # Solo el nombre
            for subservicio in servicio.subservicios:
                lista_servicios.append(f"{servicio.nombre} > {subservicio.nombre}")  # Incluye subservicios
        return lista_servicios

# Ejemplo de uso
arbol_servicios = ArbolServicios()

# Crear servicios y subservicios
arbol_servicios.agregar_servicio("Servicio1", "Subservicio1")
arbol_servicios.agregar_servicio("Servicio1", "Subservicio2")
arbol_servicios.agregar_servicio("Servicio2")

# Obtener lista de servicios y subservicios
for servicio in arbol_servicios.obtener_lista_servicios():
    print(servicio)