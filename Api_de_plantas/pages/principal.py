import json

import reflex as rx

with open("db/plantas_domesticas.json", "r", encoding="UTF-8") as archivo:
    data = json.load(archivo)
    plantas_domesticas: list = data["plantas_domesticas"]

print(plantas_domesticas)

def contenedor_planta(planta: dict) -> rx.Component:
    return rx.box(
        rx.image(planta["imagen"]),
        rx.text(planta["nombre"]),
        rx.text(planta["humedad_ideal"]),
        rx.text(planta["area_natural"]),
        bg="#000000"
    )

def main() -> rx.Component:
    return rx.box(
        rx.text("Plantas domésticas", size="7", weight="bold"),
        rx.grid(
            *[contenedor_planta(planta) for planta in plantas_domesticas]
        ),
        bg="#000000"
    )
