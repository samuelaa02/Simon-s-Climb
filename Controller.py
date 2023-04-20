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
        print(self.model.player.rect.x)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        print("left")
                        self.model.player.velocity.x = -5
                    elif event.key == pygame.K_RIGHT:
                        self.model.player.velocity.x = 5
                    elif event.key == pygame.K_UP and self.model.player.grounded:
                        self.model.player.velocity.y = -15
                
                

    def update(self):
        #updates the game state
        self.model.player.physicsUpdate()



    def run(self):
        pass
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.handle_events()
            self.update()
            #self.view.updateView(self.model.entities)

