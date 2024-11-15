from selenium import webdriver
#from selenium.webdriver.edge.service import Service
#from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
#import msedgedriver_autoinstaller

# Instalar Microsoft Edge WebDriver automáticamente
#msedgedriver_autoinstaller.install()

# Configurar las opciones de Edge para deshabilitar la verificación SSL
options = Options()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-features=IsolateOrigins,site-per-process")
options.add_argument("--disable-web-security")

# Crear una instancia del navegador Edge
driver = webdriver.Edge()

# URL del sitio web
url = "https://www.tiobe.com/tiobe-index/"

# Realizar la solicitud a la página
driver.get(url)

# Esperar a que la tabla esté presente
wait = WebDriverWait(driver, 10)
table = wait.until(EC.presence_of_element_located((By.ID, "top20")))

# Verificar si se encontró la tabla correctamente
if table:
    print("Tabla encontrada correctamente.")
else:
    print("No se encontró la tabla.")

# Extraer los datos de la tabla
data = []
rows = table.find_elements(By.TAG_NAME, "tr")
for row in rows[1:]:  # Ignorar la primera fila de encabezados
    cols = row.find_elements(By.TAG_NAME, "td")
    if len(cols) == 5:  # Asegurarse de que la fila tiene 5 columnas
        data.append([col.text.strip() for col in cols])

# Imprimir los datos extraídos para depurar
print("Datos extraídos:")
for item in data:
    print(item)

# Convertir los datos en un DataFrame de Pandas
df = pd.DataFrame(data, columns=["Nov 2024", "Nov 2023", "Change", "Programming Language", "Ratings"])

# Guardar el DataFrame en un archivo Excel
df.to_excel("Lenguajes_de_programacion_mas_usados_2024.xlsx", index=False)
print("Archivo Excel 'Lenguajes de programacion mas usados 2024.xlsx' generado exitosamente.")

# Cerrar el WebDriver
driver.quit()