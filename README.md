# TP Web Scraping
Trabajo Práctico de Web Scraping para la materia Taller de Lenguajes - UNO

# Descripción
Utilice el programa Visual Studio Code para aplicar las tecnicas de Web Scraping, dónde escribí mi script en el lenguaje de programación PYTHON (.py), dónde en un directorio llamado "TP" instale las distintas librerias (requests ; BeautifulSoup ; pandas ; openpyxl). En este script realiza Web Scraping de tres sitios web que contienen información sobre 3 ranking's de lenguajes de programación (más usado, mejor pagados, complejidad). Utiliza "requests" para hacer las solicitudes HTTP, "BeautifulSoup" para parsear el contenido HTML y XML, y "pandas" (para trabajar con datos en forma de tablas) junto con "openpyxl" (para interactuar con archivos Excel) para exportar los datos extraídos a archivos de Excel, los cuales incluyen tablas y listas de los distintos ranking de lenguajes de programación.

# Extración de datos
Sitio web 1: Ranking de los lenguajes de programación más usados en 2024, obtenido de (https://www.tiobe.com/tiobe-index/)

Sitio web 2: Ranking de los lenguajes de programación que mejor pagan en 2024, obtenido de (https://golang.withcodeexample.com/blog/top-highest-paying-programming-languages-to-learn-in-2024/)

Sitio web 3: Ranking de lenguajes de programación ordenados de fácil a difícil según su complejidad, obtenido de (https://www.digitalogy.co/blog/programming-languages-from-easy-to-hard/)

# Exportación a Excel (.xlsx)
Para cada sitio web, los datos extraídos se organizan en "DataFrames" de "pandas" y luego se exportan a archivos de Excel (.xlsx) con sus respectivos títulos y datos.
Se utiliza "openpyxl" para ajustar el formato (ancho de las columnas, la alineación de los textos y la inserción de títulos personalizados en las primeras filas).

# Archivos de Excel
Se guardan tres archivos (.xlsx) distintos:

1- Lenguajes de programación más usados 2024.xlsx

2-Lenguajes de Programación que mejor pagan en 2024.xlsx

3-Lenguajes de Programación ordenados de fácil a difícil según su complejidad.xlsx

# Instalación de librerias
pip install requests beautifulsoup4 pandas openpyxl

# Conclusión
El script genera tres archivos de Excel, cada uno con un ranking diferente de lenguajes de programación según su uso, salario o dificultad, y los guarda en el formato adecuado para su posterior análisis y presentación.
