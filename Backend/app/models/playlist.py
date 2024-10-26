from . import db

class Playlist(db.Model):
    __tablename__ = 'lista_reproduccion'

    id_lista_reproduccion = db.Column(db.Integer, primary_key=True)
    nombre_lista = db.Column(db.String(100), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Relación con canciones
    canciones = db.relationship('Cancion', secondary='cancion_lista_reproduccion', backref=db.backref('listas', lazy=True))

    def __repr__(self):
        return f'<Playlist {self.nombre_lista}>'
