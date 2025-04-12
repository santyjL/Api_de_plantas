import reflex as rx

from styles import PaletaDeColores, Tamaños


def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href, color=PaletaDeColores.TERCIARIO_NARANJA.value)

def links() -> rx.Component:
    return rx.flex(
        social_link(icon="github",href="https://github.com/santyjL/Api_de_plantas"),
        justify="end",
        width = "100%",
        spacing="3"
    )

def footer() -> rx.Component:
    return rx.el.footer(
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
                        "SifNiento",
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                    ),
                    links(),
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
                padding= Tamaños.PADDING_MEDIANO.value
            ),
            spacing="5",
            width="100%",
            bg = PaletaDeColores.SECUNDARIO_CELESTE.value,


        ),
