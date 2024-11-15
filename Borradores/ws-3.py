from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
#mport msedgedriver_autoinstaller
import pandas as pd

# Instalar Microsoft Edge WebDriver automáticamente
#msedgedriver_autoinstaller.install()

# Crear una instancia del navegador Edge
driver = webdriver.Edge()

# URL del sitio web
url = "https://www.tiobe.com/tiobe-index/"

# Realizar la solicitud a la página
driver.get(url)

# Encontrar la tabla
table = driver.find_element(By.ID, "top20")

# Extraer los datos de la tabla
data = []
rows = table.find_elements(By.TAG_NAME, "tr")
for row in rows[1:]:  # Ignorar la primera fila de encabezados
    cols = row.find_elements(By.TAG_NAME, "td")
    if len(cols) == 5:  # Asegurarse de que la fila tiene 5 columnas
        print([col.text for col in cols])  # Ver qué datos estás extrayendo
        data.append([col.text.strip() for col in cols])

# Convertir los datos en un DataFrame de Pandas
df = pd.DataFrame(data, columns=["Nov 2024", "Nov 2023", "Change", "Programming Language", "Ratings"])

# Guardar el DataFrame en un archivo Excel
df.to_excel("Lenguajes_de_programacion_mas_usados_2024.xlsx", index=False)
print("Archivo Excel 'Lenguajes de programacion mas usados 2024.xlsx' generado exitosamente.")

# Cerrar el WebDriver
driver.quit()