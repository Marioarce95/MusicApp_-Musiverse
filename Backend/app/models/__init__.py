from .. import db  # Importa db desde el __init__.py principal de la aplicación

# Importación de los modelos para que estén disponibles en la aplicación
from .usuario import Usuario
from .artista import Artista
from .album import Album
from .cancion import Cancion
from .playlist import Playlist
from .cancion_lista_reproduccion import CancionListaReproduccion

