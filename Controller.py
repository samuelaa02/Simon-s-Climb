#handles control of entities and player
import pygame, sys, Stage


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        #ai.self = ai

    def handle_events(self):
        #Controls for character movement
        #print(self.model.player.rect.x)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.model.player.moveLeft()
        if keys[pygame.K_RIGHT]:
            self.model.player.moveRight()
        if keys[pygame.K_UP]:
            self.model.player.playerJump()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F11:
                        pygame.display.toggle_fullscreen()
                      
    def update(self):
        #updates the game state
        self.handle_events()
        self.model.player.physicsUpdate(self.model)
        for enemy in self.model.enemies:
            enemy.enemyUpdate(self.model)
        
        for collectible in self.model.collectibles:
            collectible.collectibleCollide(self.model.player)
            if(collectible.interacted and collectible.pickup):
                self.model.collectibles.remove(collectible)
            if(collectible.interacted and collectible.type == 'FLAG'):
                self.model.changeStage(self.model.stage.nextLevel)
            if(collectible.interacted and collectible.type == 'DOG'):
                self.view.endScreen = True



