# gestor_cliente.py
from cliente import Cliente

class GestorCliente:
    def __init__(self):
        self.clientes_prioritarios = []  # Lista de clientes prioritarios
        self.clientes_cola = []  # Cola regular de clientes
        self.diccionario_clientes = {}  # Diccionario de clientes por ID
        self.historial_pila = []  # Historial de clientes atendidos

    # Método para agregar cliente
    def agregar_cliente(self, cliente):
        if cliente.es_prioritario:
            self.clientes_prioritarios.append(cliente)  # Agregar a la lista de prioritarios
            print(f"Cliente prioritario {cliente.nombre} agregado a la lista de atención.")
        else:
            self.clientes_cola.append(cliente)  # Agregar a la cola regular
            print(f"Cliente {cliente.nombre} agregado a la cola de espera.")

        self.diccionario_clientes[cliente.id_cliente] = cliente  # Guardar cliente en el diccionario

    # Método para atender cliente
    def atender_cliente(self):
        if self.clientes_prioritarios:
            cliente = self.clientes_prioritarios.pop()  # Atender el último prioritario
        elif self.clientes_cola:
            cliente = self.clientes_cola.pop(0)  # Atender el primero de la cola
        else:
            print("No hay clientes en espera.")
            return None
        
        self.historial_pila.append(cliente)  # Guardar el cliente en el historial de atención
        print(f"Cliente {cliente.nombre} atendido.")
        return cliente