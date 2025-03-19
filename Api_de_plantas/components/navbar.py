import reflex as rx

from styles import PaletaDeColores, Tamaños


def navbar() -> rx.Component:
    return rx.hstack(
        rx.image(src="/favicon.ico"),
        bg = PaletaDeColores.TERCIARIO_CAFE.value,
        heigth = "6em",
        padding= Tamaños.PADDING_PEQUEÑO.value,
        width = "100%",
        indez_z = 5
    )