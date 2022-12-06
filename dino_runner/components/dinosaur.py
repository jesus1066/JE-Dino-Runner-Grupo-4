import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import  JUMPING, DUCKING, RUNNING


class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    JUMP_VELOCITY = 8.5
    Y_POS_DUCK = 340

    def __init__(self):
        self.image = RUNNING[0]   
        self.dino_rect = self.image.get_rect() #get_rect devuelve las posiciones del dinosaurio
        self.dino_rect.x = self.X_POS          #Sobre escribimos en la posicion x que le asignamos 
        self.dino_rect.y = self.Y_POS          #Sobre escribimos en la posicion y que le asignamos
        self.jump_velocity = self.JUMP_VELOCITY
        self.step_index = 0
        self.running = True
        self.jumping = False
        self.dino_duck =False


    def update(self, user_input):
        if self.running:
           self.run()
        elif self.jumping:
            self.jump()
        elif self.dino_duck:
            self.duck()

        if user_input[pygame.K_UP] and not self.jumping:
            self.jumping = True
            self.running = False
        elif not self.jumping:
            self.running = True

        if user_input[pygame.K_DOWN] and not self.jumping:
            self.dino_duck= True
            self.running = False
            self.jumping = False
        elif not self.jumping:
            self.running = True
            self.dino_rect.x = self.X_POS
            self.dino_rect.y = self.Y_POS

        if self.step_index >= 10:
            self.step_index = 0 #si pasa index pasa los 10 se resetea a 0 y se vueve a comenzar
    
    def run (self):
         self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1] #operacion ternaria si el index se cumple se asigna RUNNING[0] caso contrario RUNNING[1]
         self.step_index += 1 #variable aux para aumentar
    
    def jump(self):
        self.image = JUMPING
        self.dino_rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.dino_rect.y = self.Y_POS
            self.jumping = False
            self.jump_velocity = self.JUMP_VELOCITY
    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1] #operacion ternaria si el index se cumple se asigna RUNNING[0] caso contrario RUNNING[1]
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1 #variable aux para aumentar

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))  #(blit)Ayuda a dibujar cosas luego pasamos donde quiero que me lo dibuje priemro en x y luego en y
                                                                       