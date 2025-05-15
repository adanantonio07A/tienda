#Este archivo se usa para preparar un cliente de pruebas:
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app
import pytest

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

#Esto nos da acceso a la API como si estuviéramos haciendo peticiones reales.

# función para obtener un token
def get_auth_token(client):
    response = client.post("/login", data={"username": "admin@mail.com", "password": "admin123"})
    assert response.status_code == 200
    return response.json()["access_token"]


from sqlalchemy.orm import Session
from database import SessionLocal
from models import Usuario
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@pytest.fixture(scope="module", autouse=True)
def crear_usuario_test():
    """
    Fixture que se ejecuta automáticamente para asegurar que el usuario de test existe.
    """
    db: Session = SessionLocal()
    usuario_existente = db.query(Usuario).filter(Usuario.nombre == "admin").first()

    if not usuario_existente:
        hashed_password = pwd_context.hash("admin123")
        usuario = Usuario(nombre="admin", email="admin@mail.com", hashed_password=hashed_password)
        db.add(usuario)
        db.commit()

    db.close()

