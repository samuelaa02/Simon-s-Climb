import pygame, sys, Stage

PLAYER_SPRITE = './sprites/player_sprite.png'

BEETLE = 'BEETLE'
BEETLE_SPRITE = './sprites/beetle_sprite.png'
BEETLE_STRENGTH = 2

ANT = 'ANT'
ANT_SPRITE = './sprites/ant_sprite.png'
ANT_STRENGTH = 1.2

EGG = 'EGG'
EGG_SPRITE = './sprites/egg_sprite.png'

FLAG = 'FLAG'
FLAG_SPRITE = './sprites/flag_sprite.png'

GRAVITY = 0.2
FRICTION = 1
PLAYER_SPEED = .5
MAX_SPEED = 3.5
ENEMY_SPEED = 0.03  
ENEMY_MAX_SPEED = 1
JUMP_HEIGHT = 6

class Entity:
    def __init__(self, sprite, x, y, gravity, friction):
        self.sprite = pygame.image.load(sprite)
        self.rect = pygame.Rect((x,y),self.sprite.get_size())
        self.velocity = pygame.math.Vector2(x=0,y=0)
        self.gravity = gravity
        self.grounded = False
        self.friction = friction
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
            if(self.gravity):
                self.velocity.y += GRAVITY
        else:
            if (self.friction):
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
        super().__init__(PLAYER_SPRITE, x, y, True, True)
        self.eggs = 0
    
    def playerJump(self):
        if self.grounded:
            #negative is up
            self.velocity.y = -JUMP_HEIGHT
            self.grounded = False


class Enemy(Entity):
    def __init__(self, type, x, y):
        self.enemyType = type
        if(self.enemyType == BEETLE):
            super().__init__(BEETLE_SPRITE, x, y, True, False)
        elif(self.enemyType == ANT):
            super().__init__(ANT_SPRITE, x, y, True, False)
    
    def enemyUpdate(self, model):
            self.aiMovement(model)
            self.physicsUpdate(model)
            self.knockbackPlayer(model.player)

    def knockbackPlayer(self, player):
        if self.rect.colliderect(player.rect):
            self.velocity.x = 0
            if(self.enemyType == BEETLE):
                #check direction
                if self.direction == 'left':
                    leftline = (self.rect.topleft, self.rect.bottomleft)
                    if player.rect.clipline(leftline):
                        player.velocity.x = -MAX_SPEED * BEETLE_STRENGTH 
                else:
                    rightline = (self.rect.topright, self.rect.bottomright)
                    if player.rect.clipline(rightline):
                        player.velocity.x = MAX_SPEED * BEETLE_STRENGTH 
            elif(self.enemyType == ANT):
                if(player.velocity.x < 0):
                    player.velocity.x = MAX_SPEED * ANT_STRENGTH 
                elif (player.velocity.x > 0):
                    player.velocity.x = -MAX_SPEED * ANT_STRENGTH 
                player.velocity.y = -MAX_SPEED * ANT_STRENGTH


    def moveRight(self):
        if self.velocity.x < ENEMY_MAX_SPEED:
            self.velocity.x += ENEMY_SPEED
        if self.direction != 'right':
            self.direction = 'right'

    def moveLeft(self):
        if self.velocity.x > -ENEMY_MAX_SPEED:
            self.velocity.x -= ENEMY_SPEED
        if self.direction != 'left':
            self.direction = 'left'

    def aiMovement(self, model):
            if (self.direction == 'left'):
                enemyGridPos = (int((self.rect.right-1)/32),int((self.rect.y)/32))
                if((enemyGridPos[0]-1) < 0):
                    self.moveRight()
                else:
                    try:
                        if((model.stage.stageLayout[enemyGridPos[1]+1][enemyGridPos[0]-1] is not None) and (model.stage.stageLayout[enemyGridPos[1]][enemyGridPos[0]-1] is None)):
                            self.moveLeft()
                        else:
                            self.moveRight()
                    except:
                        self.moveRight()
            else:
                enemyGridPos = (int((self.rect.left+1)/32),int((self.rect.y)/32))
                if((enemyGridPos[0]+1) == (model.stage.dimensions[0])):
                    self.moveLeft()
                else:
                    try:
                        if((model.stage.stageLayout[enemyGridPos[1]+1][enemyGridPos[0]+1] is not None) and (model.stage.stageLayout[enemyGridPos[1]][enemyGridPos[0]+1] is None)):
                            self.moveRight()
                        else:
                            self.moveLeft()
                    except:
                        self.moveLeft()
            

            
class Collectible:
    def __init__(self, type, x, y):
        if(type == EGG):
            self.type = EGG
            self.sprite = pygame.image.load(EGG_SPRITE)
            self.pickup = True
        elif(type == FLAG):
            self.type = FLAG
            self.sprite = pygame.image.load(FLAG_SPRITE)
            self.pickup = False
        self.rect = pygame.Rect((x,y),self.sprite.get_size())
        self.rect.center = (x+16,y+16)
        self.interacted = False
        

    #completes the level and starts the next one
    def flagAction(self, player):
        self.interacted = True

    #collects the egg
    def eggAction(self, player):
        if not self.interacted:
            self.interacted = True
            player.eggs += 1


    def collectibleCollide(self, entity):
        if (self.rect.colliderect(entity.rect)):
            if self.type == EGG:
                self.eggAction(entity)
            elif self.type == FLAG:
                self.flagAction(entity)
