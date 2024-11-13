import flet as ft
from gestor_usuarios import gestor_usuarios
from menu_principal import MenuPrincipal
from menu_opciones import MenuOpciones
from ventana_bienvenida import VentanaBienvenida
from ventana_servicios import VentanaServicios
from modelos_servicios import ArbolServicios, NodoServicio

# Clase de Registro
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
        # Usamos lambda para pasar el arbol de servicios correctamente al Login
        MenuPrincipal(self.page, Registro, lambda p: Login(p, arbol_servicios)).mostrar()

class Login:
    def __init__(self, page, arbol_servicios):
        self.page = page
        self.arbol_servicios = arbol_servicios  # Instancia del árbol de servicios
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
        # Ahora solo pasamos los métodos para manejar clientes y sucursales
        menu_opciones = MenuOpciones(self.page, self.manejar_clientes, self.manejar_sucursales)
        menu_opciones.mostrar()

    def manejar_clientes(self, e):
        ventana_bienvenida = VentanaBienvenida(self.page, self.arbol_servicios)
        ventana_bienvenida.mostrar()

    def manejar_sucursales(self, e):
        print("Opción de sucursales seleccionada.")

    def volver_menu(self, e):
        # Usamos lambda para pasar el arbol de servicios correctamente al Login
        MenuPrincipal(self.page, Registro, lambda p: Login(p, self.arbol_servicios)).mostrar()

# Función principal
def main(page: ft.Page):
    page.title = "Sistema de Registro y Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Crear y agregar servicios al árbol
    global arbol_servicios
    arbol_servicios = ArbolServicios()

    # Crear servicio "Préstamos" y agregarlo al árbol
    prestamos = arbol_servicios.agregar_servicio("Préstamos", "Descripción del servicio de préstamos")
    
    # Crear subservicios para "Préstamos"
    prestamos_hipotecarios = NodoServicio("Préstamos Hipotecarios", "Subservicio de préstamos hipotecarios")
    prestamos_viajes = NodoServicio("Préstamos de Viajes", "Subservicio de préstamos para viajes")
    
    # Agregar los subservicios a "Préstamos"
    prestamos.agregar_subservicio(prestamos_hipotecarios)
    prestamos.agregar_subservicio(prestamos_viajes)

    # Crear servicio "Tarjetas de Crédito" y agregarlo al árbol
    tarjetas_credito = arbol_servicios.agregar_servicio("Tarjetas de Crédito", "Descripción del servicio de tarjetas de crédito")

    # Crear el menú principal pasando el árbol de servicios al Login
    MenuPrincipal(page, Registro, lambda p: Login(p, arbol_servicios)).mostrar()

ft.app(target=main)