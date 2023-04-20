import pygame, sys

PLAYER_SPRITE = 'player_sprite.png'
BEETLE = 'BEETLE'

BEETLE_SPRITE = 'beetle_sprite.png'
BEETLE_STRENGTH = 2

ANT = 'ANT'
ANT_SPRITE = 'ant_sprite.png'
ANT_STRENGTH = 1.5
GRAVITY = 1
PLAYER_SPEED = 1
MAX_SPEED = 10
JUMP_HEIGHT = 13

class Entity:
    def __init__(self, sprite, x, y, gravity):
        self.sprite = pygame.image.load(sprite)
        self.rect = self.sprite.get_rect()
        self.velocity = pygame.math.Vector2(x=0,y=0)
        self.gravity = gravity
        self.grounded = True
        self.direction = 'left'
        self.state = 'idle'

    def physicsUpdate(self):
        #gravity acceleration
        #calc velocity/new position
        #check if new position collides with anything
        #if it does perform appropriate action
        #otherwise, move to that location

        # gravity
        self.velocity.y += GRAVITY

        # update position based on velocity
        self.rect.x += int(self.velocity.x)
        self.rect.y += int(self.velocity.y)

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

    # update the entity state based on values stored
    def stateUpdate(self):
        if self.velocity.x == 0 and self.velocity.y == 0:
            self.state = 'idle'
        elif self.velocity.x != 0:
            self.state = 'moving'

    # add velocity to the right as long as it is below the max speed
    def moveRight(self):
        if self.velocity.x < MAX_SPEED:
            self.velocity.x += PLAYER_SPEED
        if self.direction != 'right':
            self.direction = 'right'

    # add velocity to the left as long as it is below the max speed
    def moveLeft(self):
        if self.velocity.x > -MAX_SPEED:
            self.velocity.x -= PLAYER_SPEED
        if self.direction != 'left':
            self.direction = 'left'
    
    # add velocity upward as long as it is below the max speed
    def moveUp(self):
        if self.velocity.y > -MAX_SPEED:
            self.velocity.y -= PLAYER_SPEED
    
    # add velocity downward as long as it is below the max speed
    def moveDown(self):
        if self.velocity.y < MAX_SPEED:
            self.velocity.y += PLAYER_SPEED
    



class Player(Entity):
    def __init__(self, x, y):
        super().__init__(PLAYER_SPRITE, x, y, True)
    
    def playerJump(self):
        if self.grounded:
            #negative is up
            self.velocity.y = -JUMP_HEIGHT
            self.grounded = False


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