import pandas as pd
import requests
#import xlsxwriter
URL = "https://www.tiobe.com/tiobe-index/"
tabla = pd.read_html(requests.get(URL).text, flavor="bs4", decimal=',', thousands='.')
workbook=pd.ExcelWriter(r'C:\Users\campe\OneDrive\Escritorio\UNIVERSIDAD\2do Cuatrimestre 2024\Taller de Lenguajes\TP\Lenguajes de programacion mas usados 2024.xlsx')
tabla[3].to_excel(workbook,'Hoja1', index=False)
print(tabla[3])
workbook.save()