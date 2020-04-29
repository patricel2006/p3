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
fenetre = pygame.display.set_mode((COTE_FENETRE, COTE_FENETRE))
# Icone
icone = pygame.image.load(IMAGE_ICONE)
pygame.display.set_icon(icone)
# Titre
pygame.display.set_caption(TITRE_FENETRE)

# fonction qui prend en charge la gestion des collusions :
def is_wall(grille, x, y):
    """is_wall renvoie True quand la case x,y de la grille est un mur, sinon False"""

    # les coordonnées de MG doivent impérativement être de type entier :
    x = int(x)
    y = int(y)

    # affichage de la grille et des coordonnées de MG :
    print("Voici la grille telle que définie dans le fichier design :", grille)
    print("coordonnée x de MG :", x)
    print("coordonnée y de MG :", y)
    print(grille[y][x])
    if grille[y][x] != 'm':
        return False
    return True

# fonction qui place les trois objets dans le labyrinthe :
def put_objects(grille, x, y):
    """put_objects répartit les trois objets dont MG a besoin, dans le labyrinthe"""

    # initialisation des objets dans le labyrinthe :
    position_objet1 = pygame.image.load(OBJET1).convert()
    fenetre.blit(position_objet1, (8, 0))

    #position_objet2 = pygame.image.load(OBJET2).convert()
    #fenetre.blit(position_objet2, (x, y))
    #pygame.display.flip()

    #position_objet3 = pygame.image.load(OBJET3).convert()
    #fenetre.blit(position_objet3, (x, y))
    #pygame.display.flip()



# BOUCLE PRINCIPALE
continuer = 1
while continuer:
    # Chargement et affichage de l'écran d'accueil
    accueil = pygame.image.load(IMAGE_ACCUEIL).convert()
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
                # Variable choix qui sera passée en paramètre à la méthode generer :
                choix = 0

            elif event.type == KEYDOWN:
                # Lancement du jeu sur la touche espace :
                if event.key == K_SPACE:
                    # on quitte l'écran d'accueil :
                    continuer_accueil = 0
                # On définit l'architecture du jeu dans un fichier texte :
                    choix = 'design'
    # on vérifie que le joueur a bien fait le choix de commencer à jouer
    # pour ne pas charger s'il quitte
    if choix != 0:
        # Chargement du fond
        fond = pygame.image.load(IMAGE_FOND).convert()
        fenetre.blit(fond, (0, 0))

        # l'architecture du labyrinthe est placé dans la variable niveau :
        niveau = Niveau(choix)
        niveau.generer()
        niveau.afficher(fenetre)

        # initialisation de la variable mg qui va charger l'image image_icone definie dans les constantes :
        mg = pygame.image.load(IMAGE_ICONE).convert_alpha()
        # initialisation des coordonnées de MG qui sont également définies en constantes :
        x_mg = 0
        y_mg = 0
        # affichage de l'image chargée de mg :
        fenetre.blit(mg, (x_mg, y_mg))
        # limitation de la vitesse de
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
                    elif event.key == K_RIGHT:   #and x_mg <= taille_cote_fenetre:
                        if is_wall(niveau.structure, (x_mg + TAILLE_SPRITE )/TAILLE_SPRITE , (y_mg)/TAILLE_SPRITE ) == False:
                            x_mg = x_mg + TAILLE_SPRITE

                    elif event.key == K_LEFT:  # and x_mg <= 420:
                        if is_wall(niveau.structure, (x_mg - TAILLE_SPRITE )/TAILLE_SPRITE , y_mg/TAILLE_SPRITE ) == False:
                            x_mg = x_mg - TAILLE_SPRITE

                    elif event.key == K_UP:  # and y_mg <= 420:
                        if is_wall(niveau.structure, x_mg/TAILLE_SPRITE, (y_mg - TAILLE_SPRITE )/TAILLE_SPRITE ) == False:
                            y_mg = y_mg - TAILLE_SPRITE

                    elif event.key == K_DOWN:  # and y_mg <= 420:
                        if is_wall(niveau.structure, x_mg/TAILLE_SPRITE, (y_mg + TAILLE_SPRITE )/TAILLE_SPRITE ) == False:
                            y_mg = y_mg + TAILLE_SPRITE

            

            fenetre.blit(fond, (0, 0))
            niveau.generer()
            niveau.afficher(fenetre)
            fenetre.blit(mg, (x_mg, y_mg))
            pygame.display.update()

            put_objects(niveau.structure, x=2, y=0)
            pygame.display.update()





            #def deployer_objets(grille):
                # with open(design, "r") as fichier:
                    #grille = []
                        #for ligne in fichier:



            # Victoire -> Retour à l'accueil
            #if niveau.structure[mg.case_y][mg.case_x] == 'a':
                #continuer_jeu = 0