import reflex as rx

from styles.styles import PaletaDeColores, Tamaños, Textos
from Api_de_plantas.backend.estados import PlantasState


def renderizar_tarjeta_planta(planta: dict) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.box(
                rx.image(
                    src=planta["imagen"],
                    width="250px",
                    height="150px",
                    border_radius=Tamaños.RADIUS.value
                ),
                rx.text(
                    planta["nombre"],
                    font_family="Oswald",
                    font_size=Textos.SUBTITULO.value,
                    color=PaletaDeColores.TEXTO.value
                ),
                width="270px",
                height="auto",
                padding=Tamaños.PADDING_MEDIANO.value,
                margin=Tamaños.MARGIN_PEQUEÑO.value,
                background_color=PaletaDeColores.PRINCIPAL_VERDE.value,
                border_radius=Tamaños.RADIUS.value,
                border=Tamaños.BORDER1.value,
                transition="transform 0.4s ease, box-shadow 0.4s ease",
                _hover= {
                    "transform": "translateY(-5px)",
                    "box_shadow": "0 6px 12px rgba(46, 204, 128, 1)",
                }
            )
        ),
        rx.dialog.content(
            rx.vstack(
            rx.image(
                src=planta["imagen"],
                width="100%",
                height="auto",
                border_radius=Tamaños.RADIUS.value,
                align="center",
                margin_y=Tamaños.MARGIN_PEQUEÑO.value
            ),
            rx.heading(
                planta["nombre"],
                font_family="sixtyfour",
                font_size=Textos.TITULO.value,
                color=PaletaDeColores.TEXTO.value,
            ),
            rx.text(
                f"Humedad ideal de la planta: {planta['humedad_ideal']}",
                font_family="Oswald",
                font_size=Textos.SUBTITULO.value,
                color=PaletaDeColores.TEXTO.value,
            ),
            rx.text(
                f"Área natural: {planta['area_natural']}",
                font_family="Oswald",
                font_size=Textos.SUBTITULO.value,
                color=PaletaDeColores.TEXTO.value,
            ),
            ),
            background_color=PaletaDeColores.PRINCIPAL_VERDE.value,
            width="80%",
            gap="20px",
            item_align="center",
            justify="center",
            border_radius=Tamaños.RADIUS.value,
            border=Tamaños.BORDER1.value
        )
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
        "Plantas de interior",
        "Plantas Agrícolas"
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
                gap=4,
                template_columns="repeat(3, 1fr)",
                align_items="center",
            ),
        ),
        width="70%",
        margin="0 auto",
    )