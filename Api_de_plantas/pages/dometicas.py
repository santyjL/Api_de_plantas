import reflex as rx

from Api_de_plantas.backend.estados import PlantasState
from Api_de_plantas.components.enlaces import enlace_paginas
from Api_de_plantas.components.footer import footer
from Api_de_plantas.components.grid import grid
from Api_de_plantas.components.imagenes import foto_principal
from Api_de_plantas.components.navbar import navbar
from routers import routers
from styles import PaletaDeColores


def botones_paginacion() -> rx.Component:
    return rx.hstack(
        rx.button("1",bg=PaletaDeColores.BOTONES_PAGINACION.value, on_click=lambda: PlantasState.cambiar_valor(0)),
        rx.button("2",bg=PaletaDeColores.BOTONES_PAGINACION.value, on_click=lambda: PlantasState.cambiar_valor(1)),
        justify="center",
        align_items="center",
        width="5%",
        margin="0 auto",
    )

@rx.page(route=routers.DOMESTICAS.value)
def plantas_domesticas() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                navbar(),
                foto_principal(),
                bg=PaletaDeColores.TERCIARIO_CAFE.value
            ),
            grid(),
            botones_paginacion(),
            enlace_paginas(1),
            footer()
        ),
        bg=PaletaDeColores.BG_BLANCO.value,
        background_size="cover",
        min_height="100vh",
    )