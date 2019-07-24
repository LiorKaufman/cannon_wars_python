import pygame
pygame.init()

win = pygame.display.set_mode((800,600))
pygame.display.set_caption('Cannon Wars')

# Added the font for the text surface
font = pygame.font.Font('freesansbold.ttf', 32)
#  added text for the left cannon
leftCannonText = font.render('Hello World', True, (255,255,255))
textRect = leftCannonText.get_rect()
textRect.center = (50, 50)


# Cannon ball variables
# width = 40
# height = 60
# vel = 5

# We create a clock object from the pygame library to allow us to  set our frame rate
clock = pygame.time.Clock()


class Cannon(object):

    def __init__(self, x, y, width, height, baseImage, turretImage):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.baseImage = baseImage
        self.angle = 0
        self.turretImage = turretImage

    def draw (self, win):
        win.blit(self.baseImage, (self.x, self.y + 20))
        win.blit(self.turretImage,(self.x + 20, self.y - 25))


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
    win.blit(leftCannonText, textRect)
    pygame.display.update()


# Create a new cannon object
leftCannon = Cannon(leftX, leftY, 100, 100, leftBaseImg, leftTurretImg)
rightCannon = Cannon(rightX, rightY, 100, 100, rightBaseImg, rightTurretImg)

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
        if leftCannon.angle > 10:
            leftCannon.angle -= 1
        else:
            leftCannon.angle = 10
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
