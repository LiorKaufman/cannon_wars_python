import pygame
import math

from projectileTest import Ball
from cannonClass import Cannon
pygame.init()

win = pygame.display.set_mode((1200,600))
pygame.display.set_caption('Cannon Wars')


golfBall = Ball(300,494,5,(255,255,255))
# We create a clock object from the pygame library to allow us to  set our frame rate
clock = pygame.time.Clock()

# Save the background image as a variable
bg = pygame.image.load('bg.jpg')
bg = pygame.transform.scale(bg,(800, 600))
# Left cannon variables for coordinates and effects
leftX = 50
leftY = 450
# leftAngle = 45
leftBaseImg = pygame.image.load('base_cannon.png')
leftTurretImg = pygame.image.load('left_turret.png')
# cannonLeftImg[0] = pygame.transform.rotate(pygame.transform.scale(cannonLeftImg[0],(100, 100)),leftAngle)

# Right cannon variables for coordinates and effects
# Right cannon variables
rightX = 650
rightY = 450
rightAngle = 270
rightBaseImg = pygame.image.load('base_cannon.png')
rightTurretImg = pygame.image.load('right_turret.png')



def redrawGameWindow():
    # Instead of filling the windows to load an image we use blit instead of .fill
    win.blit(bg, (0, 0))
    leftCannon.draw(win)
    rightCannon.draw(win)
    golfBall.draw(win)
    pygame.display.update()


# Create a new cannon object
leftCannon = Cannon(leftX, leftY, 100, 100, leftBaseImg, leftTurretImg,0)
rightCannon = Cannon(rightX, rightY, 100, 100, rightBaseImg, rightTurretImg, 0)

ball_list = []
run = True


while run:
    # We create a clock to allow us to have 27 frames per second
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    # We add left and right variables for the key press logic
    if keys[pygame.K_w]:
        if leftCannon.angle < 40:
            leftCannon.angle += 1
        else:
            leftCannon.angle = 40
        leftCannon.turretImage = pygame.transform.rotate(leftTurretImg, leftCannon.angle)
    if keys[pygame.K_s]:
        if leftCannon.angle > -15:
            leftCannon.angle -= 1
        else:
            leftCannon.angle = -15
        leftCannon.turretImage = pygame.transform.rotate(leftTurretImg, leftCannon.angle)
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

    redrawGameWindow()


pygame.quit()
