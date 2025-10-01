# Sistema de Gestão de Produtos (CRUD)

## 1. Descrição do Projeto

Este projeto é um **Sistema Completo de Gestão de Produtos (CRUD: Create, Read, Update, Delete)** desenvolvido em **Python** com o framework **Flask**.

A aplicação segue uma arquitetura moderna e modular, utilizando **Blueprints** para separar as funcionalidades de autenticação e de produtos. A persistência de dados é feita através do **Flask-SQLAlchemy** e o controle da estrutura do banco de dados é gerido com **Flask-Migrate** (Alembic).

O sistema permite registar, listar, editar e remover produtos com validações rigorosas, além de um sistema de autenticação de utilizadores seguro (hashing de senhas com `Werkzeug`).

## 2. Tecnologias Utilizadas

* **Backend:** Python, Flask (3.1.2)
* **Banco de Dados:** Flask-SQLAlchemy (camada ORM)
* **Migrações:** Flask-Migrate (Alembic)
* **Segurança:** Werkzeug (para hashing de senhas)
* **Configuração:** `python-dotenv`
* **Frontend:** HTML5, Jinja2, CSS3 (Estilos modernos e responsivos), JavaScript (Uso de AJAX na remoção de produtos).

## 3. Funcionalidades Chave

### 3.1 Autenticação e Segurança
* **Login/Logout:** Acesso protegido por utilizador e senha.
* **Controle de Acesso:** O decorador `@login_required` garante que apenas utilizadores autenticados acedam às rotas de gestão de produtos.
* **Hashing de Senhas:** As senhas são armazenadas de forma segura (não em texto simples).

### 3.2 Gestão de Produtos (CRUD)
* **Registo de Produtos:** Campos para Código (único), Nome, Quantidade e Preço.
* **Listagem de Produtos:** Tabela responsiva exibindo o status de estoque (`Produto em estoque` ou `Produto em falta`).
* **Edição de Produtos:** Permite alterar Nome, Quantidade e Preço (o Código é fixo).
* **Remoção com AJAX:** A remoção do produto é feita com uma requisição `DELETE` para o endpoint `/api/remover/<codigo>`, garantindo uma experiência de utilizador fluida sem recarregar a página.

## 4. Estrutura do Projeto

Módulo / Componente	Caminho do Arquivo	Função Principal (O que faz)
PACOTE PRINCIPAL	sistema_produtos/	O contêiner de toda a lógica da aplicação Flask.
App Factory	__init__.py	Cria a instância do Flask (create_app), configura e registra os Blueprints.
Extensões	extensions.py	Inicializa as instâncias de SQLAlchemy e Migrate.
Modelos (ORM)	models.py	Define a estrutura da Base de Dados (Classes Produto e Usuario).
BLUEPRINT: AUTENTICAÇÃO	auth/	Gerencia o acesso ao sistema.
Rotas de Acesso	auth/routes.py	Lógica para login e logout.
BLUEPRINT: PRODUTOS	produtos/	Gerencia as funcionalidades de CRUD.
Rotas CRUD	produtos/routes.py	Rotas para cadastrar, listar, editar e o endpoint API de remoção.
FRONTEND / RECURSOS	templates/	Arquivos HTML (Jinja2) das páginas e o layout base.
static/js/app.js	Contém a lógica JavaScript da aplicação, incluindo a função AJAX para remoção de produtos.
CONFIG. E SETUP	config.py	Configurações de ambiente para desenvolvimento e produção.
requirements.txt	Lista de todas as bibliotecas Python necessárias.
migrations/	Pasta com os scripts de migração de BD (Flask-Migrate/Alembic).


## 5. Instalação e Execução

### 5.1. Pré-requisitos
* Python 3.8+
* `pip`

### 5.2. Configuração do Ambiente

1.  **Clone o repositório e crie o ambiente virtual:**
    ```bash
    git clone [LINK DO REPOSITÓRIO]
    cd sistema_produtos_projeto_curso
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    # ou
    venv\Scripts\activate     # Windows
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure o arquivo `.env`:**
    Crie um arquivo chamado **`.env`** na raiz do projeto com as seguintes variáveis (altere os valores):

    ```ini
    FLASK_SECRET_KEY="SUA_CHAVE_SECRETA_MUITO_FORTE_AQUI"
    DATABASE_URL="sqlite:///instance/produtos.db"  # Use um caminho absoluto ou relativo, mas crie a pasta 'instance'.
    ADMIN_USERNAME="admin"
    ADMIN_PASSWORD="123"
    ```

### 5.3. Inicialização do Banco de Dados

1.  **Defina a variável `FLASK_APP`:**
    ```bash
    export FLASK_APP=sistema_produtos  # Necessário para os comandos Flask CLI
    # ou no Windows: set FLASK_APP=sistema_produtos
    ```

2.  **Aplique as migrações (cria as tabelas):**
    ```bash
    flask db upgrade
    ```

3.  **Crie o utilizador administrador inicial:**
    ```bash
    flask seed-db
    ```
    *(Este comando cria o utilizador com as credenciais definidas em `ADMIN_USERNAME` e `ADMIN_PASSWORD` no seu `.env`)*.

### 5.4. Execução da Aplicação

**Modo de Desenvolvimento:**
```bash
flask run
