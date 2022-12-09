from pygame import Surface
from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH 


class Obstacle(Sprite): #Clase base 
    def __init__(self, imagenes: list[Surface], type): #recivimos imagenes y el type el tipo de image
        self.images = imagenes
        self.type = type
        self.rect = self.images[self.type].get_rect()  #Lista de imagenes cada lsiat sera un surface
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles: list): #game_speed contiene la velocidad del juego, obstacles=lista de obstaculos
        self.rect.x -= game_speed                  #moddificamos la posicion en x de nuestra recta
        if self.rect.x <= -self.rect.width:        #la posicion en x sea menos o igual al ancho de nuestra imagen (esta en negativo por que nos interesa que el ancho de nuestra imagen por muy pequeña que sea tiene q cumplir la condicion )
            obstacles.pop()                        #pop remueve el ultimo elemento de la lista de obstaculos
        
    def draw(self, screen: Surface):
        screen.blit(self.images[self.type], (self.rect.x, self.rect.y))