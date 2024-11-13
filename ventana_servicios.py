import flet as ft
from modelos_servicios import ArbolServicios, NodoServicio

class VentanaServicios:
    def __init__(self, page, arbol_servicios: ArbolServicios):
        self.page = page
        self.arbol_servicios = arbol_servicios
        self.page.clean()
        self.page.title = "Gestión de Servicios"

    def mostrar(self):
        self.page.add(ft.Text("Servicios disponibles:"))

        # Mostrar servicios directamente del árbol
        for servicio in self.arbol_servicios.servicios:
            self.page.add(ft.Text(f"- {servicio.nombre}"))

        self.page.update()