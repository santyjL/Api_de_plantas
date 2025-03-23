import reflex as rx

from Api_de_plantas.components.footer import footer
from Api_de_plantas.components.imagenes import foto_principal
from Api_de_plantas.components.navbar import navbar
from routers import routers
from styles import PaletaDeColores, Tamaños


def cuerpo(nombre: str, width: str, height: str, redireccion: str, bg=PaletaDeColores.PRINCIPAL_VERDE.value) -> rx.Component:
    return rx.card(

        rx.vstack(
            rx.center(
                rx.text(nombre, align_items="center", font_size="2em", weight="bold"),
                align="center",
            )
        ),
        on_click=lambda: rx.redirect(redireccion),
        bg=bg,
        width=width,
        height=height,
        margin=Tamaños.MARGIN_PEQUEÑO.value,
    )

def grid_cuerpo() -> rx.Component:
    return rx.box(
        rx.grid(
            rx.vstack(
                cuerpo("Sobre Nosotros", "80vw", "30vh",routers.PRINCIPAL.value, PaletaDeColores.SECUNDARIO_CELESTE.value,),
                grid_column="span 2",
            ),
            rx.hstack(
                cuerpo("Regador de plantas automatico", "40vw", "60vh", routers.PRODUCTO.value),
                grid_row="span 2",
            ),
            cuerpo("Plantas de interior", "40vw", "27vh", routers.DOMESTICAS.value),
            cuerpo("Plantas Agricolas", "40vw", "27vh", routers.AGRICOLAS.value),
            columns="2",
            rows="3",
        ),
        width="80%",  # Ancho fijo del contenedor del grid
        margin="0 auto",  # Centrar horizontalmente
        height="100vh",  # Altura total de la ventana
        justify="center",  # Centrado vertical
        align_items="center",  # Centrado horizontal
    )

def razones() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.heading("Razones para elegirnos", size="7"),
            rx.text("texto ..."),
        ),
        height="400px",
        width="80%",  # Ancho fijo del contenedor del gridd
        margin="0 auto",  # Centrar horizontalmente
        justify="center",  # Centrado vertical
        align_items="center",  # Centrado horizontal
    )

@rx.page(route=routers.PRINCIPAL.value)
def main() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                navbar(),
                foto_principal(),
                bg=PaletaDeColores.TERCIARIO_CAFE.value
            ),
            grid_cuerpo(),
            razones(),
            footer()
        ),
        bg=PaletaDeColores.BG_BLANCO.value,
        background_size="cover",
        min_height="100vh",
    )