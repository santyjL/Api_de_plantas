import reflex as rx

from Api_de_plantas.backend.estados import PlantasState
from routers import routers
from styles import PaletaDeColores, Tamaños


def enlace_generico(label: str, redireccion: str, font_size: str, background_color: str) -> rx.Component:
    return rx.box(
        rx.center(
        rx.text(label, align_items="center", font_size="2em", weight="bold"),
        ),
        style={
            "width": "270px",
            "height": "160px",
            "text_align": "center",
            "padding": Tamaños.PADDING_MEDIANO.value,
            "margin": Tamaños.MARGIN_PEQUEÑO.value,
            "bg": background_color,
            "font_weight": "bold",
            "font_size": font_size,
            "border": Tamaños.BORDER.value,
            "border_radius": Tamaños.RADIUS.value,
            "cursor": "pointer",
        },
        on_click=rx.redirect(redireccion) if redireccion else None,
    )

def enlace_paginas(opcion: int) -> rx.Component:
    return rx.box(
        rx.grid(
            enlace_generico(
                "Menu de inicio",
                routers.PRINCIPAL.value,
                "5",
                PaletaDeColores.TERCIARIO_CAFE.value
            ),
            rx.cond(
                (opcion == 1),
                rx.box(
                    enlace_generico(
                        "Plantas Agricolas",
                        routers.AGRICOLAS.value,
                        "5",
                        PaletaDeColores.SECUNDARIO_CELESTE.value,

                    ),
                    on_click=lambda: PlantasState.cambiar_opcion(2)
                ),
                rx.box(
                    enlace_generico(
                        "Plantas Domesticas",
                        routers.DOMESTICAS.value,
                        "5",
                        PaletaDeColores.SECUNDARIO_CELESTE.value,

                    ),
                    on_click=lambda: PlantasState.cambiar_opcion(1)
                )
            ),
            enlace_generico(
                "Regador de plantas automatico",
                routers.PRODUCTO.value,
                "5",
                PaletaDeColores.TERCIARIO_CAFE.value
            ),
            columns="3",
            rows="1",
        ),
        margin="0 auto",
        width="70%",
        justify="center",
        align_items="center",
    )