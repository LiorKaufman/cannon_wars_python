import pygame
import math


pygame.init()

win = pygame.display.set_mode((1200,600))


class ball(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radius)
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius-1)



    @staticmethod
    def ballPath(startX, startY, power , ang, time):
        angle = ang
        velX = math.cos(angle) * power
        velY = (math.sin(angle) * power)

        distX = velX * time
        distY = (velY * time) + ((-4.9* (time ** 2 ))/2)

        newX = round(distX + startX)
        newY = round(startY - distY)

        return(newX, newY)


def redrawWindow():
    win.fill((64,64,64))
    golfBall.draw(win)
    pygame.draw.line(win, (255,255,255), line[0], line[1])
    pygame.display.update()

def findAngle(pos):
    sX = golfBall.x
    sY = golfBall.y
    try:
        angle = math.atan((sY - pos[1]) / (sX - pos[0]))
    except:
        angle = math.pi/2

    if pos[1] < sY and pos[0] > sX:
        angle = abs(angle)
    elif pos[1] < sY and pos[0] < sX:
        angle = math.pi - angle
    elif pos[1] > sY and pos[0] < sX:
        angle = math.pi + abs(angle)
    elif pos[1] > sY and pos[0] > sX:
        angle = (math.pi *2) - angle

    return angle


golfBall = ball(300,494,5,(255,255,255))

time = 0
power = 0
angle = 0
shoot = False
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(200)
    if shoot:
        if golfBall.y < 500 - golfBall.radius:
            time += 0.05
            po = golfBall.ballPath(x, y, power, angle, time)
            golfBall.x = po[0]
            golfBall.y = po[1]
        else:
            shoot = False
            time = 0
            golfBall.y = 494

    line = [(golfBall.x, golfBall.y), pygame.mouse.get_pos()]

    redrawWindow()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not shoot:
                x = golfBall.x
                y = golfBall.y
                pos = pygame.mouse.get_pos()
                shoot = True
                power = math.sqrt((line[1][1]-line[0][1])**2 +(line[1][0]-line[0][1])**2)/8
                angle = findAngle(pos)

pygame.quit()
quit()