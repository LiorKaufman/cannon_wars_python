import pygame
pygame.init()
# Added font for text objects
font = pygame.font.Font('freesansbold.ttf', 32)

class Cannon(object):

    def __init__(self, x, y, width, height, baseImage, turretImage, power):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.baseImage = baseImage
        self.angle = 0
        self.turretImage = turretImage
        self.power = power
        self.score = 0
        self.CannonTextAngle = font.render(str(0), True, (0, 0, 0))
        self.CannonTextPower = font.render(str(0), True, (0, 0, 0))
        self.CannonTextScore = font.render(str(0), True, (0, 0, 0))
        self.shoot = False

    def draw (self, win):
        self.CannonTextAngle = font.render('Angle: ' + str(self.angle), True, (0, 0, 0))
        self.CannonTextPower = font.render('Power: ' + str(self.power), True, (0, 0, 0))
        self.CannonTextScore = font.render('Score: ' + str(self.score), True, (0, 0, 0))
        textRectAngle = self.CannonTextAngle.get_rect()
        textRectPower = self.CannonTextPower.get_rect()
        textRectScore = self.CannonTextScore.get_rect()
        textRectPower.center = (self.x + 50, self.y - 150)
        textRectAngle.center = (self.x + 50, self.y - 100)
        textRectScore.center = (self.x + 50, self.y - 200)
        pygame.draw.rect(win, (222, 150, 18), (self.x, self.y, 100, 100))
        win.blit(self.baseImage, (self.x, self.y + 20))
        win.blit(self.turretImage, (self.x + 20, self.y - 25))
        win.blit(self.CannonTextAngle, textRectAngle)
        win.blit(self.CannonTextPower, textRectPower)
        win.blit(self.CannonTextScore, textRectScore)

