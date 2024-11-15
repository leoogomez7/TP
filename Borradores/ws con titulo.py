import requests as re
from bs4 import BeautifulSoup
import pandas as pd

# Título por defecto
titulo_personalizado = "Lenguajes de programación mas usados en 2024"
print("\n" + titulo_personalizado + "\n" + "="*len(titulo_personalizado) + "\n")

# Hacer la solicitud GET
response = re.get('https://www.tiobe.com/tiobe-index/')

# Parsear el HTML con BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Buscar la tabla en el HTML
table = soup.find('table')

# Extraer las filas de la tabla
rows = table.find_all('tr')

# Crear una lista para almacenar las filas
data = []

# Iterar sobre las filas e imprimir las celdas
for row in rows:
    cells = row.find_all(['td', 'th'])  # Obtener tanto las celdas de datos (td) como los encabezados (th)
    cell_text = [cell.text.strip() for cell in cells]  # Extraer texto de las celdas
    print(cell_text)
    data.append(cell_text)  # Añadir cada fila a la lista de datos

# Definir los títulos de las columnas personalizados
custom_headers = ["Ranking Noviembre 2024", "Ranking Noviembre 2023", "-", "-", "Lenguaje de Programación", "Calificación", "Cambio"]  # Modifica estos títulos según tus necesidades

# Exportar los datos a un archivo Excel
# Crear el DataFrame con las filas de datos (excluyendo el encabezado extraído, si existe)
df = pd.DataFrame(data[1:], columns=custom_headers)  # Usa data[1:] para omitir la primera fila si es el encabezado extraído

# Exportar los datos a un archivo Excel con los títulos personalizados
df.to_excel('tiobe_index.xlsx', index=False)  # Exportar sin índice ni encabezado