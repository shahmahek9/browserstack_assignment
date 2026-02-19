from deep_translator import GoogleTranslator

def translate_titles(spanish_titles):
    translated = []

    print("\nTRANSLATED TITLES:\n")
    for title in spanish_titles:
        english = GoogleTranslator(source='es', target='en').translate(title)
        print(english)
        translated.append(english)

    return translated
