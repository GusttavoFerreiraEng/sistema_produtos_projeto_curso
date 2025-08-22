class Produto:
    # representa o esqueleto da classe de produto
    # com atributos e métodos para manipulação de produtos
    def __init__(self, nome, codigo, quantidade, preco): #funcao
        self.nome = nome # nome do produto
        self.codigo = codigo # código único do produto
        self.quantidade = quantidade # quantidade em estoque
        self.preco = preco # preço do produto

    def __repr__(self): # representação do produto como string
        # útil para depuração e visualização
        return f"Produto(nome={self.nome}, codigo={self.codigo}, quantidade={self.quantidade}, preco={self.preco})" 

    def diminuir_estoque(self, quantidade): # diminui a quantidade em estoque
        # verifica se a quantidade é válida e atualiza o estoque
        if quantidade > 0 and quantidade <= self.quantidade: #se a quantidade for positiva e menor ou igual ao estoque exibe uma mensagem
            self.quantidade -= quantidade # diminui a quantidade em estoque
        elif quantidade <= 0: #verifica se a quantidade é positiva
            raise ValueError("A quantidade a ser diminuída deve ser positiva.")
        else: # se a quantidade for maior que o estoque, lança uma exceção
            raise ValueError("Quantidade insuficiente em estoque.")

    def aumentar_estoque(self, quantidade): # aumenta a quantidade em estoque
        # verifica se a quantidade é positiva e atualiza o estoque
        if quantidade > 0:
            self.quantidade += quantidade
        else:
            raise ValueError("A quantidade a ser aumentada deve ser positiva.")

    def verificar_estoque(self): # verifica o estado do estoque
        # retorna uma mensagem dependendo da quantidade em estoque
        if self.quantidade >= 5:
            return "Produto em estoque"
        else:
            return "Produto em falta"


class SistemaProdutos: # representa o sistema de gerenciamento de produtos
    # contém uma lista de produtos e métodos para manipulação
    def __init__(self):
        self.produtos = []

    def cadastrar_produto(self, nome, codigo, quantidade, preco): # cadastra um novo produto
        # verifica se o código já existe e cria um novo produto
        for p in self.produtos:
            if p.codigo == codigo:
                raise ValueError(f"Produto com código {codigo} já existe!") 
        produto = Produto(nome, codigo, quantidade, preco) 
        self.produtos.append(produto) #adiciona o produto à lista
        # retorna uma mensagem de sucesso mas ainda não está implementado
        return f"Produto {codigo}, {nome} cadastrado com sucesso!"

    def remover_produto(self, codigo): # remove um produto pelo código
        # procura o produto pelo código e o remove da lista
        for p in self.produtos:
            if p.codigo == codigo:
                self.produtos.remove(p) #remove o produto
                # retorna uma mensagem de sucesso mas ainda não está implementado
                return f"Produto {codigo} removido com sucesso!"
        raise ValueError("Produto não encontrado.")

    def buscar_produto(self, codigo): # busca um produto pelo código
        # procura o produto na lista e retorna o objeto Produto
        for p in self.produtos:
            if p.codigo == codigo: #se o código bater
                # retorna o produto encontrado
                return p
        return None

    def listar_produtos(self): # lista todos os produtos cadastrados
        # retorna a lista de produtos la no init no começo do codigo
        return self.produtos

    def editar_produto(self, codigo, nome=None, quantidade=None, preco=None): # edita um produto existente
        # verifica se o produto existe e atualiza os atributos fornecidos 
        produto = self.buscar_produto(codigo) #busca o produto pelo código
        # se o produto não for encontrado, lança uma exceção que esse if not produto:
        if not produto:
            raise ValueError("Produto não encontrado.") 

        if nome: # verifica se o nome é fornecido
            # se o nome for fornecido, atualiza o nome do produto
            produto.nome = nome 
        if quantidade is not None: # verifica se a quantidade é fornecida
            produto.quantidade = quantidade
        if preco is not None: # verifica se o preço é fornecido
            produto.preco = preco

        return f"Produto {codigo} atualizado com sucesso!"


#cada seção do código tem uma função específica, como cadastrar, remover, buscar, listar e editar produtos.
# A classe Produto representa um produto individual, enquanto a classe SistemaProdutos gerencia uma coleção de produtos.
# As exceções são lançadas para garantir que as operações sejam válidas, como evitar duplicação de códigos ou garantir que a quantidade em estoque seja suficiente.
# O sistema é projetado para ser usado em um contexto de gerenciamento de estoque, onde produtos podem ser adicionados, removidos, atualizados e listados de forma eficiente.
# O código também inclui métodos para verificar o estado do estoque e manipular a quantidade de produtos
#se pretender adicionar mais funcionalidades, adiciona os comentarios para entender melhor o que cada parte do código faz.
# O sistema é flexível e pode ser facilmente estendido para incluir mais recursos, como persistência de dados ou integração com uma interface de usuário.