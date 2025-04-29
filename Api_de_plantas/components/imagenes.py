import reflex as rx
from styles.styles import PaletaDeColores, Tamaños, Textos
from styles.typing import effecto_typing
from styles.respiracion import effecto_respiracion


def crear_banner_principal(nombre_pagina: str) -> rx.Component:
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
                background=f"linear-gradient(45deg, {PaletaDeColores.TERCIARIO_MORADO.value}, {PaletaDeColores.TEXTO.value})",
                background_size= "400% 400%",
                color="transparent",
                padding=Tamaños.PADDING_PEQUEÑO.value,
                animation="typing 3.5s steps(100, end),blink-caret 0.5s step-end infinite, multicolor 5s linear infinite alternate",
                display="inline-block",
                max_width="fit-content",
                background_clip="text",
                _style= effecto_typing,
                _webkit_background_clip="text",
            ),
            rx.text(
                nombre_pagina,
                font_size=Textos.SUBTITULO.value,
                font_family="Sixtyfour",
                align="center",
                justify="center",
                white_space="nowrap",
                margin="0 auto",
                padding=Tamaños.PADDING_PEQUEÑO.value,
                display="inline-block",
                max_width="fit-content",
                color=PaletaDeColores.TEXTO.value,
                font_weight="medium",
                filter="drop-shadow(0px 0px 10px rgba(46, 204, 128, 0))",
                animation="respiracion 2s infinite",
                _style= effecto_respiracion,
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