import reflex as rx

from Api_de_plantas.pages.principal import main

# Configurar Reflex para servir la aplicación
app= rx.App()
app.add_page(main)
