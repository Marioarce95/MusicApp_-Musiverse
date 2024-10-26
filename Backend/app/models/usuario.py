from . import db

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id_usuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    correo_electronico = db.Column(db.String(100), nullable=False, unique=True)
    contraseña = db.Column(db.String(255), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    pais = db.Column(db.String(50), nullable=False)
    ciudad = db.Column(db.String(50), nullable=False)

    # Relación con listas de reproducción
    listas_reproduccion = db.relationship('Playlist', backref='usuario', lazy=True)

    def __repr__(self):
        return f'<Usuario {self.nombre} {self.apellido}>'
