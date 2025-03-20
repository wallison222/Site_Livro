from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    Talisman(app)  # Isso força HTTPS
    # Configuração do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'sua_chave_secreta'  # Necessário para gerenciar sessões

    db.init_app(app)

    # Importar e registrar as rotas
    from app.routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()  # Garante que as tabelas sejam criadas

    return app
