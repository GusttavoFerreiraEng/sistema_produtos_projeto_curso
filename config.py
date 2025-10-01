# config.py
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env (opcional, mas recomendado)
load_dotenv()

class Config:
    """Classe de configuração da aplicação."""
    
    # Chave secreta para proteger sessões e formulários
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'ndauhdaeufewbwuifbulfbuiaflfhuwfbuiobfoiwbuifwibufbuiaufiasunivfndbnoufdbuupb')
    
    # URL de conexão com o banco de dados
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    
    # Desativa uma funcionalidade do SQLAlchemy que não usaremos e consome recursos
    SQLALCHEMY_TRACK_MODIFICATIONS = False