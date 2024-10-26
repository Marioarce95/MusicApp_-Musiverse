import React from 'react';
import { Play, SkipBack, SkipForward } from 'lucide-react';

const MusicPlayer: React.FC = () => {
  return (
    <div className="fixed bottom-16 left-0 right-0 glass-effect p-4">
      <div className="flex items-center justify-between">
        <img src="https://images.unsplash.com/photo-1470225620780-dba8ba36b745?w=50&h=50&fit=crop" alt="Album cover" className="w-12 h-12 rounded-full" />
        <div className="flex-grow mx-4">
          <h3 className="text-sm font-semibold">Nombre de la canción</h3>
          <p className="text-xs text-gray-300">Artista</p>
        </div>
        <div className="flex items-center">
          <SkipBack className="w-6 h-6 mr-2" />
          <Play className="w-8 h-8" />
          <SkipForward className="w-6 h-6 ml-2" />
        </div>
      </div>
    </div>
  );
};

export default MusicPlayer;