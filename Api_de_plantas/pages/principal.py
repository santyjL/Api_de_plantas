
import reflex as rx

from Api_de_plantas.components.imagenes import foto_principal
from Api_de_plantas.components.navbar import navbar
from routers import routers
from styles import PaletaDeColores


@rx.page(route=routers.PRINCIPAL.value)
def main() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
            navbar(),
            foto_principal(),
            bg= PaletaDeColores.TERCIARIO_CAFE.value
            )
        ),

        bg= PaletaDeColores.BG_BLANCO.value,
        background_size="cover",
        min_height="100vh",
    )
