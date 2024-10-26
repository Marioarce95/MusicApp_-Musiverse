import os

class Config:
    # Configuración básica de la aplicación
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una_clave_secreta_segura'
    
    # Configuración de la base de datos
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:root@127.0.0.1:3306/musiverse'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Otras configuraciones (API keys, servicios externos, etc.)
    # Por ejemplo:
    # API_KEY_SERVICIO_X = os.environ.get('API_KEY_SERVICIO_X')
