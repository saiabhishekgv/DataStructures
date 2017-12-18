def detect_anagrams(word, candidates):
    d = dict()
    anagrams = []

    for i in word:
        d[i.lower()] = d.get(i.lower(),0) + 1

    c_map = dict()

    for i in candidates:
        flag = 0
        for j in i:
            c_map[j.lower()] = c_map.get(j.lower(),0)+1

        for j in i :
            if (j.lower() not in d) or (c_map.get(j.lower()) > d.get(j.lower())):
                c_map.clear()
                flag = 1
                break

        if flag == 0 :
            anagrams.append(i)
        c_map.clear()

    return anagrams



