import flet as ft

class MenuPrincipal:
    def __init__(self, page, registro_cls, login_factory):
        self.page = page
        self.registro_cls = registro_cls
        self.login_factory = login_factory

    def mostrar(self):
        self.page.clean()
        self.page.add(
            ft.Column(
                [
                    ft.Text("Menú Principal", size=20, weight=ft.FontWeight.BOLD),
                    ft.ElevatedButton("Registro de Usuario", on_click=lambda e: self.registro_cls(self.page).mostrar()),
                    ft.ElevatedButton("Iniciar Sesión", on_click=lambda e: self.login_factory(self.page).mostrar()),
                ]
            )
        )
        self.page.update()