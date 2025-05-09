from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas, crud
from database import SessionLocal
from typing import List

router = APIRouter(prefix="/productos", tags=["productos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ProductoMostrar)
def crear(producto: schemas.ProductoCrear, db: Session = Depends(get_db)):
    return crud.obtener_productos(db, skip=skip, limit=limit)

@router.get("/", response_model=List[schemas.ProductoMostrar])
def listar(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crudd.obtener_productos(db, skip=skip, limit=limit)

@router.get("/{producto_id}", response_model=schemas.ProductoMostrar)    
def obtener(producto_id: int, db: Session = Depends(get_db)):
    producto = crud.obtener_producto(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.put("/{producto_id}", response_model=schemas.ProductoMostrar)
def editar(producto_id: int, datos: schemas.ProductoEditar, db: Session = Depends(get_db)):
    producto = crud.editar_producto(db, producto_id, datos)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.delete("/{producto_id}", response_model=schemas.ProductoMostrar)
def elimminar(producto_id: int, db: Session = Depends(get_db)):
    producto = crud.eliminar_producto(db, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

