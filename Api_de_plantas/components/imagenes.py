import reflex as rx
from styles.styles import Tamaños, Textos


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
                "Somos SifNiento...", 
                class_name="typing-effect",
                font_size=Textos.TITULO.value, 
                font_family="Sixtyfour",
                align="center",
                justify="center", 
                padding=Tamaños.PADDING_PEQUEÑO.value
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