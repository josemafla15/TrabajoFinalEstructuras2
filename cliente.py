# cliente.py
class Cliente:
    def __init__(self, id_cliente, nombre, es_prioritario=False):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.historial_atencion = []
        self.es_prioritario = es_prioritario