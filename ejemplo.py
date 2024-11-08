import flet as ft

class VentanaPrincipal:
    def __init__(self, page):
        self.page = page

    def mostrar(self):
        # Limpiar la página
        self.page.clean()
        # Agregar el contenido de la ventana principal
        self.page.add(
            ft.Column(
                [
                    ft.Text("Ventana Principal", size=20),
                    ft.ElevatedButton(
                        "Ir a Ventana Secundaria", 
                        on_click=self.ir_a_ventana_secundaria
                    )
                ]
            )
        )
        self.page.update()

    def ir_a_ventana_secundaria(self, e):
        # Instancia y muestra la VentanaSecundaria
        ventana_secundaria = VentanaSecundaria(self.page)
        ventana_secundaria.mostrar()


class VentanaSecundaria:
    def __init__(self, page):
        self.page = page

    def mostrar(self):
        # Limpiar la página
        self.page.clean()
        # Agregar el contenido de la ventana secundaria
        self.page.add(
            ft.Column(
                [
                    ft.Text("Ventana Secundaria", size=20),
                    ft.ElevatedButton(
                        "Volver a Ventana Principal", 
                        on_click=self.volver_a_principal
                    )
                ]
            )
        )
        self.page.update()

    def volver_a_principal(self, e):
        # Instancia y muestra la VentanaPrincipal
        ventana_principal = VentanaPrincipal(self.page)
        ventana_principal.mostrar()


# Función principal para ejecutar la aplicación
def main(page: ft.Page):
    page.title = "Ejemplo de Navegación en Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Instancia y muestra la VentanaPrincipal
    ventana_principal = VentanaPrincipal(page)
    ventana_principal.mostrar()

# Ejecutar la aplicación
ft.app(target=main)