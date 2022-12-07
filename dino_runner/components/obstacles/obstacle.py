from pygame import Surface
from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH


class Obstacle(Sprite):
    def __init__(self, imagenes: list[Surface], type): #recivimos imagenes y el type el tipo de image
        self.images = imagenes
        self.type = type
        self.rect = self.images[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles: list):
        self.rect.x -= game_speed
        if self.rect.x <= -self.rect.width:
            obstacles.pop() #pop remueve el ultimo elemento de la lista
        

    def draw(self, screen: Surface):
        screen.blit(self.images[self.type], (self.rect.x, self.rect.y))