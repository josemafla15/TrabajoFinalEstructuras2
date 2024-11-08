import flet as ft
from gestor_usuarios import gestor_usuarios
from menu_principal import MenuPrincipal
from menu_opciones import MenuOpciones
from ventana_bienvenida import VentanaBienvenida
from ventana_servicios import VentanaServicios
from modelos_servicios import ArbolServicios, NodoServicio

class Registro:
    def __init__(self, page):
        self.page = page
        self.id_input = ft.TextField(label="ID de Usuario", width=200)
        self.contraseña_input = ft.TextField(label="Contraseña", password=True, width=200)
        self.mensajes = ft.Column()

    def mostrar(self):
        self.page.clean()
        self.page.add(
            ft.Column(
                [
                    ft.Text("Registro de Usuario", size=20, weight=ft.FontWeight.BOLD),
                    self.id_input,
                    self.contraseña_input,
                    ft.ElevatedButton("Registrar", on_click=self.registrar_usuario),
                    ft.ElevatedButton("Volver al menú", on_click=self.volver_menu),
                    self.mensajes,
                ]
            )
        )
        self.page.update()

    def registrar_usuario(self, e):
        id_usuario = self.id_input.value
        contraseña_usuario = self.contraseña_input.value
        if gestor_usuarios.registrar_usuario(id_usuario, contraseña_usuario):
            self.mensajes.controls.append(ft.Text("Usuario registrado exitosamente.", color="green"))
            self.id_input.value = ""
            self.contraseña_input.value = ""
        else:
            self.mensajes.controls.append(ft.Text("El ID ya está registrado. Intente con otro.", color="red"))
        self.page.update()

    def volver_menu(self, e):
        MenuPrincipal(self.page, Registro, Login).mostrar()

class Login:
    def __init__(self, page):
        self.page = page
        self.arbol_servicios = ArbolServicios()  # Instancia del árbol de servicios
        self.id_input = ft.TextField(label="ID de Usuario", width=200)
        self.contraseña_input = ft.TextField(label="Contraseña", password=True, width=200)
        self.mensajes = ft.Column()

    def mostrar(self):
        self.page.clean()
        self.page.add(
            ft.Column(
                [
                    ft.Text("Inicio de Sesión", size=20, weight=ft.FontWeight.BOLD),
                    self.id_input,
                    self.contraseña_input,
                    ft.ElevatedButton("Iniciar sesión", on_click=self.realizar_login),
                    ft.ElevatedButton("Volver al menú", on_click=self.volver_menu),
                    self.mensajes,
                ]
            )
        )
        self.page.update()

    def realizar_login(self, e):
        id_usuario = self.id_input.value
        contraseña_usuario = self.contraseña_input.value
        if gestor_usuarios.verificar_usuario(id_usuario, contraseña_usuario):
            self.redirigir_a_menu_opciones()
        else:
            self.mensajes.controls.append(ft.Text("ID o contraseña incorrectos.", color="red"))
        self.page.update()

    def redirigir_a_menu_opciones(self):
        menu_opciones = MenuOpciones(self.page, self.manejar_clientes, self.manejar_sucursales, self.manejar_servicios)
        menu_opciones.mostrar()

    def manejar_clientes(self, e):
        ventana_bienvenida = VentanaBienvenida(self.page, self.arbol_servicios)
        ventana_bienvenida.mostrar()

    def manejar_sucursales(self, e):
        print("Opción de sucursales seleccionada.")

    def manejar_servicios(self, e):
        ventana_servicios = VentanaServicios(self.page)
        ventana_servicios.mostrar()

    def volver_menu(self, e):
        MenuPrincipal(self.page, Registro, Login).mostrar()

def main(page: ft.Page):
    page.title = "Sistema de Registro y Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Crear y agregar servicios al árbol
    arbol_servicios = ArbolServicios()

    # Crear servicios
    servicio1 = NodoServicio("Servicio1", "Descripción del servicio 1")
    arbol_servicios.agregar_servicio(servicio1)

    servicio2 = NodoServicio("Servicio2", "Descripción del servicio 2")
    arbol_servicios.agregar_servicio(servicio2)

    # Crear subservicios para el primer servicio
    subservicio1 = NodoServicio("Subservicio1", "Descripción del subservicio 1")
    servicio1.agregar_subservicio(subservicio1)

    MenuPrincipal(page, Registro, Login).mostrar()

ft.app(target=main)