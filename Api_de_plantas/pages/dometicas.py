import reflex as rx

from Api_de_plantas.backend.estados import PlantasState
from Api_de_plantas.components.enlaces import crear_barra_navegacion as enlace_paginas
from Api_de_plantas.components.footer import crear_pie_pagina as footer
from Api_de_plantas.components.grid import crear_rejilla_plantas as grid
from Api_de_plantas.components.imagenes import crear_banner_principal as foto_principal
from Api_de_plantas.components.navbar import crear_barra_superior as navbar
from routers import routers
from styles.styles import PaletaDeColores


def botones_paginacion() -> rx.Component:
    """
    Crea una barra de botones para la paginación de plantas de interior.

    Genera dos botones numerados que permiten al usuario navegar entre las diferentes
    páginas de plantas de interior. Cada botón actualiza el estado de la página actual
    cuando se hace clic.

    Returns:
        rx.Component: Un componente de pila horizontal con botones de paginación.
    """
    return rx.hstack(
        rx.button("1",bg=PaletaDeColores.BOTONES_PAGINACION.value, on_click=lambda: PlantasState.cambiar_valor(0),cursor="pointer"),
        rx.button("2",bg=PaletaDeColores.BOTONES_PAGINACION.value, on_click=lambda: PlantasState.cambiar_valor(1),cursor="pointer"),
        rx.button("3",bg=PaletaDeColores.BOTONES_PAGINACION.value, on_click=lambda: PlantasState.cambiar_valor(2),cursor="pointer"),
        justify="center",
        align_items="center",
        width="5%",
        margin="0 auto",
    )

@rx.page(route=routers.DOMESTICAS.value)
def plantas_domesticas() -> rx.Component:
    """
    Página que muestra información sobre plantas de interior (domésticas).

    Esta página incluye una barra de navegación, un banner principal, una rejilla
    que muestra las plantas de interior, botones de paginación para navegar entre
    diferentes conjuntos de plantas, una barra de navegación adicional y un pie de página.

    Returns:
        rx.Component: La estructura completa de la página de plantas de interior.
    """
    return rx.box(
        rx.vstack(
            rx.box(
                navbar(),
                foto_principal(),
                bg=PaletaDeColores.TERCIARIO_MORADO.value
            ),
            grid(),
            botones_paginacion(),
            enlace_paginas(1),
            footer()
        ),
        bg=PaletaDeColores.BG.value,
        background_size="cover",
        min_height="100vh",
    )