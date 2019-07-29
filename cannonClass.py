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
        self.CannonTextAngle = font.render(str(5), True, (255, 255, 255))
        self.CannonTextPower = font.render(str(0), True, (255, 255, 255))
        self.shoot = False

    def draw (self, win):
        self.CannonTextAngle = font.render(str(self.angle), True, (255, 255, 255))
        self.CannonTextPower = font.render(str(self.power), True, (255, 255, 255))
        textRectAngle = self.CannonTextAngle.get_rect()
        textRectPower = self.CannonTextPower.get_rect()
        textRectAngle.center = (self.x + 50, self.y - 150)
        textRectPower.center = (self.x + 100, self.y - 150)
        win.blit(self.baseImage, (self.x, self.y + 20))
        win.blit(self.turretImage,(self.x + 20, self.y - 25))
        win.blit(self.CannonTextAngle, textRectAngle)
        win.blit(self.CannonTextPower, textRectPower)

