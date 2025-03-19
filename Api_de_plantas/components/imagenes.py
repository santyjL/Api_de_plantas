import reflex as rx

from styles import Tamaños


def foto_principal() -> rx.Component:
    return rx.image(
        src="/foto1.png",
        width="100%",
        height="auto",
        object_fit="cover",
    )