from fastapi import FastAPI
from router.router import user


app = FastAPI(
    title= "Plataforma de Consultas de Servicios de Streaming",
    description= "Netflix, Hulu, Amazon & Disney",
    version="1.0"

)

app.include_router(user)