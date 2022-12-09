import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import  DEFAULT_TYPE, DUCKING_HAMMER, DUCKING_SHIELD, HAMMER_TYPE, JUMPING, DUCKING, JUMPING_HAMMER, JUMPING_SHIELD, RUNNING, RUNNING_HAMMER, RUNNING_SHIELD, SHIELD_TYPE
from dino_runner.utils.texr_utils import draw_message_component

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER }
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER }
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER }



class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    JUMP_VELOCITY = 8.5
    Y_POS_DUCK = 340 #La posicion en y cuando el Dino se agache

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]   
        self.dino_rect = self.image.get_rect() #get_rect devuelve las posiciones del dinosaurio
        self.dino_rect.x = self.X_POS          #Sobre escribimos en la posicion x que le asignamos 
        self.dino_rect.y = self.Y_POS          #Sobre escribimos en la posicion y que le asignamos
        self.jump_velocity = self.JUMP_VELOCITY
        self.step_index = 0
        self.running = True
        self.jumping = False
        self.dino_duck =False
        self.has_power_up = False #Para verificar si tiene un power_up
        self.shield = False   #La bandera para saber si tiene escudo esta en falso por el momento
        self.shield_time_up = 0 #Tiempo de expiración
        self.show_text = False #Para mostrar el tiempo
        self.hammer = False


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
            self.dino_duck = False

        elif user_input[pygame.K_DOWN] and not self.jumping:
            self.dino_duck= True
            self.running = False
            self.jumping = False
        elif not self.jumping: #si no esta saltando se devuelve que el Dino siga corriendo y las posiciones originales
            self.running = True
            self.dino_duck =False
            self.jumping = False
            
        if self.step_index >= 10:
            self.step_index = 0 #si pasa index pasa los 10 se resetea a 0 y se vueve a comenzar
    
    def run (self):
        self.image = RUN_IMG[self.type][0] if self.step_index < 5 else RUN_IMG[self.type][1] #operacion ternaria si el index se cumple se asigna RUNNING[0] caso contrario RUNNING[1]
        self.step_index += 1 #variable aux para aumentar
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
    
    def jump(self):
        self.image = JUMP_IMG[self.type]
        self.dino_rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.dino_rect.y = self.Y_POS
            self.jumping = False
            self.jump_velocity = self.JUMP_VELOCITY
    def duck(self):
        self.image = DUCK_IMG[self.type][0] if self.step_index < 5 else DUCK_IMG[self.type][1] #operacion ternaria si el index se cumple se asigna RUNNING[0] caso contrario RUNNING[1]
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK #la nuevo posicion en y para que se agache
        self.step_index += 1 #variable aux para aumentar

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))  #(blit)Ayuda a dibujar cosas luego pasamos donde quiero que me lo dibuje priemro en x y luego en y
    
    def check_power_up(self, screen): #Usa la pantalla en la que esta rendelizando para saber si esta con un power_up
        if self.shield:               #Verificamos si tiene el escudo
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks()) /1000, 2)    #Hacemos que  time_to_show redondeamos el tiempo (quitandole el tiempo que tenemos en ese momento) 
            if time_to_show >= 0 and self.show_text:     #Si a un queda tiempo y el text es verdadero
                draw_message_component(                  #Esto creamos para que nos muestre el mensaje
                   f"Shield enabled for: {time_to_show}",
                   screen,
                   font_size = 18,
                   pos_x_center = 500,
                   pos_y_center= 40
                )
            else:
                self.shield = False
                self.type  = DEFAULT_TYPE
    
    def check_power_up_hammer(self, screen): #Usa la pantalla en la que esta rendelizando para saber si esta con un power_up
        if self.hammer:               #Verificamos si tiene el escudo
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks()) /1000, 2)    #Hacemos que  time_to_show redondeamos el tiempo (quitandole el tiempo que tenemos en ese momento) 
            if time_to_show >= 0 and self.show_text:     #Si a un queda tiempo y el text es verdadero
                draw_message_component(                  #Esto creamos para que nos muestre el mensaje
                   f"Shield enabled for: {time_to_show}",
                   screen,
                   font_size = 18,
                   pos_x_center = 500,
                   pos_y_center= 40
                )
            else:
                self.shield = False
                self.type  = DEFAULT_TYPE
                                                        