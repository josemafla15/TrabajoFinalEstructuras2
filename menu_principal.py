import flet as ft

class MenuPrincipal:
    def __init__(self, page, registro_cls, login_cls):
        self.page = page
        self.registro_cls = registro_cls
        self.login_cls = login_cls

    def mostrar(self):
        self.page.clean()
        self.page.add(
            ft.Column(
                [
                    ft.Text("Bienvenido al Sistema", size=24, weight=ft.FontWeight.BOLD),
                    ft.ElevatedButton("Registrar nuevo usuario", on_click=self.abrir_registro),
                    ft.ElevatedButton("Iniciar sesión", on_click=self.abrir_login),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        self.page.update()

    def abrir_registro(self, e):
        self.registro_cls(self.page).mostrar()

    def abrir_login(self, e):
        self.login_cls(self.page).mostrar()