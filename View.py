#responsible for displaying all sprites and camera movement

import pygame

class View:
    def __init__(self, screen_width, screen_height, background_color):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.background_color = background_color
    
    def draw_background(self):
        self.screen.fill(self.background_color)
        # Draw other background elements like clouds or hills
        
    def draw_entities(self, entities):
        for entity in entities:
            # Draw the entity on the screen using its position and sprite
        
    def update_screen(self):
        pygame.display.update()
