from typing import Literal

from pydantic import BaseModel


class DistanciaEntrada(BaseModel):
    origem_lat: float
    origem_lon: float
    destino_lat: float
    destino_lon: float


class DistanciaResposta(BaseModel):
    distancia_km: float


class DuracaoEntrada(BaseModel):
    distancia_km: float
    meio_transporte: Literal["carro", "onibus", "aviao"]


class DuracaoResposta(BaseModel):
    duracao_horas: float


class InformacoesApi(BaseModel):
    nome: str
    descricao: str


class StatusApi(BaseModel):
    status: str
