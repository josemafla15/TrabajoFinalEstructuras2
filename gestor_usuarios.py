from usuario import Usuario

class GestorUsuarios:
    def __init__(self):
        self.usuarios_registrados = {}

    def register_user(self, id_usuario, password):
        if id_usuario in self.usuarios_registrados:
            return False
        self.usuarios_registrados[id_usuario] = Usuario(id_usuario, password)
        return True

    def check_user(self, id_usuario, password):
        usuario = self.usuarios_registrados.get(id_usuario)
        return usuario is not None and usuario.password == password

# Instancia global del gestor de usuarios
manager_user = GestorUsuarios() 