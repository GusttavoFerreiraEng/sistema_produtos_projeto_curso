# sistema_produtos/produtos/routes.py
from flask import Blueprint, render_template, redirect, url_for, session, flash, request
from ..models import Produto, db
from functools import wraps

# Cria o blueprint
produtos_bp = Blueprint('produtos', __name__, template_folder='../templates')

# Decorador para verificar se o utilizador está logado
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "usuario" not in session:
            flash("Por favor, faça o login para aceder a esta página.", "warning")
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

# --- ROTAS DO BLUEPRINT DE PRODUTOS ---

@produtos_bp.route("/")
@login_required
def index():
    return render_template("cadastro_produtos.html")

@produtos_bp.route("/produtos")
@login_required
def listar():
    produtos = Produto.query.all()
    return render_template("lista_produtos.html", produtos=produtos)

@produtos_bp.route("/cadastrar", methods=["POST"])
@login_required
def cadastrar():
    try:
        codigo = int(request.form['codigo'])
        nome = request.form['nome']
        quantidade = int(request.form['quantidade'])
        preco = float(request.form['preco'])

        if Produto.query.filter_by(codigo=codigo).first():
            flash(f"Produto com o código {codigo} já existe!", "warning")
            return redirect(url_for('produtos.index'))

        novo_produto = Produto(codigo=codigo, nome=nome, quantidade=quantidade, preco=preco)
        db.session.add(novo_produto)
        db.session.commit()
        flash("Produto registado com sucesso!", "success")
        return redirect(url_for('produtos.listar'))

    except ValueError:
        flash("Os campos 'código', 'quantidade' e 'preço' devem ser números válidos.", "danger")
        return redirect(url_for('produtos.index'))

@produtos_bp.route("/remover/<int:codigo>")
@login_required
def remover(codigo):
    produto = Produto.query.filter_by(codigo=codigo).first_or_404()
    db.session.delete(produto)
    db.session.commit()
    flash("Produto removido com sucesso!", "success")
    return redirect(url_for('produtos.listar'))

@produtos_bp.route("/editar/<int:codigo>", methods=["GET", "POST"])
@login_required
def editar(codigo):
    produto = Produto.query.filter_by(codigo=codigo).first_or_404()

    if request.method == "POST":
        try:
            produto.nome = request.form['nome']
            produto.quantidade = int(request.form['quantidade'])
            produto.preco = float(request.form['preco'])
            
            db.session.commit()
            flash("Produto editado com sucesso!", "success")
            return redirect(url_for('produtos.listar'))
        except ValueError:
            flash("Os campos 'quantidade' e 'preço' devem ser números válidos.", "danger")
            return render_template("editar_produtos.html", produto=produto)

    return render_template("editar_produtos.html", produto=produto)