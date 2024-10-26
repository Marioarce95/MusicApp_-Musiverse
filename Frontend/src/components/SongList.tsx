import React, { useEffect, useState } from 'react';
import { obtenerCanciones } from '../services/api';

interface Cancion {
  id_cancion: number;
  titulo: string;
  artista: string;
  album: string;
}

const SongList: React.FC = () => {
  const [canciones, setCanciones] = useState<Cancion[]>([]);
  const [cargando, setCargando] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const cargarCanciones = async () => {
      try {
        const data = await obtenerCanciones();
        setCanciones(data);
        setCargando(false);
      } catch (err) {
        setError('Error al cargar las canciones');
        setCargando(false);
      }
    };

    cargarCanciones();
  }, []);

  if (cargando) return <div>Cargando canciones...</div>;
  if (error) return <div>{error}</div>;

  return (
    <div className="mt-4">
      <h2 className="text-2xl font-bold mb-4">Canciones Populares</h2>
      <ul>
        {canciones.map((cancion) => (
          <li key={cancion.id_cancion} className="glass-effect mb-2 p-3 rounded-lg">
            <h3 className="font-semibold">{cancion.titulo}</h3>
            <p className="text-sm text-gray-300">{cancion.artista} - {cancion.album}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SongList;
