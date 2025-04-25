import reflex as rx

from Api_de_plantas.components.footer import crear_pie_pagina
from Api_de_plantas.components.imagenes import crear_banner_principal
from Api_de_plantas.components.navbar import crear_barra_superior
from routers import routers
from styles.styles import PaletaDeColores, Tamaños, Textos

def pagina_no_disponible() -> rx.Component:
    """
    Crea un mensaje de "Página no disponible" para secciones en desarrollo.

    Genera un componente flex con un encabezado centrado que indica que la página
    solicitada no está disponible actualmente. Se utiliza para secciones que están
    planificadas pero aún no han sido implementadas.

    Returns:
        rx.Component: Un componente flex con un mensaje de página no disponible.
    """
    return rx.flex(
        rx.heading(
            '"Pagina no disponible"',
            align="center",
            font_family="Itim",
            font_size=Textos.TITULO.value,
            color=PaletaDeColores.TEXTO.value,
            weight="medium",
            border=Tamaños.BORDER.value,
            padding=Tamaños.PADDING_MEDIANO.value,
            margin=Tamaños.MARGIN_GRANDE.value
        ),
        direction="column",
        justify="center",
        align="center",
        width="100%",
        height="100vh"
    )

@rx.page(route=routers.PRODUCTO.value)
def regador() -> rx.Component:
    """
    Página que mostrará información sobre el regador de plantas automático.

    Esta página actualmente muestra un mensaje de "Página no disponible" ya que
    la funcionalidad del regador de plantas automático está en desarrollo. Incluye
    una barra de navegación, un banner principal y un pie de página.

    Returns:
        rx.Component: La estructura de la página del regador de plantas automático.
    """
    return rx.box(
        rx.vstack(
            rx.box(
                crear_barra_superior(),
                crear_banner_principal(),
                bg=PaletaDeColores.TERCIARIO_MORADO.value
            ),
            pagina_no_disponible(),
            crear_pie_pagina()
        ),
        bg=PaletaDeColores.BG.value,
        background_size="cover",
        min_height="100vh",
    )