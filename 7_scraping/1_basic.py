
# Extraer información de una página web

import requests
import re

url = 'https://www.abc.es/' # url de la página web

response = requests.get(url) # hacer una petición a la página web

if response.status_code == 200:
    print('La página web se ha cargado correctamente')

    html = response.text # obtener el contenido de la página web

    # regular expresones para encontrar los enlaces (precio, nombre, imagen)
    price_pattern = r'<span class="price">(.+?)</span>'
    match = re.search(price_pattern, html)

    if match:
        print('Precio encontrado:', match.group(1))

