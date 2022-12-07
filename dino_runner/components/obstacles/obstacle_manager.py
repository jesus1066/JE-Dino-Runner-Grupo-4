from random import randint
import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager:  #manegador de obstaculos
    def __init__(self):
        self.obstacles: list[Obstacle]= []

    def update (self, game):
        if len(self.obstacles) == 0:
            if randint (0,2) == 0:     #si el numero quenerado dentro de un rango es igual a 0 se añade un cactus largo
                self.obstacles.append(Cactus(LARGE_CACTUS))
            elif randint (0, 2) == 1:   #si el numero quenerado dentro de un rango es igual a 1 se añade un cactus pequeño
                self.obstacles.append(Cactus(SMALL_CACTUS)) 

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
    
    def draw(self, screen):
        for obstacle in self.obstacles:   #iteramos entre nuestros obstaculos
            obstacle.draw(screen)         #dibujamos