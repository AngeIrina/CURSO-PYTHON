
# Como hacer peticiones a APIs con Python con y sin dependencias.

# 1. Sin dependencias: modulos nativos de Python
# import urllib.request 
# import json

# api_posts = 'https://jsonplaceholder.typicode.com/posts'

# try:
#     # Hacemos la peticion a la API
#     response = urllib.request.urlopen(api_posts)
#     # Leemos el contenido de la respuesta
#     data = response.read()
#     # Convertimos a JSON
#     json_data = json.loads(data.decode['utf-8'])
#     print(json_data) # Imprimimos el resultado
#     response.close() # Cerramos la respuesta
# except urllib.error.URLError as e:
#     print(f'Error en la solicitud: {e}')


# # 2. Con dependencias: requests
# import requests 

# api_posts = 'https://jsonplaceholder.typicode.com/posts'
# response = requests.get(api_posts) # Hacemos la peticion a la API
# json = response.json() # Convertimos a JSON
# print(json) # Imprimimos el resultado


# # Peticion POST - Hay que pasarle todo el objeto
# api_posts = 'https://jsonplaceholder.typicode.com/posts'
# response = requests.post(api_posts, json={
#     'title': 'foo',
#     'body': 'bar',
#     'userId': 1
# }) # Hacemos la peticion a la API. 
# # El body, title y userId son los datos que enviamos a la API. Se pueden pasar por fuera tambien (params={...}).
# print(response.status_code())


# # PUT.
# api_posts = 'https://jsonplaceholder.typicode.com/posts'

# try:
#  response = requests.put(api_posts, json={
#     'title': 'foo',
#     'body': 'bar',
#     'userId': 1,
#     'id': 1
# }) 
#  print(response.status_code())
# except requests.exceptions.RequestException as e:
#     print(f'Error en la solicitud: {e}')



# Usar la API de OpenAI
# Debemos pasarle la API Key y el modelo a usar.
# En este caso, usaremos el modelo gpt-3.5-turbo.

# Ref: https://platform.openai.com/docs/api-reference/chat/create

OPENAI_KEY = 'sk-...' # API Key de OpenAI.
# La API Key se puede obtener desde la pagina de OpenAI.

import json
import requests

def call_openai_gpt(api_key, prompt):
    url = 'https://api.openai.com/v1/chat/completions' # URL de la API de OpenAI.
    headers = {
        "Content-Type": "application/json", 
        "Authorization": f"Bearer {OPENAI_KEY}" # Bearer es el tipo de autenticacion que se usa. 
         }
    data = {
        "model": "gpt-3.5-turbo", # Modelo a usar.
        "messages": [{"role": "user", "content": prompt}],}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

api_response = call_openai_gpt(OPENAI_KEY, "Escribe un poema sobre la luna")

print(api_response)


# Llamamos la API de DEEPSEEK 
# Lo mismo que antes, pero con la API de DEEPSEEK. Cambiando url, model, api_key y prompt.




