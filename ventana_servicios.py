import flet as ft
from modelos_servicios import NodoServicio, ArbolServicios

class VentanaServicios:
    def __init__(self, page: ft.Page, menu_opciones):
        self.page = page
        self.menu_opciones = menu_opciones
        self.page.title = "Gestión de Servicios"
        
        # Crear el árbol de servicios
        self.arbol_servicios = ArbolServicios()

        # Elementos de la interfaz para agregar servicio y subservicios
        self.servicio_nombre_input = ft.TextField(label="Nombre del Servicio", width=200)
        self.servicio_descripcion_input = ft.TextField(label="Descripción del Servicio", width=200)
        self.subservicio_nombre_input = ft.TextField(label="Nombre del Subservicio", width=200)
        self.subservicio_descripcion_input = ft.TextField(label="Descripción del Subservicio", width=200)
        
        self.agregar_servicio_button = ft.ElevatedButton("Agregar Servicio", on_click=self.agregar_servicio)
        self.mensaje_servicio = ft.Column()

        # Elementos para mostrar los servicios agregados
        self.mostrar_servicios_button = ft.ElevatedButton("Ver Servicios", on_click=self.mostrar_servicios)
        self.lista_servicios = ft.Column()

        # Botón para volver al Menú de Opciones
        self.volver_button = ft.ElevatedButton("Volver al Menú de Opciones", on_click=self.volver_menu)

    def mostrar(self):
        # Limpiar la página antes de añadir la nueva interfaz
        self.page.clean()

        # Añadir los controles de la ventana de servicios
        self.page.add(
            ft.Row([  # Row para organizar las columnas
                ft.Column([  # Columna para agregar servicio
                    self.servicio_nombre_input,
                    self.servicio_descripcion_input,
                    self.subservicio_nombre_input,
                    self.subservicio_descripcion_input,
                    self.agregar_servicio_button,
                    self.mensaje_servicio,
                    self.mostrar_servicios_button
                ], width=300),
                ft.Column([  # Columna para ver los servicios
                    self.lista_servicios
                ], width=400)
            ]),
            self.volver_button  # Botón para volver al menú de opciones
        )
        self.page.update()

    def agregar_servicio(self, e):
        nombre_servicio = self.servicio_nombre_input.value
        descripcion_servicio = self.servicio_descripcion_input.value
        nombre_subservicio = self.subservicio_nombre_input.value
        descripcion_subservicio = self.subservicio_descripcion_input.value
    
        if nombre_servicio and descripcion_servicio:
            # Aquí se crea el nodo de servicio con nombre y descripción
            servicio = NodoServicio(nombre_servicio, descripcion_servicio)
    
            if nombre_subservicio and descripcion_subservicio:
                # Crear un subservicio si se proporcionan estos datos
                subservicio = NodoServicio(nombre_subservicio, descripcion_subservicio)
                servicio.agregar_subservicio(subservicio)
    
            # Agregar el servicio al árbol
            self.arbol_servicios.agregar_servicio(servicio)
    
            self.mensaje_servicio.controls.append(ft.Text(f"Servicio '{nombre_servicio}' agregado."))
            if nombre_subservicio:
                self.mensaje_servicio.controls.append(ft.Text(f"  - Subservicio '{nombre_subservicio}' agregado."))
    
        else:
            self.mensaje_servicio.controls.append(ft.Text("Debe ingresar un nombre y una descripción para el servicio.", color="red"))
        
        self.page.update()

    def mostrar_servicios(self, e):
        self.lista_servicios.controls.clear()

        if not self.arbol_servicios.servicios:
            self.lista_servicios.controls.append(ft.Text("No hay servicios disponibles."))
        else:
            for servicio in self.arbol_servicios.servicios:
                self.lista_servicios.controls.append(ft.Text(f"Servicio: {servicio.nombre} - {servicio.descripcion}"))
                for subservicio in servicio.subservicios:
                    self.lista_servicios.controls.append(ft.Text(f"  - Subservicio: {subservicio.nombre} - {subservicio.descripcion}"))

        self.page.update()

    def volver_menu(self, e):
        # Volver al menú de opciones y limpiar la página
        self.page.clean()
        self.menu_opciones.mostrar()