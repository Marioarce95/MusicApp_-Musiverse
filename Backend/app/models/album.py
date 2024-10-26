from . import db

class Album(db.Model):
    __tablename__ = 'album'

    id_album = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    id_artista = db.Column(db.Integer, db.ForeignKey('artista.id_artista'), nullable=False)
    ano_lanzamiento = db.Column(db.Integer, nullable=False)

    # Relación con canciones
    canciones = db.relationship('Cancion', backref='album', lazy=True)

    def __repr__(self):
        return f'<Album {self.titulo} ({self.ano_lanzamiento})>'
