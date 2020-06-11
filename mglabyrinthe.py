"""
Jeu Mac Gyver Labyrinthe
Jeu dans lequel Mac Gyver doit récupérer 3 objets nécessaires pour endormir le garde et sortir du labyrinthe.
Script Python
Fichiers : mglabyrinthe.py, mgclasses.py, mgconstantes.py, design, + images
"""

import pygame
import random
from pygame.locals import *

from mgclasses import *
from mgconstantes import *

pygame.init()

# initialisation des coordonnées des trois objets :
x_objet1 = -1
y_objet1 = -1

x_objet2 = -1
y_objet2 = -1

x_objet3 = -1
y_objet3 = -1

# booléens qui serviront à determiner si les objets ont été ou non collectés :
bool_objet1 = False
bool_objet2 = False
bool_objet3 = False

# initialisation de la fenêtre de jeu (carré de 15*15)
fenetre = pygame.display.set_mode((COTE_FENETRE, COTE_FENETRE))
# chargement de l'image de MG :
icone = pygame.image.load(IMAGE_ICONE)
# affichage de l'image de MG :
pygame.display.set_icon(icone)
# initialisation du titre de la fenetre d'accueil :
pygame.display.set_caption(TITRE_FENETRE)


# fonction qui prend en charge la gestion des collusions :
def is_wall(grille, x, y):
    """is_wall renvoie True quand la case x,y de la grille est un mur, sinon False"""

    # les coordonnées de MG doivent impérativement être de type entier :
    x = int(x)
    y = int(y)

    if grille[y][x] != 'm':
        return False
    return True


def is_Depart(grille, x, y):
    """is_Depart renvoie True quand la case x,y de la grille est la case Départ"""

    x = int(x)
    y = int(y)

    if grille[y][x] != 'd':
        return False
    return True

def get_objects1(grille, x, y):
    x = int(x)
    y = int(y)

    if (x == x_objet1 and y == y_objet1) == True:
        print("cette case contient l'objet 1 !")
        return True

def get_objects2(grille, x, y):
    x = int(x)
    y = int(y)

    if (x == x_objet2 and y == y_objet2) == True:
        print("cette case contient l'objet 2 !")
        return True

def get_objects3(grille, x, y):
    x = int(x)
    y = int(y)

    if (x == x_objet3 and y == y_objet3) == True:
        print("cette case contient l'objet 3 !")
        return True

# Boucle principale :
continuer = 1
compteur_objets = 0

