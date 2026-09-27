from fastapi import FastAPI

from app.controllers import calculos, informacoes

app = FastAPI(
    title="API Secundária - Planejador de Viagens",
    description="API para cálculos simples de viagens.",
    version="1.0.0",
)

app.include_router(informacoes.router)
app.include_router(calculos.router)
