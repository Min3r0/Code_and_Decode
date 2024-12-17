# Code_and_Decode

Ce projet est une implémentation du chiffrement et du déchiffrement de César. Vous pouvez chiffrer un message avec une
clé spécifique ou déchiffrer un message avec une clé fournie. Si aucune clé n'est fournie lors du déchiffrement, le
programme tentera toutes les clés possibles (force brute).

## Fonctionnalités 🛠️

- `caesar_code` : Permet de chiffrer un message donné avec un décalage spécifique.
- `caesar_decode` : Permet de déchiffrer un message avec une clé donnée ou de tenter toutes les clés via une approche de
  force brute.

## Exemple d'utilisation

Voici un exemple de code principal (`Main.py`) utilisant les deux modules de chiffrement et de déchiffrement :

```python
from Caesar_code import caesar_code
from Caesar_decode import caesar_decode

print(caesar_decode("erqmrxu à wrxv !"))
print(caesar_code("Hello World !", 8))
```

## Fichiers du projet 📂

- **`Main.py`** : Contient un exemple démontrant comment utiliser les fonctions de chiffrement et de déchiffrement.
- **`Caesar_code.py`** : Contient la fonction `caesar_code` pour chiffrer un message.
- **`Caesar_decode.py`** : Contient la fonction `caesar_decode` pour décrypter un message avec ou sans clé.
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