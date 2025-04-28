import reflex as rx
from styles.styles import Tamaños, Textos
from styles.typing import effecto_typing


def crear_banner_principal() -> rx.Component:
    """
    Crea un componente de banner principal con una imagen de fondo y un encabezado.

    El banner principal muestra el nombre de la empresa "Somos SifNiento..." con un efecto
    de escritura sobre una imagen de fondo.

    Returns:
        rx.Component: Un componente de caja con una imagen de fondo y un encabezado animado.
    """
    return rx.box(
        rx.flex(
            rx.heading(
                ">_Somos SifNiento...",
                font_size=Textos.TITULO.value,
                font_family="Sixtyfour",
                align="center",
                border_right="0.15em solid rgb(40, 200,192)",
                overflow="hidden",
                justify="center",
                white_space="nowrap",
                margin="0 auto",
                padding=Tamaños.PADDING_PEQUEÑO.value,
                animation="typing 3.5s steps(100, end),blink-caret 0.5s step-end infinite",
                display="inline-block",
                max_width="fit-content",
                _style= effecto_typing
            ),
            direction="column",
            justify="center",
            align="center",
            width="100%",
            height="100%",
        ),
        background="center/cover url('/foto1.png')",
        align_items="center",
        justify="center",
        width="100vw",  # Ancho total de la ventana
        height="512px",  # Alto total de la ventana
        margin="0px",   # Elimina márgenes
    )