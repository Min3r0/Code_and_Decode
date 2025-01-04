def binary_decode(binary_string):
    try:
        if len(binary_string) % 8 != 0:
            raise ValueError("La chaîne binaire doit être un multiple de 8 bits.")

        bytes_list = [binary_string[i:i + 8] for i in range(0, len(binary_string), 8)]

        text = ''.join([chr(int(byte, 2)) for byte in bytes_list])
        return text

    except ValueError as e:
        return f"Erreur : {e}"
