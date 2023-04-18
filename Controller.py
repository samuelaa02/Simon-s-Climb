#handles control of entities and player
import pygame
import sys


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        #ai.self = ai

    def handle_events(self):
        #Controls for character movement

        #basic control outline for up, down, left, right, spacebar(jumping)
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.keys['up'] = True
                elif event.key == pygame.K_DOWN:
                    self.keys['down'] = True
                elif event.key == pygame.K_LEFT:
                    self.keys['left'] = True
                elif event.key == pygame.K_RIGHT:
                    self.keys['right'] = True
                elif event.key == pygame.K_SPACE:
                    self.keys['space'] = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.keys['up'] = False
                elif event.key == pygame.K_DOWN:
                    self.keys['down'] = False
                elif event.key == pygame.K_LEFT:
                    self.keys['left'] = False
                elif event.key == pygame.K_RIGHT:
                    self.keys['right'] = False
                elif event.key == pygame.K_SPACE:
                    self.keys['space'] = False

    def update(self):
        #updatest the game state
        pass


    def run(self):
        pass
        #clock = pygame.time.Clock()
        #while True:
        #    clock.tick(60)
        #    self.handle_events()
        #    self.update()

