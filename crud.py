"""from sqlalchemy.orm import Session
import models, schemas

def crear_producto(db: Session, producto: schemas.ProductoCrear):
    db_producto = models.Producto(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def obtener_productos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Producto).filter(models.Producto.id == producto_id).first()

def editar_producto(db: Session, producto_id: int, datos: schemas.ProductoEditar):
    producto = db.query(models.Producto).filter(models.Producto.id == producto_id.first())
    if producto:
        for campo, valor in datos.dict().items():
            setattr(producto, campo, valor)
        db.commit()
        db.refresh(producto)
    return producto

def eliminar_producto(db: Session, producto_id: int):
    producto = db.query(models.Producto).filter(models.Producto.id == producto_id.first())
    if producto:
        db.delete(producto)
        db.commit()

    return producto
"""
from sqlalchemy.orm import Session
import models, schemas, auth

# Productos
def get_productos(db: Session):
    return db.query(models.Producto).all()

def get_producto(db: Session, producto_id: int):
    return db.query(models.Producto).filter(models.Producto.id == producto_id).first()

def crear_producto(db: Session, producto: schemas.ProductoCreate):
    db_producto = models.Producto(**producto.model_dump())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def eliminar_producto(db: Session, producto_id: int):
    db_producto = get_producto(db, producto_id)
    if db_producto:
        db.delete(db_producto)
        db.commit()
    return db_producto
def actualizar_producto(db: Session, producto_id: int, datos: schemas.ProductoUpdate):
    producto = db.query(models.Producto).filter(models.Producto.id == producto_id).first()
    if producto is None:
        return None
    for campo, valor in datos.model_dump().items():
        setattr(producto, campo, valor)
    db.commit()
    db.refresh(producto)
    return producto

# Clientes
def get_clientes(db: Session):
    return db.query(models.Cliente).all()

def get_cliente(db: Session, cliente_id: int):
    return db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()

def crear_cliente(db: Session, cliente: schemas.ClienteCreate):
    db_cliente = models.Cliente(**cliente.model_dump())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def eliminar_cliente(db: Session, cliente_id: int):
    db_cliente = get_cliente(db, cliente_id)
    if db_cliente:
        db.delete(db_cliente)
        db.commit()
    return db_cliente

def actualizar_cliente(db: Session, cliente_id: int, datos: schemas.ClienteUpdate):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
    if cliente is None:
        return None
    for campo, valor in datos.model_dump().items():
        setattr(cliente, campo, valor)
    db.commit()
    db.refresh(cliente)
    return cliente

def crear_usuario(db: Session, usuario: schemas.UsuarioCreate):
    hashed_password = auth.hashear_password(usuario.password)
    db_usuario = models.Usuario(
        nombre=usuario.nombre,
        email=usuario.email,
        hashed_password=hashed_password
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def obtener_usuario_por_email(db: Session, email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()
