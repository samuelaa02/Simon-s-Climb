# object responsible for handling current stage layout information

import pygame, sys, array


class Stage:
    def __init__(self, filepath):
        self.filepath = filepath
        self.load_level()
        
        pass

    def load_level(self):
        with open(self.filepath) as file:

            self.stageName = file.readline()
            stageDim = file.readline().split()
            self.dimensions = pygame.math.Vector2(int(stageDim[0]), int(stageDim[1]))
            self.background = file.readline()
            spawnPt = file.readline().split
            self.spawnPoint = pygame.math.Vector2(int(spawnPt[0]), int(spawnPt[1]))

            if(file.readline() != "Platforms"):
                sys.exit("~~Expected \"Platforms\" title after spawnpoint information.~~")
            self.stageLayout[self.dimensions.x][self.dimensions.y]

            tempPlatformInfo = file.readline()
            while(tempPlatformInfo != "Enemies"):
                tempPlatformInfo.split()
                try:
                    self.stageLayout[int(tempPlatformInfo[1])][int(tempPlatformInfo[2])] = Platform(tempPlatformInfo[0],int(tempPlatformInfo[1]),int(tempPlatformInfo[2]))
                except:
                    sys.exit("~~Invalid platform definition.~~\n")
                tempPlatformInfo = file.readline()

            tempEnemyInfo = file.readline()
            while(tempEnemyInfo != "Collectibles"):
                tempEnemyInfo.split()
                try: 
                    self.enemies.append(tempEnemyInfo)
                except:
                    sys.exit("~~Invalid Enemy definition.~~\n")
                tempEnemyInfo = file.readline()

            tempCollectInfo = file.readline()
            while (tempCollectInfo != ""):
                tempCollectInfo.split()
                try: 
                    self.collectibles.append(tempCollectInfo)
                except:
                    sys.exit("~~Invalid Collectible definition.~~\n")
                tempCollectInfo = file.readline()

    

    #needs work
class Platform:
    def __init__(self, material, posx, posy):
        self.material = material
        self.variant = 0
        self.position = pygame.math.Vector2(posx, posy)

