from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import Config
from .routes import api

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(api)

    return app