while continuer:
    # Chargement et affichage de l'écran d'accueil
    accueil = pygame.image.load(IMAGE_ACCUEIL).convert()
    fenetre.blit(accueil, (0, 0))

    # Rafraichissement de l'écran :
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
                # Variable choix qui prendra la valeur du fichier design si la partie commence :
                choix = 0

            elif event.type == KEYDOWN:
                # Lancement du jeu sur la touche espace :
                if event.key == K_SPACE:
                    # on quitte l'écran d'accueil :
                    continuer_accueil = 0
                    # la variable choix contient maintenant l'architecture du labyrinthe dans un fichier texte :
                    choix = 'design'
    # on vérifie que le joueur a bien fait le choix de commencer à jouer
    # pour ne pas charger s'il choisit de quitter le jeu :
    if choix != 0:
        # Chargement du fond
        fond = pygame.image.load(IMAGE_FOND).convert()
        # affichage aux coordonnées 0,0 soit en haut à gauche de la fenetre de jeu :
        fenetre.blit(fond, (0, 0))

        # l'architecture du labyrinthe est placée dans la variable niveau :
        niveau = Niveau(choix)
        # chargement du niveau :
        niveau.generer()
        # affichage du niveau à l'écran :
        niveau.afficher(fenetre)

        # initialisation de la variable mg qui va charger l'image image_icone definie dans les constantes :
        mg = pygame.image.load(IMAGE_ICONE).convert_alpha()

        # affichage de l'image chargée de mg :
        fenetre.blit(mg, (x_mg, y_mg))

        # limitation de la vitesse de boucle :
        pygame.time.Clock().tick(30)

        # boucles qui gèrent le placement aléatoire des objets :
        boucle1 = True
        boucle2 = True
        boucle3 = True

        # boucle qui gère la possibilité de quitter ou non le jeu :
        while continuer_jeu:
            # attente des entrées utilisateur :
            for event in pygame.event.get():

                # Si l'utilisateur quitte, on met la variable qui continue le jeu
                # et la variable générale à 0 pour fermer la fenêtre
                if event.type == QUIT:
                    continuer_jeu = 0
                    continuer = 0

                elif event.type == KEYDOWN:
                    # Si l'utilisateur presse Echap ici, on revient seulement à l'accueil :
                    if event.key == K_ESCAPE:
                        continuer_jeu = 0

                    # Touches de déplacement de Mac Gyver

                    elif event.key == K_RIGHT:
                        # si la case n'est pas un mur, MG peut aller dessus :
                        if is_wall(niveau.structure, (x_mg + TAILLE_SPRITE) / TAILLE_SPRITE,
                                   (y_mg) / TAILLE_SPRITE) == False:
                            x_mg = x_mg + TAILLE_SPRITE
                            # si la case contient un objet :

                    elif event.key == K_LEFT:
                        if is_wall(niveau.structure, (x_mg - TAILLE_SPRITE) / TAILLE_SPRITE,
                                   y_mg / TAILLE_SPRITE) == False:
                            x_mg = x_mg - TAILLE_SPRITE

                    elif event.key == K_UP:
                        if is_wall(niveau.structure, x_mg / TAILLE_SPRITE,
                                   (y_mg - TAILLE_SPRITE) / TAILLE_SPRITE) == False:
                            y_mg = y_mg - TAILLE_SPRITE

                    elif event.key == K_DOWN:
                        if is_wall(niveau.structure, x_mg / TAILLE_SPRITE,
                                   (y_mg + TAILLE_SPRITE) / TAILLE_SPRITE) == False:
                            y_mg = y_mg + TAILLE_SPRITE

                    if get_objects1(niveau.structure, (x_mg) / TAILLE_SPRITE, (y_mg) / TAILLE_SPRITE) == True:
                        compteur_objets = compteur_objets + 1
                        bool_objet1 = True
                    if get_objects2(niveau.structure, (x_mg) / TAILLE_SPRITE, (y_mg) / TAILLE_SPRITE) == True:
                        compteur_objets = compteur_objets + 1
                        bool_objet2 = True
                    if get_objects3(niveau.structure, (x_mg) / TAILLE_SPRITE, (y_mg) / TAILLE_SPRITE) == True:
                        compteur_objets = compteur_objets + 1
                        bool_objet3 = True

            # rafraichissement du fond, du design du labyrinthe et de la position de MG :
            fenetre.blit(fond, (0, 0))
            niveau.generer()
            niveau.afficher(fenetre)
            fenetre.blit(mg, (x_mg, y_mg))

            # boucle qui prend en charge le placement aléatoire de l'objet1 dans le labyrinthe :
            if bool_objet1 == False:
                while boucle1 == True:
                    # tirage aléatoire des coordonnées x et y de objet2 :
                    x_objet1 = random.randint(0, 14)
                    y_objet1 = random.randint(0, 14)

                    if is_wall(niveau.structure, x_objet1, y_objet1) == False and is_Depart(niveau.structure, x_objet1, y_objet1) == False:
                        objet1 = pygame.image.load(OBJET1).convert()
                        fenetre.blit(objet1, (x_objet1 * TAILLE_SPRITE, y_objet1 * TAILLE_SPRITE))
                        # sortie de la boucle :
                        boucle1 = False
                # Une fois que le tirage est correct et après être sorti, chargement et affichage de l'objet2 :
                if boucle1 == False:
                    objet1 = pygame.image.load(OBJET1).convert()
                    fenetre.blit(objet1, (x_objet1 * TAILLE_SPRITE, y_objet1 * TAILLE_SPRITE))


            # boucle qui prend en charge le placement aléatoire de l'objet2 dans le labyrinthe :
            if bool_objet2 == False:
                while boucle2 == True:
                    # tirage aléatoire des coordonnées x et y de objet2 :
                    x_objet2 = random.randint(0, 14)
                    y_objet2 = random.randint(0, 14)

                    if is_wall(niveau.structure, x_objet2, y_objet2) == False and is_Depart(niveau.structure, x_objet2, y_objet2) == False:
                        objet2 = pygame.image.load(OBJET2).convert()
                        fenetre.blit(objet2, (x_objet2 * TAILLE_SPRITE, y_objet2 * TAILLE_SPRITE))
                        # sortie de la boucle :
                        boucle2 = False
                # Une fois que le tirage est correct et après être sorti, chargement et affichage de l'objet2 :
                if boucle2 == False:
                    objet2 = pygame.image.load(OBJET2).convert()
                    fenetre.blit(objet2, (x_objet2 * TAILLE_SPRITE, y_objet2 * TAILLE_SPRITE))

            # boucle qui prend en charge le placement aléatoire de l'objet3 dans le labyrinthe :
            if bool_objet3 == False:
                while boucle3 == True:
                    # tirage aléatoire des coordonnées x et y de l'objet3 :
                    x_objet3 = random.randint(0, 14)
                    y_objet3 = random.randint(0, 14)
                    if is_wall(niveau.structure, x_objet3, y_objet3) == False and is_Depart(niveau.structure, x_objet3, y_objet3) == False:
                        objet3 = pygame.image.load(OBJET3).convert()
                        fenetre.blit(objet3, (x_objet3 * TAILLE_SPRITE, y_objet3 * TAILLE_SPRITE))
                        # sortie de la boucle :
                        boucle3 = False
                # Une fois que le tirage est correct et après être sorti, chargement et affichage de l'objet3 :
                if boucle3 == False:
                    objet3 = pygame.image.load(OBJET3).convert()
                    fenetre.blit(objet3, (x_objet3 * TAILLE_SPRITE, y_objet3 * TAILLE_SPRITE))
            pygame.display.update()
            # gestion de la fin de partie :
            # Si les trois objets ont bien été collectés sur la case du gardien :
            if x_mg / TAILLE_SPRITE == x_fin and y_mg / TAILLE_SPRITE == y_fin and compteur_objets == 3:
                print("Bravo ! Vous avez gagné la partie !")
                continuer_jeu = 0

            # Si les trois objets n' ont pas été collectés sur la case du gardien :
            elif x_mg / TAILLE_SPRITE == x_fin and y_mg / TAILLE_SPRITE == y_fin and compteur_objets < 3:
                print("C'est perdu !")
                continuer_jeu = 0



