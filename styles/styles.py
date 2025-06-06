from enum import Enum

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Itim&display=swap",
    "https://fonts.googleapis.com/css2?family=Oswald:wght@200..700&display=swap",
    "https://fonts.googleapis.com/css2?family=Sixtyfour:BLED,SCAN@90,-53..100&display=swap"
]

class PaletaDeColores(Enum):
    BG = "#131A29"
    PRINCIPAL_VERDE = "#132829"
    SECUNDARIO_AZUL = "#262556"
    TERCIARIO_MORADO = "#3E1A45"

    BOTONES_PAGINACION = "#625211"
    BOTONES = "#262556"

    TEXTO= "#FFFFFF"
    TEXTO1 = "#71bfa6"
    TEXTO2 = "#9A9AC6"

class Textos(Enum):
    TITULO = "2.5em"
    SUBTITULO = "1.7em"
    TEXTO = "1em"

class Tamaños(Enum):
    PADDING_MEDIANO = "1em"
    PADDING_PEQUEÑO = "0.5em"

    MARGIN_PEQUEÑO = "0.5em"
    MARGIN_MEDIANO = "1em"
    MARGIN_GRANDE = "1.5em"

    BORDER1 = "3px solid #2ECC80"
    BORDER2 = "3px solid #3134CE"
    RADIUS = "2em"