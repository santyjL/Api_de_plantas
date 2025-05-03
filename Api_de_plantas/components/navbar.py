import reflex as rx

from Api_de_plantas.backend.estados import PlantasState
from styles.styles import PaletaDeColores, Tamaños, Textos
from styles.hover import aparecion
from routers import routers


def crear_enlaces_navegacion() -> rx.Component:
    """
    Crea un menú de navegación con enlaces a diferentes secciones de la aplicación.

    Returns:
        rx.Component: Un componente flex que contiene enlaces de navegación.
    """
    def crear_elemento_nav(titulo: str, enlace: str) -> rx.Component:
        """
        Crea un elemento de navegación estilizado con un título y enlace.

        Args:
            titulo (str): El texto a mostrar para el elemento de navegación.
            enlace (str): La ruta a la que redirigir cuando se hace clic en el elemento.

        Returns:
            rx.Component: Un componente de encabezado estilizado como elemento de navegación.
        """
        return rx.heading(
            titulo,
            color=PaletaDeColores.TEXTO.value,
            font_size=Textos.TEXTO.value,
            font_family="sixtyfour",
            weight="regular",
            spacing="3px",
            cursor="pointer",
            transition="background 0.3s linear, box-shadow 0.4s linear",
            border_radius=Tamaños.RADIUS.value,
            padding="3px",
            bg="transparent",
            _hover=aparecion,
            on_click=rx.redirect(enlace)
        )

    return rx.flex(
        crear_elemento_nav("Home", routers.PRINCIPAL.value),
        crear_elemento_nav("Regador", routers.PRODUCTO.value),
        rx.box(
            crear_elemento_nav("P.Agricolas", routers.AGRICOLAS.value),
            on_click=lambda: PlantasState.cambiar_opcion(2)
        ),
        rx.box(
            crear_elemento_nav("P.Interior", routers.DOMESTICAS.value),
            on_click=lambda: PlantasState.cambiar_opcion(1)
        ),
        justify="center",
        spacing="4"
    )


def crear_barra_superior() -> rx.Component:
    return rx.box(
        rx.center(
            rx.image(src="/favicon.ico", border_radius="50%",margin_x="6px"),
            crear_enlaces_navegacion(),
            bg=PaletaDeColores.TERCIARIO_MORADO.value,
            height="auto",
            padding=Tamaños.PADDING_PEQUEÑO.value,
            width="720px",
            z_index="8",
            justify="center",
            align="center",
            margin="0 auto",
            border_radius=Tamaños.RADIUS.value,
        ),
        position="fixed",
        top="0px",
        left="50%",
        opacity="0.9",
        transform="translateX(-50%)",
        width="720px",
        z_index="10",
        margin_y="10px"
    )