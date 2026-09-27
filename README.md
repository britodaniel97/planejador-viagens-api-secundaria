# API Secundária - Planejador de Viagens

Serviço REST em FastAPI para calcular a distância entre dois pontos e estimar a duração de uma viagem. Não acessa banco de dados nem serviços externos.

## Instalação e execução

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
```

A documentação interativa fica em `http://localhost:8001/docs`.

## Executar com Docker

```bash
docker build -t planejador-viagens-secundaria .
docker run --rm -p 8001:8001 planejador-viagens-secundaria
```

## Rotas

- `GET /` — informações da API.
- `GET /health` — status do serviço.
- `POST /distancia` — calcula a distância em quilômetros pela fórmula de Haversine. Exemplo:

```json
{
  "origem": {"latitude": -23.55, "longitude": -46.63},
  "destino": {"latitude": -22.91, "longitude": -43.17}
}
```

- `POST /duracao-estimada` — estima a duração em horas; os meios aceitos são `carro`, `onibus` e `aviao`. Exemplo:

```json
{"distancia_km": 430, "meio_transporte": "carro"}
```

## Arquitetura

As rotas ficam separadas dos modelos e da classe que implementa os cálculos.

<!-- Inserir aqui a imagem do fluxograma da arquitetura. -->
