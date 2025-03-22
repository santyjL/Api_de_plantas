import reflex as rx

from Api_de_plantas.components.footer import footer
from Api_de_plantas.components.grid import grid
from Api_de_plantas.components.imagenes import foto_principal
from Api_de_plantas.components.navbar import navbar
from routers import routers
from styles import PaletaDeColores

pagina = 0
@rx.page(route=f"{routers.AGRICOLAS.value}/{pagina}")
def plantas_agricolas() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                navbar(),
                foto_principal(),
                bg=PaletaDeColores.TERCIARIO_CAFE.value
            ),
            grid(2,pagina),
            footer()
        ),
        bg=PaletaDeColores.BG_BLANCO.value,
        background_size="cover",
        min_height="100vh",
    )