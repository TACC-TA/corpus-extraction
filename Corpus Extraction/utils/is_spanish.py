import sys
import os

# Get the path to the parent directory
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the parent directory to the Python path
sys.path.append(parent_dir)

from langdetect import detect_langs

def is_spanish(text, target_lang='es'):
    lang_probs = detect_langs(text)
    for elem in lang_probs:
        lang = elem.lang
        prob = elem.prob
        if lang == target_lang and prob > 0.6:
            return True
    return False