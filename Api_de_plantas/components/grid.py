import reflex as rx

from styles.styles import PaletaDeColores, Tamaños, Textos
from Api_de_plantas.backend.estados import PlantasState


def renderizar_tarjeta_planta(planta: dict) -> rx.Component:
    """
    Crea un componente de tarjeta para mostrar información de una planta.

    Args:
        planta (dict): Diccionario que contiene datos de la planta con claves 'imagen', 'nombre',
                      'humedad_ideal', y 'area_natural'.

    Returns:
        rx.Component: Un componente de caja estilizado que contiene información de la planta.
    """
    return rx.box(
        rx.vstack(
            rx.image(
                src=planta["imagen"],
                width="250px",
                height="150px",
                border_radius=Tamaños.RADIUS.value
            ),
            rx.box(
                rx.text(
                    planta["nombre"],
                    font_family="Oswald",
                    font_size=Textos.SUBTITULO.value,
                    color=PaletaDeColores.TEXTO.value
                ),
                rx.text(
                    planta["humedad_ideal"],
                    font_family="Oswald",
                    font_size=Textos.TEXTO.value,
                    color=PaletaDeColores.TEXTO.value
                ),
                rx.text(
                    planta["area_natural"],
                    font_family="Oswald",
                    font_size=Textos.TEXTO.value,
                    color=PaletaDeColores.TEXTO.value
                ),
                align="start"
            )
        ),
        width="270px",
        height="auto",
        padding=Tamaños.PADDING_MEDIANO.value,
        margin=Tamaños.MARGIN_PEQUEÑO.value,
        bg=PaletaDeColores.PRINCIPAL_VERDE.value,
        border_radius=Tamaños.RADIUS.value,
        border=Tamaños.BORDER1.value
    )


def crear_rejilla_plantas() -> rx.Component:
    """
    Crea una rejilla responsiva para mostrar tarjetas de plantas según la página y opción actual.

    La rejilla muestra plantas de la página actual y muestra un título basado en la opción seleccionada
    (plantas de interior o plantas agrícolas).

    Returns:
        rx.Component: Un componente de caja que contiene un título y una rejilla de tarjetas de plantas.
    """
    titulo = rx.cond(
        PlantasState.opcion == 1,
        "🎍Plantas de interior🎍",
        "🎍Plantas agrícolas🎍"
    )

    return rx.box(
        rx.text(
            titulo,
            font_size=Textos.TITULO.value,
            weight="bold",
            align="center",
            margin=Tamaños.MARGIN_GRANDE.value,
            color=PaletaDeColores.SECUNDARIO_AZUL,
            font_family="Itim"
        ),
        rx.cond(
            (PlantasState.pagina < 0) | (PlantasState.pagina >= 3),
            rx.text(
                "Página no encontrada",
                font_size=Textos.SUBTITULO.value,
                weight="bold",
                font_family="Itim"
            ),
            rx.grid(
                rx.foreach(
                    PlantasState.pagina_actual,
                    lambda planta: renderizar_tarjeta_planta(planta)
                ),
                columns="3",
                rows="3",
                justify="center",
                align_items="center",
            ),
        ),
        width="70%",
        margin="0 auto",
    )