# gestor_cliente.py
from cliente import Cliente

class GestorCliente:
    def __init__(self):
        self.clientis_prioritarys = []  # Lista de clientes prioritarios
        self.clients_queue = []  # Cola regular de clientes
        self.clients_diccionary = {}  # Diccionario de clientes por ID
        self.stack_record = []  # Historial de clientes atendidos

    # Método para agregar cliente
    def append_client(self, cliente):
        if cliente.is_prioritary:
            self.clientis_prioritarys.append(cliente)  # Agregar a la lista de prioritarios
            print(f"Cliente prioritario {cliente.name} agregado a la lista de atención.")
        else:
            self.clients_queue.append(cliente)  # Agregar a la cola regular
            print(f"Cliente {cliente.name} agregado a la cola de espera.")

        self.clients_diccionary[cliente.id_client] = cliente  # Guardar cliente en el diccionario

    # Método para atender cliente
    def attend_client(self):
        if self.clientis_prioritarys:
            cliente = self.clientis_prioritarys.pop()  # Atender el último prioritario
        elif self.clients_queue:
            cliente = self.clients_queue.pop(0)  # Atender el primero de la cola
        else:
            print("No hay clientes en espera.")
            return None
        
        self.stack_record.append(cliente)  # Guardar el cliente en el historial de atención
        print(f"Cliente {cliente.name} atendido.")
        return cliente