import reflex as rx

from styles.styles import PaletaDeColores, Tamaños, Textos
from Api_de_plantas.backend.estados import PlantasState


def contenedor_planta(planta: dict) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.image(src=planta["imagen"], width="250px", height="150px",
                     border_radius = Tamaños.RADIUS.value),
            rx.box(
                rx.text(planta["nombre"], font_family="Oswald",
                         font_size=Textos.SUBTITULO.value, color=PaletaDeColores.TEXTO.value),
                rx.text(planta["humedad_ideal"], font_family="Oswald",
                        font_size=Textos.TEXTO.value, color=PaletaDeColores.TEXTO.value),
                rx.text(planta["area_natural"], font_family="Oswald",
                        font_size=Textos.TEXTO.value, color=PaletaDeColores.TEXTO.value),
                align="start"
            )
        ),
        width="270px",
        height="auto",
        padding=Tamaños.PADDING_MEDIANO.value,
        margin=Tamaños.MARGIN_PEQUEÑO.value,
        bg=PaletaDeColores.PRINCIPAL_VERDE.value,
        border_radius = Tamaños.RADIUS.value
    )

def grid() -> rx.Component:
    titulo = rx.cond(
        PlantasState.opcion == 1,
        "🎍Plantas de interior🎍",
        "🎍Plantas agrícolas🎍"
    )

    return rx.box(
        rx.text(titulo, size=Textos.TITULO.value, weight="bold",
                align="center", margin=Tamaños.MARGIN_GRANDE.value,
                color=PaletaDeColores.SECUNDARIO_CELESTE,font_family="Itim"),
        rx.cond(
            (PlantasState.pagina < 0) | (PlantasState.pagina >= 3),
            rx.text("Página no encontrada",
                    size=Textos.SUBTITULO.value, weight="bold",
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