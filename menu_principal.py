import flet as ft

class MenuPrincipal:
    def __init__(self, page, register_cls, login_factory):
        self.page = page
        self.register_cls = register_cls
        self.login_factory = login_factory

    def view(self):
        self.page.clean()
        self.page.add(
            ft.Column(
                [
                    ft.Text("Menú Principal", size=20, weight=ft.FontWeight.BOLD),
                    ft.ElevatedButton("Registro de Usuario", on_click=lambda e: self.register_cls(self.page).view()),
                    ft.ElevatedButton("Iniciar Sesión", on_click=lambda e: self.login_factory(self.page).view()),
                ]
            )
        )
        self.page.update()