import pygame, sys, Stage

PLAYER_SPRITE = './sprites/player_sprite.png'

BEETLE = 'BEETLE'
BEETLE_SPRITE = './sprites/beetle_sprite.png'
BEETLE_STRENGTH = 2

ANT = 'ANT'
ANT_SPRITE = './sprites/ant_sprite.png'
ANT_STRENGTH = 1.5

EGG = 'EGG'
EGG_SPRITE = './sprites/egg_sprite.png'

FLAG = 'FLAG'
FLAG = './sprites/flag_sprite.png'

GRAVITY = 1
FRICTION = 2
PLAYER_SPEED = 1
MAX_SPEED = 8
JUMP_HEIGHT = 13

class Entity:
    def __init__(self, sprite, x, y, gravity):
        self.sprite = pygame.image.load(sprite)
        self.rect = pygame.Rect((x,y),self.sprite.get_size())
        self.velocity = pygame.math.Vector2(x=0,y=0)
        self.gravity = gravity
        self.grounded = False
        self.direction = 'left'
        self.state = 'idle'
       

    def physicsUpdate(self, model):
        #gravity acceleration
        #calc velocity/new position
        #check if new position collides with anything
        #if it does perform appropriate action
        #otherwise, move to that location

        # gravity
        self.gravityFriction()
        

        self.horizontalMove()
        self.horizontalCollision(model)
        self.verticalMove()
        self.verticalCollision(model)

        #check for screen bounds

    def horizontalMove(self):
        self.rect.x += int(self.velocity.x)

    def horizontalCollision(self, model):
        platforms = self.getCollisions(model)
        for platform in platforms:
            #moving right
            if self.velocity.x > 0:
                self.rect.right = platform.rect.left
            #moving left
            elif self.velocity.x < 0:
                self.rect.left = platform.rect.right
            self.velocity.x = 0


    def verticalMove(self):
        self.rect.y += int(self.velocity.y)
    
    def verticalCollision(self, model):
        #self.rect.bottom += 1

        platforms = self.getCollisions(model)
        if not platforms:
            self.grounded = False
        for platform in platforms:
            #moving down
            if self.velocity.y > 0:
                self.rect.bottom = platform.rect.top
                self.grounded = True
            #moving up
            elif self.velocity.y < 0:
                self.rect.top = platform.rect.bottom
            self.velocity.y = 0


    def getCollisions(self, model):
        collisions = []
        for y, row in enumerate(model.stage.stageLayout):
            for x, platform in enumerate(row):
                if platform is not None and isinstance(platform, Stage.Platform):
                    if self.rect.colliderect(platform.rect):
                        collisions.append(platform)
        return collisions
    
    def gravityFriction(self):
        if not self.grounded:
            self.velocity.y += GRAVITY
        else:
            if self.velocity.x < FRICTION and self.velocity.x > -FRICTION:
                self.velocity.x = 0
            elif self.velocity.x > 0:
                self.velocity.x -= FRICTION
            elif self.velocity.x < 0:
                self.velocity.x += FRICTION
        
        
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

        self.moving_left = False

    def physicsUpdate(self, model):
        #apply gravity
        self.gravityFriction()


         #turn around if enemy reaches edge of screen
        if self.rect.right >= model.stage.resolution[0]:
            self.moving_left = True
        elif self.rect.left <= 0:
            self.moving_left = False

        # check if enemy is at edge of screen
        if self.moving_left and self.rect.left <= 0:
            self.rect.left = 0
            self.moving_left = False
        elif not self.moving_left and self.rect.right >= model.stage.resolution[0]:
            self.rect.right = model.stage.resolution[0]
            self.moving_left = True

        # check for collisions with platforms
        platforms = self.getCollisions(model)
        for platform in platforms:
            #check if enemy is colliding with left or right side of platform
            if self.rect.bottom > platform.rect.top and self.rect.top < platform.rect.bottom:
                if self.rect.right > platform.rect.left and self.velocity.x > 0:
                    self.moving_left = True
                elif self.rect.left < platform.rect.right and self.velocity.x < 0:
                    self.moving_left = False


            # check if enemy is colliding with top or bottom of platform
            if self.rect.right > platform.rect.left and self.rect.left < platform.rect.right:
                if self.rect.bottom > platform.rect.top and self.velocity.y > 0:
                    self.rect.bottom = platform.rect.top
                    self.velocity.y = 0
                    self.grounded = True
            elif self.rect.top < platform.rect.bottom and self.velocity.y < 0:
                self.rect.top = platform.rect.bottom
                self.velocity.y = 0


        # update enemy position based on direction
        if self.moving_left:
            self.horizontalMove()
            self.moveLeft()
            self.horizontalCollision(model)
        else:
            self.horizontalMove()
            self.moveRight()
            self.horizontalCollision(model)


            
class Collectible:
    def __init__(self, type, x, y):
        self.sprite = type
        self.rect = self.sprite.get_rect()