# sistema_produtos/__init__.py
import os
from flask import Flask
from .models import db
from dotenv import load_dotenv

load_dotenv()

def create_app(test_config=None): # 1. Parâmetro para configs de teste
    app = Flask(__name__)

    # --- Bloco de Configuração ---
    if test_config is None:
        # MODO NORMAL: Executa quando a aplicação roda normalmente
        app.config.from_object('config.Config')
        app.config['FLASK_SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    else:
        # MODO TESTE: Executa quando o pytest chama a função
        app.config.from_mapping(test_config)
    # --- Fim do Bloco de Configuração ---

    # A inicialização do DB e dos blueprints acontece para ambos os modos
    db.init_app(app)
    @app.cli.command("init-db")
    def init_db_command(): 
        """Cria as tabelas do banco de dados."""
        db.create_all()
        print("Banco de dados inicializado.")
        
    # Importa e regista os blueprints
    from .produtos.routes import produtos_bp
    from .auth.routes import auth_bp
    app.register_blueprint(produtos_bp)
    app.register_blueprint(auth_bp)



    return app


