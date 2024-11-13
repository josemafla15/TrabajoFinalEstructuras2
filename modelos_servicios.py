class NodoServicio:
    def __init__(self, nombre, descripcion=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.subservicios = []

    def agregar_subservicio(self, subservicio):
        # Evitar duplicados
        for s in self.subservicios:
            if s.nombre == subservicio.nombre:
                return  # No agregar duplicado
        self.subservicios.append(subservicio)

class ArbolServicios:
    def __init__(self):
        self.raiz = NodoServicio("Servicios")  # Raíz general para todos los servicios
        self.servicios = []

    def agregar_servicio(self, nombre_servicio, nombre_subservicio=None):
        # Si no se pasa un subservicio, se agrega un nuevo servicio principal
        nuevo_servicio = NodoServicio(nombre_servicio)
        
        # Si el servicio tiene un subservicio
        if nombre_subservicio is None:
            self.servicios.append(nuevo_servicio)
        else:
            # Buscar si el servicio ya existe, en cuyo caso se agrega un subservicio
            for servicio in self.servicios:
                if servicio.nombre == nombre_servicio:
                    servicio.agregar_subservicio(NodoServicio(nombre_subservicio))
                    return
            # Si no existe el servicio principal, lo agregamos junto con su subservicio
            nuevo_servicio.agregar_subservicio(NodoServicio(nombre_subservicio))
            self.servicios.append(nuevo_servicio)

    def obtener_lista_servicios(self):
        lista_servicios = []
        
        # Agregar todos los servicios y subservicios
        for servicio in self.servicios:
            lista_servicios.append(servicio.nombre)  # Servicio principal
            for subservicio in servicio.subservicios:
                lista_servicios.append(f"  - {subservicio.nombre}")  # Subservicio con sangría
        return lista_servicios

# Ejemplo de uso
arbol_servicios = ArbolServicios()
arbol_servicios.agregar_servicio("Servicio1", "Subservicio1")
arbol_servicios.agregar_servicio("Servicio1", "Subservicio2")
arbol_servicios.agregar_servicio("Servicio2")

# Obtener lista de servicios y subservicios
for servicio in arbol_servicios.obtener_lista_servicios():
    print(servicio)