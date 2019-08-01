import pygame
pygame.init()
# Added font for text objects
font = pygame.font.Font('freesansbold.ttf', 32)



class Cannon(object):

    def __init__(self, x, y, power, front, back, chas, bow, imgMap):
        self.x = x
        self.y = y
        self.angle = 0
        self.power = power
        self.score = 0
        self.CannonTextAngle = font.render(str(0), True, (0, 0, 0))
        self.CannonTextPower = font.render(str(0), True, (0, 0, 0))
        self.CannonTextScore = font.render(str(0), True, (0, 0, 0))
        self.shoot = False
        self.front = front
        self.back = back
        self.chas = chas
        self.bow = bow
        self.imgMap = imgMap

    def draw (self, win):
        self.CannonTextAngle = font.render('Angle: ' + str(self.angle), True, (0, 0, 0))
        self.CannonTextPower = font.render('Power: ' + str(self.power), True, (0, 0, 0))
        self.CannonTextScore = font.render('Score: ' + str(self.score), True, (0, 0, 0))
        textRectAngle = self.CannonTextAngle.get_rect()
        textRectPower = self.CannonTextPower.get_rect()
        textRectScore = self.CannonTextScore.get_rect()
        textRectPower.center = (self.x + 50, self.y - 250)
        textRectAngle.center = (self.x + 50, self.y - 200)
        textRectScore.center = (self.x + 50, self.y - 300)
        win.blit(self.CannonTextAngle, textRectAngle)
        win.blit(self.CannonTextPower, textRectPower)
        win.blit(self.CannonTextScore, textRectScore)
        win.blit(self.chas, (self.imgMap[4], self.imgMap[5]))
        win.blit(self.front, (self.imgMap[0], self.imgMap[1]))
        win.blit(self.back, (self.imgMap[2], self.imgMap[3]))
        win.blit(self.bow, (self.imgMap[6], self.imgMap[7]))

