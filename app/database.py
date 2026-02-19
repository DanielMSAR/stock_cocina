from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///datos/stock_cocina.db"

engine = create_engine(
    DATABASE_URL,
    echo=True,  # Muestra SQL en consola (útil en desarrollo)
    future=True
)

SessionLocal = sessionmaker(bind=engine)
