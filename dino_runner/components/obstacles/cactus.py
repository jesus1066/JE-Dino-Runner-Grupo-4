
from pygame import Surface
from random import randint   #randint genera un número entero de forma aleatoria entre un rango

from dino_runner.components.obstacles.obstacle import Obstacle

class Cactus(Obstacle):
    Y_POS_LARGE_CACTUS = 325     #constante de la posicion en y donde queremos que este el cactus
    Y_POS_SMALL_CACTUS = 325
    def __init__(self, imagenes: list[Surface]):
        super().__init__(imagenes, randint (0,2)) #super inite le decimos que dibuje en la posicion y el cactus y que se genere de manera alatoria 0,1,2 las imagenes
        self.rect.y = self.Y_POS_LARGE_CACTUS 
        self.rect.y = self.Y_POS_LARGE_CACTUS
