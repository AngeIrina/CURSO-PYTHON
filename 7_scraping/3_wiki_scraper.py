from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests


url = 'https://www.example.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url)


if response.status_code == 200:
    print("Page fetched successfully")

    soup = BeautifulSoup(response.text, 'html.parser')

# Extraer todos los titulos (h1)
from urllib.parse import urljoin

titulos = [titulo.string for titulo in soup.find_all('h1')]
print(titulos)

# Extraer todos los enlaces (a)
enlaces = [urljoin(url, enlace.get('href')) for enlace in soup.find_all('a')]
print(enlaces) # Son enlaces relativos, podemos usar urljoin para convertirlos en absolutos (de forma que venga con toda la informacion)

# Extraer todo el contenido de la pagina de texto
contenido = soup.get_text()
print(contenido)

# Extraer el texto del elemento con id="main"
main = soup.find(id='main').get_text()
print(main)

# extraer de la id mw-content-text
# content_text = soup.find('div', {'id': 'mw-content-text'}).get_text()
# print(content_text)

# extrar el open graph si existe
# og_image = soup.find('meta', {'property': 'og:image'})
    
og_image = soup.find('meta', property='og:image')
if og_image:
    print(og_image['content'])
else:
    print('No se encontró la imagen')

# scrape_url('https://midu.dev')