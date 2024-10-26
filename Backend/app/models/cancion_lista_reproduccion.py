from . import db

class CancionListaReproduccion(db.Model):
    __tablename__ = 'cancion_lista_reproduccion'

    id_cancion = db.Column(db.Integer, db.ForeignKey('cancion.id_cancion'), primary_key=True)
    id_lista_reproduccion = db.Column(db.Integer, db.ForeignKey('lista_reproduccion.id_lista_reproduccion'), primary_key=True)

    def __repr__(self):
        return f'<CancionListaReproduccion Cancion: {self.id_cancion}, Lista: {self.id_lista_reproduccion}>'
