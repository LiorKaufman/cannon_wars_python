import pygame
from projectile import Ball
from cannonClass import Cannon

# Start pygame
pygame.init()

# Window Variables:
game_width = 1400
game_height = 625
win = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption('Cannon Wars')
font = pygame.font.Font('freesansbold.ttf', 32)

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
# Left Cannon images
frontWheel = pygame.image.load('./images/pieces/front-wheel.png')
backWheel = pygame.image.load('./images/pieces/backwheel.png')
chassis = pygame.image.load('./images/pieces/chassis.png')
bow = pygame.image.load('./images/pieces/bow.png')
# Left cannon images scaling
frontWheel = pygame.transform.scale(frontWheel, (100, 100))
backWheel = pygame.transform.scale(backWheel, (75, 75))
chassis = pygame.transform.scale(chassis, (220, 150))
bow = pygame.transform.scale(bow, (230, 70))

# Coordinates for the leftcannon images
# **** Requires refactoring ****
leftImgMap = [leftX + 100, leftY + 75, leftX - 20, leftY + 100, leftX, leftY - 30, leftX, leftY - 50]

# Create the left cannon object
leftCannon = Cannon(leftX, leftY, 0, frontWheel, backWheel, chassis, bow, leftImgMap)
# Right cannon variables for coordinates and effects
# **** Should be refactored  ****
rightX = 1050
rightY = 450

# right cannon images - uses a few images from the left cannon images
rightChassis = pygame.image.load('./images/pieces/rightChassis.png')
rightBow = pygame.image.load('./images/pieces/rightBow.png')
# right cannon images scaling
rightChassis = pygame.transform.scale(rightChassis, (220, 150))
rightBow = pygame.transform.scale(rightBow, (230, 70))

# right cannon img coordinates
# ***** Requires refactoring*****
rightImgMap = [rightX, rightY + 75, rightX + 150, rightY + 100, rightX, rightY - 30, rightX, rightY - 50]
# Create the right cannon object
rightCannon = Cannon(rightX, leftY, 0, frontWheel, backWheel, rightChassis, rightBow, rightImgMap)

# Redraw window function call all the draw methonds of the different objects
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
    #  Changes text based on the turn of the players: Left or Right
    if turn:
        turnText = font.render('Left Cannon Turn', True, (0, 0, 0))
        textRectTurn = turnText.get_rect()
        textRectTurn.center = (600, 75)
        win.blit(turnText, textRectTurn)
    else:
        turnText = font.render('Right Cannon Turn', True, (0, 0, 0))
        textRectTurn = turnText.get_rect()
        textRectTurn.center = (600, 75)
        win.blit(turnText, textRectTurn)

    pygame.display.update()


# Create lists for the cannonballs
leftAmmo = [cannonBallLeft]
rightAmmo = [cannonBallRight]
# Main variables for the game
run = True
time = 0
turn = True
# The Game loop that runs the game
while run:
    # Framerate update
    clock.tick(100)

    # Main projectile collision logic loop
    for ammo in leftAmmo:
        if leftCannon.shoot:
            # Makes sure the ball does not go under the screen
            if ammo.y < 600 - ammo.radius:
                time += 0.12
                pos = ammo.ballPath(round(game_width*0.1), 450, leftCannon.power, leftCannon.angle, time)
                ammo.x = pos[0]
                ammo.y = pos[1]
                # Checks the y coordinates  and x coordinates of the projectile compared to the right cannon
                if ammo.y + ammo.radius > 420:
                    if ammo.x + ammo.radius > rightCannon.x and ammo.x + ammo.radius < game_width - 100:
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


     # Main projectile collision logic loop
    for ammo in rightAmmo:
        if rightCannon.shoot:
            # Check that the cannonball projectile does not fall down to the screen
            if ammo.y < 600 - ammo.radius:
                time += 0.12
                pos = ammo.ballPath(round(game_width*0.9), 450, -rightCannon.power, rightCannon.angle, time)
                ammo.x = pos[0]
                ammo.y = pos[1]
                # Checks logic for collision with the left cannon
                if ammo.y + ammo.radius > 420:
                    if ammo.x + ammo.radius < leftCannon.x + 200 and ammo.x + ammo.radius > 100:
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
            leftCannon.bow = pygame.transform.rotate(bow, leftCannon.angle)
        if keys[pygame.K_s]:
            if leftCannon.angle > 0:
                leftCannon.angle -= 1
            else:
                leftCannon.angle = 0
            leftCannon.bow = pygame.transform.rotate(bow, leftCannon.angle)
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
    if turn:
        if keys[pygame.K_SPACE]:
            if len(leftAmmo) <= 0:
                leftAmmo.append(Ball(round(game_width*0.1), 450, 5, (0, 0, 0)))
            if not leftCannon.shoot and not rightCannon.shoot:
                leftCannon.shoot = True
                x = leftAmmo[0].x
                y = leftAmmo[0].y
                turn = False


    # Right cannon controls
    if not rightCannon.shoot:
        if keys[pygame.K_UP]:
            if rightCannon.angle < 90:
                rightCannon.angle += 1
            else:
                rightCannon.angle = 90
            rightCannon.bow = pygame.transform.rotate(rightBow, -rightCannon.angle)
        if keys[pygame.K_DOWN]:
            if rightCannon.angle > 0:
                rightCannon.angle -= 1
            else:
                rightCannon.angle = 0
            rightCannon.bow = pygame.transform.rotate(rightBow, -rightCannon.angle)
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
    if turn == False:
        if keys[pygame.K_k]:
            if len(rightAmmo) <= 0:
                rightAmmo.append(Ball(round(game_width*0.9), 450, 5, (0, 0, 0)))
            if not rightCannon.shoot and not leftCannon.shoot:
                rightCannon.shoot = True
                x = rightAmmo[0].x
                y = rightAmmo[0].y
                turn = True
    redrawGameWindow()


pygame.quit()
