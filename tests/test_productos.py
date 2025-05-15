#def test_crear_producto(client):
#    response = client.post("/productos/", json={
#        "nombre": "producto test 1",
#        "descripcion": "producto generado de test auto 1",
#        "precio": 25.99
#    })
#    assert response.status_code == 200 or response.status_code == 401
from conftest import get_auth_token

def test_crear_producto(client):
    token = get_auth_token(client)
    headers = {"Authorization": f"Bearer {token}"}

    response = client.post("/productos/", json={
        "nombre": "producto test 1",
        "descripcion": "producto generado de test auto 1",
        "precio": 25.99
    }, headers=headers)

    assert response.status_code == 200


def test_listar_productos(client):
    response = client.get("/productos/")
    assert response.status_code in (200, 401)  # dependiendo si requiere login
