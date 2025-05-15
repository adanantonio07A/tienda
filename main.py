"""
from fastapi import FastAPI
from database import Base, engine

app = FastAPI(title="API Tienda", version="1.0")
#Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8080, log_level="debug")

"""
"""
from fastapi import FastAPI
from database import Base, engine
from routers import productos
try:
    Base.metadata.create_all(bind=engine)

    app = FastAPI(title="API Tienda", version="1.0")
    app.include_router(productos.router)

except Exception as e:
    print(">>> Error al iniciar la app:")
    print(e)

if __name__ == "__main__":
    import uvicorn
    try:
        uvicorn.run("main:app", host="127.0.0.1", port=8080, log_level="debug")
    except Exception as e:
        print(">>> Error al ejecutar uvicorn:")
        print(e)
"""
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas, auth
from database import SessionLocal, engine
from typing import List, Optional
from fastapi import Query

from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from jose import JWTError
from datetime import timedelta

from auth import crear_token_acceso, verificar_password

from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.security import OAuth2


class OAuth2PasswordBearerWithCookie(OAuth2):
    def __init__(self, tokenUrl: str):
        flows = OAuthFlowsModel(password={"tokenUrl": tokenUrl})
        super().__init__(flows=flows)

    async def __call__(self, request):
        authorization: str = request.headers.get("Authorization")
        if not authorization:
            raise HTTPException(status_code=403, detail="No autorizado")
        return authorization.split(" ")[1]

models.Base.metadata.create_all(bind=engine)
#Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependencia para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rutas productos
@app.post("/productos/", response_model=schemas.Producto)
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db),
    usuario_actual: str = Depends(auth.obtener_usuario_actual)):
    return crud.crear_producto(db, producto)

#@app.get("/productos/", response_model=list[schemas.Producto])
#def listar_productos(db: Session = Depends(get_db)):
#    return crud.get_productos(db)

@app.get("/productos/", response_model=List[schemas.Producto])
def listar_productos(nombre: Optional[str] = Query(None), db: Session = Depends(get_db)):
    if nombre:
        return db.query(models.Producto).filter(models.Producto.nombre.ilike(f"%{nombre}%")).all()
    return db.query(models.Producto).all()


@app.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db),
    usuario_actual: str = Depends(auth.obtener_usuario_actual)):
    prod = crud.eliminar_producto(db, producto_id)
    if not prod:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"ok": True}

@app.put("/productos/{producto_id}", response_model=schemas.Producto)
def editar_producto(producto_id: int, datos: schemas.ProductoUpdate, db: Session = Depends(get_db),
    usuario_actual: str = Depends(auth.obtener_usuario_actual)):
    producto = crud.actualizar_producto(db, producto_id, datos)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@app.get("/productos/buscar/", response_model=List[schemas.Producto])
def buscar_productos(nombre: str, db: Session = Depends(get_db),
                     usuario_actual: str = Depends(auth.obtener_usuario_actual)):
    return db.query(models.Producto).filter(models.Producto.nombre.ilike(f"%{nombre}%")).all()

@app.get("/clientes/buscar/", response_model=List[schemas.Cliente])
def buscar_clientes(nombre: str, db: Session = Depends(get_db),
                    usuario_actual: str = Depends(auth.obtener_usuario_actual)):
    return db.query(models.Cliente).filter(models.Cliente.nombre.ilike(f"%{nombre}%")).all()


# Rutas clientes
@app.post("/clientes/", response_model=schemas.Cliente)
def crear_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    return crud.crear_cliente(db, cliente)

#@app.get("/clientes/", response_model=list[schemas.Cliente])
#def listar_clientes(db: Session = Depends(get_db)):
#    return crud.get_clientes(db)

@app.get("/clientes/", response_model=List[schemas.Cliente])
def listar_clientes(nombre: Optional[str] = Query(None), db: Session = Depends(get_db)):
    if nombre:
        return db.query(models.Cliente).filter(models.Cliente.nombre.ilike(f"%{nombre}%")).all()
    return db.query(models.Cliente).all()


@app.delete("/clientes/{cliente_id}")
def eliminar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cli = crud.eliminar_cliente(db, cliente_id)
    if not cli:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return {"ok": True}

@app.put("/clientes/{cliente_id}", response_model=schemas.Cliente)
def editar_cliente(cliente_id: int, datos: schemas.ClienteUpdate, db: Session = Depends(get_db)):
    cliente = crud.actualizar_cliente(db, cliente_id, datos)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@app.post("/register", response_model=schemas.UsuarioOut)
def registrar_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = crud.obtener_usuario_por_email(db, usuario.email)
    if db_usuario:
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    return crud.crear_usuario(db, usuario)

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = crud.obtener_usuario_por_email(db, form_data.username)
    if not usuario or not verificar_password(form_data.password, usuario.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    
    access_token = crear_token_acceso(data={"sub": usuario.email})
    return {"access_token": access_token, "token_type": "bearer"}


# TODO:
#🧪 Pruebas con login real y token JWT

#🧪 Pruebas con base de datos temporal

# ⚙️ O seguimos con Jenkins y CI/CD

# to run the code:
#uvicorn main:app --reload

#para pytest:


