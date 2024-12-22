from Affine_code import affine_code
from Affine_decode import affine_decode
from Caesar_code import caesar_code
from Caesar_decode import caesar_decode
from Vigenere_code import vigenere_code
from Vigenere_decode import vigenere_decode

print(caesar_decode("erqmrxu à wrxv !", 3))
print(caesar_code("Hello World !", 8))

message = "bonjour"
key = "cle"

result = vigenere_code(message, key)
print("Message chiffré :", result)

encrypted_message = "dzrlzyt"
key = "cle"

result = vigenere_decode(encrypted_message, key)
print("Message déchiffré :", result)

print(affine_code("code", 17, 3))
print(affine_decode("lhct", 17, 3))
