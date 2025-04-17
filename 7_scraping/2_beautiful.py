
from bs4 import BeautifulSoup
import requests

url = 'https://www.example.com'
response = requests.get(url)

if response.status_code == 200:
    print("Page fetched successfully")

    soup = BeautifulSoup(response.text, 'html.parser')

    # print(soup.prettify()) 
    title_tag = soup.title
    if title_tag:
        print("Title of the page:", title_tag.text)


# Buscar precio usando bs
price_span =  soup.find_all('span', class_='price')
if price_span:
   print("Price of the page:", price_span.text)


# Buscar todos los precios
price_spans = soup.find_all('span', class_='price') # Span es opcional
for price in price_spans:
    print("Precio del producto:", price.text)

# Obtener todos los productos y nombres
products = soup.find_all('div', class_='product')
for product in products:
    name = product.find('h2', class_='product-name').text # h2, div es opcional.
    price = product.find('span', class_='price').text # podemos usar otros atributos
    print(f"Product: {name}, Price: {price}")  
    
