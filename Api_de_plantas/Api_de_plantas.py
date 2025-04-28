import reflex as rx

from Api_de_plantas.pages.agricolas import plantas_agricolas
from Api_de_plantas.pages.dometicas import plantas_domesticas
from Api_de_plantas.pages.producto import regador
from Api_de_plantas.pages.principal import main
from styles.styles import STYLESHEETS

# Configurar Reflex para servir la aplicación
app = rx.App(
    stylesheets=STYLESHEETS
)
app.add_page(main)
app.add_page(plantas_agricolas)
app.add_page(plantas_domesticas)
app.add_page(regador)
