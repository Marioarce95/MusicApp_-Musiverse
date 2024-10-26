from ..models import db, Cancion, Artista, Album, Playlist

class MusicService:

    @staticmethod
    def crear_cancion(titulo, duracion, genero, id_album, id_artista):
        nueva_cancion = Cancion(titulo=titulo, duracion=duracion, genero=genero, id_album=id_album, id_artista=id_artista)
        db.session.add(nueva_cancion)
        db.session.commit()
        return nueva_cancion

    @staticmethod
    def crear_artista(nombre_artista):
        nuevo_artista = Artista(nombre_artista=nombre_artista)
        db.session.add(nuevo_artista)
        db.session.commit()
        return nuevo_artista

    @staticmethod
    def crear_album(titulo, ano_lanzamiento, id_artista):
        nuevo_album = Album(titulo=titulo, ano_lanzamiento=ano_lanzamiento, id_artista=id_artista)
        db.session.add(nuevo_album)
        db.session.commit()
        return nuevo_album

    @staticmethod
    def crear_playlist(nombre_lista, id_usuario):
        nueva_playlist = Playlist(nombre_lista=nombre_lista, id_usuario=id_usuario)
        db.session.add(nueva_playlist)
        db.session.commit()
        return nueva_playlist

    @staticmethod
    def agregar_cancion_a_playlist(id_cancion, id_lista_reproduccion):
        playlist = Playlist.query.get(id_lista_reproduccion)
        cancion = Cancion.query.get(id_cancion)
        if playlist and cancion:
            playlist.canciones.append(cancion)
            db.session.commit()
            return playlist
        return None

    @staticmethod
    def obtener_canciones_por_artista(id_artista):
        return Cancion.query.filter_by(id_artista=id_artista).all()

    @staticmethod
    def obtener_albumes_por_artista(id_artista):
        return Album.query.filter_by(id_artista=id_artista).all()

    @staticmethod
    def obtener_canciones_de_album(id_album):
        return Cancion.query.filter_by(id_album=id_album).all()

    @staticmethod
    def actualizar_cancion(id_cancion, **kwargs):
        cancion = Cancion.query.get(id_cancion)
        if cancion:
            for key, value in kwargs.items():
                setattr(cancion, key, value)
            db.session.commit()
            return cancion
        return None

    @staticmethod
    def eliminar_cancion(id_cancion):
        cancion = Cancion.query.get(id_cancion)
        if cancion:
            db.session.delete(cancion)
            db.session.commit()
            return True
        return False

    @staticmethod
    def buscar_canciones(query):
        return Cancion.query.filter(Cancion.titulo.ilike(f"%{query}%")).all()
