from ..models import db, Artista

class ArtistaService:
    @staticmethod
    def crear_artista(nombre_artista):
        nuevo_artista = Artista(nombre_artista=nombre_artista)
        db.session.add(nuevo_artista)
        db.session.commit()
        return nuevo_artista

    @staticmethod
    def obtener_artista(id_artista):
        return Artista.query.get_or_404(id_artista)

    @staticmethod
    def actualizar_artista(id_artista, nombre_artista):
        artista = Artista.query.get_or_404(id_artista)
        artista.nombre_artista = nombre_artista
        db.session.commit()
        return artista

    @staticmethod
    def eliminar_artista(id_artista):
        artista = Artista.query.get_or_404(id_artista)
        db.session.delete(artista)
        db.session.commit()
