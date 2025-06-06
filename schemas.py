"""
from pydantic import BaseModel
from typing import Optional

class ProductoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    stock: int

class ProductoCrear(ProductoBase):
    pass

class ProductoEditar(ProductoBase):
    pass

class ProductoMostrar(ProductoBase):
    id: int

    class Config:
        from_attributes = True
"""
from pydantic import BaseModel

class ProductoBase(BaseModel):
    nombre: str
    descripcion: str | None = None

class ProductoCreate(ProductoBase):
    pass

class Producto(ProductoBase):
    id: int

    class Config:
        from_attributes = True

class ProductoUpdate(BaseModel):
    nombre: str
    descripcion: str | None = None


class ClienteBase(BaseModel):
    nombre: str
    email: str

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int

    class Config:
        from_attributes = True

class ClienteUpdate(BaseModel):
    nombre: str
    email: str

class UsuarioCreate(BaseModel):
    nombre: str
    email: str
    password: str

class UsuarioOut(BaseModel):
    id: int
    nombre: str
    email: str

    class Config:
        from_attributes = True
