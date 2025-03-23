import reflex as rx

from Api_de_plantas.backend.estados import PlantasState
from styles import PaletaDeColores, Tamaños


def contenedor_planta(planta: dict) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.image(planta["imagen"], width="250px", height="auto"),
            rx.box(
                rx.text(planta["nombre"]),
                rx.text(planta["humedad_ideal"]),
                rx.text(planta["area_natural"]),
                align="start"
            )
        ),
        width="270px",
        height="auto",
        padding=Tamaños.PADDING_MEDIANO.value,
        margin=Tamaños.MARGIN_PEQUEÑO.value,
        bg=PaletaDeColores.PRINCIPAL_VERDE.value
    )

def grid() -> rx.Component:
    titulo = rx.cond(
        PlantasState.opcion == 1,
        "🎍Plantas domésticas🎍",
        "🎍Plantas agrícolas🎍"
    )

    return rx.box(
        rx.text(titulo, size="8", weight="bold", align="center", margin=Tamaños.MARGIN_GRANDE.value),
        rx.cond(
            (PlantasState.pagina < 0) | (PlantasState.pagina >= 3),
            rx.text("Página no encontrada", size="7", weight="bold"),
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