# -*- coding: utf-8 -#-
#
# Auteur        : Cédric Kreis
# Programme     : Brute force
# Fonctions     : Applique un brute force sur un fichier .zip avec un
#                 dictionnaire
# Créé le       : 27.08.2020
# Modifié le    :
# Version       : 1
# Python        : 2.7.16+
#
#-------------------------------------------------------------------------------
from compteur import *
import zipfile
import sys

m = 0
compteur = compteur()

if len(sys.argv) != 3:
    print "Syntaxe : [Script] [ZIPFILE] [Dictionary]"
    sys.exit()

filename = str (sys.argv[1])
dicotionary = str (sys.argv[2])

file_to_open = zipfile.ZipFile(filename)
with open(dicotionary, 'r' ) as f:

    for line in f.readlines():
        password = line.strip('\n')
        m += 1

        try:
            file_to_open.extractall(pwd=password)
            #password = 'Mot de passe trouvé : %s' % password
            print "Nombre de tentative : %s fois" %m
            print 'Mot de passe trouvé : %s' % password
            print "Il y a %s mots en tout dans le dictionnaire" %compteur

        except:
            pass
