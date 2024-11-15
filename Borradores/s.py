import requests
from bs4 import BeautifulSoup
import pandas as pd

# Función para hacer scraping y obtener datos
def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Aquí extraes datos específicos. Ejemplo:
    items = soup.select('.item-class')  # Cambia '.item-class' según la página
    ranks = []
    for item in items:
        title = item.select_one('.title-class').text.strip()  # Cambia '.title-class'
        score = float(item.select_one('.score-class').text.strip())  # Cambia '.score-class'
        ranks.append({'Title': title, 'Score': score})
    
    return ranks

# URLs para scraping (puedes usar diferentes URLs)
url_ranking_1 = 'https://example.com/ranking1'
url_ranking_2 = 'https://example.com/ranking2'

# Obtener datos
data_ranking_1 = scrape_data(url_ranking_1)
data_ranking_2 = scrape_data(url_ranking_2)

# Convertir a DataFrame
df_ranking_1 = pd.DataFrame(data_ranking_1).sort_values(by='Score', ascending=False)
df_ranking_2 = pd.DataFrame(data_ranking_2).sort_values(by='Score', ascending=False)

# Guardar en un archivo de Excel con dos pestañas
with pd.ExcelWriter('rankings.xlsx') as writer:
    df_ranking_1.to_excel(writer, sheet_name='Ranking 1', index=False)
    df_ranking_2.to_excel(writer, sheet_name='Ranking 2', index=False)

print("Archivo Excel generado: rankings.xlsx")