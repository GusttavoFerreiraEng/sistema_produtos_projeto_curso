from sistema_produtos.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class Produto(db.Model):
    """Representa um produto no banco de dados."""
    id = db.Column(db.Integer, primary_key=True)
    
    # A coluna 'codigo' estava faltando, adicionei ela aqui
    codigo = db.Column(db.Integer, unique=True, nullable=False)
    
    nome = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Produto(nome={self.nome}, codigo={self.codigo})"

    def verificar_estoque(self):
        """Verifica se o produto está em falta."""
        return "Produto em estoque" if self.quantidade >= 5 else "Produto em falta"

class Usuario(db.Model):
    """Representa um usuário no sistema."""
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), unique=True, nullable=False)
    senha_hash = db.Column(db.String(256), nullable=False)

    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def check_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)