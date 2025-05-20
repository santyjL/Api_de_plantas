import reflex as rx
import json
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


with open("db/plantas_domesticas.json", "r", encoding="UTF-8") as archivo:
    data = json.load(archivo)
    api_plantas_domesticas = data["api_plantas_domesticas"]

with open("db/plantas_agricolas.json", "r", encoding="UTF-8") as archivo:
    data = json.load(archivo)
    api_plantas_agricolas = data["api_plantas_agricolas"]

async def api_plantas_agricolas_funcion():
    return api_plantas_agricolas

async def api_plantas_domesticas_funcion():
    return api_plantas_domesticas

app.api.add_api_route("/api/plantas_agricolas", api_plantas_agricolas_funcion)
app.api.add_api_route("/api/plantas_domesticas", api_plantas_domesticas_funcion)