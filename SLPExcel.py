import openpyxl
from openpyxl.styles import Font
from openpyxl import Workbook

# PRECIO DEL DIA DEL SLP
contenido = open("SLPdata.csv", "r")
lineas = contenido.readlines()          # Copio el contenido del archivo SLPdata.csv a una lista
contenido.close()
ultima_linea = lineas[len(lineas)-1]

# VALORES VARIABLES
Fecha = ultima_linea.split(sep=',"')[0]
Precio = ultima_linea.split(sep=',"')[1]
SLP_hoy = int(input("SLP en tu inventario hoy: "))
i = len(lineas)

# Escribo el Excel

if (len(lineas)-1) == 0:

    book = Workbook()
    sheet = book.active

    sheet['A1'] = "Fecha"
    sheet['A1'].font = Font(bold=True)

    sheet['B1'] = "Precio"
    sheet['B1'].font = Font(bold=True)

    sheet['C1'] = "SLP_hoy"
    sheet['C1'].font = Font(bold=True)

    sheet[f'A{i+1}'] = Fecha
    sheet[f'B{i+1}'] = Precio
    sheet[f'C{i+1}'] = SLP_hoy

    book.save('SLP.xlsx')

else:
    documento = openpyxl.load_workbook('SLP.xlsx')
    sheet = documento.active


    sheet[f'A{i+1}'] = Fecha
    sheet[f'B{i+1}'] = Precio
    sheet[f'C{i+1}'] = SLP_hoy

    documento.save('SLP.xlsx')
