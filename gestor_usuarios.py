from usuario import Usuario

class GestorUsuarios:
    def __init__(self):
        self.usuarios_registrados = {}

    def registrar_usuario(self, id_usuario, contraseña):
        if id_usuario in self.usuarios_registrados:
            return False
        self.usuarios_registrados[id_usuario] = Usuario(id_usuario, contraseña)
        return True

    def verificar_usuario(self, id_usuario, contraseña):
        usuario = self.usuarios_registrados.get(id_usuario)
        return usuario is not None and usuario.contraseña == contraseña

# Instancia global del gestor de usuarios
gestor_usuarios = GestorUsuarios() 