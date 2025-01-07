def hexa_decode(hex_message):
    if not isinstance(hex_message, str):
        raise ValueError("Le message en hexadécimal doit être une chaîne de caractères.")

    try:
        message = bytes.fromhex(hex_message).decode("utf-8")
    except ValueError:
        raise ValueError("La chaîne hexadécimale est invalide ou ne peut pas être décodée.")

    return message
