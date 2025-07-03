import random

from circleshape import *
from constants import *

class Asteroid(CircleShape):
    #Initialize as a Circle shape
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen,"green", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()  # Remove the current (large) asteroid

        # Don't split if too small
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Generate random split angle between 20 and 50 degrees
        angle = random.uniform(20, 50)

        # Create two new velocity vectors by rotating the original velocity
        velocity1 = self.velocity.rotate(angle) * 1.2
        velocity2 = self.velocity.rotate(-angle) * 1.2

        # Compute new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new asteroids at the current position
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid1.velocity = velocity1
        asteroid2.velocity = velocity2

        # You must add these new asteroids to your game's asteroid group manually
        return [asteroid1, asteroid2]
        
        