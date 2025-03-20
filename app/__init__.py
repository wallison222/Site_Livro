from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, static_folder="static")
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        # Importação dentro do contexto para evitar importação circular
        from . import models  
        db.create_all()

    from app.routes import main  
    app.register_blueprint(main)

    return app




