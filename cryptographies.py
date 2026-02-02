
def abbacrypt(text):
    reference = {"a":"b", "c":"d", "e":"f", "g":"h", "i":"j", "k":"l", "m":"n", "o":"p", "q":"r", "s":"t", "u":"v", "w":"x", "y":"z"}
    encrypted = ""
    selected_char = ""
    text = text.lower()
    splitted = list(text)
    for letter in splitted:
        selected_char = ""
        for key,value in reference.items():
            if letter == key:
                selected_char = value
            elif letter == value:
                selected_char = key
        if selected_char != "":
            encrypted = encrypted + selected_char
        else:
            encrypted = encrypted + letter

    return encrypted
