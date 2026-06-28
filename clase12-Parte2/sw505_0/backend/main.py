from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from pydantic import BaseModel
from datetime import datetime
import os

# 1. Configuración de Conexión a PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://admin:secretpassword@db:5432/sisman")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 2. Modelo de Base de Datos (SQLAlchemy)
class UsuarioDB(Base):
    __tablename__ = "tb_usuario"
    id_usuario = Column(Integer, primary_key=True, autoincrement=True, index=True)
    alias_usuario = Column(String(50), unique=True, nullable=False, index=True)
    nombres = Column(String(100), nullable=False)
    # Genera la fecha actual en la creación, y la actualiza automáticamente en cada modificación
    fec_sistema = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

# Crea la tabla automáticamente en PostgreSQL al iniciar
Base.metadata.create_all(bind=engine)

# 3. Esquemas de Validación (Pydantic)
class UsuarioBase(BaseModel):
    alias_usuario: str
    nombres: str

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioResponse(UsuarioBase):
    id_usuario: int
    fec_sistema: datetime

    class Config:
        from_attributes = True

# 4. Inicialización de FastAPI
app = FastAPI(title="API Gestión de Usuarios")

# Dependencia para manejar la sesión de la DB en cada petición
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 5. Controladores (Rutas CRUD)

@app.post("/gest_usuario", response_model=UsuarioResponse)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    db_user = db.query(UsuarioDB).filter(UsuarioDB.alias_usuario == usuario.alias_usuario).first()
    if db_user:
        raise HTTPException(status_code=400, detail="El alias_usuario ya existe")
    
    nuevo_usuario = UsuarioDB(alias_usuario=usuario.alias_usuario, nombres=usuario.nombres)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

@app.get("/gest_usuario", response_model=list[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(UsuarioDB).all()

@app.get("/gest_usuario/{id_usuario}", response_model=UsuarioResponse)
def obtener_usuario(id_usuario: int, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioDB).filter(UsuarioDB.id_usuario == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@app.put("/gest_usuario/{id_usuario}", response_model=UsuarioResponse)
def actualizar_usuario(id_usuario: int, usuario: UsuarioCreate, db: Session = Depends(get_db)):
    db_user = db.query(UsuarioDB).filter(UsuarioDB.id_usuario == id_usuario).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    # Validar que si cambia el alias, no colisione con otro existente
    alias_existente = db.query(UsuarioDB).filter(
        UsuarioDB.alias_usuario == usuario.alias_usuario, 
        UsuarioDB.id_usuario != id_usuario
    ).first()
    if alias_existente:
        raise HTTPException(status_code=400, detail="El alias ya está en uso")

    db_user.alias_usuario = usuario.alias_usuario
    db_user.nombres = usuario.nombres
    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete("/gest_usuario/{id_usuario}")
def eliminar_usuario(id_usuario: int, db: Session = Depends(get_db)):
    db_user = db.query(UsuarioDB).filter(UsuarioDB.id_usuario == id_usuario).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    db.delete(db_user)
    db.commit()
    return {"mensaje": f"Usuario {id_usuario} eliminado correctamente"}
