from circleshape import *
from constants import *

class Shot(CircleShape):
    #Initialize as a Circle shape
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        
    def draw(self, screen):
        pygame.draw.circle(screen,"yellow", self.position, self.radius, 0)
        
    def update(self, dt):
        self.position += self.velocity * dt