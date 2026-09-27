from fastapi import APIRouter

from app.models.calculos import InformacoesApi, StatusApi

router = APIRouter()


@router.get("/", response_model=InformacoesApi)
def obter_informacoes() -> InformacoesApi:
    return InformacoesApi(
        nome="API Secundária - Planejador de Viagens",
        descricao="API para cálculos de distância e duração estimada de viagens.",
    )


@router.get("/health", response_model=StatusApi)
def verificar_saude() -> StatusApi:
    return StatusApi(status="ok")
