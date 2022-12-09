from fastapi import APIRouter
from config.conexion import engine
from model.user import pelicula, actor, genero
from sqlalchemy import func, select

user = APIRouter()


# 1 - Consulta1


@user.get("/get_max_duration/{year}/{platform}/{tipo}", tags=["Querys"])
def get_max_duration(year: int, platform: str, tipo: str):
    with engine.connect() as conn:
        result = conn.execute(select(pelicula.c.duracion, pelicula.c.titulo)
                              .where(pelicula.c.ano_lanzamiento == year)
                              .where(pelicula.c.plataforma == platform)
                              .where(pelicula.c.tipo == tipo)
                              .order_by(pelicula.c.duracion.desc())
                              )

        return result.first()


# 2 - Consulta 2
#   El request debe ser: get_count_plataform(plataforma)

@user.get("/get_count_platform/{platform}", tags=["Querys"])
def get_count_platform(platform: str):
    with engine.connect() as conn:
        result = conn.execute(
            select(pelicula.c.plataforma, func.count(pelicula.c.tipo).label("Cantidad"), pelicula.c.tipo)
            .where(pelicula.c.plataforma == platform)
            .group_by(pelicula.c.tipo)
            )

        return result.fetchall()


# 3-Consulta 3

@user.get("/get_listedin/{genre}", tags=["Querys"])
def get_listedin(genre: str):
    with engine.connect() as conn:
        result = conn.execute(select(pelicula.c.plataforma, func.count(pelicula.c.plataforma).label("Cantidad"))
                              .join(genero, pelicula.c.indice == genero.c.indice)
                              .where(genero.c.genero == genre)
                              .group_by(pelicula.c.plataforma)
                              .order_by(func.count(pelicula.c.plataforma).desc()))

        return result.first()


# 4- Consulta 4

@user.get("/get_actor/{platform}", tags=["Querys"])
def get_actor(platform: str, year: int):
    with engine.connect() as conn:
        result = conn.execute(select(func.count(actor.c.nombre).label("Cantidad"), actor.c.nombre)
                              .join(pelicula, pelicula.c.indice == actor.c.indice)
                              .where(pelicula.c.ano_lanzamiento == year)
                              .where(pelicula.c.plataforma == platform)
                              .where(actor.c.nombre != "Sin dato")
                              .group_by(actor.c.nombre)
                              .order_by(func.count(actor.c.nombre).desc()))

        return result.first()
