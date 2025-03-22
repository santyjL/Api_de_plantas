import json

import reflex as rx

from styles import PaletaDeColores, Tamaños

with open("db/plantas_domesticas.json", "r", encoding="UTF-8") as archivo:
    data = json.load(archivo)
    plantas_domesticas: list = data["plantas_domesticas"]

with open("db/plantas_agricolas.json", "r", encoding="UTF-8") as archivo:
    data = json.load(archivo)
    plantas_agricolas: list = data["plantas_agricolas"]

def dividir_cantidad_de_plantas(lista_plantas: list, tamano: int = 9) -> list:
    return [lista_plantas[i:i + tamano] for i in range(0, len(lista_plantas), tamano)]

def contenedor_planta(planta: dict) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.image(planta["imagen"], width="250px", height="auto"),
            rx.box(
                rx.text(planta["nombre"], size="6", weight="bold"),
                rx.text(planta["humedad_ideal"], size="4", weight="bold"),
                rx.text(planta["area_natural"], size="3"),
                align="start"
            )
        ),
        width="270px",
        height="auto",
        padding=Tamaños.PADDING_MEDIANO.value,
        margin=Tamaños.MARGIN_PEQUEÑO.value,
        bg=PaletaDeColores.PRINCIPAL_VERDE.value
    )

def grid(opcion: int, pagina_var) -> rx.Component:
    plantas = plantas_domesticas if opcion == 1 else plantas_agricolas
    titulo = "Plantas domésticas" if opcion == 1 else "Plantas agrícolas"
    sublistas = dividir_cantidad_de_plantas(plantas)

    return rx.box(
        rx.text(titulo, size="7", weight="bold"),
        rx.cond(
            (pagina_var < 0) | (pagina_var >= len(sublistas)),
            rx.text("Página no encontrada", size="7", weight="bold"),
            rx.grid(
                rx.foreach(
                    sublistas[pagina_var],
                    contenedor_planta
                ),
                columns="3",
                rows="3",
                justify="center",
                align_items="center",
            )
        ),
        width="80%",
        margin="0 auto",
    )