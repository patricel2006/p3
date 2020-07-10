import pygame
from pygame.locals import *

class Perso:
    """classe qui représente le personnage de MG"""
    def __init__(self, abcisse, ordonnee, image):
        self.x = abcisse
        self.y = ordonnee
        self.image = image