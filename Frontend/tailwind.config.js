/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        'purple-dark': '#4A0E4E',
        'purple-light': '#8E44AD',
      },
    },
  },
  plugins: [],
  darkMode: 'class',
};