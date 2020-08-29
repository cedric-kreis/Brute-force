# -*- coding: utf-8 -#-
#
# Auteur        : Cédric Kreis
# Programme     : Compteur de ligne
# Fonctions     : Cette fonction compte le nombre de ligne pour un fichier texte
# Créé le       : 27.08.2020
# Modifié le    :
# Version       : 1
# Python        : 2.7.16+
#
#-------------------------------------------------------------------------------

import sys


def compteur():
    n = 0
    dicotionary = str (sys.argv[2])

    with open(dicotionary, 'r') as f:
        for line in f:
            n += 1
        return n
