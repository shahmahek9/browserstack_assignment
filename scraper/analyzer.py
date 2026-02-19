import re
from collections import Counter

def analyze_words(english_titles):
    text = " ".join(english_titles).lower()
    words = re.findall(r'\b[a-z]{4,}\b', text)

    freq = Counter(words)

    print("\nWORDS REPEATED MORE THAN TWICE:")
    for word, count in freq.items():
        if count > 2:
            print(word, count)
