import pygame, sys, Controller, Model, View

pygame.init()

model = Model.Model()
view = View.View()
controller = Controller.Controller(model, view)
clock = pygame.time.Clock()

while True:
    controller.update()
    view.updateView(model)
    clock.tick(60)