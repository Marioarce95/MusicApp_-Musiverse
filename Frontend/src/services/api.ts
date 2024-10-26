import axios, { AxiosInstance } from 'axios';

const api: AxiosInstance = axios.create({
  baseURL: '/api',
});

// Obtener canciones
export const obtenerCanciones = async () => {
  const response = await api.get('/canciones');
  return response.data;
};

// Obtener detalles de una canción específica
export const obtenerCancion = async (id: number) => {
  const response = await api.get(`/cancion/${id}`);
  return response.data;
};

// Obtener artistas
export const obtenerArtistas = async () => {
  const response = await api.get('/artistas');
  return response.data;
};

// Obtener detalles de un artista específico
export const obtenerArtista = async (id: number) => {
  const response = await api.get(`/artista/${id}`);
  return response.data;
};

// Crear un nuevo artista
export const crearArtista = async (nombreArtista: string) => {
  const response = await api.post('/artistas', { nombre_artista: nombreArtista });
  return response.data;
};

// Obtener álbumes
export const obtenerAlbums = async () => {
  const response = await api.get('/albums');
  return response.data;
};

// Obtener detalles de un álbum específico
export const obtenerAlbum = async (id: number) => {
  const response = await api.get(`/album/${id}`);
  return response.data;
};

// Obtener playlists
export const obtenerPlaylists = async () => {
  const response = await api.get('/playlists');
  return response.data;
};

// Obtener detalles de una playlist específica
export const obtenerPlaylist = async (id: number) => {
  const response = await api.get(`/playlist/${id}`);
  return response.data;
};

// Añade más funciones según sea necesario

