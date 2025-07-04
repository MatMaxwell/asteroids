import random

from circleshape import *
from constants import *

class Asteroid(CircleShape):
    # Initialize as a Circle shape
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        # Load and scale image
        self.original_image = pygame.image.load("assets/Asteroid.png").convert_alpha()

        scale_factor = 3
        diameter = int(self.radius * 2 * scale_factor)
        self.original_image = pygame.transform.scale(self.original_image, (diameter, diameter))

        # Image used for rendering (rotated if needed)
        self.image = self.original_image
        self.rect = self.image.get_rect(center=self.position)

        self.angle = random.uniform(0, 360)
        self.spin = random.uniform(-60, 60)

    def draw(self, screen):
        # Update rect center each frame in case of movement
        self.rect = self.image.get_rect(center=self.position)
        screen.blit(self.image, self.rect)

    def update(self, dt):
        self.position += self.velocity * dt

        # Rotate image
        #self.angle += self.spin * dt
        #self.image = pygame.transform.rotate(self.original_image, self.angle)

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
        