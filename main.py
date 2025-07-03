# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from score import *

def main():
    
    #Initialize the game engine
    pygame.init()
    
    #Set the screen variable to be drawn
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #Initialize Score and Display it
    score = Score()
    fontX = 15
    fontY = 15
    
    
    #Create a tick rate and delta time for the game
    fps = pygame.time.Clock()
    dt = 0
    
    #Divide things into groups for organization
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    #Asteroid containers
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    
    #Asteroid Field
    AsteroidField.containers = (updatable,)
    asteroidfield = AsteroidField()
    
    #Shot Containers
    shots = pygame.sprite.Group()
    Shot.containers = (updatable, drawable)
    
    Player.containers = (updatable, drawable)
    player = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
    
    #Initialize Score 
    score = Score()
    fontX = 15
    fontY = 15
    
    #Start the gaming loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        updatable.update(dt)
        
        player.timer -= dt
        
        for objects in asteroids:
            if objects.collides_with(player):
                print("Game Over!")
                print(f"SCORE:  {score.score}")
                sys.exit()
                
        for asteroid in list(asteroids):
            for shot in list(shots):
                if asteroid.collides_with(shot):
                    if asteroid.alive() and shot.alive():
                        score.score += 10
                        asteroid.split()
                        shot.kill()
                    
        for thing in drawable:
            thing.draw(screen)
            
        score.display_score(screen, fontX, fontY)
        
        pygame.display.flip()
        
        tick = fps.tick(144)
        dt = tick / 1000

if __name__ == "__main__":
    main()
