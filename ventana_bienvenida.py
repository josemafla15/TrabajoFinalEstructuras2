import flet as ft
from modelos_servicios import ArbolServicios, NodoServicio

class VentanaBienvenida:
    def __init__(self, page: ft.Page, arbol_servicios: ArbolServicios):
        self.page = page
        self.page.clean()
        self.page.title = "Bienvenido al Sistema Bancario"
        self.arbol_servicios = arbol_servicios

        # Elementos de la interfaz
        self.id_input = ft.TextField(label="ID Cliente", width=150)
        self.nombre_input = ft.TextField(label="Nombre Cliente", width=200)
        self.prioritario_checkbox = ft.Checkbox(label="¿Es prioritario?")
        self.servicio_input = ft.TextField(label="Tipo de Servicio", width=200)  # Campo de texto para servicio
        self.mensajes = ft.Column()
        self.agregar_button = ft.ElevatedButton("Agregar Cliente", on_click=self.agregar_cliente)
        self.atender_button = ft.ElevatedButton("Atender Cliente", on_click=self.atender_cliente)

        # Layout
        self.page.add(
            ft.Row([ 
                ft.Column([
                    self.id_input,
                    self.nombre_input,
                    self.prioritario_checkbox,
                    self.servicio_input,  # Mostrar el campo de texto para servicio
                    self.agregar_button,
                    self.atender_button
                ], width=300),
                ft.Column([self.mensajes], width=400)
            ])
        )

        # Cargar servicios disponibles en el mensaje
        if self.arbol_servicios.servicios:
            self.mensajes.controls.append(ft.Text("Servicios disponibles:"))
            for servicio in self.arbol_servicios.servicios:
                self.mensajes.controls.append(ft.Text(f"- {servicio.nombre}"))
        else:
            self.mensajes.controls.append(ft.Text("No hay servicios disponibles.", color="red"))

        self.page.update()

    def mostrar(self):
        self.page.update()

    def agregar_cliente(self, e):
        id_cliente = self.id_input.value
        nombre_cliente = self.nombre_input.value
        es_prioritario = self.prioritario_checkbox.value
        tipo_servicio = self.servicio_input.value

        # Validar que el servicio ingresado esté en la lista de servicios
        servicio = next((s for s in self.arbol_servicios.servicios if s.nombre.lower() == tipo_servicio.lower()), None)

        if servicio:
            self.mensajes.controls.append(ft.Text(f"Cliente {nombre_cliente} agregado con servicio {servicio.nombre}."))
        else:
            self.mensajes.controls.append(ft.Text("Servicio no encontrado. Intente nuevamente.", color="red"))

        self.page.update()

    def atender_cliente(self, e):
        self.mensajes.controls.append(ft.Text("Atendiendo al cliente..."))
        self.page.update()