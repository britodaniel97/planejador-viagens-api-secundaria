from fastapi import APIRouter

from app.models.calculos import (
    DistanciaEntrada,
    DistanciaResposta,
    DuracaoEntrada,
    DuracaoResposta,
)
from app.services.calculadora_viagem import CalculadoraViagem

router = APIRouter()
calculadora = CalculadoraViagem()


@router.post("/distancia", response_model=DistanciaResposta)
def calcular_distancia(dados: DistanciaEntrada) -> DistanciaResposta:
    distancia = calculadora.calcular_distancia(
        latitude_origem=dados.origem_lat,
        longitude_origem=dados.origem_lon,
        latitude_destino=dados.destino_lat,
        longitude_destino=dados.destino_lon,
    )
    return DistanciaResposta(distancia_km=distancia)


@router.post("/duracao-estimada", response_model=DuracaoResposta)
def calcular_duracao(dados: DuracaoEntrada) -> DuracaoResposta:
    duracao = calculadora.calcular_duracao(
        distancia_km=dados.distancia_km,
        meio_transporte=dados.meio_transporte,
    )
    return DuracaoResposta(duracao_horas=duracao)
