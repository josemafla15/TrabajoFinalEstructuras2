import flet as ft
from cliente import Cliente
from gestor_cliente import GestorCliente

class VentanaBienvenida:
    def __init__(self, page, arbol_servicios):
        self.page = page
        self.arbol_servicios = arbol_servicios
        self.gestor_cliente = GestorCliente()  # Crear una instancia de GestorCliente
        self.cliente_input = ft.TextField(label="Nombre del Cliente", width=200)
        self.id_input = ft.TextField(label="ID del Cliente", width=200)
        self.es_prioritario_checkbox = ft.Checkbox(label="Cliente Prioritario")  # Checkbox para cliente prioritario
        self.servicio_input = ft.Dropdown(label="Seleccione un Servicio", width=200)
        self.mensajes = ft.Column()

        # Cargar los servicios disponibles en el dropdown
        self.cargar_servicios()

    def cargar_servicios(self):
        # Limpiar el dropdown
        self.servicio_input.options.clear()

        # Cargar servicios del árbol en el dropdown
        for servicio in self.arbol_servicios.obtener_lista_servicios():
            self.servicio_input.options.append(ft.dropdown.Option(servicio))

        self.page.update()

    def mostrar(self):
        self.page.clean()
        self.page.add(
            ft.Column(
                [
                    ft.Text("Bienvenido a la Gestión de Clientes", size=20, weight=ft.FontWeight.BOLD),
                    self.cliente_input,
                    self.id_input,
                    self.es_prioritario_checkbox,  # Agregar checkbox a la interfaz
                    self.servicio_input,
                    ft.ElevatedButton("Agregar Cliente", on_click=self.agregar_cliente),
                    ft.ElevatedButton("Atender Cliente", on_click=self.atender_cliente),
                    self.mensajes,
                ]
            )
        )
        self.page.update()

    def agregar_cliente(self, e):
        nombre_cliente = self.cliente_input.value.strip()  # Eliminar espacios extras
        id_cliente = self.id_input.value.strip()  # Eliminar espacios extras
        es_prioritario = self.es_prioritario_checkbox.value  # Obtener el estado del checkbox
        servicio_seleccionado = self.servicio_input.value

        if nombre_cliente and id_cliente:
            cliente = Cliente(nombre_cliente, id_cliente, es_prioritario)
            if servicio_seleccionado:
                cliente.servicio = servicio_seleccionado  # Asignar servicio al cliente

            # Usamos el gestor_cliente para agregar al cliente en la cola o pila
            self.gestor_cliente.agregar_cliente(cliente)

            # Limpiar campos después de agregar el cliente
            self.cliente_input.value = ""
            self.id_input.value = ""
            self.es_prioritario_checkbox.value = False  # Desmarcar el checkbox
            self.servicio_input.value = None

            self.mensajes.controls.append(
                ft.Text(f"Cliente {nombre_cliente} agregado con ID {id_cliente}.", color="green")
            )
        else:
            self.mensajes.controls.append(ft.Text("Por favor, ingrese el nombre y el ID del cliente.", color="red"))

        self.page.update()

    def atender_cliente(self, e):
        cliente = self.gestor_cliente.atender_cliente()  # Obtener el cliente que será atendido

        if cliente:
            self.mensajes.controls.append(
                ft.Text(f"Cliente {cliente.nombre} atendido. Servicio seleccionado: {cliente.servicio}.", color="green")
            )
        else:
            self.mensajes.controls.append(
                ft.Text("No hay clientes en espera.", color="red")
            )
        
        self.page.update()