import reflex as rx

from styles import PaletaDeColores, Tamaños


def enlace_paginas(opcion:int) -> rx.Component:
    return rx.box(
        rx.grid(
            rx.box(
                rx.text("Menu de inicio",size="7", weight="bold", align="center"),
                width="270px",
                height="auto",
                justify="center",
                align_items="center",
                padding=Tamaños.PADDING_MEDIANO.value,
                margin=Tamaños.MARGIN_PEQUEÑO.value,
                bg=PaletaDeColores.TERCIARIO_CAFE.value,
                grid_column="span 1",
            ),
            rx.cond(
                (opcion == 1),
                rx.box(
                    rx.text("Plantas Agricolas",size="7", weight="bold", align="center"),
                    width="270px",
                    justify="center",
                    align_items="center",
                    height="auto",
                    padding=Tamaños.PADDING_MEDIANO.value,
                    bg=PaletaDeColores.SECUNDARIO_CELESTE.value,
                    margin=Tamaños.MARGIN_PEQUEÑO.value,
                    grid_column="span 1",
                ),
                rx.box(
                    rx.text("Plantas Domesticas",size="7", weight="bold", align="center"),
                    width="270px",
                    justify="center",
                    align_items="center",
                    height="auto",
                    padding=Tamaños.PADDING_MEDIANO.value,
                    margin=Tamaños.MARGIN_PEQUEÑO.value,
                    bg=PaletaDeColores.SECUNDARIO_CELESTE.value,
                    grid_column="span 1",
                ),
            ),

            rx.box(
                rx.text("Regador de plantas automatico",size="7", weight="bold", align="center"),
                width="270px",
                justify="center",
                align_items="center",
                height="auto",
                padding=Tamaños.PADDING_MEDIANO.value,
                margin=Tamaños.MARGIN_PEQUEÑO.value,
                bg=PaletaDeColores.TERCIARIO_CAFE.value,
                grid_column="span 1",
            ),
            columns="3",
            rows="1",
        ),
        margin="0 auto",
        width="70%",
        justify="center",
        align_items="center",
    )