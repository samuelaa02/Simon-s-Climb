#holds all information regarding the game state, including instances of all objects currently loaded

import pygame, sys, Stage, Entity

class Model:
    def __init__(self):
        self.stage = Stage.Stage("./level1.txt")
        self.enemies = self.stage.enemies
        self.collectibles = self.stage.collectibles
        self.player = Entity.Player(self.stage.spawnPoint.x,self.stage.spawnPoint.y)

    

class Level:
    def __init__(self, width, height, spawn_points, obstacles, enemies, collectibles):
        self.width = width
        self.height = height
        self.spawn_points = spawn_points
        self.obstacles = obstacles
        self.enemies = enemies
        self.collectibles = collectibles


