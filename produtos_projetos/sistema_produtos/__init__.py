# sistema_produtos/__init__.py
import os
from flask import Flask
from .models import db
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Importa e regista os blueprints
    from .produtos.routes import produtos_bp
    from .auth.routes import auth_bp # Crie este blueprint para o login/logout
    app.register_blueprint(produtos_bp)
    app.register_blueprint(auth_bp)

    return app