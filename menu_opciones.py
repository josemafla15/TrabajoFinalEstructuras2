import flet as ft
from ventana_bienvenida import VentanaBienvenida

import sys  # Necesario para usar sys.exit()

class MenuOpciones:
    def __init__(self, page, manejar_clientes, manejar_sucursales):
        self.page = page
        self.manejar_clientes = manejar_clientes
        self.manejar_sucursales = manejar_sucursales

    def mostrar(self):
        self.page.clean()
        self.page.add(
            ft.Column(
                [
                    ft.Text("Menú de Opciones", size=20, weight=ft.FontWeight.BOLD),
                    ft.ElevatedButton("Gestionar Clientes", on_click=self.manejar_clientes),
                    ft.ElevatedButton("Gestionar Sucursales", on_click=self.manejar_sucursales),
                    ft.ElevatedButton("Salir", on_click=self.salir),
                ]
            )
        )
        self.page.update()

    def salir(self, e):
        self.page.window_close()