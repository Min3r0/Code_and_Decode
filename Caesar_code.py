def caesar_code(message, decallage):
    code = ""
    message = message.lower()
    for letter in message:
        if 'a' <= letter <= 'z':
            new_letter = chr((ord(letter) - ord('a') + decallage) % 26 + ord('a'))
            code += new_letter
        else:
            code += letter
    return code
