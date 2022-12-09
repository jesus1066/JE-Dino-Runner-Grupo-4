
import random
from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH

class PowerUp(Sprite):                    #Inicializamos con un Sprite para poder interactuar
    def __init__(self, image, type):
        self.image = image                     #Insertar la imagen
        self.rect = self.image.get_rect()      #Sacar la posicion
        self.type =type                        #El tipo
        self.rect.y = random.randint(100, 150)    #Se va a generar en una altura que tendra un rango de 100 a 150
        self.rect.x = SCREEN_WIDTH + random.randint(800, 1000)    # que se genere en la pantalla en un cierto rango al final de la pantalla
        self.start_time = 0                       #El tiempo se inicia en 0 para que tenga un cierto tiempo al agarrar el escudo
    
    def update(self, game_speed, power_ups):     #power_ups para que genere en todos los obstaculos
        self.rect.x -= game_speed                #Que se mueva en la posicion x hacia la izquierda
        if self.rect.x < -self.rect.width:     # Si la posicion en x es menor a la posicion negativa de la pantalla
           power_ups.pop()                      # Si se cumple Desaparece el escudo

    def draw(self, screen):
        screen.blit(self.image, self.rect)     #para pintar


