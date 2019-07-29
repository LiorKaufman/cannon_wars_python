import pygame
from projectileTest import Ball
from cannonClass import Cannon

pygame.init()
game_width = 1200
game_height = 600
win = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption('Cannon Wars')


cannonBallRight = Ball(round(game_width*0.9), 450, 5, (255, 255, 255))
cannonBallLeft = Ball(round(game_width*0.1), 450, 5, (255, 255, 255))
# We create a clock object from the pygame library to allow us to  set our frame rate
clock = pygame.time.Clock()

# Save the background image as a variable
bg = pygame.image.load('bg.jpg')
bg = pygame.transform.scale(bg, (game_width, game_height))
# Left cannon variables for coordinates and effects
leftX = 50
leftY = 450
leftBaseImg = pygame.image.load('base_cannon.png')
leftTurretImg = pygame.image.load('left_turret.png')


# Right cannon variables for coordinates and effects
rightX = 1050
rightY = 450
rightBaseImg = pygame.image.load('base_cannon.png')
rightTurretImg = pygame.image.load('right_turret.png')


def redrawGameWindow():
    # Instead of filling the windows to load an image we use blit instead of .fill
    win.blit(bg, (0, 0))
    leftCannon.draw(win)
    rightCannon.draw(win)
    cannonBallLeft.draw(win)
    cannonBallRight.draw(win)
    pygame.draw.rect(win, (255,0,0),(100, 500,10,10))
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
        if cannonBallLeft.y < 600 - cannonBallLeft.radius:
            time += 0.08
            pos = cannonBallLeft.ballPath(round(game_width*0.1), 450, leftCannon.power, leftCannon.angle, time)
            cannonBallLeft.x = pos[0]
            cannonBallLeft.y = pos[1]
        else:
            leftCannon.shoot = False
            time = 0
            cannonBallLeft.y = 594

    if rightCannon.shoot :
        if cannonBallRight.y < 600 - cannonBallRight.radius:
            time += 0.08
            pos = cannonBallRight.ballPath(round(game_width*0.9), 450, -rightCannon.power, rightCannon.angle, time)
            cannonBallRight.x = pos[0]
            cannonBallRight.y = pos[1]
        else:
            rightCannon.shoot = False
            time = 0
            cannonBallRight.y = 594

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
        if not leftCannon.shoot and not rightCannon.shoot:
            leftCannon.shoot = True
            x = cannonBallLeft.x
            y = cannonBallLeft.y
            powerLeft = leftCannon.power
            angleLeft = leftCannon.angle

    # Right cannon controls
    if keys[pygame.K_UP]:
        if rightCannon.angle < 90:
            rightCannon.angle += 1
        else:
            rightCannon.angle = 90
        rightCannon.turretImage = pygame.transform.rotate(rightTurretImg, rightCannon.angle)
    if keys[pygame.K_DOWN]:
        if rightCannon.angle > 0:
            rightCannon.angle -= 1
        else:
            rightCannon.angle = 0
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
    if keys[pygame.K_k]:
        if not rightCannon.shoot and not leftCannon.shoot:
            rightCannon.shoot = True
            x = cannonBallRight.x
            y = cannonBallRight.y
            powerRight = rightCannon.power
            angleRight = rightCannon.angle
    redrawGameWindow()


pygame.quit()
