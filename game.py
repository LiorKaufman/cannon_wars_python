import pygame
import math

from projectileTest import Ball
from cannonClass import Cannon
pygame.init()

win = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('Cannon Wars')


cannonBall = Ball(300, 594, 5, (255, 255, 255))
# We create a clock object from the pygame library to allow us to  set our frame rate
clock = pygame.time.Clock()

# Save the background image as a variable
bg = pygame.image.load('bg.jpg')
bg = pygame.transform.scale(bg, (1200, 600))
# Left cannon variables for coordinates and effects
leftX = 50
leftY = 450
leftBaseImg = pygame.image.load('base_cannon.png')
leftTurretImg = pygame.image.load('left_turret.png')


# Right cannon variables for coordinates and effects
# Right cannon variables
rightX = 1050
rightY = 450
rightAngle = 270
rightBaseImg = pygame.image.load('base_cannon.png')
rightTurretImg = pygame.image.load('right_turret.png')



def redrawGameWindow():
    # Instead of filling the windows to load an image we use blit instead of .fill
    win.blit(bg, (0, 0))
    leftCannon.draw(win)
    rightCannon.draw(win)
    cannonBall.draw(win)
    pygame.display.update()



# Create a new cannon object
leftCannon = Cannon(leftX, leftY, 100, 100, leftBaseImg, leftTurretImg,0)


rightCannon = Cannon(rightX, rightY, 100, 100, rightBaseImg, rightTurretImg, 0)

ball_list = []
run = True
time = 0

while run:
    # We create a clock to allow us to have 27 frames per second
    clock.tick(100)

    if leftCannon.shoot:
        if cannonBall.y < 600 - cannonBall.radius:
            time += 0.08
            pos = cannonBall.ballPath(leftCannon.x + 50, leftCannon.y, leftCannon.power, leftCannon.angle, time)
            cannonBall.x = pos[0]
            cannonBall.y = pos[1]
        else:
            leftCannon.shoot = False
            time = 0
            cannonBall.y = 594


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    # Left cannon controls
    if not leftCannon.shoot:
        if keys[pygame.K_w]:
            if leftCannon.angle < 90:
                leftCannon.angle += 1
            else:
                leftCannon.angle = 90
            leftCannon.turretImage = pygame.transform.rotate(leftTurretImg, leftCannon.angle)
        if keys[pygame.K_s]:
            if leftCannon.angle > 0:
                leftCannon.angle -= 1
            else:
                leftCannon.angle = 0
            leftCannon.turretImage = pygame.transform.rotate(leftTurretImg, leftCannon.angle)
        if keys[pygame.K_d]:
            if leftCannon.power < 100:
                leftCannon.power += 1
            else:
                leftCannon.power = 100
        if keys[pygame.K_a]:
            if leftCannon.power > 0:
                leftCannon.power -= 1
            else:
                leftCannon.power = 0
    if keys[pygame.K_SPACE]:
        if not leftCannon.shoot:
            leftCannon.shoot = True
            x = cannonBall.x
            y = cannonBall.y
            power = leftCannon.power
            angle = leftCannon.angle



    # Right cannon controls
    if keys[pygame.K_UP]:
        if rightCannon.angle > -25:
            rightCannon.angle -= 1
        else:
            rightCannon.angle = -25
        rightCannon.turretImage = pygame.transform.rotate(rightTurretImg, rightCannon.angle)
    if keys[pygame.K_DOWN]:
        if rightCannon.angle < 25:
            rightCannon.angle += 1
        else:
            rightCannon.angle = 25
        rightCannon.turretImage = pygame.transform.rotate(rightTurretImg, rightCannon.angle)
    if keys[pygame.K_RIGHT]:
        if rightCannon.power < 100:
            rightCannon.power += 1
        else:
            rightCannon.power = 100
    if keys[pygame.K_LEFT]:
        if rightCannon.power > 0:
            rightCannon.power -= 1
        else:
            rightCannon.power = 0

    redrawGameWindow()


pygame.quit()
