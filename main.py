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
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

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
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.crear_producto(db, producto)

@app.get("/productos/", response_model=list[schemas.Producto])
def listar_productos(db: Session = Depends(get_db)):
    return crud.get_productos(db)

@app.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    prod = crud.eliminar_producto(db, producto_id)
    if not prod:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"ok": True}

@app.put("/productos/{producto_id}", response_model=schemas.Producto)
def editar_producto(producto_id: int, datos: schemas.ProductoUpdate, db: Session = Depends(get_db)):
    producto = crud.actualizar_producto(db, producto_id, datos)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto


# Rutas clientes
@app.post("/clientes/", response_model=schemas.Cliente)
def crear_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    return crud.crear_cliente(db, cliente)

@app.get("/clientes/", response_model=list[schemas.Cliente])
def listar_clientes(db: Session = Depends(get_db)):
    return crud.get_clientes(db)

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