def affine_code(message, a, b):
    list_first = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if a not in list_first:
        return "ERROR : a is not a prime number whit 26"

    encrypted_message = ""
    message = message.lower()
    for letter in message:
        if letter in alphabet:
            encrypted_message += alphabet[((a * alphabet.index(letter) + b) % 26)]
        else:
            encrypted_message += letter

    return encrypted_message
