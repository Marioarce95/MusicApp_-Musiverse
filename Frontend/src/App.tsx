import React from 'react';
import Navbar from './components/Navbar';
import MusicPlayer from './components/MusicPlayer';
import SongList from './components/SongList';
import { Music } from 'lucide-react';

function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-900 to-black text-white">
      <header className="glass-effect p-4 flex items-center justify-between">
        <div className="flex items-center">
          <Music className="w-8 h-8 mr-2" />
          <h1 className="text-2xl font-bold">MusicApp</h1>
        </div>
        <button className="bg-purple-light px-4 py-2 rounded-full text-sm">Iniciar sesión</button>
      </header>
      
      <main className="container mx-auto px-4 pt-8 pb-32">
        <SongList />
      </main>
      
      <MusicPlayer />
      <Navbar />
    </div>
  );
}

export default App;