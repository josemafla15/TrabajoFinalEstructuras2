import flet as ft
from cliente import Cliente
from gestor_cliente import GestorCliente

class VentanaBienvenida:
    def __init__(self, page, arbol_servicios):
        self.page = page
        self.arbol_servicios = arbol_servicios  # Instancia del árbol de servicios
        self.gestor_cliente = GestorCliente()

        # Campos de entrada
        self.cliente_input = ft.TextField(label="Nombre del Cliente", width=200)
        self.id_input = ft.TextField(label="ID del Cliente", width=200)
        self.es_prioritario_checkbox = ft.Checkbox(label="Cliente Prioritario")
        self.servicio_input = ft.Dropdown(label="Seleccione un Servicio", width=200)
        self.mensajes = ft.Column()

        # Cargar los servicios disponibles en el dropdown
        self.cargar_servicios()

    def cargar_servicios(self):
        # Limpiar las opciones previas del dropdown
        self.servicio_input.options.clear()

        # Obtener los servicios y subservicios
        lista_servicios = self.arbol_servicios.obtener_lista_servicios()

        # Agregar las opciones al Dropdown
        for servicio in lista_servicios:
            # Agregar cada servicio y subservicio como una opción
            self.servicio_input.options.append(ft.dropdown.Option(servicio))

        # Actualizar la página después de agregar las opciones
        self.page.update()

    def mostrar(self):
        # Limpiar la página antes de agregar los controles
        self.page.clean()

        # Agregar la columna de controles a la página
        self.page.add(
            ft.Column(
                [
                    ft.Text("Bienvenido a la Gestión de Clientes", size=20, weight=ft.FontWeight.BOLD),
                    self.cliente_input,
                    self.id_input,
                    self.es_prioritario_checkbox,
                    self.servicio_input,
                    ft.ElevatedButton("Agregar Cliente", on_click=self.agregar_cliente),
                    ft.ElevatedButton("Atender Cliente", on_click=self.atender_cliente),
                    self.mensajes,
                ]
            )
        )

        # Actualizar la página después de agregar los controles
        self.page.update()

    def agregar_cliente(self, e):
        nombre_cliente = self.cliente_input.value.strip()
        id_cliente = self.id_input.value.strip()
        es_prioritario = self.es_prioritario_checkbox.value
        servicio_seleccionado = self.servicio_input.value
        
        # Verificar que el nombre, ID y servicio estén seleccionados
        if not nombre_cliente or not id_cliente:
            self.mensajes.controls.append(
                ft.Text("Por favor, ingrese el nombre y el ID del cliente.", color="red")
            )
        elif not servicio_seleccionado:
            self.mensajes.controls.append(
                ft.Text("Por favor, seleccione un servicio.", color="red")
            )
        else:
            # Crear el cliente solo si los campos están completos
            cliente = Cliente(nombre_cliente, id_cliente, es_prioritario)
            cliente.servicio = servicio_seleccionado  # Asignar servicio al cliente
        
            self.gestor_cliente.agregar_cliente(cliente)
        
            # Limpiar campos después de agregar el cliente
            self.cliente_input.value = ""
            self.id_input.value = ""
            self.es_prioritario_checkbox.value = False
            self.servicio_input.value = None
        
            self.mensajes.controls.append(
                ft.Text(f"Cliente {nombre_cliente} agregado con ID {id_cliente}.", color="green")
            )
        
        # Actualizar la interfaz
        self.page.update()

    def atender_cliente(self, e):
        # Atender al siguiente cliente
        cliente = self.gestor_cliente.atender_cliente()

        if cliente:
            # Mostrar mensaje de éxito si hay un cliente atendido
            self.mensajes.controls.append(
                ft.Text(f"Cliente {cliente.nombre} atendido. Servicio seleccionado: {cliente.servicio}.", color="green")
            )
        else:
            # Mostrar mensaje de error si no hay clientes en espera
            self.mensajes.controls.append(
                ft.Text("No hay clientes en espera.", color="red")
            )

        # Actualizar la página después de atender al cliente
        self.page.update()