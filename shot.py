from circleshape import *
from constants import *
from player import *

class Shot(CircleShape):
    def __init__(self,x,y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt
        return self.position
