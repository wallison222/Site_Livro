import os
from dotenv import load_dotenv # type: ignore

# Carrega variáveis de ambiente do arquivo .env (se existir)
from datetime import timedelta
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'minha_chave_secreta')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)  # Sessão expira em 7 dias

