# Code_and_Decode

Ce projet est une implémentation du chiffrement et du déchiffrement utilisant trois méthodes : César, Vigenère, et
Affine. Vous
pouvez chiffrer un message avec une clé spécifique ou, pour la méthode Affine, avec des paramètres spécifiques (a et b)
respectant des contraintes mathématiques.
clé fournie. Dans le cas du chiffrement César, si aucune clé n'est
fournie lors du déchiffrement, le
programme tentera toutes les clés possibles (force brute).

## Fonctionnalités 🛠️

- `vigenere_code` : Permet de chiffrer un message en utilisant une clé avec l'algorithme de Vigenère.
- `vigenere_decode` : Permet de déchiffrer un message chiffré avec une clé via l'algorithme de Vigenère.
- `affine_code` : Permet de chiffrer un message en utilisant l'algorithme de chiffrement affine.
- `affine_decode` : Permet de déchiffrer un message chiffré avec l'algorithme affine.
- `caesar_code` : Permet de chiffrer un message donné avec un décalage spécifique.
- `caesar_decode` : Permet de déchiffrer un message avec une clé donnée ou de tenter toutes les clés via une approche de
  force brute.

## Exemple d'utilisation

Voici un exemple d'utilisation des modules de chiffrement et de déchiffrement pour César et Vigenère :

Voici un exemple de code principal (`Main.py`) utilisant les deux modules de chiffrement et de déchiffrement :

```python
from Caesar_code import caesar_code
from Caesar_decode import caesar_decode
from Vigenere_code import vigenere_code
from Vigenere_decode import vigenere_decode
from Affine_code import affine_code
from Affine_decode import affine_decode

print(caesar_decode("erqmrxu à wrxv !"))
print(caesar_code("Hello World !", 8))
print(vigenere_code("Hello World !", "KEY"))
print(vigenere_decode("RIJVS UYVJN !", "KEY"))
print(affine_code("Hello World !", 5, 8))
print(affine_decode("IFMMP XPSME !", 5, 8))
```

## Fichiers du projet 📂

- **`Vigenere_code.py`** : Contient la fonction `vigenere_code` pour chiffrer un message avec la méthode de Vigenère.
- **`Vigenere_decode.py`** : Contient la fonction `vigenere_decode` pour déchiffrer un message avec une clé.

- **`Main.py`** : Contient un exemple démontrant comment utiliser les fonctions de chiffrement et de déchiffrement.
- **`Caesar_code.py`** : Contient la fonction `caesar_code` pour chiffrer un message.
- **`Caesar_decode.py`** : Contient la fonction `caesar_decode` pour décrypter un message avec ou sans clé.
- **`Affine_code.py`** : Contient la fonction `affine_code` pour chiffrer un message avec la méthode affine.
- **`Affine_decode.py`** : Contient la fonction `affine_decode` pour déchiffrer un message avec la méthode affine.
- **`README.md`** : Ce fichier.

## Dépendances

Aucune dépendance externe n'est requise pour ce projet. Le code utilise uniquement des fonctionnalités natives de
Python.

## Instructions pour exécuter le projet 📋

1. Assurez-vous d'utiliser **Python 3.9** ou une version ultérieure.
2. Clonez ce projet :
   ```bash
   git clone https://github.com/Min3r0/code_and_decode.git
   ```
3. Placez-vous dans le dossier :
   ```bash
   cd code_and_decode
   ```
4. Exécutez le fichier `Main.py` pour tester les fonctionnalités :
   ```bash
   python Main.py
   ```

## Fonctionnement des Modules ⚙️

### `Affine_code.py`

Cette fonction applique l'algorithme de chiffrement affine en utilisant les paramètres définis par l'utilisateur.

Exemple :

```python
from Affine_code import affine_code

message = "hello world"
a = 5
b = 8
print(affine_code(message, a, b))  # Sortie : IFMMP XPSME
```

### `Affine_decode.py`

Permet de décrypter un message chiffré en utilisant l'algorithme affine avec des paramètres fournis.

Exemple :

```python
from Affine_decode import affine_decode

message = "IFMMP XPSME"
a = 5
b = 8
print(affine_decode(message, a, b))  # Sortie : hello world
```

### `Vigenere_code.py`

Cette fonction utilise une clé définie par l'utilisateur pour appliquer le chiffrement de Vigenère à un message.

Exemple :

```python
from Vigenere_code import vigenere_code

message = "hello world"
cle = "KEY"
print(vigenere_code(message, cle))  # Sortie : RIJVS UYVJN
```

### `Vigenere_decode.py`

Permet de décrypter un message chiffré par la méthode de Vigenère à l'aide d'une clé donnée.

Exemple :

```python
from Vigenere_decode import vigenere_decode

message = "RIJVS UYVJN"
cle = "KEY"
print(vigenere_decode(message, cle))  # Sortie : hello world
```

### `Caesar_code.py`

Cette fonction applique un décalage (clé) fourni par l'utilisateur pour chiffrer un message.

Exemple :

```python
from Caesar_code import caesar_code

message = "hello world"
decallage = 3
print(caesar_code(message, decallage))  # Sortie : khoor zruog
```

### `Caesar_decode.py`

Permet de décrypter un message chiffré par la méthode de César. Si aucune clé n'est donnée, toutes les clés possibles
sont testées pour tenter de retrouver le texte d'origine.

Exemple avec clé :

```python
from Caesar_decode import caesar_decode

message = "khoor zruog"
cle = 3
print(caesar_decode(message, cle))  # Sortie : hello world
```

Exemple sans clé :

```python
from Caesar_decode import caesar_decode

message = "khoor zruog"
print(caesar_decode(message))  # Affiche toutes les possibilités de décryptage
```

## Licence 📜

Ce projet est sous licence **MIT**. Vous êtes libre d'utiliser, modifier et redistribuer le code.

---
Créé par Romain AUGÉ