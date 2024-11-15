import requests as re
from bs4 import BeautifulSoup

# Hacer la solicitud GET
response = re.get('https://www.tiobe.com/tiobe-index/')

# Parsear el HTML con BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Buscar la tabla en el HTML
table = soup.find('table')

# Extraer las filas de la tabla
rows = table.find_all('tr')

# Iterar sobre las filas e imprimir las celdas
for row in rows:
    cells = row.find_all(['td', 'th'])  # Obtener tanto las celdas de datos (td) como los encabezados (th)
    cell_text = [cell.text.strip() for cell in cells]  # Extraer texto de las celdas
    print(cell_text)
    
    