from app import create_app

# Crear la aplicación Flask
app = create_app()

if __name__ == '__main__':
    # Ejecutar la aplicación en modo debug para desarrollo
    app.run(debug=True)
