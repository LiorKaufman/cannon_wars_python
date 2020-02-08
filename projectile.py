import pygame
import math
import random

clock = pygame.time.Clock()

class Ball(object):
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, (0,0,0), (self.x,self.y), self.radius)
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius-1)

    def drawHit(self, hitX, hitY, win):

        explode = True

        while explode:
            colorChoices = [(255,255,255), (255,255,0), (0,0,255) ,(255,255,255)]
            magnitude = 1
            while magnitude < 50:
                exploding_x = hitX + random.randrange(-1*magnitude, magnitude)
                exploding_y = hitY + random.randrange(-1*magnitude, magnitude)
                pygame.draw.circle(win, colorChoices[random.randrange(0,4)],(exploding_x,exploding_y), random.randrange(1,5))
                magnitude += 1
                clock.tick(75)
                pygame.display.update()
            explode = False

    @staticmethod
    def ballPath(startx, starty, power, ang, time):
        angle = ang * math.pi/180
        velx = abs(math.cos(angle)) * power/1.1
        vely = abs(math.sin(angle)) * power/1.1
        if power > 0:
            distX = velx * time
            distY = (vely * time) + ((-4.9 * (time ** 2)) / 2)
        else:
            distX = velx * time
            distY = -1*(vely * time) + ((-4.9 * (time ** 2)) / 2)

        newx = round(distX + startx)
        newy = round(starty - distY)


        return (newx, newy)
