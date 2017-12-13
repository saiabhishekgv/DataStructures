def word_count(phrase):
    split = phrase.split(' ')
    wc = dict()
    for i in split:
        wc[i] = wc.get(i,0) + 1

    return wc