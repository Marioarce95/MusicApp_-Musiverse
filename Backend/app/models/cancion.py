from . import db

class Cancion(db.Model):
    __tablename__ = 'cancion'

    id_cancion = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    duracion = db.Column(db.Time, nullable=False)
    genero = db.Column(db.String(50), nullable=True)
    id_album = db.Column(db.Integer, db.ForeignKey('album.id_album'), nullable=False)
    id_artista = db.Column(db.Integer, db.ForeignKey('artista.id_artista'), nullable=False)

    # Relaciones
    album = db.relationship('Album', backref='canciones', lazy=True)
    artista = db.relationship('Artista', backref='canciones', lazy=True)

    def __repr__(self):
        return f'<Cancion {self.titulo}>'
