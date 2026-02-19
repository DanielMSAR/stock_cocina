from app.database import engine, SessionLocal
from app.models.base import Base
from app.models.cocina import Cocina
from app.models.unidad_medida import UnidadMedida


def cargar_datos_iniciales():
    session = SessionLocal()

    # Verificar si ya existe una cocina
    cocina_existente = session.query(Cocina).first()

    if not cocina_existente:
        cocina = Cocina(nombre="Cocina Principal", direccion="Sin dirección")
        session.add(cocina)
        session.commit()
        print("Cocina base creada.")

    # Unidades estándar
    unidades = [
        ("kg", "peso"),
        ("g", "peso"),
        ("lt", "volumen"),
        ("unidad", "unidad"),
    ]

    for nombre, tipo in unidades:
        existe = session.query(UnidadMedida).filter_by(nombre=nombre).first()
        if not existe:
            unidad = UnidadMedida(nombre=nombre, tipo=tipo)
            session.add(unidad)

    session.commit()
    session.close()
    print("Unidades base verificadas/cargadas.")


def init_database():
    Base.metadata.create_all(bind=engine)
    print("Base de datos y tablas creadas correctamente.")
    cargar_datos_iniciales()


if __name__ == "__main__":
    init_database()
