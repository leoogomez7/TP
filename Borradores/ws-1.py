from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import IEDriverManager
import pandas as pd

# Descargar e instalar el controlador de Microsoft Edge (usando IEDriverManager)
driver_path = IEDriverManager().install()

# Configurar el navegador para usar Edge
options = webdriver.EdgeOptions()
options.add_argument('--headless')  # Opcional: Ejecutar Edge sin ventana gráfica

# Crear la instancia de WebDriver de Edge
driver = webdriver.Edge(executable_path=driver_path, options=options)  # Corregido aquí

# URL del sitio web
url = "https://www.tiobe.com/tiobe-index/"

# Cargar la página
driver.get(url)

# Esperar que la página cargue
driver.implicitly_wait(10)

# Encontrar la tabla de clasificación (con id 'top20')
table = driver.find_element(By.ID, 'top20')

# Extraer los datos de la tabla
data = []
rows = table.find_elements(By.TAG_NAME, 'tr')
for row in rows[1:]:  # Ignorar la primera fila de encabezados
    cols = row.find_elements(By.TAG_NAME, 'td')
    if len(cols) == 5:  # Asegurarse de que la fila tiene 5 columnas
        data.append([col.text.strip() for col in cols])
        
# Convertir los datos en un DataFrame de Pandas
df = pd.DataFrame(data, columns=["Nov 2024", "Nov 2023", "Change", "Programming Language", "Ratings"])

# Guardar el DataFrame en un archivo Excel
df.to_excel("Lenguajes de programacion mas usados 2024.xlsx", index=False)
print("Archivo Excel 'Lenguajes de programacion mas usados 2024.xlsx' generado exitosamente.")

# Cerrar el navegador
driver.quit()