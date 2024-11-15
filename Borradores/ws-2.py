import requests 
from bs4 import BeautifulSoup
import pandas as pd

# URL del sitio web
url = "https://www.tiobe.com/tiobe-index/"

# Realizar la solicitud HTTP
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Encontrar la tabla (modifica el selector según la estructura de la página)
table = soup.find("table", {"id": "top20", "class": "table table-striped table-top20"})

# Extraer los datos de la tabla
#data = []
#for row in table.find_all("tr"):
   # cols = row.find_all(["th", "td"])
   # data.append([col.get_text(strip=True) for col in cols])
    
    # Extraer los datos de la tabla
data = []
rows = table.find_elements(By.TAG_NAME, 'tr')
for row in rows[1:]:  # Ignorar la primera fila de encabezados
    cols = row.find_elements(By.TAG_NAME, 'td')
    if len(cols) == 5:  # Asegurarse de que la fila tiene 5 columnas
        data.append([col.text.strip() for col in cols])

# Convertir los datos en un DataFrame de Pandas
df = pd.DataFrame(data[1:], columns=data[0])

# Guardar el DataFrame en un archivo Excel
df.to_excel("Lenguajes de programacion mas usados 2024.xlsx", index=False)
print("Archivo Excel 'Lenguajes de programacion mas usados 2024.xlsx' generado exitosamente.")