import pygame, sys

PLAYER_SPRITE = 'player_sprite.png'
BEETLE = 'BEETLE'

BEETLE_SPRITE = 'beetle_sprite'
BEETLE_STRENGTH = 2
ANT = 'ANT'
ANT_STRENGTH = 1.5

class Entity:
    def __init__(self, sprite, x, y, gravity):
        self.sprite = pygame.image.load(sprite)
        self.rect = pygame.Rect((x,y), self.sprite.get_size())
        self.velocity = pygame.math.Vector2(x=0,y=0)
        self.gravity = gravity
        self.grounded = True
        self.direction = 'right'
        self.state = 'idle'

    def physicsUpdate():
        #gravity accel
        #calc velocity/new position
        #check if new position collides with anything
        #if it does perform appropriate action
        #otherwise, move to that location
        pass



class Player(Entity):
    def __init__(self, x, y):
        super().__init__(PLAYER_SPRITE, x, y, True)


class Enemy(Entity):
    def __init__(self, type, x, y):
        if(type == BEETLE):
            super().__init__(PLAYER_SPRITE, x, y, True)
            self.strength = BEETLE_STRENGTH
        elif(type == ANT):
            super().__init__(PLAYER_SPRITE, x, y, True)
            self.strength = ANT_STRENGTH
        
            


class Collectible:
    def __init__(self, sprite, type, x, y):
        self.sprite = pygame.image.load(sprite)
        self.rect = self.sprite.get_rect()