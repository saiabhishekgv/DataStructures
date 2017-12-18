def rotate(text, key):
    new_text = ''
    for i in text:
        if not i.isalpha():
            new_text += i
        else:
            char_value = ord(i)
            is_capital = True if char_value>64 and char_value<91 else False
            new_char_value = ord(i)-65 if is_capital else ord(i) - 97
            new_char_value += key
            new_char_value %= 26
            new_char_value += 65 if is_capital else 97
            new_char_value = chr(new_char_value)
            new_text += new_char_value
    return new_text



