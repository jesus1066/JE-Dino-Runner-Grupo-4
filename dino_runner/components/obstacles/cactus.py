from random import randint   #randint genera un número entero de forma aleatoria entre un rango

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS

class Cactus(Obstacle):
    CACTUS = {
        "LARGE": (LARGE_CACTUS, 300),     #constante de la posicion en y donde queremos que este el cactus
        "SMALL": (SMALL_CACTUS, 325),
    }

    def __init__(self, cactus_type):
        images, y_pos = self.CACTUS[cactus_type]
        super().__init__(images, randint (0, 2)) #super inite le decimos que dibuje en la posicion y el cactus y que se genere de manera alatoria 0,1,2 las imagenes
        self.rect.y = y_pos

