"""
Jeu Mac Gyver Labyrinthe
Jeu dans lequel Mac Gyver doit récupérer 3 objets nécessaires pour endormir le garde et sortir du labyrinthe.
Script Python
Fichiers : mglabyrinthe.py, mgclasses.py, mgconstantes.py, design, + images
"""

import pygame
from pygame.locals import *

from mgclasses import *
from mgconstantes import *

pygame.init()

# Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
# Icone
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
# Titre
pygame.display.set_caption(titre_fenetre)

# BOUCLE PRINCIPALE
continuer = 1
while continuer:
    # Chargement et affichage de l'écran d'accueil
    accueil = pygame.image.load(image_accueil).convert()
    fenetre.blit(accueil, (0, 0))

    # Rafraichissement
    pygame.display.flip()

    # On remet ces variables à 1 à chaque tour de boucle
    continuer_jeu = 1
    continuer_accueil = 1

    # BOUCLE D'ACCUEIL
    while continuer_accueil:

        # Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)

        # attente des entrées clavier utilisateur :
        for event in pygame.event.get():

            # Si l'utilisateur quitte, on met les variables
            # de boucle à 0 pour n'en parcourir aucune et fermer
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_accueil = 0
                continuer_jeu = 0
                continuer = 0
                # Variable de choix de quitter ou de jouer :
                choix = 0

            elif event.type == KEYDOWN:
                # Lancement du jeu :
                if event.key == K_SPACE:
                # continuer_accueil = 0  # On quitte l'accueil
                # choix = 'design'  # On définit l'architecture du jeu dans un fichier
                # if event.key == K_ESCAPE:
                    continuer_accueil = 0
                    choix = 'design'
    # on vérifie que le joueur a bien fait le choix de commencer à jouer
    # pour ne pas charger s'il quitte
    if choix != 0:
        # Chargement du fond
        fond = pygame.image.load(image_fond).convert()
        fenetre.blit(fond, (0, 0))

        # Génération du design à partir d'un fichier design
        niveau = Niveau(choix)  # choix a pris la valeur du fichier 'design' ligne 61
        niveau.generer()
        niveau.afficher(fenetre)

        # Création du personnage de Mac Gyver :
        mg = pygame.image.load(image_icone).convert_alpha()
        x_mg = 0
        y_mg = 0
        fenetre.blit(mg, (x_mg, y_mg))

        pygame.time.Clock().tick(30)

        # BOUCLE DE JEU
        while continuer_jeu:

            for event in pygame.event.get():

                # Si l'utilisateur quitte, on met la variable qui continue le jeu
                # ET la variable générale à 0 pour fermer la fenêtre
                if event.type == QUIT:
                    continuer_jeu = 0
                    continuer = 0

                elif event.type == KEYDOWN:
                    # Si l'utilisateur presse Echap ici, on revient seulement à l'accueil :
                    if event.key == K_ESCAPE:
                        continuer_jeu = 0

                    # Touches de déplacement de Mac Gyver
                    elif event.key == K_RIGHT:
                        x_mg = x_mg + 30
                    elif event.key == K_LEFT:
                        x_mg = x_mg - 30
                    elif event.key == K_UP:
                        y_mg = y_mg - 30
                    elif event.key == K_DOWN:
                        y_mg = y_mg + 30

            fenetre.blit(fond, (0, 0))
            niveau.generer()
            niveau.afficher(fenetre)
            fenetre.blit(mg, (x_mg, y_mg))
            pygame.display.update()
            # Victoire -> Retour à l'accueil
            #if niveau.structure[mg.case_y][mg.case_x] == 'a':
                #continuer_jeu = 0