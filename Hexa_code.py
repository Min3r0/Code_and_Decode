def hexa_code(message):
    if not isinstance(message, str):
        raise ValueError("Le message doit être une chaîne de caractères.")

    hex_message = message.encode("utf-8").hex()
    return hex_message
