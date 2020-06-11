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


objet1 = Object(2, 2, None ,False, "monsuperobjet")
print(objet1.name)
print(objet1.x, objet1.y)
print(objet1.kept)
print(objet1.image)