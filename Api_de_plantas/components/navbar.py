import reflex as rx

from Api_de_plantas.backend.estados import PlantasState
from styles.styles import PaletaDeColores, Tamaños, Textos
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
            filter="drop-shadow(0 0 20px rgba(33, 218, 147, 0.752))",
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
        justify="end",
        width="100%",
        spacing="4"
    )


def crear_barra_superior() -> rx.Component:
    """
    Crea la barra de navegación principal para la aplicación.

    La barra de navegación incluye el logotipo de la aplicación y enlaces de navegación.

    Returns:
        rx.Component: Un componente de pila horizontal que contiene el logotipo y enlaces de navegación.
    """
    return rx.hstack(
        rx.image(src="/favicon.ico"),
        crear_enlaces_navegacion(),
        bg=PaletaDeColores.TERCIARIO_MORADO.value,
        height="3em",
        padding=Tamaños.PADDING_PEQUEÑO.value,
        width="100%",
        index_z=5,
        justify="start"
    )