import math


class CalculadoraViagem:
    """Reúne os cálculos usados pela API secundária."""

    _RAIO_TERRA_KM = 6371
    _VELOCIDADES_KMH = {
        "carro": 100,
        "onibus": 80,
        "aviao": 700,
    }

    def calcular_distancia(
        self,
        latitude_origem: float,
        longitude_origem: float,
        latitude_destino: float,
        longitude_destino: float,
    ) -> float:
        lat_origem = math.radians(latitude_origem)
        lat_destino = math.radians(latitude_destino)
        diferenca_latitude = lat_destino - lat_origem
        diferenca_longitude = math.radians(longitude_destino - longitude_origem)

        haversine = (
            math.sin(diferenca_latitude / 2) ** 2
            + math.cos(lat_origem)
            * math.cos(lat_destino)
            * math.sin(diferenca_longitude / 2) ** 2
        )
        angulo = 2 * math.atan2(math.sqrt(haversine), math.sqrt(1 - haversine))
        return round(self._RAIO_TERRA_KM * angulo, 2)

    def calcular_duracao(self, distancia_km: float, meio_transporte: str) -> float:
        velocidade = self._VELOCIDADES_KMH[meio_transporte]
        return round(distancia_km / velocidade, 2)
