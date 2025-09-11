import json
import os

class Produto:
    """Representa um produto no sistema."""
    def __init__(self, nome, codigo, quantidade, preco):
        self.nome = nome
        self.codigo = codigo
        self.quantidade = quantidade
        self.preco = preco

    def __repr__(self):
        """Representação do produto para debug."""
        return f"Produto(nome={self.nome}, codigo={self.codigo}, quantidade={self.quantidade}, preco={self.preco})"

    def to_dict(self):
        """Transforma o objeto Produto em um dicionário para serialização JSON."""
        return {
            "nome": self.nome,
            "codigo": self.codigo,
            "quantidade": self.quantidade, 
            "preco": self.preco 
        }

    @staticmethod
    def from_dict(dados):
        """Cria um objeto Produto a partir de um dicionário."""
        return Produto(
            dados["nome"],
            dados["codigo"],
            dados["quantidade"],
            dados["preco"]
        )

    def diminuir_estoque(self, quantidade):
        """Diminui a quantidade do produto em estoque."""
        if not isinstance(quantidade, (int, float)) or quantidade <= 0:
            raise ValueError("A quantidade a ser diminuída deve ser um número positivo.")
        if quantidade > self.quantidade:
            raise ValueError("Quantidade insuficiente em estoque.")
        self.quantidade -= quantidade

    def aumentar_estoque(self, quantidade):
        """Aumenta a quantidade do produto em estoque."""
        if not isinstance(quantidade, (int, float)) or quantidade <= 0:
            raise ValueError("A quantidade a ser aumentada deve ser um número positivo.")
        self.quantidade += quantidade

    def verificar_estoque(self):
        """Verifica se o produto está em falta."""
        return "Produto em estoque" if self.quantidade >= 5 else "Produto em falta"


class SistemaProdutos:
    """Sistema de gerenciamento de produtos com persistência em JSON."""
    ARQUIVO_JSON = "produtos.json"

    def __init__(self):
        # Usamos um dicionário para busca rápida por código
        self.produtos = {}
        self.carregar_dados()

    def salvar_dados(self):
        """Salva os produtos no arquivo JSON."""
        # Converte os valores do dicionário (objetos Produto) em dicionários para JSON
        with open(self.ARQUIVO_JSON, "w", encoding="utf-8") as f:
            lista_produtos = [p.to_dict() for p in self.produtos.values()]
            json.dump(lista_produtos, f, indent=4, ensure_ascii=False)

    def carregar_dados(self):
        """Carrega os produtos do arquivo JSON."""
        if os.path.exists(self.ARQUIVO_JSON): 
            with open(self.ARQUIVO_JSON, "r", encoding="utf-8") as f:
                try:
                    dados = json.load(f)
                    # Adiciona os produtos ao dicionário usando o código como chave
                    self.produtos = {d['codigo']: Produto.from_dict(d) for d in dados}
                except (json.JSONDecodeError, KeyError):
                    self.produtos = {}

    def cadastrar_produto(self, nome, codigo, quantidade, preco):
        """Cadastra um novo produto, com validação completa."""
        if not isinstance(nome, str) or not nome.replace(" ", "").isalpha():
            raise ValueError("Nome inválido. Use apenas letras e espaços.")
        
        if not isinstance(quantidade, (int, float)) or quantidade < 0:
            raise ValueError("Quantidade deve ser um número não negativo.")
            
        if not isinstance(preco, (int, float)) or preco < 0:
            raise ValueError("Preço deve ser um número não negativo.")

        if codigo in self.produtos:
            raise ValueError(f"Produto com código {codigo} já existe!")
            
        produto = Produto(nome, codigo, quantidade, preco)
        self.produtos[codigo] = produto
        self.salvar_dados()
        return f"Produto {codigo}, {nome} cadastrado com sucesso!"

    def remover_produto(self, codigo):
        """Remove um produto pelo código."""
        if codigo not in self.produtos:
            raise ValueError("Produto não encontrado.")
        
        del self.produtos[codigo]
        self.salvar_dados()
        return f"Produto {codigo} removido com sucesso!"

    def buscar_produto(self, codigo):
        """Busca um produto pelo código."""
        # Usa o método .get() para evitar erro se o código não existir
        return self.produtos.get(codigo)

    def listar_produtos(self):
        """Retorna todos os produtos como uma lista."""
        return list(self.produtos.values())

    def editar_produto(self, codigo, nome=None, quantidade=None, preco=None):
        """Edita os dados de um produto existente."""
        produto = self.buscar_produto(codigo)
        if not produto:
            raise ValueError("Produto não encontrado.")

        if nome is not None:
            if not isinstance(nome, str) or not nome.replace(" ", "").isalpha():
                raise ValueError("Nome inválido. Use apenas letras e espaços.")
            produto.nome = nome

        if quantidade is not None:
            if not isinstance(quantidade, (int, float)) or quantidade < 0:
                raise ValueError("Quantidade deve ser um número não negativo.")
            produto.quantidade = quantidade

        if preco is not None:
            if not isinstance(preco, (int, float)) or preco < 0:
                raise ValueError("Preço deve ser um número não negativo.")
            produto.preco = preco

        self.salvar_dados()
        return f"Produto {codigo} atualizado com sucesso!"