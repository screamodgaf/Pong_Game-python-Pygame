from player import Player

class Enemy(Player):
    def update(self, ball):
        #move enemy basing on ball's y position
        if ball.y + ball.height/2 < self.y:
            self.y -= self.speedY
        elif ball.y -  ball.height/2 > self.y:
            self.y += self.speedY

        self.keepWithinBounds()
