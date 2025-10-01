# tests/test_auth.py
def test_login_page(client):
    """ Testa se a página de login carrega corretamente. """
    response = client.get('/login')
    assert response.status_code == 200
    assert b"Login Manager" in response.data

def test_successful_login(client, auth):
    """ Testa um login bem-sucedido e o redirecionamento. """
    response = auth.login()
    assert response.headers["Location"] == "/"