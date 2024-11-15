import requests
from bs4 import BeautifulSoup
import pandas as pd

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
    
    # Buscar y extraer el título del artículo
    title = soup.find('h1')  # Modifica según la estructura de la página
    title_text = title.text if title else "No encontrado"
    
    # Buscar y extraer todos los párrafos
    content = soup.find_all('p')  # Modifica según lo que quieras extraer
    paragraphs = [paragraph.text for paragraph in content]
    
    print("Título:", title_text)
    print("Contenido extraído:")
    for paragraph in paragraphs:
        print(paragraph)
    
    # Crear un DataFrame con los datos
    data = {
        "Título": [title_text],
        "Contenido": ["\n".join(paragraphs)]  # Unir los párrafos en una sola cadena con saltos de línea
    }
    df = pd.DataFrame(data)
    
    # Exportar a un archivo Excel
    excel_file = "datos_extraidos.xlsx"
    df.to_excel(excel_file, index=False, sheet_name="Web Scraping")
    print(f"Datos exportados exitosamente a {excel_file}")
else:
    print(f"Error al acceder a la página: {response.status_code}")