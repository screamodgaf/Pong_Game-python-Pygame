import pygame

class Player(pygame.Rect):
    def __init__(self, screen, posX, posY, playerSizeX, playerSizeY, color, speed):
        # Call the __init__ method of the base class and pass the position and size parameters
        super().__init__(posX, posY, playerSizeX, playerSizeY)
        self.color = color
        self.speedX = speed
        self.speedY = speed
        self.screen = screen
    # Override the __str__ method to change how the custom class is printed
    def __str__(self):
        return f"Player({self.x}, {self.y}, {self.width}, {self.height}, {self.color}, {self.speed}, {self.angle})"
    #define a custom method that draws the ball on the screen
    def draw(self, screen):
        # Use pygame.draw.ellipse to draw a circle using the rect and color attributes of self
        pygame.draw.rect(screen, self.color, self)

    # Define a custom method that updates the position and direction of the ball
    def update(self, ball):
        self.keepWithinBounds()
    def keepWithinBounds(self):
        if self.y <= 0:
            self.y =0
        if self.y + self.height >= self.screen.get_height():
            self.y = self.screen.get_height() - self.height
