from dino_runner.utils.constants import SHIELD, SHIELD_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Shield(PowerUp):   #Clse para darle la imagen al powerup
    def __init__(self):
        self.image = SHIELD   #Imagen del escudo
        self.type = SHIELD_TYPE   #El tipo de powerup que sera 
        super().__init__(self.image, self.type)   #un super para inicializar la clase padre con los valores que le dimos en init self.image, self.type

