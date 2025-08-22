# Sistema de Cadastro de Produtos

## 1. Descrição do Projeto
Este projeto é um **CRUD (Create, Read, Update, Delete) completo de produtos**, desenvolvido em **Python com Flask**.  
Ele utiliza **orientação a objetos (POO)** para gerenciar produtos e operações do sistema, **sem necessidade de banco de dados**.  
Ideal para aprendizado, apresentações de curso ou demonstrações de desenvolvimento web com Flask.

O sistema permite cadastrar, listar, editar e remover produtos, além de controlar o estoque e garantir **validações essenciais** para cada operação.

## FALTA O CSS

## 2. Funcionalidades Detalhadas

### 2.1 Cadastrar Produtos
- Preenche-se um formulário com:
  - **Nome**: nome do produto.
  - **Código**: número único do produto (não aceita letras).
  - **Quantidade**: número de unidades disponíveis.
  - **Preço**: valor unitário do produto.
- Validações:
  - Código **numérico e único**.
  - Quantidade e preço **positivos**.
- Resultado: Produto é adicionado à lista de produtos do sistema.

### 2.2 Listar Produtos
- Exibe todos os produtos cadastrados em uma **tabela organizada**.
- Colunas exibidas:
  - Código
  - Nome
  - Quantidade
  - Preço
  - Status do estoque (em estoque ou em falta)
- Funcionalidades adicionais (opcionais):
  - Ordenar por nome, preço ou quantidade.
  - Pesquisar por nome ou código.

### 2.3 Editar Produtos
- Permite alterar:
  - Nome
  - Quantidade
  - Preço
- O **código do produto não pode ser alterado** (garante unicidade).
- Formulário já vem preenchido com os dados atuais do produto.

### 2.4 Remover Produtos
- Permite excluir produtos do sistema.
- O usuário confirma a ação clicando no botão de remover.

### 2.5 Controle de Estoque
- Cada produto possui uma quantidade em estoque.
- Sistema avisa se a quantidade estiver **abaixo de 5 unidades**.
- Possibilidade de aumentar ou diminuir estoque diretamente pelo código Python.

### 2.6 Validações de Dados
- Código: apenas números inteiros, único.
- Nome: campo obrigatório.
- Quantidade: deve ser positiva.
- Preço: deve ser positivo.

---

## 3. Estrutura do Projeto
1. sistema_produtos/
app.py
models.py
2. assest/style.css
3. templates/index.html = editar_produtos.html = lista_produtos.html

## 4. Instalação e Execução

1. Clone ou baixe o projeto:
2. bash
   https://github.com/gusttavo00/sistema_produtos_projeto_curso.git
3. cd sistema_produtos

**ANTES INSTALAR AS BIBLIOTECAS**

pip install flask

**Depois disso para rodar e:**

python app.py


**5. Como Usar**

5.1 Cadastrar Produto

Preencha o formulário na página inicial (index.html).

Clique em "Cadastrar Produto".

Será redirecionado para a lista de produtos.

## 5.2 Listar Produtos

Clique em "Ver Produtos".

Visualize todos os produtos cadastrados e seus detalhes.

Produtos com quantidade < 5 aparecem como "Produto em falta".

## 5.3 Editar Produto

Clique em "Editar" ao lado do produto desejado.

Altere os campos nome, quantidade ou preço.

O código permanece fixo.

Clique em "Salvar Alterações".

**5.4 Remover Produto**

Clique em "Remover" ao lado do produto.

Produto será excluído imediatamente do sistema.


**6. Observações Importantes**

## Código único e numérico: garante que cada produto seja identificado corretamente.

## Sem banco de dados: os dados existem apenas enquanto a aplicação Flask estiver rodando.

## Estoque mínimo recomendado: 5 unidades.

## Sistema projetado com POO, separando a lógica de produto da lógica da aplicação web.
