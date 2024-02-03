import pygame
import sys
#custom classes:
import ball
from player import Player
from enemy import Enemy
def checkKeyEvents(player):
    # Get the state of the keyboard keys
    keys = pygame.key.get_pressed()
    # Check if the up arrow key is pressed
    if keys[pygame.K_UP]:
        # Move the rectangle up
        player.move_ip(0, -5)
    # Check if the down arrow key is pressed
    if keys[pygame.K_DOWN]:
        # Move the rectangle down
        player.move_ip(0, 5)


# Initialize pygame
pygame.init()
# Create a display surface
screen = pygame.display.set_mode((800, 600))
# Set the caption of the window
pygame.display.set_caption("Pong")
# Create a clock object
clock = pygame.time.Clock()


def createball(screen):
    ballSize = 20
    ballSpeed = 3
    posX = screen.get_width() / 2 - ballSize / 2
    posY = screen.get_height() / 2 - ballSize / 2
    ballObject = ball.Ball(screen, posX, posY, ballSize, (255, 255, 255), ballSpeed, ballSpeed)
    return ballObject
def createPlayer(screen):
    playerSizeX = 10
    playerSizeY = 60
    playerSpeed = 5
    posX = 0
    posY = screen.get_height()/2 - playerSizeY/2
    playerObject = Player(screen, posX, posY, playerSizeX, playerSizeY, (255, 255, 255), playerSpeed)
    return playerObject
def createEnemy():
    enemySizeX = 10
    enemySizeY = 60
    enemySpeed = 5
    posX = screen.get_width() - enemySizeX
    posY = screen.get_height()/2 - enemySizeY/2
    enemyObject = Enemy(screen, posX, posY, enemySizeX, enemySizeY, (255, 255, 255), enemySpeed)
    return enemyObject

#create ball object:
ball =  createball(screen)
#create player object:
player = createPlayer(screen)
#create enemy object:
enemy = createEnemy()

objectList = [i for i in [ball, player, enemy]]

def drawObjects(screen, objectList):
    for i in objectList:
        i.draw(screen)
def checkCollisions(player, enemy, ball):
    ball.checkCollisions(player)
    ball.checkCollisions(enemy)

def updateObjects(objectList, ball):
    for i in objectList:
        i.update(ball)


# Create a color object
color = pygame.Color(255, 0, 0)

# Create a variable for the game loop
running = True
# Start the game loop
while running:
    # Handle the events
    for event in pygame.event.get():
        # Check if the user clicked the close button
        if event.type == pygame.QUIT:
            # Exit the loop
            running = False
            sys.exit()
    checkKeyEvents(player)
    # Fill the screen with black
    screen.fill((0, 0, 0))

    #update object movement:
    updateObjects(objectList, ball)
    checkCollisions(player, enemy, ball)
    #draw your objects on the screen:
    drawObjects(screen, objectList)


    # Update the display
    pygame.display.update()
    # Control the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
