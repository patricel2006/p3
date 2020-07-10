import pygame
from pygame.locals import *

class Object:
    """classe qui représente un objet"""
    def __init__(self, abcisse, ordonnee, image, kept, name):
        self.x = abcisse
        self.y = ordonnee
        self.image = image
        self.kept = kept
        self.name = name


#objet1 = Object(x_objet1, y_objet1, None, False, "monsuperobjet")
#print(objet1.name)
#print(x_objet1, y_objet1)
#print(objet1.kept)
#print(objet1.image)