from flask import jsonify, request
from . import api
from ..models import db, Cancion, Artista, Album, Playlist
from ..services.artista_service import ArtistaService
from ..services.user_service import UserService as UsuarioService

# Rutas para Cancion
@api.route('/canciones', methods=['GET'])
def obtener_canciones():
    canciones = Cancion.query.all()
    return jsonify([cancion.titulo for cancion in canciones])

@api.route('/cancion/<int:id>', methods=['GET'])
def obtener_cancion(id):
    cancion = Cancion.query.get_or_404(id)
    return jsonify({
        'id': cancion.id_cancion,
        'titulo': cancion.titulo,
        'duracion': str(cancion.duracion),
        'genero': cancion.genero,
        'album': cancion.album.titulo,
        'artista': cancion.artista.nombre_artista
    })

# Rutas para Artista
@api.route('/artistas', methods=['GET'])
def obtener_artistas():
    artistas = Artista.query.all()
    return jsonify([artista.nombre_artista for artista in artistas])

@api.route('/artista/<int:id>', methods=['GET'])
def obtener_artista(id):
    artista = Artista.query.get_or_404(id)
    return jsonify({
        'id': artista.id_artista,
        'nombre': artista.nombre_artista,
        'albums': [album.titulo for album in artista.albums]
    })

@api.route('/artistas', methods=['POST'])
def crear_artista():
    data = request.json
    nuevo_artista = ArtistaService.crear_artista(data['nombre_artista'])
    return jsonify({"id": nuevo_artista.id_artista, "nombre": nuevo_artista.nombre_artista}), 201

# Rutas para Album
@api.route('/albums', methods=['GET'])
def obtener_albums():
    albums = Album.query.all()
    return jsonify([album.titulo for album in albums])

@api.route('/album/<int:id>', methods=['GET'])
def obtener_album(id):
    album = Album.query.get_or_404(id)
    return jsonify({
        'id': album.id_album,
        'titulo': album.titulo,
        'ano_lanzamiento': album.ano_lanzamiento,
        'artista': album.artista.nombre_artista,
        'canciones': [cancion.titulo for cancion in album.canciones]
    })

# Rutas para Playlist
@api.route('/playlists', methods=['GET'])
def obtener_playlists():
    playlists = Playlist.query.all()
    return jsonify([playlist.nombre_lista for playlist in playlists])

@api.route('/playlist/<int:id>', methods=['GET'])
def obtener_playlist(id):
    playlist = Playlist.query.get_or_404(id)
    return jsonify({
        'id': playlist.id_lista_reproduccion,
        'nombre': playlist.nombre_lista,
        'canciones': [cancion.titulo for cancion in playlist.canciones]
    })

# Rutas para Usuario
@api.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = UsuarioService.obtener_todos_usuarios()
    return jsonify([{
        'id': usuario.id_usuario,
        'nombre': usuario.nombre,
        'apellido': usuario.apellido,
        'correo_electronico': usuario.correo_electronico
    } for usuario in usuarios])

@api.route('/usuario/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = UsuarioService.obtener_usuario_por_id(id)
    if usuario:
        return jsonify({
            'id': usuario.id_usuario,
            'nombre': usuario.nombre,
            'apellido': usuario.apellido,
            'correo_electronico': usuario.correo_electronico,
            'fecha_nacimiento': str(usuario.fecha_nacimiento),
            'pais': usuario.pais,
            'ciudad': usuario.ciudad
        })
    return jsonify({'error': 'Usuario no encontrado'}), 404

@api.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.json
    nuevo_usuario = UsuarioService.crear_usuario(**data)
    return jsonify({
        'id': nuevo_usuario.id_usuario,
        'nombre': nuevo_usuario.nombre,
        'apellido': nuevo_usuario.apellido,
        'correo_electronico': nuevo_usuario.correo_electronico
    }), 201

@api.route('/usuario/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    data = request.json
    usuario_actualizado = UsuarioService.actualizar_usuario(id, **data)
    if usuario_actualizado:
        return jsonify({
            'id': usuario_actualizado.id_usuario,
            'nombre': usuario_actualizado.nombre,
            'apellido': usuario_actualizado.apellido,
            'correo_electronico': usuario_actualizado.correo_electronico
        })
    return jsonify({'error': 'Usuario no encontrado'}), 404

@api.route('/usuario/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    if UsuarioService.eliminar_usuario(id):
        return jsonify({'mensaje': 'Usuario eliminado correctamente'}), 200
    return jsonify({'error': 'Usuario no encontrado'}), 404

@api.route('/usuario/<int:id>/playlists', methods=['GET'])
def obtener_playlists_usuario(id):
    playlists = UsuarioService.obtener_playlists_usuario(id)
    return jsonify([{
        'id': playlist.id_lista_reproduccion,
        'nombre': playlist.nombre_lista
    } for playlist in playlists])

@api.route('/login', methods=['POST'])
def login():
    data = request.json
    usuario = UsuarioService.autenticar_usuario(data['correo_electronico'], data['contraseña'])
    if usuario:
        return jsonify({
            'id': usuario.id_usuario,
            'nombre': usuario.nombre,
            'apellido': usuario.apellido,
            'correo_electronico': usuario.correo_electronico
        })
    return jsonify({'error': 'Credenciales inválidas'}), 401
