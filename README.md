# Lisez-moi

# Projet : Application de Chiffrement/Déchiffrement 🔐

## Description 📝

Ce projet est un outil de chiffrement et de déchiffrement implémenté en Python. Il prend en charge diverses techniques,
notamment : 🔑

- **Chiffrement de César**
- **Chiffrement Affine**
- **Chiffrement de Vigenère**
- **Encodage/Décodage en binaire**
  Les utilisateurs peuvent chiffrer et déchiffrer des messages avec ces algorithmes en utilisant des clés et paramètres
  personnalisés.

## Fonctionnalités 🔒

- **Chiffrer des messages :** Sécurisez vos messages en clair en utilisant l'une des méthodes de chiffrement prises en
  charge.
- **Déchiffrer des messages :** Récupérez le texte en clair original en déchiffrant les données encodées.
- **Entrées personnalisées :** Entrez vos clés, paramètres et messages pour le chiffrement ou le déchiffrement.
- **Algorithmes pris en charge :**
    - **Chiffrement de César :** Un chiffrement par substitution qui décale les caractères d'un nombre fixe.
    - **Chiffrement Affine :** Applique des formules mathématiques pour le chiffrement et le déchiffrement.
    - **Chiffrement de Vigenère :** Utilise une clé répétée pour une substitution plus sécurisée.
    - **Conversion en binaire :** Encodez et décodez du texte en représentations binaires.

## Prérequis 🛠️

Assurez-vous que votre système dispose des éléments suivants installés :

- **Python :** Version 3.9+
- **Bibliothèques requises :** Installez les dépendances avec :

  ```bash
  pip install -r requirements.txt
  ```

## Exemples 💡

**1. Chiffrement de César**

Pour chiffrer avec le chiffrement de César :

```python
from Caesar_code import caesar_code

encrypted_message = caesar_code("Hello", shift=3)
print(encrypted_message)  # Output: Khoor
```

Pour déchiffrer avec le chiffrement de César :

```python
from Caesar_decode import caesar_decode

decrypted_message = caesar_decode("Khoor", shift=3)
print(decrypted_message)  # Output: Hello
```

**2. Chiffrement Affine**

Pour chiffrer avec le chiffrement Affine :

```python
from Affine_code import affine_code

encrypted_message = affine_code("Hello", a=5, b=8)
print(encrypted_message)  # Output: Encrypted text
```

Pour déchiffrer avec le chiffrement Affine :

```python
from Affine_decode import affine_decode

decrypted_message = affine_decode("Encrypted text", a=5, b=8)
print(decrypted_message)  # Output: Hello
```

**3. Chiffrement de Vigenère**

Pour chiffrer avec le chiffrement de Vigenère :

```python
from Vigenere_code import vigenere_code

encrypted_message = vigenere_code("Hello", "KEY")
print(encrypted_message)  # Output: Vigenère-encrypted text
```

Pour déchiffrer avec le chiffrement de Vigenère :

```python
from Vigenere_decode import vigenere_decode

decrypted_message = vigenere_decode("Vigenère-encrypted text", "KEY")
print(decrypted_message)  # Output: Hello
```

**4. Conversion en Binaire**

Pour encoder en binaire :

```python
from Binaire_code import binary_code

binary_message = binary_code("Hello")
print(binary_message)  # Output: Binary representation
```

Pour décoder depuis le binaire :

```python
from Binaire_decode import binary_decode

text_message = binary_decode("Binary representation")
print(text_message)  # Output: Hello
```

## Comment Exécuter 💻

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/Min3r0/Code_and_Decode
   cd encryption_decryption_app
   ```

2. Lancez l'application :

   ```bash
   python main.py
   ```

## Licence 📜

Ce projet est sous licence **MIT**. Vous êtes libre d'utiliser, modifier et redistribuer le code.

---
Créé par Romain AUGÉ
