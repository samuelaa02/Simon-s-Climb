#holds all information regarding the game state, including instances of all objects currently loaded

import pygame, sys, Stage, Entity

START_STAGE = "./level1.txt"

class Model:
    def __init__(self):
        self.stage = Stage.Stage(START_STAGE)
        self.enemies = self.stage.enemies
        self.collectibles = self.stage.collectibles
        self.player = Entity.Player(self.stage.spawnPoint.x,self.stage.spawnPoint.y)

    def changeStage(self, nextStage):
        self.stage = Stage.Stage(nextStage)
        self.enemies = self.stage.enemies
        self.collectibles = self.stage.collectibles
        (self.player.rect.x, self.player.rect.y) = (int(self.stage.spawnPoint.x),int(self.stage.spawnPoint.y))
    

class Level:
    def __init__(self, width, height, spawn_points, obstacles, enemies, collectibles):
        self.width = width
        self.height = height
        self.spawn_points = spawn_points
        self.obstacles = obstacles
        self.enemies = enemies
        self.collectibles = collectibles


