import pygame, sys

PLAYER_SPRITE = 'player_sprite.png'
BEETLE = 'BEETLE'

BEETLE_SPRITE = 'beetle_sprite.png'
BEETLE_STRENGTH = 2

ANT = 'ANT'
ANT_SPRITE = 'ant_sprite.png'
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

    def physicsUpdate(self):
        #gravity acceleration
        #calc velocity/new position
        #check if new position collides with anything
        #if it does perform appropriate action
        #otherwise, move to that location

         # apply gravity
        #self.velocity.y += self.gravity

        # update position based on velocity
        self.rect = self.velocity
        self.rect.y += self.velocity.y

        # check for collisions
        """"
        self.grounded = False
        for platform in self.stageLayout:
            if self.rect.colliderect(platform.rect):
                if self.velocity.y > 0:
                    self.rect.bottom = platform.rect.top
                    self.velocity.y = 0
                    self.grounded = True
                elif self.velocity.y < 0:
                    self.rect.top = platform.rect.bottom
                    self.velocity.y = 0
        """
        #check for screen bounds


         # update direction and state
        if self.velocity.x > 0:
            self.direction = 'right'
            self.state = 'walk'
        elif self.velocity.x < 0:
            self.direction = 'left'
            self.state = 'walk'
        else:
            self.state = 'idle'


class Player(Entity):
    def __init__(self, x, y):
        super().__init__(PLAYER_SPRITE, x, y, True)


class Enemy(Entity):
    def __init__(self, type, x, y):
        if(type == BEETLE):
            super().__init__(BEETLE_SPRITE, x, y, True)
            self.strength = BEETLE_STRENGTH
        elif(type == ANT):
            super().__init__(ANT_SPRITE, x, y, True)
            self.strength = ANT_STRENGTH
        
            


class Collectible:
    def __init__(self, sprite, type, x, y):
        self.sprite = pygame.image.load(sprite)
        self.rect = self.sprite.get_rect()