import reflex as rx

from Api_de_plantas.components.footer import footer
from Api_de_plantas.components.imagenes import foto_principal
from Api_de_plantas.components.navbar import navbar
from routers import routers
from styles import PaletaDeColores


@rx.page(route=routers.AGRICOLAS.value)
def plantas_agricolas() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                navbar(),
                foto_principal(),
                bg=PaletaDeColores.TERCIARIO_CAFE.value
            ),
            footer()
        ),
        bg=PaletaDeColores.BG_BLANCO.value,
        background_size="cover",
        min_height="100vh",
    )