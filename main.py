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
from button import *

#Initialize the game engine
pygame.init()

#Set up the screen varibale
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Backgrounds for the Menu and Game
MenuBG = pygame.image.load("assets/Background.png")
GameBG = pygame.image.load("assets/gameBG.png")

#Initialize Score 
score = Score()
fontX = 15
fontY = 15

def play():
    
    #Set caption at top
    pygame.display.set_caption("Game")
    
    #Create a tick rate and delta time for the game
    fps = pygame.time.Clock()
    dt = 0
    
    #score to zero or back to zero
    score.score = 0
    
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
    
    #Player Containers
    Player.containers = (updatable, drawable)
    player = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)
    
    #Start the gaming loop
    running = True
    while running:
        #Exiting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.blit(GameBG, (0, 0))
        updatable.update(dt)
        player.timer -= dt
        
        #This if asteroid collides with player
        for objects in asteroids:
            if objects.collides_with(player):
                game_over()
        
        #It shot collides with asteroid    
        for asteroid in list(asteroids):
            for shot in list(shots):
                if asteroid.collides_with(shot):
                    if asteroid.alive() and shot.alive():
                        score.score += 10
                        asteroid.split()
                        shot.kill()
        
        #Draw all things that are drawable            
        for thing in drawable:
            thing.draw(screen)
        
        #Display the score    
        score.display_score(screen, fontX, fontY)
        
        #Updates entire screen
        pygame.display.flip()
        
        #FPS and Delta Time
        tick = fps.tick(144)
        dt = tick / 1000

def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

def main_menu():
    pygame.display.set_caption("Menu")
    
    while True:
        screen.blit(MenuBG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("ASTEROIDS", True, "#ff0000")
        MENU_RECT = MENU_TEXT.get_rect(center=(960, 300))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(960, 500), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(960, 650), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def game_over():
    pygame.display.set_caption("Menu")
    while True:
        screen.blit(MenuBG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("GAMEOVER", True, "#ff0000")
        MENU_RECT = MENU_TEXT.get_rect(center=(960, 300))
        
        SCORE_TEXT = get_font(32).render(f"SCORE: {score.score}", True, "#ffffff")
        SCORE_RECT = SCORE_TEXT.get_rect(center=(960, 450))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(960, 650), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(960, 800), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)
        screen.blit(SCORE_TEXT, SCORE_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
    
main_menu()
