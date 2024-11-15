from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Configuración de Selenium (cambia el path a donde esté tu controlador)
driver_path = "ruta/al/chromedriver"  # Cambia este path
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Abre la página web
driver.get("https://www.tiobe.com/tiobe-index/")

# Espera hasta que la tabla esté presente (tiempo de espera máximo de 10 segundos)
try:
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )

    # Extrae filas de la tabla
    rows = table.find_elements(By.TAG_NAME, "tr")
    data = []

    # Iterar sobre las filas e extraer el texto de las celdas
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        cell_text = [cell.text.strip() for cell in cells]
        if cell_text:  # Asegurarse de que la fila tenga datos
            data.append(cell_text)

    # Crear el DataFrame y guardarlo en un archivo Excel
    df = pd.DataFrame(data)
    df.to_excel("tiobe_index_selenium.xlsx", index=False, header=False)
    print("La tabla ha sido guardada en 'tiobe_index_selenium.xlsx'")

finally:
    # Cierra el navegador
    driver.quit()
