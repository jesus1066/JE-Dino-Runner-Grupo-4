import random 
import pygame
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.shield import Shield

class PowerUpManager:            #Esta clase sera para definir en que momento queremos que aparescan los escudos
    def __init__(self):          #constructor 
        self.power_ups = []      #Lista de power_ups vacia
        self.when_appears = 0    #para que aparezcan al inicio sera un 0
    
    def generate_power_up(self, current_score):      #Pasamos el score para tener un punto de partida y un punto medio para recien comenzar a generar los power_up
        if len(self.power_ups) == 0 and self.when_appears == current_score:          #condicion para que no hayga ningun power_up dentro de la lista de power_up
            power = random.randint(1 , 2)        #una variable power igual a un rango randomico de 1 a 2
            if (power == 1 ):                    #si es 1  generara un escudo
                self.power_ups.append(Shield())
                self.when_appears = random.randint(self.when_appears + 300, self.when_appears + 400)   #Cada 300 o 400 puntos aumentaremos un power_up (la suma de cada uno a lo largo del juego se aumentara )
            elif power == 2:                     #si es 2 generara un marillo
                self.power_ups.append(Hammer())
                self.when_appears = random.randint(self.when_appears + 100, self.when_appears + 200)
                
    
    def update(self, current_score, game_speed, player):
        self.generate_power_up(current_score)     #genere un power_up pero primero valida si tenemos power_ups
        for power_up in self.power_ups:           #iteramos los power_up sacamos de nuestralista
            power_up.update(game_speed, self.power_ups)    #Para que el power_up se actualize y se valla moviendo, la lista para que salga de la pantalla
            if player.dino_rect.colliderect(power_up.rect):  #condicionamos si el jugador tiene una colicion directa con nuestro power up
                power_up.start_time = pygame.time.get_ticks()  #(Generamos el tiempo actual) inicializamos el tiempo en el que se esta
                player.shield = True                           #El escudo esta en true
                player.hammer = True
                player.show_text = True                        #True para que muestre el texto
                player.type = power_up.type                    #cambiamos el tipo al tipo que tiene el power up que tiene generado
                time_random = random.randint (5, 8)            #Le definimos un tiempo para que se mantenga el escudo entre un rango de 5 a 7 segundos
                player.shield_time_up = power_up.start_time +(time_random * 1000)  #Le asignamos el tiempo que le dimos y le multiplicamos por que es en segundos
                self.power_ups.remove(power_up)          #Removemos lo que chocamos con el powerup
        
    
    def draw(self, screen): #Dibujamos
        for power_up in self.power_ups:          
            power_up.draw(screen)                #Dibujamos el power_up que tengamos
    
    def reset_power_ups(self):                   #Esto solo sirve cuando inica el juego
        self.power_ups = []                     #para vaciar nuestra lista
        self.when_appears = random.randint(300, 400)   #Reinicamos el tiempo en el que apareceran nuestras listas

