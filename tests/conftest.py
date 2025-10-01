import pytest
from sistema_produtos import create_app
from sistema_produtos.extensions import db
from sistema_produtos.models import Usuario

# Fixture para criar uma instância da aplicação para testes
@pytest.fixture()
def app():
    app = create_app({
        'TESTING': True,
        'SECRET_KEY': 'testing',  # Chave secreta SÓ para testes 
        # É uma boa prática usar um banco de dados em memória para testes
        # para não tocar no seu banco de dados real.
         'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:', 
    })
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:", # Usa uma base de dados em memória para os testes
        "WTF_CSRF_ENABLED": False, # Desativa CSRF nos formulários de teste
    })

    with app.app_context():
        db.create_all() # Cria as tabelas na base de dados em memória
        yield app
        db.drop_all() # Limpa a base de dados depois dos testes

# Fixture para ter um cliente de teste
@pytest.fixture()
def client(app):
    return app.test_client()

# Fixture de autenticação para facilitar o login/logout
@pytest.fixture()
def auth(client, app):
    class AuthActions:
        def login(self, username='admin', password='123'): # Primeiro, cria o utilizador na base de dados de teste
            with app.app_context():
                user = Usuario(usuario=username)
                user.set_senha(password)
                db.session.add(user)
                db.session.commit()
            # Agora, faz o post para a rota de login
            return client.post('/login', data={'usuario': username, 'senha': password})

        def logout(self):
            return client.get('/logout')

    return AuthActions()