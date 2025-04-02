import reflex as rx

from Api_de_plantas.backend.estados import PlantasState
from styles import PaletaDeColores, Tamaños


def contenedor_planta(planta: dict) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.image(src=planta["imagen"], width="250px", height="150px"),
            rx.box(
                rx.text(planta["nombre"], font_family="Oswald"),
                rx.text(planta["humedad_ideal"], font_family="Oswald"),
                rx.text(planta["area_natural"], font_family="Oswald"),
                align="start"
            )
        ),
        width="270px",
        height="auto",
        padding=Tamaños.PADDING_MEDIANO.value,
        margin=Tamaños.MARGIN_PEQUEÑO.value,
        bg=PaletaDeColores.PRINCIPAL_VERDE.value,
        border = Tamaños.BORDER.value,
        border_radius = Tamaños.RADIUS.value
    )

def grid() -> rx.Component:
    titulo = rx.cond(
        PlantasState.opcion == 1,
        "🎍Plantas domésticas🎍",
        "🎍Plantas agrícolas🎍"
    )

    return rx.box(
        rx.text(titulo, size="8", weight="bold",
                align="center", margin=Tamaños.MARGIN_GRANDE.value,
                font_family="Itim"),
        rx.cond(
            (PlantasState.pagina < 0) | (PlantasState.pagina >= 3),
            rx.text("Página no encontrada",
                    size="7", weight="bold",
                    font_family="Itim"),
            rx.grid(
                rx.foreach(
                    PlantasState.pagina_actual,
                    lambda planta: contenedor_planta(planta)
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