def vigenere_code(message: str, key: str) -> str:
    encrypted_message = ""
    message = message.lower()
    key = key.lower()
    for i in range(len(message)):
        if 'a' <= message[i] <= 'z':
            encrypted_lettre = ord(message[i]) + (ord(key[i % len(key)]) - ord('a'))
            if encrypted_lettre > ord('z'):
                encrypted_lettre -= 26

            encrypted_message += chr(encrypted_lettre)
        else:
            encrypted_message += message[i]

    return encrypted_message
