
from pygame import Surface
from random import randint

from dino_runner.components.obstacles.obstacle import Obstacle

class Cactus(Obstacle):
    Y_POS_LARGE_CACTUS = 300
    
    def __init__(self, imagenes: list[Surface]):
        super().__init__(imagenes, randint (0,2))
        self.rect.y = self.Y_POS_LARGE_CACTUS