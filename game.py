import pygame
pygame.init()

win = pygame.display.set_mode((800,600))
pygame.display.set_caption('Cannon Wars')



# Cannon ball variables
# width = 40
# height = 60
# vel = 5

# We create a clock object from the pygame library to allow us to  set our frame rate
clock = pygame.time.Clock()


class Cannon(object):

    def __init__(self, x, y, width, height, image, angle):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.angle = angle

    def draw (self, win):
        win.blit(self.image, (self.x, self.y))


# Save the background image as a variable
bg = pygame.image.load('bg.jpg')
bg = pygame.transform.scale(bg,(800, 600))
cannonImg = pygame.image.load('cannon.jpg')
# Left cannon variables for coordinates and effects
leftX = 50
leftY = 450
leftAngle = 45
cannonLeftImg = [cannonImg]
cannonLeftImg[0] = pygame.transform.rotate(pygame.transform.scale(cannonLeftImg[0],(100, 100)),leftAngle)

# Right cannon variables for coordinates and effects
# Right cannon variables
rightX = 650
rightY = 450
rightAngle = 270
cannonRightImg = [pygame.transform.flip(cannonImg, True, False)]
cannonRightImg[0] = pygame.transform.rotate((pygame.transform.scale(cannonRightImg[0],(100, 100))),rightAngle)


def redrawGameWindow():
    # Instead of filling the windows to load an image we use blit instead of .fill
    win.blit(bg, (0, 0))
    leftCannon.draw(win)
    rightCannon.draw(win)
    pygame.display.update()


# Create a new cannon object
leftCannon = Cannon(leftX, leftY, 100, 100, cannonLeftImg[0], leftAngle)
rightCannon = Cannon(rightX, rightY, 100, 100, cannonRightImg[0], rightAngle)

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
        if leftCannon.angle < 80:
            leftCannon.angle += 1
        else:
            leftCannon.angle = 80
        leftCannon.image = pygame.transform.rotate(cannonLeftImg[0], leftCannon.angle)
    if keys[pygame.K_s]:
        if leftCannon.angle <= 30:
            leftCannon.angle = 30
        else:
            leftCannon.angle -= 1
        leftCannon.image = pygame.transform.rotate(cannonLeftImg[0], leftCannon.angle)
    if keys[pygame.K_UP]:
        if rightCannon.angle < 135:
            rightCannon.angle += 1
        else:
            rightCannon.angle = 135
        rightCannon.image = pygame.transform.rotate(cannonRightImg[0], rightCannon.angle)
    if keys[pygame.K_DOWN]:
        if rightCannon.angle <= 30:
            rightCannon.angle = 30
        else:
            rightCannon.angle -= 1
        rightCannon.image = pygame.transform.rotate(cannonRightImg[0], rightCannon.angle)
    redrawGameWindow()


pygame.quit()
