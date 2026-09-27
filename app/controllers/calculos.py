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
        latitude_origem=dados.origem.latitude,
        longitude_origem=dados.origem.longitude,
        latitude_destino=dados.destino.latitude,
        longitude_destino=dados.destino.longitude,
    )
    return DistanciaResposta(distancia_km=distancia)


@router.post("/duracao-estimada", response_model=DuracaoResposta)
def calcular_duracao(dados: DuracaoEntrada) -> DuracaoResposta:
    duracao = calculadora.calcular_duracao(
        distancia_km=dados.distancia_km,
        meio_transporte=dados.meio_transporte,
    )
    return DuracaoResposta(duracao_horas=duracao)
