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

#class Character:
#    def __init__(self, x, y, health, state):
#        self.x = x
#        self.y = y
#        self.health = health
#        self.state = state                      #for animations or abilities
#
#class Entity:
#    def __init__(self, x, y, health, damage, state):
#        self.x = x
#        self.y = y
#        self.health = health
#        self.damage = damage
#        self.state = state                      # alive/dead/ stunned etc
#
#class Enemy(Entity):
#    def __init__(self, x, y, health, damage, state, attack_pattern):
#        super().__init__(x, y, health, damage, state)
#        self.attack_pattern = attack_pattern
#
#class GameProgression:
#    def __init__(self, current_level, fruits_collected, bird_eggs_collected):
#        self.current_level = current_level
#        self.fruits_collected = fruits_collected
#        self.bird_eggs_collected = bird_eggs_collected

#may or may not need a tree class? depends on how it interacts with the player
"""class Tree:
    def __init__(self, x, y, width, height, branches):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.branches = branches
        
    def is_colliding_with_player(self, player_rect):
        tree_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return tree_rect.colliderect(player_rect)
        
    def shake(self):
        for branch in self.branches:
            branch.shake()
    
    etc etc
"""
