import cv2
from numpy import *

from exercice1 import *


def detections (video, element, masque = "cercle", couleur = array ([255, 0, 255])):

    # Initialisation

    clavierStable = False

    
    # Détection image par image
    
    while True:
        
        # Lecture
        succes, uneImage = video.read ()
        if succes is False:
            break
        
        # Traitement
        detecte = detection (uneImage, element, masque, couleur)
        
        # Affichage
        cv2.imshow ("Detection :", detecte)
        
        # Fermeture
        pressionEchap = cv2.waitKey (1) & 0xFF == 27
        if clavierStable and pressionEchap:
            break
        elif not (clavierStable or pressionEchap):
            clavierStable = True
