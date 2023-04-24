import pygame, sys, Controller, Model, View

pygame.init()

model = Model.Model()
view = View.View()
controller = Controller.Controller(model, view)
clock = pygame.time.Clock()

while True:
    """for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    """
    #view.updateResolution(model.stage.resolution)
    
    controller.update()
    
    view.updateView(model)
    clock = pygame.time.Clock()