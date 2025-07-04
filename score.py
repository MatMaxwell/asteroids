import pygame

class Score():
    

    def __init__(self):
        self.score = 0
        
    def display_score(self,screen, x, y):
        pygame.font.init()
        font = pygame.font.Font("freesansbold.ttf", 80) 
        score_img = font.render(f"SCORE: {str(self.score)}", True, [255,255,255])
        screen.blit(score_img, (x,y))
        
        
        