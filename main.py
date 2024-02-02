# Import the pygame module
import pygame
import sys

class Ball(pygame.Rect):
    def __init__(self, posX, posY, size, color, ballSpeedX, ballSpeedY):
        # Call the __init__ method of the base class and pass the position and size parameters
        super().__init__(posX, posY, size, size)
        self.color = color
        self.ballSpeedX = ballSpeedX
        self.ballSpeedY = ballSpeedY
    # Override the __str__ method to change how the custom class is printed
    def __str__(self):
        return f"Ball({self.x}, {self.y}, {self.width}, {self.height}, {self.color}, {self.speed}, {self.angle})"
    #define a custom method that draws the ball on the screen
    def draw(self, screen):
        # Use pygame.draw.ellipse to draw a circle using the rect and color attributes of self
        pygame.draw.ellipse(screen, self.color, self)

    def checkCollisions(self, collidingObject):
        if self.colliderect(collidingObject):
            print("collision")
            self.ballSpeedX *= -1

    # Define a custom method that updates the position and direction of the ball
    def update(self, screen, ball):
        # Move the rect by the change in position using the move method of the base class
        '''
        if self.x + self.width >=  screen.get_width():
            self.ballSpeedX *= -1
            self.x = screen.get_width() - self.width
        elif self.x  <=  0:
            self.ballSpeedX *= -1
            self.x = 0
        '''
        if self.y + self.height >= screen.get_height():
            self.ballSpeedY *= -1
            self.y = screen.get_height() - self.height
        elif self.y <= 0:
            self.ballSpeedY *= -1
            self.y = 0

        self.x += self.ballSpeedX
        self.y += self.ballSpeedY

class Player(pygame.Rect):
    def __init__(self, posX, posY, playerSizeX, playerSizeY, color, speed):
        # Call the __init__ method of the base class and pass the position and size parameters
        super().__init__(posX, posY, playerSizeX, playerSizeY)
        self.color = color
        self.speedX = speed
        self.speedY = speed
    # Override the __str__ method to change how the custom class is printed
    def __str__(self):
        return f"Player({self.x}, {self.y}, {self.width}, {self.height}, {self.color}, {self.speed}, {self.angle})"
    #define a custom method that draws the ball on the screen
    def draw(self, screen):
        # Use pygame.draw.ellipse to draw a circle using the rect and color attributes of self
        pygame.draw.rect(screen, self.color, self)

    # Define a custom method that updates the position and direction of the ball
    def update(self, screen, ball):
        self.keepWithinBounds()
    def keepWithinBounds(self):
        if self.y <= 0:
            self.y =0
        if self.y + self.height >= screen.get_height():
            self.y = screen.get_height() - self.height

class Enemy(Player):
    def update(self, screen,  ball):
        #move enemy basing on ball's y position
        if ball.y + ball.height/2 < self.y:
            self.y -= self.speedY
        elif ball.y -  ball.height/2 > self.y:
            self.y += self.speedY

        self.keepWithinBounds()

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


def createBall():
    ballSize = 20
    ballSpeed = 3
    posX = screen.get_width() / 2 - ballSize / 2
    posY = screen.get_height() / 2 - ballSize / 2
    ball = Ball(posX, posY, ballSize, (255, 255, 255), ballSpeed, ballSpeed)
    return ball
def createPlayer():
    playerSizeX = 10
    playerSizeY = 60
    playerSpeed = 5
    posX = 0
    posY = screen.get_height()/2 - playerSizeY/2
    player = Player(posX, posY, playerSizeX, playerSizeY, (255, 255, 255), playerSpeed)
    return player
def createEnemy():
    enemySizeX = 10
    enemySizeY = 60
    enemySpeed = 5
    posX = screen.get_width() - enemySizeX
    posY = screen.get_height()/2 - enemySizeY/2
    enemy = Enemy(posX, posY, enemySizeX, enemySizeY, (255, 255, 255), enemySpeed)
    return enemy

#create ball object:
ball = createBall()
#create player object:
player = createPlayer()
#create enemy object:
enemy = createEnemy()

objectList = [i for i in [ball, player, enemy]]

def drawObjects(screen, objectList):
    for i in objectList:
        i.draw(screen)
def checkCollisions(player, enemy, ball):
    ball.checkCollisions(player)
    ball.checkCollisions(enemy)

def updateObjects(screen, objectList, ball):
    for i in objectList:
        i.update(screen, ball)


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

    #draw your objects on the screen:
    #drawObjects(listOfObjectsToDraw, objects)
    updateObjects(screen, objectList, ball)
    checkCollisions(player, enemy, ball)
    drawObjects(screen, objectList)


    # Update the display
    pygame.display.update()
    # Control the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
