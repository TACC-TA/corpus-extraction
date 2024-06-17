from PyPDF2 import PdfReader
import re
import pandas as pd

# Function to extract text from each page of the PDF
def extract_text_from_pdf(pdf_path):
    pdf_reader = PdfReader(pdf_path)
    text_data = []
    for page in pdf_reader.pages:
        text_data.append(page.extract_text())
    return text_data

# Function to extract dictionary entries
def extract_dictionary_entries(text_data):
    entries = []
    entry_pattern = re.compile(r'\b([A-ZÑÁÉÍÓÚÜa-zñáéíóúü]+)\b\s+-\s+([^\n]+)')
    for page in text_data:
        matches = entry_pattern.findall(page)
        entries.extend(matches)
    return entries

# Path to the PDF file
pdf_path = '567754321-Diccionario-Niraq-Masi-Simikuna-Taqi.pdf'

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Extract dictionary entries
dictionary_entries = extract_dictionary_entries(pdf_text)

# Convert to DataFrame
df = pd.DataFrame(dictionary_entries, columns=['Quechua', 'Español'])

# Save to Excel
df.to_excel('Quechua_Spanish_Dictionary.xlsx', index=False)