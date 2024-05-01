def remove_html_entities(text):
    pattern = re.compile(r'&[^;]+;')
    return pattern.sub('', text)