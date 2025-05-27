from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import os

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "tienda_db")
DB_USER = os.getenv("DB_USER", "tiendauser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "tiendapass")

DATABASE_URL = (
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

#DATABASE_URL = "mysql+mysqlconnector://root:root@localhost:3306/tienda_db"

try:
    engine = create_engine(DATABASE_URL)

    # 💥 Esto forzará la conexión real
    with engine.connect() as connection:
        print("✅ Conexión exitosa a MySQL")
except Exception as e:
    print("❌ Error de conexión a MySQL:")
    print(e)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+mysqlconnector://emdep:3md3p@localhost:3306/tienda_db"
engine = None
try:
    engine = create_engine(DATABASE_URL)
    # FORZAR CONEXIÓN
    with engine.connect() as connection:
        print(">>> Conexión exitosa a MySQL")
except Exception as e:
    print(">>> Error de conexión a MySQL:")
    print(e)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
"""
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+mysqlconnector://emdep:3md3p@localhost:3306/tienda_db"
try:
    engine = create_engine(DATABASE_URL)
except Exception as e:
    print(e)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
"""