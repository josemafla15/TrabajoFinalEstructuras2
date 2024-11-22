import flet as ft
from grafoSucursales import GrafoSucursales
from menu_opciones import *

class VentanaSucursales:
    def __init__(self, page, grafo_sucursales, manage_clients, manage_branches):
        self.page = page
        self.grafo_sucursales = grafo_sucursales
        self.manage_clients = manage_clients
        self.manage_branches = manage_branches

        # Controles de la interfaz
        self.sucursal_input = ft.TextField(label="Nombre de la Sucursal", width=200)
        self.sucursal1_input = ft.Dropdown(label="Sucursal 1", width=200)
        self.sucursal2_input = ft.Dropdown(label="Sucursal 2", width=200)
        self.distancia_input = ft.TextField(label="Distancia (km)", width=200)
        self.messages = ft.Column()

        # Cargar opciones iniciales
        self.cargar_opciones()

    def cargar_opciones(self):
        self.sucursal1_input.options.clear()
        self.sucursal2_input.options.clear()

        for sucursal in self.grafo_sucursales.sucursales.keys():
            self.sucursal1_input.options.append(ft.dropdown.Option(sucursal))
            self.sucursal2_input.options.append(ft.dropdown.Option(sucursal))

    def view(self):
        self.page.clean()
        self.page.add(
            ft.Column(
                [
                    ft.Text("Gestión de Sucursales", size=20, weight=ft.FontWeight.BOLD),
                    self.sucursal_input,
                    ft.ElevatedButton("Agregar Sucursal", on_click=self.append_branch),
                    self.sucursal1_input,
                    self.sucursal2_input,
                    self.distancia_input,
                    ft.ElevatedButton("Conectar Sucursales", on_click=self.conect_branches),
                    ft.ElevatedButton("Ver Conexiones", on_click=self.view_conexiones),
                    ft.ElevatedButton("Volver al Menú", on_click=self.volver_menu),
                    self.messages,
                ]
            )
        )
        self.page.update()

    def append_branch(self, e):
        name_sucursal = self.sucursal_input.value.strip()
        if name_sucursal:
            if self.grafo_sucursales.append_branch(name_sucursal):
                self.messages.controls.append(ft.Text(f"Sucursal '{name_sucursal}' agregada exitosamente.", color="green"))
                self.cargar_opciones()
            else:
                self.messages.controls.append(ft.Text(f"La sucursal '{name_sucursal}' ya existe.", color="red"))
        else:
            self.messages.controls.append(ft.Text("El nombre de la sucursal no puede estar vacío.", color="red"))
        self.page.update()

    def conect_branches(self, e):
        sucursal1 = self.sucursal1_input.value
        sucursal2 = self.sucursal2_input.value
        try:
            distancia = float(self.distancia_input.value)
        except ValueError:
            self.messages.controls.append(ft.Text("Por favor, ingrese una distancia válida.", color="red"))
            self.page.update()
            return

        if sucursal1 and sucursal2 and distancia > 0:
            if self.grafo_sucursales.conect_branches(sucursal1, sucursal2, distancia):
                self.messages.controls.append(ft.Text(f"Sucursales '{sucursal1}' y '{sucursal2}' conectadas exitosamente.", color="green"))
            else:
                self.messages.controls.append(ft.Text("Las sucursales seleccionadas no existen.", color="red"))
        else:
            self.messages.controls.append(ft.Text("Complete todos los campos antes de conectar sucursales.", color="red"))
        self.page.update()

    def view_conexiones(self, e):
        conexiones = self.grafo_sucursales.get_conections()
        self.messages.controls.clear()
        self.messages.controls.append(ft.Text("Conexiones entre sucursales:", weight=ft.FontWeight.BOLD))
        for sucursal, vecinos in conexiones.items():
            for vecino, distancia in vecinos.items():
                self.messages.controls.append(ft.Text(f"{sucursal} -> {vecino}: {distancia} km", color="blue"))
        self.page.update()

    def volver_menu(self, e):
        # Redirigir al menú principal
        menu_opciones = MenuOpciones(self.page, self.manage_clients, self.manage_branches)
        menu_opciones.view()