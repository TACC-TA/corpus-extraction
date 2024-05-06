import requests
from PyPDF2 import PdfReader
from io import BytesIO
import csv
import nltk
from nltk.corpus import stopwords
import urllib3



from langdetect import detect_langs

def is_spanish(text, target_lang='es'):
    lang_probs = detect_langs(text)
    for elem in lang_probs:
        lang = elem.lang
        prob = elem.prob
        if lang == target_lang and prob > 0.6:
            return True
    return False


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://fcctp.usmp.edu.pe/librosfcctp/DICCIONARIO-Quechua-espanol-VOL_2.pdf"

response = requests.get(url)

response.raise_for_status()

pdf_file = BytesIO (response.content)


pdf_reader = PdfReader(pdf_file)

text = " "
for page in pdf_reader.pages:
    text += page.extract_text()



print (text)
