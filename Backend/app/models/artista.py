from . import db

class Artista(db.Model):
    __tablename__ = 'artista'

    id_artista = db.Column(db.Integer, primary_key=True)
    nombre_artista = db.Column(db.String(100), nullable=False, unique=True)

    # Relación con álbumes y canciones
    albums = db.relationship('Album', backref='artista', lazy=True)
    canciones = db.relationship('Cancion', backref='artista', lazy=True)

    def __repr__(self):
        return f'<Artista {self.nombre_artista}>'
