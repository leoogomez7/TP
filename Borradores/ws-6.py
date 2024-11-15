import requests as re
from bs4 import BeautifulSoup
import pandas as pd

# Hacer la solicitud GET
response = re.get('https://www.tiobe.com/tiobe-index/')

# Parsear el HTML con BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Buscar la tabla en el HTML
table = soup.find('table')

# Extraer las filas de la tabla
rows = table.find_all('tr')

# Crear una lista para almacenar las filas de datos y los encabezados
data = []
header = []

  
    # Iterar sobre las filas e imprimir las celdas
    # Procesar la primera fila como encabezado, el resto como datos
for i, row in enumerate(rows):
    cells = row.find_all(['td', 'th']) # Obtener tanto las celdas de datos (td) como los encabezados (th)
    cell_text = [cell.text.strip() for cell in cells] # Extraer texto de las celdas
    print(cell_text)

    # Separar encabezado de los datos
    if i == 0:
        header = cell_text  # La primera fila será el encabezado
    else:
        data.append(cell_text)  # Las siguientes filas serán los datos # Añadir cada fila a la lista de datos

# Exportar los datos a un archivo Excel y Crear un DataFrame con encabezado y datos ("columns=header")
df = pd.DataFrame(data, columns=header)
df.to_excel('tiobe_index.xlsx', index=False, header=False)  # Exportar sin índice ni encabezado