import reflex as rx

from Api_de_plantas.backend.estados import PlantasState
from routers import routers
from styles.styles import PaletaDeColores, Tamaños, Textos


def crear_boton_navegacion(etiqueta: str, ruta_redireccion: str, color_fondo: str) -> rx.Component:
    """
    Crea un botón de navegación estilizado con la etiqueta y ruta de redirección especificadas.

    Args:
        etiqueta (str): El texto a mostrar en el botón.
        ruta_redireccion (str): La ruta a la que redirigir cuando se hace clic en el botón.
        color_fondo (str): El color de fondo del botón.

    Returns:
        rx.Component: Un componente de botón estilizado con redirección al hacer clic.
    """
    return rx.button(
        rx.center(
            rx.text(
                etiqueta,
                align_items="center",
                font_size=Textos.SUBTITULO.value,
                weight="bold",
                font_family="Itim"
            ),
        ),
        style={
            "width": "270px",
            "height": "100px",
            "text_align": "center",
            "padding": Tamaños.PADDING_MEDIANO.value,
            "margin": Tamaños.MARGIN_PEQUEÑO.value,
            "bg": color_fondo,
            "font_weight": "bold",
            "border": Tamaños.BORDER2.value,
            "border_radius": Tamaños.RADIUS.value,
            "cursor": "pointer",
        },
        on_click=rx.redirect(ruta_redireccion) if ruta_redireccion else None,
    )


def crear_barra_navegacion(opcion: int) -> rx.Component:
    """
    Crea una barra de navegación con botones para diferentes secciones de la aplicación.

    La barra de navegación incluye un botón de inicio, un botón para alternar entre tipos de plantas
    (agrícolas o de interior), y un botón de producto.

    Args:
        opcion (int): La opción seleccionada actualmente (1 para plantas de interior, 2 para plantas agrícolas).

    Returns:
        rx.Component: Un componente de caja que contiene una rejilla de botones de navegación.
    """
    return rx.box(
        rx.grid(
            crear_boton_navegacion(
                "Menu de inicio",
                routers.PRINCIPAL.value,
                PaletaDeColores.BOTONES.value
            ),
            rx.cond(
                (opcion == 1),
                rx.box(
                    crear_boton_navegacion(
                        "Plantas Agricolas",
                        routers.AGRICOLAS.value,
                        PaletaDeColores.BOTONES.value,
                    ),
                    on_click=lambda: PlantasState.cambiar_opcion(2)
                ),
                rx.box(
                    crear_boton_navegacion(
                        "Plantas de interior",
                        routers.DOMESTICAS.value,
                        PaletaDeColores.BOTONES.value,
                    ),
                    on_click=lambda: PlantasState.cambiar_opcion(1)
                )
            ),
            crear_boton_navegacion(
                "Regador de plantas automatico",
                routers.PRODUCTO.value,
                PaletaDeColores.BOTONES.value
            ),
            columns="3",
            rows="1",
        ),
        margin="0 auto",
        width="70%",
        justify="center",
        align_items="center",
    )