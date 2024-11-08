import flet as ft
from ventana_servicios import VentanaServicios

class MenuOpciones:
    def __init__(self, page, callback_clientes, callback_sucursales, callback_servicios):
        self.page = page
        self.callback_clientes = callback_clientes
        self.callback_sucursales = callback_sucursales
        self.callback_servicios = callback_servicios
        # Añadimos la instancia de servicios para que se reutilice
        self.ventana_servicios = None

    def mostrar(self):
        self.page.clean()
        self.page.title = "Menú de Opciones"

        # Botones para gestionar diferentes ventanas
        self.page.add(
            ft.Column(
                [
                    ft.ElevatedButton("Gestión de Clientes", on_click=self.callback_clientes),
                    ft.ElevatedButton("Gestión de Sucursales", on_click=self.callback_sucursales),
                    ft.ElevatedButton("Gestión de Servicios", on_click=self.manejar_servicios)
                ]
            )
        )
        self.page.update()

    def manejar_servicios(self, e):
        # Reutilizar la instancia si ya existe, sino crearla
        if self.ventana_servicios is None:
            self.ventana_servicios = VentanaServicios(self.page, self)
        self.ventana_servicios.mostrar()