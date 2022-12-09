from pygame import Surface
from pygame.sprite import Sprite
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD, SCREEN_WIDTH

class Brid(Sprite):
    
    def __init__(self, Y_POS_BIRD):
        self.images = BIRD[0]
        self.rect = self.images.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = Y_POS_BIRD
        self.step_index = 0
    
    def update(self, game_speed, obstacles: list):
        self.run()
        self.rect.x -= game_speed                  #moddificamos la posicion en x de nuestra recta
        if self.rect.x <= -self.rect.width:        #la posicion en x sea menos o igual al ancho de nuestra imagen (esta en negativo por que nos interesa que el ancho de nuestra imagen por muy pequeña que sea tiene q cumplir la condicion )
            obstacles.pop()
        

    def run(self):
        self.images = BIRD[0] if self.step_index < 5 else BIRD[1] #operacion ternaria si el index se cumple se asigna RUNNING[0] caso contrario RUNNING[1]
        self.step_index += 1 
        if self.step_index >= 10:
            self.step_index = 0
        
    def draw(self, screen: Surface):
        screen.blit(self.images, (self.rect.x, self.rect.y))
