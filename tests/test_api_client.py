from fastapi.testclient import TestClient
from main import app  # o el punto de entrada de tu API

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert "Bienvenido" in response.text or response.json()

def test_crear_producto():
    response = client.post("/productos/", json={
        "nombre": "Producto Test",
        "precio": 10.5,
        "cantidad": 5
    })
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == "Producto Test"
