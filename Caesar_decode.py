def caesar_decoder_bruteforce(decrypt_function):
    def wrapper(message, key=None):
        if key is None:
            print("Aucune clé fournie. Tentative de toutes les clés possibles :")
            for potential_key in range(26):
                possible_message = decrypt_function(message, potential_key)
                print(f"Clé {potential_key:02d} : {possible_message}")
        else:
            return decrypt_function(message, key)

    return wrapper


@caesar_decoder_bruteforce
def caesar_decode(message, key):
    decoded_message = ""
    message = message.lower()
    for letter in message:
        if 'a' <= letter <= 'z':
            new_letter = chr((ord(letter) - ord('a') - key) % 26 + ord('a'))
            decoded_message += new_letter
        else:
            decoded_message += letter
    return decoded_message
