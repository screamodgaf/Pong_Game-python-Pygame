import pygame

class Ball(pygame.Rect):
    def __init__(self, screen, posX, posY, size, color, ballSpeedX, ballSpeedY):
        # Call the __init__ method of the base class and pass the position and size parameters
        super().__init__(posX, posY, size, size)
        self.color = color
        self.ballSpeedX = ballSpeedX
        self.ballSpeedY = ballSpeedY
        self.screen = screen
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
    def update(self, ball):
        # Move the rect by the change in position using the move method of the base class
        '''
        if self.x + self.width >=  screen.get_width():
            self.ballSpeedX *= -1
            self.x = screen.get_width() - self.width
        elif self.x  <=  0:
            self.ballSpeedX *= -1
            self.x = 0
        '''
        if self.y + self.height >= self.screen.get_height():
            self.ballSpeedY *= -1
            self.y = self.screen.get_height() - self.height
        elif self.y <= 0:
            self.ballSpeedY *= -1
            self.y = 0

        self.x += self.ballSpeedX
        self.y += self.ballSpeedY