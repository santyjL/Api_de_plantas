import reflex as rx

from styles import PaletaDeColores


def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"), href=href)

def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href)

def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.flex(
                justify="between",
                spacing="6",
                flex_direction=["column", "column", "row"],
                width="100%",
            ),
            rx.divider(),
            rx.flex(
                rx.hstack(
                    rx.image(
                        src="/favicon.ico",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.text(
                        "© 2024 Reflex, Inc",
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                    ),
                    spacing="2",
                    align="center",
                    justify_content=[
                        "center",
                        "center",
                        "start",
                    ],
                    width="100%",
                ),
                spacing="4",
                flex_direction=["column", "column", "row"],
                width="100%",
            ),
            spacing="5",
            width="100%",
        ),
        bg = PaletaDeColores.SECUNDARIO_CELESTE.value,
        width="100%",
    )