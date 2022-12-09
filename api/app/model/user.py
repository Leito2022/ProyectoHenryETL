from sqlalchemy import Table, Column
from sqlalchemy.types import Integer, String
from config.conexion import engine,meta



pelicula = Table("pelicula",meta,
            Column("tipo", String(30)) ,
            Column("titulo", String(50)),
            Column("director", String(120)) ,
            Column("ano_lanzamiento", Integer),
            Column("duracion", Integer) ,
            Column("indice", String(20)) ,
            Column("plataforma", String(20)) )



actor = Table("actor",meta,
            Column("nombre", String(30)) ,
            Column("indice", Integer),
           )


genero = Table("genero",meta,
            Column("genero", String(30)),
            Column("indice", Integer)
           )



meta.create_all(engine)