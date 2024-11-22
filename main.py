import flet as ft
from gestor_usuarios import manager_user
from menu_principal import MenuPrincipal
from menu_opciones import MenuOpciones
from ventana_bienvenida import VentanaBienvenida
from frame_services import Ventanaservices
from models_services import TreeServices, Nodoservice
from grafoSucursales import GrafoSucursales
from ventana_sucursales import VentanaSucursales

# Clase de Registro
class Registro:
    def __init__(self, page):
        self.page = page
        self.id_input = ft.TextField(label="ID de Usuario", width=200)
        self.password_input = ft.TextField(label="password", password=True, width=200)
        self.messages = ft.Column()

    def view(self):
        self.page.clean()
        self.page.add(
            ft.Column(
                [
                    ft.Text("Registro de Usuario", size=20, weight=ft.FontWeight.BOLD),
                    self.id_input,
                    self.password_input,
                    ft.ElevatedButton("Registrar", on_click=self.register_user),
                    ft.ElevatedButton("Volver al menú", on_click=self.volver_menu),
                    self.messages,
                ]
            )
        )
        self.page.update()

    def register_user(self, e):
        id_usuario = self.id_input.value
        password_usuario = self.password_input.value
        if manager_user.register_user(id_usuario, password_usuario):
            self.messages.controls.append(ft.Text("Usuario registrado exitosamente.", color="green"))
            self.id_input.value = ""
            self.password_input.value = ""
        else:
            self.messages.controls.append(ft.Text("El ID ya está registrado. Intente con otro.", color="red"))
        self.page.update()

    def volver_menu(self, e):
        # Usamos lambda para pasar el arbol de services correctamente al Login
        MenuPrincipal(self.page, Registro, lambda p: Login(p, tree_services, grafo_sucursales)).view()

class Login:
    def __init__(self, page, tree_services, grafo_sucursales):
        self.page = page
        self.tree_services = tree_services  # Instancia del árbol de services
        self.grafo_sucursales = grafo_sucursales  # Instancia del grafo de sucursales
        self.id_input = ft.TextField(label="ID de Usuario", width=200)
        self.password_input = ft.TextField(label="password", password=True, width=200)
        self.messages = ft.Column()

    def view(self):
        self.page.clean()
        self.page.add(
            ft.Column(
                [
                    ft.Text("Inicio de Sesión", size=20, weight=ft.FontWeight.BOLD),
                    self.id_input,
                    self.password_input,
                    ft.ElevatedButton("Iniciar sesión", on_click=self.realizar_login),
                    ft.ElevatedButton("Volver al menú", on_click=self.volver_menu),
                    self.messages,
                ]
            )
        )
        self.page.update()

    def realizar_login(self, e):
        id_usuario = self.id_input.value
        password_usuario = self.password_input.value
        if manager_user.check_user(id_usuario, password_usuario):
            self.redirigir_a_menu_opciones()
        else:
            self.messages.controls.append(ft.Text("ID o password incorrectos.", color="red"))
        self.page.update()

    def redirigir_a_menu_opciones(self):
        # Pasamos las funciones para gestionar clientes y sucursales
        menu_opciones = MenuOpciones(self.page, self.manage_clients, self.manage_branches)
        menu_opciones.view()

    def manage_clients(self, e):
        ventana_bienvenida = VentanaBienvenida(self.page, self.tree_services)
        ventana_bienvenida.view()

    def manage_branches(self, e):
        ventana_sucursales = VentanaSucursales(self.page, self.grafo_sucursales)
        ventana_sucursales.view()

    def volver_menu(self, e):
        # Usamos lambda para pasar el arbol de services y el grafo al Login
        MenuPrincipal(self.page, Registro, lambda p: Login(p, self.tree_services, self.grafo_sucursales)).view()

# Función principal
def main(page: ft.Page):
    page.title = "Sistema de Registro y Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Crear y agregar services al árbol
    global tree_services
    tree_services = TreeServices()

    # Crear servicio "Préstamos" y agregarlo al árbol
    prestamos = tree_services.append_service("Préstamos", "Descripción del servicio de préstamos")
    
    # Crear subservices para "Préstamos"
    prestamos_hipotecarios = Nodoservice("Préstamos Hipotecarios", "Subservicio de préstamos hipotecarios")
    prestamos_viajes = Nodoservice("Préstamos de Viajes", "Subservicio de préstamos para viajes")
    
    # Agregar los subservices a "Préstamos"
    prestamos.agregar_subservicio(prestamos_hipotecarios)
    prestamos.agregar_subservicio(prestamos_viajes)

    # Crear servicio "Tarjetas de Crédito" y agregarlo al árbol
    tarjetas_credito = tree_services.append_service("Tarjetas de Crédito", "Descripción del servicio de tarjetas de crédito")

    # Crear el grafo de sucursales
    global grafo_sucursales
    grafo_sucursales = GrafoSucursales()

    # Crear el menú principal pasando el árbol de services y el grafo al Login
    MenuPrincipal(page, Registro, lambda p: Login(p, tree_services, grafo_sucursales)).view()

ft.app(target=main)