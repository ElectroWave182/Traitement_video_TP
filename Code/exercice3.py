import cv2
from numpy import *
from pathlib import Path


global imageLunettes
cheminImages = str (Path (__file__).resolve ().parent) + "/images/"
lunettesPng = cv2.imread (cheminImages + "sunglasses.png", cv2.IMREAD_UNCHANGED)


def ajuster (image, nouvHauteur, nouvLargeur):

    # Initialisation

    hauteur = image.shape [0]
    largeur = image.shape [1]
    profondeur = image.shape [2]

    ajustee = array ([[
            [0] * profondeur
            for _ in range (nouvLargeur)
        ]
        for _ in range (nouvHauteur)
    ])
    
    
    # Traitement
    
    for nouvLigne in range (nouvHauteur):
        for nouvColonne in range (nouvLargeur):
        
            # Coordonnées décimales -> le "+ 1" de la sécurité :[]
            pixel = ajustee [nouvLigne] [nouvColonne]
            ligne = nouvLigne * hauteur / (nouvHauteur + 1)
            colonne = nouvColonne * largeur / (nouvLargeur + 1)
            
            # Pixélisation par moyenne pondérée
            for couleur in range (profondeur):
                pixel [couleur] += image [int (ligne)] [int (colonne)] [couleur] * (int (ligne) - ligne + 1) * (int (colonne) - colonne + 1)
                pixel [couleur] += image [int (ligne)] [int (colonne) + 1] [couleur] * (int (ligne) - ligne + 1) * (colonne - int (colonne))
                pixel [couleur] += image [int (ligne) + 1] [int (colonne)] [couleur] * (ligne - int (ligne)) * (int (colonne) - colonne + 1)
                pixel [couleur] += image [int (ligne) + 1] [int (colonne) + 1] [couleur] * (ligne - int (ligne)) * (colonne - int (colonne))
                
    
    # Sortie
    
    return ajustee


def lunettes (image, gauche, haut, diametre):

    # Initialisation

    copie = image.copy ()
    hauteur = lunettesPng.shape [0]
    largeur = lunettesPng.shape [1]
    
    coefAgrandissement = diametre / largeur
    nouvHauteur = int (coefAgrandissement * hauteur)
    nouvLargeur = int (coefAgrandissement * largeur)

    lunettesAjustees = ajuster (lunettesPng, nouvHauteur, nouvLargeur)
    decalageGauche = gauche
    decalageHaut = haut + int (diametre * 0.18)


    # Superposition
    
    for ligne in range (nouvHauteur):
        for colonne in range (nouvLargeur):
            pixelBase = copie [ligne + decalageHaut] [colonne + decalageGauche]
            pixelLunettes = lunettesAjustees [ligne] [colonne]
            
            opacite = pixelLunettes [3] / 255
            for couleur in range (3):
                pixelBase [couleur] = pixelBase [couleur] * (1 - opacite)
                pixelBase [couleur] += pixelLunettes [couleur] * opacite
                pixelBase [couleur] = int (pixelBase [couleur])
    
    
    # Sortie
    
    return copie
    