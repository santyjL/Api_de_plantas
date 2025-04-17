import reflex as rx

from Api_de_plantas.backend.estados import PlantasState
from Api_de_plantas.components.footer import crear_pie_pagina
from Api_de_plantas.components.imagenes import crear_banner_principal
from Api_de_plantas.components.navbar import crear_barra_superior
from routers import routers
from styles.styles import PaletaDeColores, Tamaños, Textos


def cuerpo(nombre: str, width: str, height: str,
        redireccion: str, bg=PaletaDeColores.PRINCIPAL_VERDE.value,
        texto:str= "") -> rx.Component:
    """
    Crea una tarjeta interactiva con título, texto y redirección.
    
    Esta función genera una tarjeta que muestra información y actúa como un enlace
    a otras secciones de la aplicación cuando se hace clic.
    
    Args:
        nombre (str): El título que se mostrará en la tarjeta.
        width (str): El ancho de la tarjeta (puede incluir unidades como px, vw, etc.).
        height (str): La altura de la tarjeta (puede incluir unidades como px, vh, etc.).
        redireccion (str): La ruta a la que redirigir cuando se hace clic en la tarjeta.
        bg (str, opcional): El color de fondo de la tarjeta. Por defecto es verde principal.
        texto (str, opcional): El texto descriptivo que se mostrará en la tarjeta.
        
    Returns:
        rx.Component: Un componente de tarjeta con los estilos y contenido especificados.
    """
    return rx.card(
        rx.center(
            rx.vstack(
                rx.heading(nombre, align="center",
                        font_size=Textos.TITULO.value, weight="bold",
                        font_family="Itim"),
                rx.text(texto, align="center",font_size=Textos.TEXTO.value,
                font_family="Oswald",width="80%"),
                align="center",
                justify="center",
            )
        ),
        on_click=lambda: rx.redirect(redireccion),
        bg=bg,
        width=width,
        height=height,
        margin=Tamaños.MARGIN_PEQUEÑO.value,
        border=Tamaños.BORDER.value,
        border_radius=Tamaños.RADIUS.value,
        cursor="pointer",
    )

def grid_cuerpo() -> rx.Component:
    """
    Crea una rejilla responsiva con tarjetas de información para la página principal.
    
    La rejilla contiene tarjetas para "Sobre Nosotros", "Regador de plantas automático",
    "Plantas de interior" y "Plantas Agrícolas", cada una con su propia descripción
    y redirección a la sección correspondiente.
    
    Returns:
        rx.Component: Un componente de caja que contiene una rejilla de tarjetas informativas.
    """
    return rx.box(
        rx.grid(
            rx.vstack(
                cuerpo("Sobre Nosotros", "80vw", "30vh",routers.PRINCIPAL.value,
                 PaletaDeColores.SECUNDARIO_CELESTE.value, texto="""
                 Este proyecto tiene como objetivo principal vender y promover el cuido de las plantas en escuelas y comunidades,
                 apoyando a las comunidades agricolas. Contiene una lista detallada de plantas domesticas y agricolas,
                 con sus respectivas caracteristicas y necesidades para su cuido ideal.
                 """),
                grid_column="span 2",
            ),
            rx.hstack(
                cuerpo("Regador de plantas automatico", "40vw", "60vh", routers.PRODUCTO.value,
                      texto="""
                      Sistema de riego automático inteligente para tus plantas.
                      Controla el riego de forma precisa y mantén tus plantas saludables
                      con nuestra tecnología innovadora. Ideal para jardines y huertos.
                      """),
                grid_row="span 2",
            ),
            rx.box(
                cuerpo("Plantas de interior", "40vw", "27vh", routers.DOMESTICAS.value,
                      texto="""
                      Descubre nuestra selección de plantas de interior perfectas para
                      decorar y purificar el aire de tu hogar. Incluye guías de cuidado
                      y consejos de mantenimiento.
                      """),
                on_click=lambda: PlantasState.cambiar_opcion(1),
            ),
            rx.box(
                cuerpo("Plantas Agricolas", "40vw", "27vh", routers.AGRICOLAS.value,
                      texto="""
                      Explora nuestra colección de plantas agrícolas de alta calidad.
                      Cultivos tradicionales y especializados con información detallada
                      sobre su siembra y cosecha.
                      """),
                on_click=lambda: PlantasState.cambiar_opcion(2),
            ),
            columns="2",
            rows="3",
        ),
        width="80%",  # Ancho fijo del contenedor del grid
        margin="0 auto",  # Centrar horizontalmente
        height="100vh",  # Altura total de la ventana
        justify="center",  # Centrado vertical
        align_items="center",  # Centrado horizontal
    )


@rx.page(route=routers.PRINCIPAL.value)
def main() -> rx.Component:
    """
    Página principal de la aplicación.
    
    Esta página muestra una barra de navegación, un banner principal,
    una rejilla con información sobre las diferentes secciones de la aplicación
    y un pie de página.
    
    Returns:
        rx.Component: La estructura completa de la página principal.
    """
    return rx.box(
        rx.vstack(
            rx.box(
                crear_barra_superior(),
                crear_banner_principal(),
                bg=PaletaDeColores.TERCIARIO_NARANJA.value
            ),
            grid_cuerpo(),
            crear_pie_pagina()
        ),
        bg=PaletaDeColores.BG_BLANCO.value,
        background_size="cover",
        min_height="100vh",
    )