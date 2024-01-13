#!/usr/bin/env python3
import sys
import string

translator = str.maketrans('', '', string.punctuation)

# Fonction pour vérifier si un mot contient des caractères numériques
def has_numbers(word):
    return any(char.isdigit() for char in word)

# Lecture de toute la ligne depuis STDIN (entrée standard)
for line in sys.stdin:
    # Pour supprimer les espaces en début et fin de ligne
    line = line.strip()
    # Supprimer la ponctuation et diviser la ligne en mots
    words = line.translate(translator).split()

    # Boucler sur le tableau de mots et imprimer le mot avec le compteur 1 vers STDOUT
    for word in words:
        # Vérifier si le mot contient des caractères numériques
        if word and not has_numbers(word):
            # Écrire les résultats vers STDOUT (sortie standard);
            # Ce que nous imprimons ici sera l'entrée pour l'étape de réduction, c'est-à-dire l'entrée pour reducer.py
            print(word.lower(), '\t', 1)
