import requests
from bs4 import BeautifulSoup

url = 'https://hiraoka.com.pe/audio-y-musica/audifonos'

response = requests.get(url)
if response.status_code == 200:
    # Parseamos el contenido HTML de la página
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # En este ejemplo, supongamos que las noticias están en elementos <div> con la clase "noticia"
    productos = soup.find_all('strong', class_='product name product-item-name')
    
    # Iteramos sobre las noticias y extraemos el título y el enlace
    for producto in productos:
        titulo = producto.find('a')
        titulo_no_espacios = titulo.text.lstrip()
        
        print(f'Título: {titulo_no_espacios}')
else:
    print(f'Error al acceder a la página: {response.status_code}')
