from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class Cocina(Base):
    __tablename__ = "cocina"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    direccion: Mapped[str] = mapped_column(String, nullable=True)
    activa: Mapped[bool] = mapped_column(Boolean, default=True)
