# object responsible for handling current stage layout information

import pygame, sys, array, Entity

#load all platform images

PLATFORM_SIZE = 32

class Stage:

    def __init__(self, filepath):
        self.filepath = filepath
        self.load_level()
        self.resolution = (self.dimensions[0] * PLATFORM_SIZE, self.dimensions[1] * PLATFORM_SIZE)
        

    def load_level(self):
        with open(self.filepath) as file:

            self.stageName = file.readline()
            stageDim = file.readline().split()
            self.dimensions = (int(stageDim[0]), int(stageDim[1]))
            backgroundfp = file.readline().rstrip()
            print(backgroundfp)
            self.background = pygame.image.load(backgroundfp)
            spawnPt = file.readline().split()  
            self.spawnPoint = pygame.math.Vector2(int(spawnPt[0]), int(spawnPt[1]))


            if(file.readline() != "Platforms\n"):
                sys.exit("~~Expected \"Platforms\" title after spawnpoint information.~~")
            self.stageLayout = [[None for _ in range(self.dimensions[0])] for _ in range(self.dimensions[1])]

            tempPlatformInfo = file.readline()
            while(tempPlatformInfo != "Enemies\n"):
                tempPlatformInfo = tempPlatformInfo.split(" ")
                try:
                    self.stageLayout[self.dimensions[1]-1-int(tempPlatformInfo[2])][int(tempPlatformInfo[1])] = Platform(tempPlatformInfo[0],int(tempPlatformInfo[1]),self.dimensions[1]-1-int(tempPlatformInfo[2]))
                except:
                    sys.exit("~~Invalid platform definition.~~\n")
                tempPlatformInfo = file.readline()

            tempEnemyInfo = file.readline()
            self.enemies = []
            while(tempEnemyInfo != "Collectibles\n"):
                tempEnemyInfo = tempEnemyInfo.split(" ")
                try: 
                    self.enemies.append(Entity.Enemy(tempEnemyInfo[0], int(tempEnemyInfo[1])*PLATFORM_SIZE, int(tempEnemyInfo[2])*PLATFORM_SIZE))
                except:
                    sys.exit("~~Invalid Enemy definition.~~\n")
                tempEnemyInfo = file.readline()

            tempCollectInfo = file.readline()
            self.collectibles = []
            while (tempCollectInfo != ""):
                tempCollectInfo = tempCollectInfo.split(" ")
                try: 
                    self.collectibles.append(tempCollectInfo)
                except:
                    sys.exit("~~Invalid Collectible definition.~~\n")
                tempCollectInfo = file.readline()

    

    #needs work
class Platform:
    
    def __init__(self, material, posx, posy):
        self.material = material
        self.rect = pygame.Rect((posx * PLATFORM_SIZE, posy * PLATFORM_SIZE),(PLATFORM_SIZE,PLATFORM_SIZE))

