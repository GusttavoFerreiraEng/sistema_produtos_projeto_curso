from flask import Flask, render_template, request, redirect, url_for # Importa as bibliotecas necessárias do Flask
from models import SistemaProdutos # Importa a classe SistemaProdutos do arquivo models.py

app = Flask(__name__) # Cria uma instância do Flask
# Cria uma instância do SistemaProdutos para gerenciar os produtos
sistema = SistemaProdutos() 

@app.route('/') # Define a rota para a página inicial
def index(): 
    return render_template("index.html")  # Renderiza o template index.html

@app.route('/cadastrar', methods=["POST"]) # Define a rota para cadastrar um novo produto
def cadastrar():
    nome = request.form['nome'] # Obtém o nome do produto do formulário
    codigo = request.form['codigo'] # Obtém o código do produto do formulário
    quantidade = int(request.form['quantidade']) # Obtém a quantidade do produto do formulário
    preco = float(request.form['preco']) # Obtém o preço do produto do formulário
    codigo = int(codigo)    # Converte o código do produto para inteiro para nao digitar letras
 
    try:
        sistema.cadastrar_produto(nome, codigo, quantidade, preco) # Cadastra o produto no sistema
        return redirect(url_for('listar')) # Redireciona para a lista de produtos após o cadastro
    except ValueError as e: # Captura erros de valor, como código duplicado
        return str(e) 
 
@app.route('/produtos') # Define a rota para listar todos os produtos cadastrados
def listar():
    return render_template("lista_produtos.html", produtos=sistema.listar_produtos())  # Renderiza o template lista_produtos.html com a lista de produtos

@app.route('/remover/<codigo>') # Define a rota para remover um produto pelo código
def remover(codigo):
    try: 
        sistema.remover_produto(codigo) # Remove o produto do sistema
    except ValueError as e: 
        return str(e)
    return redirect(url_for('listar')) # Redireciona para a lista de produtos após a remoção

@app.route('/editar/<codigo>', methods=["GET", "POST"]) # Define a rota para editar um produto pelo código
def editar(codigo): 
    produto = sistema.buscar_produto(int(codigo)) # Busca o produto pelo código
    if not produto: 
        return "Produto não encontrado." 

    if request.method == "POST": # Se o método for POST, atualiza os dados do produto
        nome = request.form['nome'] # Obtém o novo nome do produto do formulário
        quantidade = int(request.form['quantidade']) # Obtém a nova quantidade do produto do formulário
        preco = float(request.form['preco']) # Obtém o novo preço do produto do formulário
        sistema.editar_produto(produto.codigo, nome, quantidade, preco) # Edita o produto no sistema
        return redirect(url_for('listar')) # Redireciona para a lista de produtos após a edição

    return render_template("editar_produtos.html", produto=produto) # Exibe o formulário de edição com os dados do produto

if __name__ == "__main__": # Executa o aplicativo Flask
    # Se o script for executado diretamente, inicia o servidor Flask
    app.run(debug=True)


# O código acima define um sistema de gerenciamento de produtos usando Flask para criar uma interface web.
# Ele permite cadastrar, listar, remover e editar produtos, utilizando a classe SistemaProdutos para gerenciar os dados dos produtos.
# A aplicação é estruturada com rotas que respondem a diferentes ações do usuário, como cadastrar um novo produto ou editar um existente.
# As exceções são tratadas para garantir que as operações sejam válidas, como evitar duplicação de códigos ou garantir que a quantidade em estoque seja suficiente.
# A aplicação é projetada para ser simples e funcional, permitindo fácil interação com o sistema de produtos através de uma interface web.
