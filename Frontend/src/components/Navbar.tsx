import React from 'react';
import { Home, Search, Library, User } from 'lucide-react';

const Navbar: React.FC = () => {
  return (
    <nav className="fixed bottom-0 left-0 right-0 glass-effect p-4">
      <ul className="flex justify-around">
        <li><Home className="text-white" /></li>
        <li><Search className="text-white" /></li>
        <li><Library className="text-white" /></li>
        <li><User className="text-white" /></li>
      </ul>
    </nav>
  );
};

export default Navbar;