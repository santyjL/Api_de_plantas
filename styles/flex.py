"""
Estilos de flexbox para la aplicación de plantas.

Este módulo contiene diccionarios de estilos para los componentes flex
utilizados en la aplicación, que pueden aplicarse directamente con el
parámetro 'style' en los componentes de Reflex.
"""

# Estilos para el contenedor principal
contenedor_principal = {
    "width": "80%",
    "max_width": "1200px",
    "margin": "2em auto",
    "padding": "1em",
}

# Estilos para el flex principal (columna)
flex_principal = {
    "direction": "column",
    "width": "100%",
    "gap": "1em",
}

# Estilos para filas flex
flex_fila = {
    "direction": "row",
    "width": "100%",
    "flex_wrap": "wrap",
}

# Estilos para columnas flex
flex_columna = {
    "direction": "column",
    "width": "100%",
}

# Estilos para elementos de ancho completo
item_completo = {
    "width": "100%",
    "padding": "1em",
    "flex_basis": "100%",
}

# Estilos para elementos de media anchura
item_medio = {
    "width": "100%",
    "padding": "1em",
    "flex_basis": "50%",
}

# Estilos para elementos pequeños
item_pequeño = {
    "width": "100%",
    "padding": "0.5em",
    "flex_basis": "100%",
}

# Estilos para tarjetas con efecto hover
tarjeta = {
    "box_shadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
    "transition": "transform 0.3s ease, box-shadow 0.3s ease",
    "_hover": {
        "transform": "translateY(-5px)",
        "box_shadow": "0 6px 12px rgba(0, 0, 0, 0.15)",
    },
}

# Estilos combinados para tarjetas interactivas
tarjeta_interactiva = {
    "bg": "#ffffff",  # Color de fondo predeterminado
    "border_radius": "0.5rem",
    "cursor": "pointer",
    "box_shadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
    "transition": "transform 0.3s ease, box-shadow 0.3s ease",
    "_hover": {
        "transform": "translateY(-5px)",
        "box_shadow": "0 6px 12px rgba(0, 0, 0, 0.80)",
    },
}

# Estilos para el contenido de las tarjetas
contenido_tarjeta = {
    "direction": "column",
    "width": "100%",
    "height": "100%",
    "align_items": "center",
    "justify_content": "center",
}

# Estilos para el texto dentro de las tarjetas
texto_tarjeta = {
    "width": "100%",
    "height": "100%",
    "gap": "1em",
    "align_items": "center",
    "justify_content": "center",
}