from Affine_code import affine_code
from Affine_decode import affine_decode
from Binaire_code import binary_code
from Binaire_decode import binary_decode
from Caesar_code import caesar_code
from Caesar_decode import caesar_decode
from Hexa_code import hexa_code
from Hexa_decode import hexa_decode
from Vigenere_code import vigenere_code
from Vigenere_decode import vigenere_decode

# Exemple de déchiffrement avec le chiffre de César
print(caesar_decode("erqmrxu à wrxv !", 3))
# Exemple d'encodage avec le chiffre de César
print(caesar_code("Hello World !", 8))

# Exemple d'encodage avec Vigenère
message = "bonjour"
key = "cle"
result = vigenere_code(message, key)
print("Message chiffré :", result)

# Exemple de déchiffrement avec Vigenère
encrypted_message = "dzrlzyt"
key = "cle"
result = vigenere_decode(encrypted_message, key)
print("Message déchiffré :", result)

# Exemple d'encodage affine
print(affine_code("code", 17, 3))
# Exemple de déchiffrement affine
print(affine_decode("lhct", 17, 3))

text = "BONJOUR"
binary_encoded = binary_code(text)
print("Texte original :", text)
print("Encodage binaire (8 bits) :", binary_encoded)

binary_data = "0100100001100101011011000110110001101111"
decoded_text = binary_decode(binary_data)
print(decoded_text)

message = "Bonjour, comment ça va ?"
code_hex = hexa_code(message)
print(f"Message codé en hexa : {code_hex}")

hex_message = "426f6e6a6f75722c20636f6d6d656e74206361c3a0207661203f"  # Correspond à "Bonjour, comment ça va ?"
message_decode = hexa_decode(hex_message)
print(f"Message décodé : {message_decode}")
