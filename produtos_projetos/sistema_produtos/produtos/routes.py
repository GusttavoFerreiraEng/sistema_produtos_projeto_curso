# sistema_produtos/produtos/routes.py
from flask import Blueprint, render_template, redirect, url_for, session
from ..models import Produto # Importa a partir da pasta pai

# Cria o blueprint
produtos_bp = Blueprint('produtos', __name__, template_folder='templates')

@produtos_bp.route("/")
def index():
    if "usuario" in session:
        return render_template("cadastro_produtos.html")
    return redirect(url_for("auth.login")) # Aponta para o blueprint de autenticação

@produtos_bp.route("/produtos")
def listar():
    # ... sua lógica para listar produtos ...
    produtos = Produto.query.all()
    return render_template("lista_produtos.html", produtos=produtos)

# ... mova todas as outras rotas de produtos para cá ...