class Nodoservice:
    def __init__(self, name, description=None):
        self.name = name
        self.description = description
        self.subservices = []  # Lista para los subservices

    def agregar_subservicio(self, subservicio):
        # Evitar duplicados
        for s in self.subservices:
            if s.name == subservicio.name:
                return  # No agregar duplicado
        self.subservices.append(subservicio)

class TreeServices:
    def __init__(self):
        self.raiz = Nodoservice("services")
        self.services = []

    def append_service(self, name_servicio, description=None):
        # Agregar un servicio a la lista
        nuevo_servicio = Nodoservice(name_servicio, description)
        self.services.append(nuevo_servicio)
        return nuevo_servicio  # Devuelve el servicio recién creado para poder agregarle subservices

    def obtener_lista_services(self):
        lista_services = []
        for servicio in self.services:
            lista_services.append(servicio.name)  # Solo el name
            for subservicio in servicio.subservices:
                lista_services.append(f"{servicio.name} > {subservicio.name}")  # Incluye subservices
        return lista_services

# Ejemplo de uso
tree_services = TreeServices()

# Crear services y subservices
tree_services.append_service("Servicio1", "Subservicio1")
tree_services.append_service("Servicio1", "Subservicio2")
tree_services.append_service("Servicio2")

# Obtener lista de services y subservices
for servicio in tree_services.obtener_lista_services():
    print(servicio)