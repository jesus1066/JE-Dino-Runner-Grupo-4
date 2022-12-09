
import pygame
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FONT_COLOR = (0, 0, 0)
FONT_SIZE = 30
FONT_STYLE = "freesansbold.ttf"

def draw_message_component(
    message,      #mesaje 
    screen,       #la pantalla
    font_color = FONT_COLOR,  #el color de la fuente
    font_size = FONT_SIZE,    #tamaño de la fuente
    pos_y_center = SCREEN_HEIGHT  // 2,   #las posiciones en x y y
    pos_x_center = SCREEN_WIDTH  // 2,

):
    font = pygame.font.Font(FONT_STYLE, font_size)
    text = font.render(message, True, font_color)
    text_rect = text.get_rect()
    text_rect.center = (pos_x_center, pos_y_center)
    screen.blit(text, text_rect)  #imprimir el mensaje en la pantalla