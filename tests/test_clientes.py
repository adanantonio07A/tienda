from conftest import get_auth_token

def test_listar_clientes(client):
    response = client.get("/clientes/")
    assert response.status_code in (200, 401)

def test_crear_cliente(client):
    token = get_auth_token(client)
    headers = {"Authorization": f"Bearer {token}"}

    nuevo_cliente = {
        "nombre": "Antonio4",
        "email": "tonito4@mail.com"
    }
    response = client.post("/clientes/", json=nuevo_cliente, headers=headers)
    assert response.status_code == 200

