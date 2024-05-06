import requests
from PyPDF2 import PdfReader
from io import BytesIO
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


from langdetect import detect_langs

def is_spanish(text, target_lang='es'):
    lang_probs = detect_langs(text)
    for elem in lang_probs:
        lang = elem.lang
        prob = elem.prob
        if lang == target_lang and prob > 0.6:
            return True
    return False

url = "https://repositorio.minedu.gob.pe/bitstream/handle/20.500.12799/7490/Yachachinapaq%20simikuna%20-%20Urin%20Qichwa%20vocabulario%20pedag%C3%B3gico%20quechua%20sure%C3%B1o.pdf?sequence=1&isAllowed=y"


response = requests.get(url)

response.raise_for_status()

pdf_file = BytesIO (response.content)


pdf_reader = PdfReader(pdf_file)

text = ""
for page in pdf_reader.pages:
    text += page.extract_text()


words = text.split()

print(words[:10])
