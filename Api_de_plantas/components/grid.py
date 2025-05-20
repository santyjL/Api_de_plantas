import reflex as rx

from styles.styles import PaletaDeColores, Tamaños, Textos
from Api_de_plantas.backend.estados import PlantasState
from styles.hover import movimiento_y


def campo_modal_planta(titulo: str, valor: str):
    return rx.box(
        rx.text(
            titulo,
            font_family="Itim",
            font_size=Textos.SUBTITULO.value,
            color=PaletaDeColores.TEXTO.value,
            weight="bold",
        ),
        rx.text(
            valor,
            font_family="Oswald",
            font_size=Textos.TEXTO.value,
            color=PaletaDeColores.TEXTO.value,
        ),
        margin_y="4px"
    )


def renderizar_tarjeta_planta(planta: dict) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.box(
                rx.center(
                    rx.icon(
                        tag="leaf",
                        size=48,
                        color="green",
                        top="40px",
                    ),
                ),
                rx.image(
                    src=planta["imagen"],
                    width="250px",
                    height="150px",
                    border_radius=Tamaños.RADIUS.value,
                    margin_y=Tamaños.MARGIN_PEQUEÑO.value,
                    loading="lazy",
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
                role="dialog",
                cursor="pointer",
                _hover= movimiento_y
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
                    weight="medium",
                    word_spacing="3px",
                    color=PaletaDeColores.TEXTO.value,
                ),
                campo_modal_planta("Nombre científico", planta.get("nombre_cientifico", "N/A")),
                campo_modal_planta("Tipo de planta", planta.get("tipo_planta", "N/A")),
                campo_modal_planta("Área natural", planta.get("area_natural", "N/A")),
                campo_modal_planta("Humedad ideal", planta.get("humedad_ideal", "N/A")),
                campo_modal_planta("Temperatura ideal", planta.get("temperatura_ideal", "N/A")),
                campo_modal_planta("Altitud óptima", planta.get("altitud_optima", "N/A")),
                campo_modal_planta("Tipo de suelo", planta.get("tipo_suelo", "N/A")),
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
            color=PaletaDeColores.TEXTO.value,
            font_family="Itim",
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
