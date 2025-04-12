import reflex as rx

from Api_de_plantas.components.footer import footer
from Api_de_plantas.components.imagenes import foto_principal
from Api_de_plantas.components.navbar import navbar
from routers import routers
from styles.styles import PaletaDeColores, Tamaños

def pagina_no_disponible() -> rx.Component:
    return rx.flex(
        rx.heading(
            '"Pagina no disponible"',
            align="center",
            color=PaletaDeColores.TEXTO.value,
            font_family="Sixtyfour",
            font_size="2em",
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
    return rx.box(
        rx.vstack(
            rx.box(
                navbar(),
                foto_principal(),
                bg=PaletaDeColores.TERCIARIO_NARANJA.value
            ),
            pagina_no_disponible(),
            footer()
        ),
        bg=PaletaDeColores.BG_NEGRO.value,
        background_size="cover",
        min_height="100vh",
    )