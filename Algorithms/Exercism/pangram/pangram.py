def is_pangram(sentence):
    charList = [False]*26

    for i in sentence:
        i = i.lower()
        if 96<ord(i) and ord(i)<123:
            charList[ord(i)-97] = True

    for i in charList:
        if i==False:
            return False

    return True
