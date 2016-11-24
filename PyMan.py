import os, sys
import pygame
from pygame.locals import *


# Class definitions
class PyManMain:
    """The main PyMan class - Initialization and game loop."""

    def __init__(self, width=640, height=480):
        """initialize"""
        """initialize PyGame"""
        pygame.init()
        """Set window size"""
        self.width = width
        self.height = height
        """create the screen"""
        self.screen = pygame.display.set_mode(self.width, self.height)
