import cv2
from matplotlib import pyplot
from pathlib import Path

from exercice1 import *
from exercice2 import *


def main ():

    # Initialisation
    
    nbLignes = 1
    nbColonnes = 3
    compteur = 1

    cheminImages = str (Path (__file__).resolve ().parent) + "/images/"
    unBasketeur = cv2.imread (cheminImages + "one.jpg")
    desBasketeurs = cv2.imread (cheminImages + "multiple.jpg")
    quentin = cv2.VideoCapture (cheminImages + "video1.mp4")
    onu = cv2.VideoCapture (cheminImages + "video2.mp4")


    # Exercice 1

    visage = detection (unBasketeur, element = "visage")
    visages = detection (desBasketeurs, element = "visage")
    
    
    # Exercice 3
    
    deformation = ajuster (desBasketeurs, 250, 250)
    
    
    # Affichage
    
    pyplot.subplot (nbLignes, nbColonnes, compteur)
    pyplot.imshow (cv2.cvtColor (visage, cv2.COLOR_BGR2RGB))
    pyplot.title ("Exercice 1 : 1 visage")
    compteur += 1
    
    pyplot.subplot (nbLignes, nbColonnes, compteur)
    pyplot.imshow (cv2.cvtColor (visages, cv2.COLOR_BGR2RGB))
    pyplot.title ("Exercice 1 : plusieurs visages")
    compteur += 1
    
    pyplot.subplot (nbLignes, nbColonnes, compteur)
    pyplot.imshow (deformation)
    pyplot.title ("Exercice 3")
    compteur += 1
    
    pyplot.show ()
    
    
    # Exercice 2
    
    detections (quentin, element = "visage")
    detections (onu, element = "visage")
    detections (onu, element = "yeux", couleur = array ([255, 0, 0]))
    
    
    # Exercice 3
    
    detections (quentin, element = "visage", masque = "lunettes")
    

main ()
