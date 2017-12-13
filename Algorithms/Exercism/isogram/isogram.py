def is_isogram(string):
    hm = dict()
    for i in string:
        hm[i] = hm.get(i,0)+1
        if hm[i]>1:
            return False

    return True

