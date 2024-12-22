def modular_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def affine_decode(code, a, b):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    m = len(alphabet)
    a_inv = modular_inverse(a, m)
    if a_inv is None:
        raise ValueError("a n'a pas d'inverse modulaire, choisissez un a valide avec a et 26 premiers entre eux.")
    decoded_message = ""
    for letter in code:
        if letter in alphabet:
            decoded_message += alphabet[((alphabet.index(letter) - b) * a_inv) % m]
        else:
            decoded_message += letter
    return decoded_message
