def vigenere_decode(message: str, key: str) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decoded_message = ""
    key = key.lower()
    key_length = len(key)
    key_indices = [alphabet.index(k) for k in key]

    for i, char in enumerate(message):
        if char.lower() in alphabet:
            char_index = alphabet.index(char.lower())
            key_index = key_indices[i % key_length]
            decoded_char = alphabet[(char_index - key_index) % len(alphabet)]
            decoded_message += decoded_char
        else:

            decoded_message += char

    return ''.join(decoded_message)
