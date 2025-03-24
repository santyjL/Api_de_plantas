import json
from typing import Dict, List

import reflex as rx


class PlantasState(rx.State):
    opcion_cambio = 0
    numero: int = 0
    pagina: int = 0
    opcion: int = 2

    @rx.var
    def plantas_actuales(self) -> List[Dict]:
        with open("db/plantas_domesticas.json", "r", encoding="UTF-8") as archivo:
            data = json.load(archivo)
            plantas_domesticas = data["plantas_domesticas"]

        with open("db/plantas_agricolas.json", "r", encoding="UTF-8") as archivo:
            data = json.load(archivo)
            plantas_agricolas = data["plantas_agricolas"]

        return plantas_domesticas if self.opcion == 1 else plantas_agricolas

    @rx.var
    def sublistas(self) -> List[List[Dict]]:
        plantas = self.plantas_actuales
        return [plantas[i:i + 9] for i in range(0, len(plantas), 9)]

    @rx.var
    def pagina_actual(self) -> List[Dict]:
        return self.sublistas[self.pagina] if self.sublistas else []

    def cambiar_opcion(self, opcion: int):
        self.opcion_cambio = opcion
        self.opcion = self.opcion_cambio

    def cambiar_valor(self, num: int):
        self.numero = num
        self.pagina = self.numero