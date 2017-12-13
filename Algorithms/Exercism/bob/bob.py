import re
def hey(phrase):
    if len(phrase) == 0 :
        return "Fine. Be that way!"

    chillout = re.findall("!",phrase)
    if(len(chillout)>0) and chillout[-1]==len(phrase)-1 and phrase == phrase.upper():
            return "Whoa, chill out!"

    chillout = re.findall("\?", phrase)
    if (len(chillout) > 0):
            return "Sure."

    return "Whatever."
