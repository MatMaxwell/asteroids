import pygame


from circleshape import *
from constants import *
from shot import *


class Player(CircleShape):
    #Initialize as a Circle shape, and create rotation var
    def __init__(self, x, y, shots_group):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.shots_group = shots_group
        
    
    #Class to draw a triangle
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    #This will draw the player which is a triangle
    def draw(self, screen):
        pygame.draw.polygon(screen, "red", self.triangle(), 2 )
    
    #This will rotate the triangle   
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    #This will move the player    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt    
    
    #Based on the key we will call rotate or move   
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()
            
        
    def shoot(self):
        
        shot = Shot(self.position.x, self.position.y)  
        
        velocity = pygame.Vector2(0, 1)  
        velocity = velocity.rotate(self.rotation) 
        velocity = velocity * PLAYER_SHOOT_SPEED  
        
        shot.velocity = velocity
        
        self.timer = PLAYER_SHOOT_COOLDOWN
        
        self.shots_group.add(shot)
        

        
            
        
        
    
        
        
        
        
