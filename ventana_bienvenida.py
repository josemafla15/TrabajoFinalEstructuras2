import flet as ft
from cliente import Cliente
from gestor_cliente import GestorCliente

class VentanaBienvenida:
    def __init__(self, page, tree_services):
        self.page = page
        self.tree_services = tree_services  # Instancia del árbol de services
        self.gestor_cliente = GestorCliente()

        # Campos de entrada
        self.cliente_input = ft.TextField(label="name del Cliente", width=200)
        self.id_input = ft.TextField(label="ID del Cliente", width=200)
        self.is_prioritary_checkbox = ft.Checkbox(label="Cliente Prioritario")
        self.servicio_input = ft.Dropdown(label="Seleccione un Servicio", width=200)
        self.messages = ft.Column()

        # Cargar los services disponibles en el dropdown
        self.cargar_services()

    def cargar_services(self):
        # Limpiar las opciones previas del dropdown
        self.servicio_input.options.clear()

        # Obtener los services y subservices
        lista_services = self.tree_services.obtener_lista_services()

        # Agregar las opciones al Dropdown
        for servicio in lista_services:
            # Agregar cada servicio y subservicio como una opción
            self.servicio_input.options.append(ft.dropdown.Option(servicio))

        # Actualizar la página después de agregar las opciones
        self.page.update()

    def view(self):
        # Limpiar la página antes de agregar los controles
        self.page.clean()

        # Agregar la columna de controles a la página
        self.page.add(
            ft.Column(
                [
                    ft.Text("Bienvenido a la Gestión de Clientes", size=20, weight=ft.FontWeight.BOLD),
                    self.cliente_input,
                    self.id_input,
                    self.is_prioritary_checkbox,
                    self.servicio_input,
                    ft.ElevatedButton("Agregar Cliente", on_click=self.append_client),
                    ft.ElevatedButton("Atender Cliente", on_click=self.attend_client),
                    self.messages,
                ]
            )
        )

        # Actualizar la página después de agregar los controles
        self.page.update()

    def append_client(self, e):
        name_cliente = self.cliente_input.value.strip()
        id_client = self.id_input.value.strip()
        is_prioritary = self.is_prioritary_checkbox.value
        servicio_seleccionado = self.servicio_input.value
        
        # Verificar que el name, ID y servicio estén seleccionados
        if not name_cliente or not id_client:
            self.messages.controls.append(
                ft.Text("Por favor, ingrese el name y el ID del cliente.", color="red")
            )
        elif not servicio_seleccionado:
            self.messages.controls.append(
                ft.Text("Por favor, seleccione un servicio.", color="red")
            )
        else:
            # Crear el cliente solo si los campos están completos
            cliente = Cliente(name_cliente, id_client, is_prioritary)
            cliente.servicio = servicio_seleccionado  # Asignar servicio al cliente
        
            self.gestor_cliente.append_client(cliente)
        
            # Limpiar campos después de agregar el cliente
            self.cliente_input.value = ""
            self.id_input.value = ""
            self.is_prioritary_checkbox.value = False
            self.servicio_input.value = None
        
            self.messages.controls.append(
                ft.Text(f"Cliente {name_cliente} agregado con ID {id_client}.", color="green")
            )
        
        # Actualizar la interfaz
        self.page.update()

    def attend_client(self, e):
        # Atender al siguiente cliente
        cliente = self.gestor_cliente.attend_client()

        if cliente:
            # view mensaje de éxito si hay un cliente atendido
            self.messages.controls.append(
                ft.Text(f"Cliente {cliente.name} atendido. Servicio seleccionado: {cliente.servicio}.", color="green")
            )
        else:
            # view mensaje de error si no hay clientes en espera
            self.messages.controls.append(
                ft.Text("No hay clientes en espera.", color="red")
            )

        # Actualizar la página después de atender al cliente
        self.page.update()