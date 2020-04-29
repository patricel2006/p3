"""Classes du jeu de Labyrinthe Mac Gyver"""

import pygame
from pygame.locals import *
from mgconstantes import *


class Niveau:
    """Classe permettant de créer, puis d'afficher, la structure du labyrinthe"""

    # methode initialisant les caracteristiques des objets de la classe Niveau :
    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0

    def generer(self):
        """Méthode permettant de générer le niveau en fonction du fichier.
        On crée une liste générale, contenant une liste de cases par ligne à afficher"""
        # On ouvre le fichier
        with open(self.fichier, "r") as fichier:
            # initialisation de ma grille sous forme de liste vide :
            structure_niveau = []
            # On parcourt les lignes du fichier
            for ligne in fichier:
                ligne_niveau = []
                # On parcourt les sprites (lettres) contenus dans le fichier
                for sprite in ligne:
                    # On ignore les "\n" de fin de ligne
                    if sprite != '\n':
                        # On ajoute le sprite à la liste de la ligne
                        ligne_niveau.append(sprite)
                # On ajoute la ligne à la liste du niveau
                structure_niveau.append(ligne_niveau)
            # On sauvegarde cette structure
            self.structure = structure_niveau  # shéma de la grille

    def afficher(self, fenetre):
        """Méthode permettant d'afficher le niveau en fonction
        de la liste de structure renvoyée par generer()"""
        # Chargement des images (seule celle d'arrivée contient de la transparence)
        mur = pygame.image.load(IMAGE_MUR).convert()
        depart = pygame.image.load(IMAGE_DEPART).convert()
        arrivee = pygame.image.load(IMAGE_ARRIVEE).convert_alpha()

        # On parcourt toute la grille : lignes + colonnes :
        # initialisation du numéro de ligne à zéro :
        num_ligne = 0
        # boucle qui parcourt toutes les lignes de la grille :
        for ligne in self.structure:
            # On initialise le numéro de case à zéro :
            num_case = 0
            # boucle qui parcourt toutes les cases de la ligne :
            for sprite in ligne:
                # On calcule la position réelle en pixels en multipliant par la taille de chaque case (30 pixels)
                x = num_case * TAILLE_SPRITE
                y = num_ligne * TAILLE_SPRITE
                if sprite == 'm':  # m = Mur
                    # je colle l'image du mur sur la case correspondante :
                    fenetre.blit(mur, (x, y))
                elif sprite == 'd':  # d = Départ
                    # je colle l'image du départ sur la case qui convient :
                    fenetre.blit(depart, (x, y))
                elif sprite == 'a':  # a = Arrivée
                    fenetre.blit(arrivee, (x, y))
                num_case += 1
            num_ligne += 1


class Perso:
    """Classe permettant de créer le personnage de Mac Gyver"""

    def __init__(self, niveau):
        # Sprites du personnage
        #self.mg = pygame.image.load("images/macgyver.png").convert_alpha()
        # Position du personnage en cases et en pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        # Direction par défaut
        self.direction = self.droite
        # Niveau dans lequel le personnage se trouve
        self.niveau = niveau

