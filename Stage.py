# object responsible for handling current stage layout information

import pygame, sys


class Stage:
    def __init__(self, filepath):
        
        self.filepath = filepath
        self.load_level()
        
        pass

    def load_level(self):
        with open(self.filepath) as file:
            for line in file:
                #read in and validate information
                
                pass
    

    #needs work
class Platform:
    def __init__(self, material, variant, posx, posy):
        self.material = material
        self.variant = variant
        self.position = pygame.math.Vector2(posx, posy)

