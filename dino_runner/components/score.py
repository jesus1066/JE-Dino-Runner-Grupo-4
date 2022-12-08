import pygame

from dino_runner.utils.constants import FORNT_STYLE

class Score:
    def __init__(self):
        self.current_score = 0

    def update(self, game):
        self.current_score += 1
        if self.current_score % 100 == 0:  #por cada 100 puntos se incrementera la velocidad en +2
            game.game_speed += 2

    def draw(self, screen):
        font = pygame.font.Font(FORNT_STYLE, 22) #nombre de la fuente y el tamaño
        message = font.render(f'Score: {self.current_score}', True, (0, 0, 0)) #render nos permite pasar cual str que queramos 
        message_rect = message.get_rect()
        message_rect.center = (1000, 50)
        screen.blit(message, message_rect)