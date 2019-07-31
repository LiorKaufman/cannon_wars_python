import pygame
from projectile import Ball
from cannonClass import Cannon

# Start pygame
pygame.init()
# Window Variables:
game_width = 1200
game_height = 600
win = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption('Cannon Wars')

# Create first cannon balls
# **** Should be refactored  ****
cannonBallRight = Ball(round(game_width*0.9), 450, 5, (0, 0, 0))
cannonBallLeft = Ball(round(game_width*0.1), 450, 5, (0, 0, 0))
# We create a clock object from the pygame library to allow us to  set our frame rate
clock = pygame.time.Clock()

# Save the background image as a variable
bg = pygame.image.load('bg.jpg')
bg = pygame.transform.scale(bg, (game_width, game_height))
# Left cannon variables for coordinates and effects
# **** Should be refactored  ****
leftX = 50
leftY = 450
leftBaseImg = pygame.image.load('base_cannon.png')
leftTurretImg = pygame.image.load('left_turret.png')


# Right cannon variables for coordinates and effects
# **** Should be refactored  ****
rightX = 1050
rightY = 450
rightBaseImg = pygame.image.load('base_cannon.png')
rightTurretImg = pygame.image.load('right_turret.png')


def redrawGameWindow():
    # Instead of filling the windows to load an image we use blit instead of .fill
    win.blit(bg, (0, 0))
    # Draw all objects in one function
    leftCannon.draw(win)
    rightCannon.draw(win)
    # Draw the cannon ball only if we have ammo
    if len(leftAmmo) > 0:
        leftAmmo[0].draw(win)

    if len(rightAmmo) > 0:
        rightAmmo[0].draw(win)
    pygame.display.update()


# Create new cannon objects
leftCannon = Cannon(leftX, leftY, 100, 100, leftBaseImg, leftTurretImg,0)
rightCannon = Cannon(rightX, rightY, 100, 100, rightBaseImg, rightTurretImg, 0)
# Create lists for the cannonballs
leftAmmo = [cannonBallLeft]
rightAmmo = [cannonBallRight]
# Main variables for the game
run = True
time = 0

while run:
    clock.tick(140)

    for ammo in leftAmmo:
        if leftCannon.shoot:
            if ammo.y < 600 - ammo.radius:
                time += 0.1
                pos = ammo.ballPath(round(game_width*0.1), 450, leftCannon.power, leftCannon.angle, time)
                ammo.x = pos[0]
                ammo.y = pos[1]
                if ammo.x + ammo.radius > rightCannon.x:
                    leftCannon.shoot = False
                    time = 0
                    ammo.drawHit(ammo.x, ammo.y, win)
                    leftAmmo.pop(leftAmmo.index(ammo))
                    leftCannon.score += 1
            else:
                leftCannon.shoot = False
                time = 0
                ammo.drawHit(ammo.x,ammo.y, win)
                leftAmmo.pop(leftAmmo.index(ammo))

    for ammo in rightAmmo:
        if rightCannon.shoot:
            if ammo.y < 600 - ammo.radius:
                time += 0.1
                pos = ammo.ballPath(round(game_width*0.9), 450, -rightCannon.power, rightCannon.angle, time)
                ammo.x = pos[0]
                ammo.y = pos[1]
                if ammo.y > 500 - ammo.radius:
                    if ammo.x + ammo.radius < leftCannon.x + 150:
                        rightCannon.shoot = False
                        time = 0
                        ammo.drawHit(ammo.x, ammo.y, win)
                        rightAmmo.pop(rightAmmo.index(ammo))
                        rightCannon.score += 1
            else:
                rightCannon.shoot = False
                time = 0
                ammo.drawHit(ammo.x, ammo.y, win)
                rightAmmo.pop(rightAmmo.index(ammo))

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
        if len(leftAmmo) <= 0:
            leftAmmo.append(Ball(round(game_width*0.1), 450, 5, (0, 0, 0)))
        if not leftCannon.shoot and not rightCannon.shoot:
            leftCannon.shoot = True
            x = leftAmmo[0].x
            y = leftAmmo[0].y


    # Right cannon controls
    if not rightCannon.shoot:
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
        if len(rightAmmo) <= 0:
            rightAmmo.append(Ball(round(game_width*0.9), 450, 5, (0, 0, 0)))
        if not rightCannon.shoot and not leftCannon.shoot:
            rightCannon.shoot = True
            x = rightAmmo[0].x
            y = rightAmmo[0].y
    redrawGameWindow()


pygame.quit()
