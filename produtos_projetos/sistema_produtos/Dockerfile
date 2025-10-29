# Usar uma imagem oficial do Python
FROM python:3.11-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar os ficheiros de dependências
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o resto do código da aplicação
COPY . .

# Expor a porta que o Gunicorn vai usar
EXPOSE 5000

# Comando para correr a aplicação com Gunicorn (servidor de produção)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]