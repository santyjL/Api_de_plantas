import reflex as rx

from styles.styles import PaletaDeColores, Tamaños


def crear_enlace_social(icono: str, href: str) -> rx.Component:
    """
    Crea un enlace a redes sociales con un icono.

    Args:
        icono (str): El nombre del icono a mostrar.
        href (str): La URL a la que enlazar.

    Returns:
        rx.Component: Un componente de enlace con el icono y URL especificados.
    """
    return rx.link(
        rx.icon(icono),
        href=href,
        color=PaletaDeColores.TERCIARIO_MORADO.value
    )


def crear_enlaces_sociales() -> rx.Component:
    """
    Crea un contenedor flex con enlaces a redes sociales.

    Actualmente incluye un enlace a GitHub para el repositorio del proyecto.

    Returns:
        rx.Component: Un componente flex que contiene enlaces a redes sociales.
    """
    return rx.flex(
        crear_enlace_social(
            icono="github",
            href="https://github.com/santyjL/Api_de_plantas"
        ),
        justify="end",
        width="100%",
        spacing="3"
    )


def crear_pie_pagina() -> rx.Component:
    """
    Crea el componente de pie de página para la aplicación.

    El pie de página incluye el logotipo de la aplicación, el nombre de la marca y enlaces a redes sociales.

    Returns:
        rx.Component: Un elemento de pie de página con marca y enlaces sociales.
    """
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
                crear_enlaces_sociales(),
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
            padding=Tamaños.PADDING_MEDIANO.value
        ),
        spacing="5",
        width="100%",
        bg=PaletaDeColores.TERCIARIO_MORADO.value,
    )
