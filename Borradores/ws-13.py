import requests
from bs4 import BeautifulSoup

# URL de la página
url = "https://www.linkedin.com/pulse/navigating-learning-curve-definitive-ranking-languages-ibrahim-khalil/"

# Headers para simular una solicitud desde un navegador
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

# Hacer la solicitud GET
response = requests.get(url, headers=headers)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Buscar y extraer datos específicos (por ejemplo, títulos, párrafos, etc.)
    title = soup.find('h1')  # Modifica según la estructura de la página
    content = soup.find_all('p')  # Modifica según lo que quieras extraer
    
    print("Título:", title.text if title else "No encontrado")
    for paragraph in content:
        print(paragraph.text)
else:
    print(f"Error al acceder a la página: {response.status_code}")
