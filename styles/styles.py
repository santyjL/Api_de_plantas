from enum import Enum

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Itim&display=swap",
    "https://fonts.googleapis.com/css2?family=Oswald:wght@200..700&display=swap",
    "https://fonts.googleapis.com/css2?family=Sixtyfour:BLED,SCAN@90,-53..100&display=swap"
]

class PaletaDeColores(Enum):
    BG_BLANCO = "#EEEEEE"
    BG_NEGRO= "#111111"
    PRINCIPAL_VERDE = "#63C569"
    SECUNDARIO_CELESTE = "#92AAF9"
    TERCIARIO_NARANJA = "#F95216"

    BOTONES_PAGINACION = "#D9D9D9"
    BOTONES = "#EECC8D"

    TEXTO= "#FFFFFF"

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

    BORDER = "3px solid #FFFFFF"
    RADIUS = "2em"