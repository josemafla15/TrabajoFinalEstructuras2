import flet as ft
from ventana_bienvenida import VentanaBienvenida

import sys  # Necesario para usar sys.exit()

class MenuOpciones:
    def __init__(self, page, manage_clients, manage_branches):
        self.page = page
        self.manage_clients = manage_clients
        self.manage_branches = manage_branches

    def view(self):
        self.page.clean()
        self.page.add(
            ft.Column(
                [
                    ft.Text("Menú de Opciones", size=20, weight=ft.FontWeight.BOLD),
                    ft.ElevatedButton("Gestionar Clientes", on_click=self.manage_clients),
                    ft.ElevatedButton("Gestionar Sucursales", on_click=self.manage_branches),
                    ft.ElevatedButton("Salir", on_click=self.salir),
                ]
            )
        )
        self.page.update()

    def salir(self, e):
        self.page.window_close()