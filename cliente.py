class Cliente:
    def __init__(self, nombre, id_cliente, es_prioritario=False):
        self.nombre = nombre
        self.id_cliente = id_cliente
        self.es_prioritario = es_prioritario
        self.servicios = []

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)