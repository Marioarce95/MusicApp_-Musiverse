from flask import Blueprint

# Blueprint para la API
api = Blueprint('api', __name__)

# Importar las rutas para registrarlas en el blueprint
from . import api