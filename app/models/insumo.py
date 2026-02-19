from sqlalchemy import Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class Insumo(Base):
    __tablename__ = "insumo"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    cocina_id: Mapped[int] = mapped_column(ForeignKey("cocina.id"))
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    unidad_id: Mapped[int] = mapped_column(ForeignKey("unidad_medida.id"))
    stock_actual: Mapped[float] = mapped_column(Float, default=0)
    stock_minimo: Mapped[float] = mapped_column(Float, default=0)
    costo_unitario: Mapped[float] = mapped_column(Float, default=0)
    activo: Mapped[bool] = mapped_column(Boolean, default=True)
