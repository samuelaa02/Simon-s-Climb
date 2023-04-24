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
        #print(self.model.player.rect.x)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # using key.getpressed; events.key only registered holding the key down as a single press
                # this will call the function for the entire duration the key is pressed instead
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    self.model.player.moveLeft()
                if keys[pygame.K_RIGHT]:
                    self.model.player.moveRight()
                if keys[pygame.K_UP]:
                    self.model.player.playerJump()
                
                
    def update(self):
        #updates the game state
        self.handle_events()
        self.model.player.physicsUpdate(self.model)
        for enemy in self.model.enemies:
            enemy.physicsUpdate(self.model)


