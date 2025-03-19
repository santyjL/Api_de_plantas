from enum import Enum


class PaletaDeCOlores(Enum):
    BG_BLANCO = "#FFFFFF"
    PRINCIPAL_VERDE = "#1BAF25"
    SECUNDARIO_CELESTE = "#5A77D6"
    TERCIARIO_CAFE = "#943F0A"

class Tamaños(Enum):
    PADDING_MEDIANO = "1em"
    PADDING_PEQUEÑO = "0.5em"

    MARGIN_PEQUEÑO = "0.5em"
    MARGIN_MEDIANO = "1em"
    MARGIN_GRANDE = "1.5em"