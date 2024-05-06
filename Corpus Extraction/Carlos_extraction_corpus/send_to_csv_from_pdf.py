import csv
from pdfminer.high_level import extract_text

# Extrae el texto del archivo PDF
text = extract_text('/home/carlos-garcia/Descargas/quechua_recetas.pdf')

# Divide el texto en palabras
words = text.split()

# Abre el archivo CSV en modo escritura
with open('quechua_recetas.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Escribe las palabras en el archivo CSV
    for word in words:
        writer.writerow([word])