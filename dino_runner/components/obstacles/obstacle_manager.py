from random import randint
import pygame
from dino_runner.components.obstacles import brid
from dino_runner.components.obstacles.brid import Brid
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import HAMMER_TYPE
from dino_runner.utils.texr_utils import draw_message_component
#from dino_runner.utils.constants import BIRD


class ObstacleManager:  #manegador de obstaculos
    Y_POS_BIRD =255
    #Y_POS_BIRD =300 Tamaño para que el pajaro este abajo
    def __init__(self):
        self.obstacles: list[Obstacle]= []

    def update (self, game):
        if len(self.obstacles) == 0:
            option = randint (0,2)
            if option == 0:     #si el numero quenerado dentro de un rango es igual a 0 se añade un cactus largo
                self.obstacles.append(Cactus("LARGE"))
            elif option == 1:   #si el numero quenerado dentro de un rango es igual a 1 se añade un cactus pequeño
                self.obstacles.append(Cactus("SMALL")) 
            elif option == 2:
              self.obstacles.append(Brid(self.Y_POS_BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if  game.player.dino_rect.colliderect(obstacle.rect) and game.player.type == HAMMER_TYPE:   # si es dino coliciona con un objeto y es igual a la imagen del martillo
                    self.obstacles.pop()
            elif not game.player.shield:        #Si el jugador tiene el escudo ingnora todo los obstaculos
                if game.player.dino_rect.colliderect(obstacle.rect):         #Si el player dino hace una colicion directa con algun obstaculo el juego se acaba
                    game.player_heart_manager.reduce_heart_count()           #Dela clase game llamamos a la clase player_heart_manager y entramos al metodo reduce_heart_count() para reducir las vidas
                    if game.player_heart_manager.heart_count > 0:     #Preguntamos si el contador de corazones es mayor a 0
                        self.obstacles.pop()                                 #Eliminamos el ultimo obstaculo que estaba
                    else:                                                    #caso contrario se acaba el juego
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count += 1
    
    def draw(self, screen):
        for obstacle in self.obstacles:   #iteramos entre nuestros obstaculos
            obstacle.draw(screen)         #dibujamos
    
    def reset_obstacles(self):
        self.obstacles = []