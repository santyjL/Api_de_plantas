import reflex as rx

from Api_de_plantas.backend.estados import PlantasState
from Api_de_plantas.components.footer import crear_pie_pagina
from Api_de_plantas.components.imagenes import crear_banner_principal
from Api_de_plantas.components.navbar import crear_barra_superior
from routers import routers
from textos import pagina_principal_text
from styles.styles import PaletaDeColores, Tamaños, Textos
from styles.flex import (contenedor_principal, flex_principal,
                        item_completo, item_medio, item_pequeño,
                        tarjeta_interactiva, contenido_tarjeta, texto_tarjeta)

(sobre_nosotros,
plantas_interiores,
plantas_agricolas,
regador_automatico) = pagina_principal_text

def cuerpo(nombre: str, width: str, height: str,color_texto: str,
        redireccion: str, bg=PaletaDeColores.PRINCIPAL_VERDE.value,
        texto:str= "", border=Tamaños.BORDER1.value) -> rx.Component:

    """Crea una tarjeta interactiva con título, texto y redirección."""

    estilo_tarjeta = dict(tarjeta_interactiva)
    estilo_tarjeta["bg"] = bg
    estilo_tarjeta["width"] = width
    estilo_tarjeta["height"] = height
    estilo_tarjeta["margin"] = Tamaños.MARGIN_PEQUEÑO.value
    estilo_tarjeta["border"] = border
    estilo_tarjeta["border_radius"] = Tamaños.RADIUS.value

    return rx.card(
        rx.flex(
            rx.vstack(
                rx.heading(
                    nombre,
                    font_size=Textos.TITULO.value,
                    weight="bold",
                    font_family="Itim"
                    ),
                rx.text(
                    texto,
                    font_size=Textos.TEXTO.value,
                    font_family="Oswald",
                    width="100%",
                    color=color_texto
                    ),
                style=texto_tarjeta
            ),
            style=contenido_tarjeta
        ),
        on_click=lambda: rx.redirect(redireccion),
        style=estilo_tarjeta
    )

def flex_cuerpo() -> rx.Component:

    """Layout flexible con tarjetas de información para la página principal."""
    # Estilo para el encabezado

    header_style = dict(item_completo)
    header_style["margin_bottom"] = "2rem"

    # Estilo para la columna grande (flex: 2)
    columna_grande_style = dict(item_medio)
    columna_grande_style["flex"] = "2"

    # Estilo para las columnas pequeñas (flex: 1)
    columna_pequeña_style = dict(item_pequeño)
    columna_pequeña_style["flex"] = "1"

    return rx.container(
        # Header/Banner principal
        rx.flex(
            rx.flex(
                cuerpo(
                    "Sobre Nosotros", "100%", "auto",PaletaDeColores.TEXTO2.value, routers.PRINCIPAL.value,
                    PaletaDeColores.SECUNDARIO_AZUL.value, texto=sobre_nosotros,
                    border=Tamaños.BORDER2.value
                    ),
                style=flex_principal
            ),
            style=header_style
        ),

        # Main content - Layout de 2 columnas principales
        rx.flex(
            # Columna izquierda - Plantas apiladas verticalmente
            rx.flex(
                # Plantas de interior
                rx.box(
                cuerpo(
                    "Plantas de interior", "100%", "100%", PaletaDeColores.TEXTO1.value,routers.DOMESTICAS.value,
                    texto=plantas_interiores
                    ),
                    on_click=lambda: PlantasState.cambiar_opcion(1)
                ),

                # Plantas Agrícolas
                rx.box(
                cuerpo(
                    "Plantas Agricolas", "100%", "100%", PaletaDeColores.TEXTO1.value, routers.AGRICOLAS.value,
                    texto=plantas_agricolas
                    ),
                    on_click=lambda: PlantasState.cambiar_opcion(2)
                ),
                direction="column",
                width="100%",
                flex="1",
                gap="1em"
            ),

            # Columna derecha - Regador de plantas (más grande)
            rx.flex(
                cuerpo(
                    "Regador de plantas automatico", "100%", "100%", PaletaDeColores.TEXTO1.value, routers.PRODUCTO.value,
                    texto=regador_automatico
                    ),
                flex="2",
                width="100%"
            ),

            direction="row",
            width="100%",
            flex_wrap="wrap",
            gap="1em"
        ),

        style=contenedor_principal
    )


@rx.page(route=routers.PRINCIPAL.value)
def main() -> rx.Component:
    """Página principal de la aplicación."""
    return rx.box(
        rx.vstack(
            rx.box(
                crear_barra_superior(),
                crear_banner_principal("Pagina Principal"),
                bg=PaletaDeColores.TERCIARIO_MORADO.value,
                width="100%",
            ),
            flex_cuerpo(),
            crear_pie_pagina()
        ),
        bg=PaletaDeColores.BG.value,
        background_size="cover",
        min_height="100vh",
        width="100%",
        spacing="0",
    )