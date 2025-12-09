import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        # Importar partes de la app dentro del contexto
        from . import routes
        from . import models
        
        # Crear tablas si no existen
        db.create_all()

    return app
