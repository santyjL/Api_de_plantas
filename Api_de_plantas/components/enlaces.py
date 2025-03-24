import reflex as rx

from Api_de_plantas.backend.estados import PlantasState
from routers import routers
from styles import PaletaDeColores, Tamaños


def enlace_paginas(opcion: int) -> rx.Component:
    return rx.box(
        rx.grid(
            rx.link(
                "Menu de inicio",  # Texto directo como hijo
                href=routers.PRINCIPAL.value,
                style={
                    "width": "270px",
                    "height": "auto",
                    "textAlign": "center",
                    "padding": Tamaños.PADDING_MEDIANO.value,
                    "margin": Tamaños.MARGIN_PEQUEÑO.value,
                    "backgroundColor": PaletaDeColores.TERCIARIO_CAFE.value,
                    "fontWeight": "bold",
                    "fontSize": "size-7",
                }
            ),
            rx.cond(
                (opcion == 1),
                rx.link(
                    "Plantas Agricolas",  # Texto directo como hijo
                    href=routers.AGRICOLAS.value,
                    style={
                        "width": "270px",
                        "height": "auto",
                        "textAlign": "center",
                        "padding": Tamaños.PADDING_MEDIANO.value,
                        "margin": Tamaños.MARGIN_PEQUEÑO.value,
                        "backgroundColor": PaletaDeColores.SECUNDARIO_CELESTE.value,
                        "fontWeight": "bold",
                        "fontSize": "size-7",
                    },
                    on_click = lambda: PlantasState.cambiar_opcion(2)
                ),
                rx.link(
                    "Plantas Domesticas",  # Texto directo como hijo
                    href=routers.DOMESTICAS.value,
                    style={
                        "width": "270px",
                        "height": "auto",
                        "textAlign": "center",
                        "padding": Tamaños.PADDING_MEDIANO.value,
                        "margin": Tamaños.MARGIN_PEQUEÑO.value,
                        "backgroundColor": PaletaDeColores.SECUNDARIO_CELESTE.value,
                        "fontWeight": "bold",
                        "fontSize": "size-7",
                    },
                    on_click = lambda: PlantasState.cambiar_opcion(1),
                ),
            ),
            rx.link(
                "Regador de plantas automatico",  # Texto directo como hijo
                href=routers.PRODUCTO.value,
                style={
                    "width": "270px",
                    "height": "auto",
                    "textAlign": "center",
                    "padding": Tamaños.PADDING_MEDIANO.value,
                    "margin": Tamaños.MARGIN_PEQUEÑO.value,
                    "backgroundColor": PaletaDeColores.TERCIARIO_CAFE.value,
                    "fontWeight": "bold",
                    "fontSize": "size-7",
                }
            ),
            columns="3",
            rows="1",
        ),
        margin="0 auto",
        width="70%",
        justify="center",
        align_items="center",
    )