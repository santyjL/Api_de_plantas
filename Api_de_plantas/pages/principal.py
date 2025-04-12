from socketserver import ForkingTCPServer
import reflex as rx

from Api_de_plantas.backend.estados import PlantasState
from Api_de_plantas.components.footer import footer
from Api_de_plantas.components.imagenes import foto_principal
from Api_de_plantas.components.navbar import navbar
from routers import routers
from styles import PaletaDeColores, Tamaños


def cuerpo( nombre: str, width: str, height: str,
        redireccion: str, bg=PaletaDeColores.PRINCIPAL_VERDE.value,
        texto:str= "") -> rx.Component:

    return rx.card(

        rx.center(
            rx.vstack(
                rx.heading(nombre, align="center",
                        font_size="2em", weight="bold",
                        font_family="Itim"),
                rx.text(texto, align="center",font_size="1.2em",
                font_family="Oswald",width="80%"),
                align="center",
                justify="center",
            )
        ),
        on_click=lambda: rx.redirect(redireccion),
        bg=bg,
        width=width,
        height=height,
        margin=Tamaños.MARGIN_PEQUEÑO.value,
        border=Tamaños.BORDER.value,
        border_radius=Tamaños.RADIUS.value,
        cursor="pointer",
    )

def grid_cuerpo() -> rx.Component:
    return rx.box(
        rx.grid(
            rx.vstack(
                cuerpo("Sobre Nosotros", "80vw", "30vh",routers.PRINCIPAL.value,
                 PaletaDeColores.SECUNDARIO_CELESTE.value, texto="""
                 Este proyecto tiene como objetivo principal vender y promover el cuido de las plantas en escuelas y comunidades,
                 apoyando a las comunidades agricolas. Contiene una lista detallada de plantas domesticas y agricolas,
                 con sus respectivas caracteristicas y necesidades para su cuido ideal.
                 """),
                grid_column="span 2",
            ),
            rx.hstack(
                cuerpo("Regador de plantas automatico", "40vw", "60vh", routers.PRODUCTO.value,
                      texto="""
                      Sistema de riego automático inteligente para tus plantas.
                      Controla el riego de forma precisa y mantén tus plantas saludables
                      con nuestra tecnología innovadora. Ideal para jardines y huertos.
                      """),
                grid_row="span 2",
            ),
            rx.box(
                cuerpo("Plantas de interior", "40vw", "27vh", routers.DOMESTICAS.value,
                      texto="""
                      Descubre nuestra selección de plantas de interior perfectas para
                      decorar y purificar el aire de tu hogar. Incluye guías de cuidado
                      y consejos de mantenimiento.
                      """),
                on_click=lambda: PlantasState.cambiar_opcion(1),
            ),
            rx.box(
                cuerpo("Plantas Agricolas", "40vw", "27vh", routers.AGRICOLAS.value,
                      texto="""
                      Explora nuestra colección de plantas agrícolas de alta calidad.
                      Cultivos tradicionales y especializados con información detallada
                      sobre su siembra y cosecha.
                      """),
                on_click=lambda: PlantasState.cambiar_opcion(2),
            ),
            columns="2",
            rows="3",
        ),
        width="80%",  # Ancho fijo del contenedor del grid
        margin="0 auto",  # Centrar horizontalmente
        height="100vh",  # Altura total de la ventana
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
                bg=PaletaDeColores.TERCIARIO_NARANJA.value
            ),
            grid_cuerpo(),
            footer()
        ),
        bg=PaletaDeColores.BG_BLANCO.value,
        background_size="cover",
        min_height="100vh",
    )