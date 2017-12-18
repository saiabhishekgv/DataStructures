
import re
from collections import Counter

def word_count(phrase):
    reg = re.compile(r'[a-z0-9\']+')
    wc = dict()
    print reg.findall(phrase.lower())
    for w in reg.findall(phrase.lower()):
        word = w.strip("':.")
        wc[word] = wc.get(word,0)+1
    return wc