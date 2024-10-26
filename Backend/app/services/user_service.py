from ..services.user_service import UserService as UsuarioService
from werkzeug.security import generate_password_hash, check_password_hash

class UserService:
    @staticmethod
    def crear_usuario(nombre, apellido, correo_electronico, contraseña, fecha_nacimiento, pais, ciudad):
        nuevo_usuario = Usuario(
            nombre=nombre,
            apellido=apellido,
            correo_electronico=correo_electronico,
            contraseña=generate_password_hash(contraseña),
            fecha_nacimiento=fecha_nacimiento,
            pais=pais,
            ciudad=ciudad
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        return nuevo_usuario

    @staticmethod
    def autenticar_usuario(correo_electronico, contraseña):
        usuario = Usuario.query.filter_by(correo_electronico=correo_electronico).first()
        if usuario and check_password_hash(usuario.contraseña, contraseña):
            return usuario
        return None

    @staticmethod
    def actualizar_usuario(id_usuario, **kwargs):
        usuario = Usuario.query.get(id_usuario)
        if not usuario:
            return None
        
        for key, value in kwargs.items():
            if key == 'contraseña':
                value = generate_password_hash(value)
            setattr(usuario, key, value)
        
        db.session.commit()
        return usuario

    @staticmethod
    def eliminar_usuario(id_usuario):
        usuario = Usuario.query.get(id_usuario)
        if not usuario:
            return False
        
        db.session.delete(usuario)
        db.session.commit()
        return True

    @staticmethod
    def obtener_usuario_por_id(id_usuario):
        return Usuario.query.get(id_usuario)

    @staticmethod
    def obtener_todos_usuarios():
        return Usuario.query.all()

    @staticmethod
    def obtener_playlists_usuario(id_usuario):
        usuario = Usuario.query.get(id_usuario)
        if usuario:
            return usuario.listas_reproduccion
        return []
