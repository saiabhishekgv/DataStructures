def decode(string):
    s = ''
    number = 0
    char = ''
    for i in string:
        if 96<ord(i)<123 or 65<ord(i)< 91:
            char = i
            for k in range(number):
                s += char
        else :
            number = number*10 + int(i)
    return s

def encode(string):
    s = ''
    prev = ''
    count = 0
    flag = 0
    for i in string:
        if flag == 0:
            flag = 1
            prev = i
            count = 1
            continue
        if i == prev:
            count += 1
        else :
            s += str(count) + prev
            count = 1
            prev = i

    s += str(count) + prev
    return s