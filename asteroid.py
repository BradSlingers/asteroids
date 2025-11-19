from circleshape import *
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt
        return self.position
    
    def split(self):
        vel = self.velocity
        radi = self.radius
        x = self.position.x
        y = self.position.y

        self.kill()
        if radi <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        first_new_vec = vel.rotate(angle)
        second_new_vec = vel.rotate(-angle)
        new_rad = radi - ASTEROID_MIN_RADIUS

        first_roid = Asteroid(x,y,new_rad)
        second_roid = Asteroid(x,y, new_rad)
        first_roid.velocity = first_new_vec * 1.2
        second_roid.velocity = second_new_vec * 1.2
       

        
