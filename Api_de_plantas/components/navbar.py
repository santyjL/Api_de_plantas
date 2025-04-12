import reflex as rx

from Api_de_plantas.backend.estados import PlantasState
from styles.styles import PaletaDeColores, Tamaños
from routers import routers

def links() -> rx.Component:
    def elemento(titulo: str, link:str) -> rx.Component:
        return rx.heading(
            titulo,
            color = PaletaDeColores.SECUNDARIO_CELESTE.value,
            font_size="1em",
            font_family = "sixtyfour",
            cursor="pointer",
            filter="drop-shadow(0 0 20px rgba(33, 218, 147, 0.752))",
            on_click=rx.redirect(link)
        ),

    return rx.flex(

        elemento("Home", routers.PRINCIPAL.value),
        elemento("Regador", routers.PRODUCTO.value),
        rx.box(elemento("P.Agricolas", routers.AGRICOLAS.value),
               on_click=lambda: PlantasState.cambiar_opcion(2)),
        rx.box(elemento("P.Interior", routers.DOMESTICAS.value),
               on_click=lambda: PlantasState.cambiar_opcion(1)),
        justify= "end",
        width = "100%",
        spacing="4"
    )

def navbar() -> rx.Component:
    return rx.hstack(
        rx.image(src="/favicon.ico"),
        links(),
        bg = PaletaDeColores.TERCIARIO_NARANJA.value,
        heigth = "6em",
        padding= Tamaños.PADDING_PEQUEÑO.value,
        width = "100%",
        indez_z = 5,
        justify="start"
    )