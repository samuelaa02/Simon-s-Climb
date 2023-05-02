import pygame, sys, Stage, Entity
from Entity import Player, Enemy, Entity, Collectible

#images
WOOD0 = pygame.image.load("./tiles/Wood0.png")
WOOD1 = pygame.image.load("./tiles/Wood1.png")
WOOD2 = pygame.image.load("./tiles/Wood2.png")
WOOD3 = pygame.image.load("./tiles/Wood3.png")
WOOD4 = pygame.image.load("./tiles/Wood4.png")
WOOD5 = pygame.image.load("./tiles/Wood5.png")
WOOD6 = pygame.image.load("./tiles/Wood6.png")
WOOD7 = pygame.image.load("./tiles/Wood7.png")
WOOD8 = pygame.image.load("./tiles/Wood8.png")
WOOD9 = pygame.image.load("./tiles/Wood9.png")
WOOD10 = pygame.image.load("./tiles/Wood10.png")
WOOD11 = pygame.image.load("./tiles/Wood11.png")
WOOD12 = pygame.image.load("./tiles/Wood12.png")
WOOD13 = pygame.image.load("./tiles/Wood13.png")
WOOD14 = pygame.image.load("./tiles/Wood14.png")
WOOD15 = pygame.image.load("./tiles/Wood15.png")
WOOD16 = pygame.image.load("./tiles/Wood16.png")
WOOD17 = pygame.image.load("./tiles/Wood17.png")
WOOD18 = pygame.image.load("./tiles/Wood18.png")
WOOD19 = pygame.image.load("./tiles/Wood19.png")
WOOD20 = pygame.image.load("./tiles/Wood20.png")
WOOD21 = pygame.image.load("./tiles/Wood21.png")
WOOD22 = pygame.image.load("./tiles/Wood22.png")
WOOD23 = pygame.image.load("./tiles/Wood23.png")
WOOD24 = pygame.image.load("./tiles/Wood24.png")
WOOD25 = pygame.image.load("./tiles/Wood25.png")
WOOD26 = pygame.image.load("./tiles/Wood26.png")
WOOD27 = pygame.image.load("./tiles/Wood27.png")
WOOD28 = pygame.image.load("./tiles/Wood28.png")
WOOD29 = pygame.image.load("./tiles/Wood29.png")
WOOD30 = pygame.image.load("./tiles/Wood30.png")
WOOD31 = pygame.image.load("./tiles/Wood31.png")
WOOD32 = pygame.image.load("./tiles/Wood32.png")
MISSING = pygame.image.load("./tiles/MISSING.png")


class View:
    
    def __init__(self):
        pygame.display.set_caption("Simon's Climb")
        displayFlags = pygame.SCALED | pygame.RESIZABLE | pygame.FULLSCREEN
        self.gameWindow = pygame.display.set_mode((512, 512), displayFlags)
    
    def updateResolution(self, new_res):
        displayFlags = pygame.SCALED | pygame.RESIZABLE | pygame.FULLSCREEN
        self.gameWindow = pygame.display.set_mode(new_res, displayFlags)

    def updateView(self, model):
        if(model.stage.resolution != self.gameWindow.get_size()):
            self.updateResolution(model.stage.resolution)
            #pygame.display.toggle_fullscreen()
        self.drawBackground(model.stage)
        self.drawStage(model.stage)
        self.drawEntities([model.player] + model.enemies + model.collectibles)
        #self.drawGUI()
        pygame.display.flip()
    
    def drawBackground(self, stage):
        #self.updateResolution(stage.resolution)
        self.gameWindow.blit(stage.background,stage.background.get_rect())

    def drawStage(self, stage):
        for y, row in enumerate(stage.stageLayout):
            for x, platform in enumerate(row):
                if platform is not None and isinstance(platform, Stage.Platform):
                    self.gameWindow.blit(self.getPlatformVariant(platform.material), platform.rect)


    def drawEntities(self, entities):
        for entity in entities:
            entity.rect.clamp_ip(self.gameWindow.get_rect())
            if isinstance(entity, Player):
                self.gameWindow.blit(pygame.transform.flip(entity.sprite,(entity.direction == 'right'),False), entity.rect)
            elif isinstance(entity, Enemy):
                self.gameWindow.blit(pygame.transform.flip(entity.sprite,(entity.direction == 'right'),False), entity.rect)
            elif isinstance(entity, Collectible):
                self.gameWindow.blit(entity.sprite, entity.rect)



    def drawGUI(self):
        pass

    def getPlatformVariant(self,material):
        match material:
            case "Wood0":
                return WOOD0
            case "Wood1":
                return WOOD1
            case "Wood2":
                return WOOD2
            case "Wood3":
                return WOOD3
            case "Wood4":
                return WOOD4
            case "Wood5":
                return WOOD5
            case "Wood6":
                return WOOD6
            case "Wood7":
                return WOOD7
            case "Wood8":
                return WOOD9
            case "Wood9":
                return WOOD9
            case "Wood10":
                return WOOD10
            case "Wood11":
                return WOOD11
            case "Wood12":
                return WOOD12
            case "Wood13":
                return WOOD13
            case "Wood14":
                return WOOD14
            case "Wood15":
                return WOOD15
            case "Wood16":
                return WOOD16
            case "Wood17":
                return WOOD17
            case "Wood18":
                return WOOD18
            case "Wood19":
                return WOOD19
            case "Wood20":
                return WOOD20
            case "Wood21":
                return WOOD21
            case "Wood22":
                return WOOD22
            case "Wood23":
                return WOOD23
            case "Wood24":
                return WOOD24
            case "Wood25":
                return WOOD25
            case "Wood26":
                return WOOD26
            case "Wood27":
                return WOOD27
            case "Wood28":
                return WOOD28
            case "Wood29":
                return WOOD29
            case "Wood30":
                return WOOD30
            case "Wood31":
                return WOOD31
            case "Wood32":
                return WOOD32
            case _:
                return MISSING
            