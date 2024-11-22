import flet as ft
from models_services import TreeServices, Nodoservice

class Ventanaservices:
    def __init__(self, page, tree_services: TreeServices):
        self.page = page
        self.tree_services = tree_services
        self.page.clean()
        self.page.title = "Gestión de services"

    def view(self):
        self.page.add(ft.Text("services disponibles:"))

        # view services directamente del árbol
        for service in self.tree_services.services:
            self.page.add(ft.Text(f"- {service.name}"))

        self.page.update()