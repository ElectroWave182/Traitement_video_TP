import cv2
from numpy import *
from pathlib import Path

from exercice3 import *


global cascadeFaces, cascadeYeux
cheminCascades = str (Path (__file__).resolve ().parent) + "/cascades/"
cascadeFaces = cv2.CascadeClassifier (cheminCascades + "haarcascade_frontalface_alt.xml")
cascadeYeux = cv2.CascadeClassifier (cheminCascades + "haarcascade_eye_tree_eyeglasses.xml")


def cercle (image, positionHorizontale, positionVerticale, rayon, couleur = array ([255, 0, 255])):

    # Initialisation
    
    epaisseur = int (rayon ** 0.5 * 2)
    envergure = rayon + epaisseur
    
    hauteur = image.shape [0]
    largeur = image.shape [1]
    copie = image.copy ()
    
    
    # Gestion des erreurs
    
    if len (couleur) != 3:
        print ("Une couleur doit être un arrangement de taille 3.")
        print ("Couleur donnée : " + str (couleur))
        exit (0)
    
    if 0 > positionVerticale or positionVerticale + envergure >= hauteur:
        print ("Sortie des limites verticales à " + str (positionVerticale) + " de l'image.")
        exit (0)
    
    if 0 > positionHorizontale or positionHorizontale + envergure >= largeur:
        print ("Sortie des limites horizontales à " + str (positionHorizontale) + " de l'image.")
        exit (0)
    
    
    # Dessin du cercle
    
    for ligne in range (positionVerticale - envergure, positionVerticale + envergure):
        for colonne in range (positionHorizontale - envergure, positionHorizontale + envergure):
            pixel = copie [ligne] [colonne]
            
            equationCercle = (ligne - positionVerticale) ** 2
            equationCercle += (colonne - positionHorizontale) ** 2
            equationCercle -= rayon ** 2
            
            if abs (equationCercle) < epaisseur ** 2:
                for numCouleur in range (3):
                    pixel [numCouleur] = couleur [numCouleur]
                    
                    
    # Sortie
    
    return copie


def detection (image, element, masque = "cercle", couleur = array ([255, 0, 255])):

    # Initialisation

    copie = image.copy ()
    
    
    # Gestion des erreurs
    
    match element:
    
        case "visage":
            coordonnees = cascadeFaces.detectMultiScale (copie, minNeighbors = 4, minSize = (20, 20), scaleFactor = 1.1)
            
        case "yeux":
            if masque == "lunettes":
                print ("Les lunettes ne peuvent être superposées que sur un visage.")
                exit (0)
            coordonnees = cascadeYeux.detectMultiScale (copie, minNeighbors = 3, scaleFactor = 1.1)
            
        case other:
            messageErreur = "L'élément à détecter "
            messageErreur += '"'
            messageErreur += str (element)
            messageErreur += '"'
            messageErreur += " n'est pas reconnu.\nÉléments possibles : "
            messageErreur += "visage, "
            messageErreur += "yeux."
            print (messageErreur)
            exit (0)


    # Parcours de chaque visage
    
    for gauche, haut, diametre, _ in coordonnees:
        rayon = diametre // 2
        
        match masque:
    
            case "cercle":
                copie = cercle (copie, gauche + rayon, haut + rayon, rayon, couleur)
                
            case "lunettes":
                copie = lunettes (copie, gauche, haut, diametre)
                
            case other:
                messageErreur = "Le masque "
                messageErreur += '"'
                messageErreur += str (masque)
                messageErreur += '"'
                messageErreur += " n'a pas été créé.\nMasques possibles : "
                messageErreur += "cercle, "
                messageErreur += "lunettes."
                print (messageErreur)
                exit (0)
    
    
    # Sortie
    
    return copie
