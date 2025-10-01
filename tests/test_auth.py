# tests/test_auth.py

# Testa se a página de login carrega
def test_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b"Login Manager" in response.data

# Testa um login bem-sucedido
def test_successful_login(client, auth):
    response = auth.login() # Verifica se fomos redirecionados para a página principal
    assert response.status_code == 302
    assert response.headers["Location"] == "/"

# Testa um login com senha errada
def test_wrong_password_login(client, auth): # Faz o login com uma senha errada
    response = client.post(
        '/login',
        data={'usuario': 'admin', 'senha': 'wrongpassword'},
        follow_redirects=True  # <--- Adicione este parâmetro!
    )
    # Verifica se a mensagem de erro aparece na página final
    assert b"Utilizador ou senha inv" in response.data

# Testa o acesso a uma página protegida sem login
def test_login_required_for_products(client):
    response = client.get('/produtos')  # Deve redirecionar para a página de login
    assert response.status_code == 302
    assert '/login' in response.headers["Location"]

# Testa o logout
def test_logout(client, auth):
    auth.login() # Faz o login primeiro
    response = auth.logout() # Deve redirecionar para a página de login
    assert response.status_code == 302
    assert '/login' in response.headers["Location"]