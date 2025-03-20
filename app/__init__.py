from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config  # Certifique-se de que a configuração do banco está correta

db = SQLAlchemy()  # Definição global sem inicializar com `app`
migrate = Migrate()  # O mesmo vale para o Migrate

def create_app():
    app = Flask(__name__, static_folder="static")

    app.config.from_object(Config)

    db.init_app(app)  # Agora sim, inicializa com `app`
    migrate.init_app(app, db)  # Inicializa migração corretamente

    with app.app_context():
        from app import models  # Garante que os modelos sejam importados
        db.create_all()

    from app.routes import main  # ✅ Importa as rotas corretamente DENTRO da função
    app.register_blueprint(main)  # ✅ Registra o Blueprint corretamente

    return app





