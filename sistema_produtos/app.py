import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from dotenv import load_dotenv
from functools import wraps

# --- Bloco de importação correto e limpo ---
from sistema_produtos.extensions import db, migrate
from sistema_produtos.models import Produto, Usuario

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

# --- CONFIGURAÇÕES DA APLICAÇÃO ---
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///produtos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# --- INICIALIZAÇÃO DAS EXTENSÕES ---
db.init_app(app)
migrate.init_app(app, db)

# --- DECORATORS ---
def login_required(f):
    """
    Decorador que verifica se o usuário está logado na sessão.
    Se não estiver, redireciona para a página de login.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "usuario" not in session:
            flash("Por favor, faça login para acessar esta página.", "warning")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# --- COMANDOS CLI ---
@app.cli.command("seed-db")
def seed_db_command():
    """Cria o usuário admin inicial no banco de dados."""
    with app.app_context():
        admin_username = os.getenv('ADMIN_USERNAME')
        if not Usuario.query.filter_by(usuario=admin_username).first():
            admin = Usuario(usuario=admin_username)
            admin.set_senha(os.getenv('ADMIN_PASSWORD'))
            db.session.add(admin)
            db.session.commit()
            print(f"Usuário admin '{admin_username}' criado com sucesso.")
        else:
            print(f"Usuário admin '{admin_username}' já existe.")

# --- ROTAS DE AUTENTICAÇÃO ---
@app.route("/login", methods=["GET", "POST"])
def login():
    if "usuario" in session:
        return redirect(url_for("index"))
        
    if request.method == "POST":
        usuario_form = request.form.get("usuario")
        senha_form = request.form.get("senha")
        usuario_db = Usuario.query.filter_by(usuario=usuario_form).first()

        if usuario_db and usuario_db.check_senha(senha_form):
            session["usuario"] = usuario_db.usuario
            flash("Login realizado com sucesso!", "success")
            return redirect(url_for("index"))
        else:
            flash("Usuário ou senha inválidos.", "danger")
    
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout(): 
    session.pop("usuario", None)
    flash("Logout realizado com sucesso!", "success")
    return redirect(url_for("login"))
    
# --- ROTAS PRINCIPAIS E CRUD DE PRODUTOS ---
@app.route("/")
@login_required
def index(): 
    return render_template("cadastro_produtos.html")
    
@app.route("/produtos")
@login_required
def listar():
    produtos = Produto.query.all()
    return render_template("lista_produtos.html", produtos=produtos)

@app.route("/cadastrar", methods=["POST"])
@login_required
def cadastrar():
    required_fields = ['codigo', 'nome', 'quantidade', 'preco']
    if not all(field in request.form and request.form[field] for field in required_fields):
        flash("Todos os campos são obrigatórios e não podem estar vazios.", "danger")
        return redirect(url_for('index'))

    try:
        codigo = int(request.form['codigo'])
        quantidade = int(request.form['quantidade'])
        preco = float(request.form['preco'])

        if Produto.query.filter_by(codigo=codigo).first():
            flash(f"Produto com código {codigo} já existe!", "warning")
            return redirect(url_for('index'))
            
        novo_produto = Produto(
            nome=request.form['nome'],
            codigo=codigo,
            quantidade=quantidade,
            preco=preco
        )
        db.session.add(novo_produto)
        db.session.commit()
        flash("Produto cadastrado com sucesso!", "success")
        return redirect(url_for('listar'))

    except ValueError:
        flash("Os campos 'código', 'quantidade' e 'preço' devem ser números válidos.", "danger")
        return redirect(url_for('index'))

@app.route("/remover/<int:codigo>")
@login_required
def remover(codigo):
    produto = Produto.query.filter_by(codigo=codigo).first_or_404()
    db.session.delete(produto)
    db.session.commit()
    flash("Produto removido com sucesso!", "success")
    return redirect(url_for('listar'))
    
@app.route("/editar/<int:codigo>", methods=["GET", "POST"])
@login_required
def editar(codigo):
    produto = Produto.query.filter_by(codigo=codigo).first_or_404()

    if request.method == "POST":
        required_fields = ['nome', 'quantidade', 'preco']
        if not all(field in request.form and request.form[field] for field in required_fields):
            flash("Todos os campos são obrigatórios e não podem estar vazios.", "danger")
            return render_template("editar_produtos.html", produto=produto)
            
        try:
            produto.nome = request.form['nome']
            produto.quantidade = int(request.form['quantidade'])
            produto.preco = float(request.form['preco'])
            
            db.session.commit()
            flash("Produto editado com sucesso!", "success")
            return redirect(url_for('listar'))

        except ValueError:
            flash("Os campos 'quantidade' e 'preço' devem ser números válidos.", "danger")
            return render_template("editar_produtos.html", produto=produto)

    return render_template("editar_produtos.html", produto=produto)

if __name__ == "__main__":

    app.run(debug=True)
