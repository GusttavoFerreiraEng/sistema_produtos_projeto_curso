# sistema_produtos/auth/routes.py

from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from ..models import Usuario  # Importa o modelo Usuario da pasta pai
from .. import db             # Importa a instância db do __init__.py

# Cria o Blueprint para a autenticação
# O primeiro argumento 'auth' é o nome do blueprint
# O segundo é o nome do módulo
# O terceiro aponta para a pasta de templates correta
auth_bp = Blueprint('auth', __name__, template_folder='../templates')

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    # Se o utilizador já estiver logado, redireciona para a página principal
    if "usuario" in session:
        return redirect(url_for('produtos.index')) # Note que agora usamos 'produtos.index'

    if request.method == "POST":
        usuario_form = request.form["usuario"]
        senha_form = request.form["senha"]

        usuario_db = Usuario.query.filter_by(usuario=usuario_form).first() #procura no banco de dados se existe usuario e senha que foi digitado

        if usuario_db and usuario_db.check_senha(senha_form):
            session["usuario"] = usuario_db.usuario
            session["email"] = usuario_db.email 
            session["id"] = usuario_db.id #teste para estudos....
            flash("Login realizado com sucesso!", "success")
            return redirect(url_for("produtos.index")) # Redireciona para o blueprint de produtos
        else:
            flash("Utilizador ou senha inválidos.", "error")
            return redirect(url_for("auth.login")) # Redireciona de volta para o login

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    """Finaliza a sessão do utilizador e volta para o login"""
    session.pop("usuario", None)
    flash("Logout realizado com sucesso!", "success")
    return redirect(url_for("auth.login")) # Redireciona para a página de login do blueprint 'auth'