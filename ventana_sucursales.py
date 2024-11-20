import flet as ft
from grafoSucursales import GrafoSucursales

class VentanaSucursales:
    def __init__(self, page, grafo_sucursales):
        self.page = page
        self.grafo_sucursales = grafo_sucursales

        # Controles de la interfaz
        self.sucursal_input = ft.TextField(label="Nombre de la Sucursal", width=200)
        self.sucursal1_input = ft.Dropdown(label="Sucursal 1", width=200)
        self.sucursal2_input = ft.Dropdown(label="Sucursal 2", width=200)
        self.distancia_input = ft.TextField(label="Distancia (km)", width=200)
        self.mensajes = ft.Column()

        # Cargar opciones iniciales
        self.cargar_opciones()

    def cargar_opciones(self):
        self.sucursal1_input.options.clear()
        self.sucursal2_input.options.clear()

        for sucursal in self.grafo_sucursales.sucursales.keys():
            self.sucursal1_input.options.append(ft.dropdown.Option(sucursal))
            self.sucursal2_input.options.append(ft.dropdown.Option(sucursal))

    def mostrar(self):
        self.page.clean()
        self.page.add(
            ft.Column(
                [
                    ft.Text("Gestión de Sucursales", size=20, weight=ft.FontWeight.BOLD),
                    self.sucursal_input,
                    ft.ElevatedButton("Agregar Sucursal", on_click=self.agregar_sucursal),
                    self.sucursal1_input,
                    self.sucursal2_input,
                    self.distancia_input,
                    ft.ElevatedButton("Conectar Sucursales", on_click=self.conectar_sucursales),
                    ft.ElevatedButton("Mostrar Conexiones", on_click=self.mostrar_conexiones),
                    self.mensajes,
                ]
            )
        )
        self.page.update()

    def agregar_sucursal(self, e):
        nombre_sucursal = self.sucursal_input.value.strip()
        if nombre_sucursal:
            if self.grafo_sucursales.agregar_sucursal(nombre_sucursal):
                self.mensajes.controls.append(ft.Text(f"Sucursal '{nombre_sucursal}' agregada exitosamente.", color="green"))
                self.cargar_opciones()
            else:
                self.mensajes.controls.append(ft.Text(f"La sucursal '{nombre_sucursal}' ya existe.", color="red"))
        else:
            self.mensajes.controls.append(ft.Text("El nombre de la sucursal no puede estar vacío.", color="red"))
        self.page.update()

    def conectar_sucursales(self, e):
        sucursal1 = self.sucursal1_input.value
        sucursal2 = self.sucursal2_input.value
        try:
            distancia = float(self.distancia_input.value)
        except ValueError:
            self.mensajes.controls.append(ft.Text("Por favor, ingrese una distancia válida.", color="red"))
            self.page.update()
            return

        if sucursal1 and sucursal2 and distancia > 0:
            if self.grafo_sucursales.conectar_sucursales(sucursal1, sucursal2, distancia):
                self.mensajes.controls.append(ft.Text(f"Sucursales '{sucursal1}' y '{sucursal2}' conectadas exitosamente.", color="green"))
            else:
                self.mensajes.controls.append(ft.Text("Las sucursales seleccionadas no existen.", color="red"))
        else:
            self.mensajes.controls.append(ft.Text("Complete todos los campos antes de conectar sucursales.", color="red"))
        self.page.update()

    def mostrar_conexiones(self, e):
        conexiones = self.grafo_sucursales.obtener_conexiones()
        self.mensajes.controls.clear()
        self.mensajes.controls.append(ft.Text("Conexiones entre sucursales:", weight=ft.FontWeight.BOLD))
        for sucursal, vecinos in conexiones.items():
            for vecino, distancia in vecinos.items():
                self.mensajes.controls.append(ft.Text(f"{sucursal} -> {vecino}: {distancia} km", color="blue"))
        self.page.update()