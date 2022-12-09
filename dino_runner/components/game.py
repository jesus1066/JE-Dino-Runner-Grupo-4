import pygame

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.player_hearts.player_heart_manager import PlayerHeartManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.score import Score
from dino_runner.utils.constants import BG, DINO_DEAD, DINO_START, FORNT_STYLE, GAME_OVER, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.utils.texr_utils import draw_message_component

INITIAL_GAME_SPEED = 20

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = INITIAL_GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.player_heart_manager = PlayerHeartManager()
        self.power_up_manager = PowerUpManager()
        self.score = Score()
        self.death_count = 0
      

        self.executing = False
    
    def execute(self):   #otro punto de inicio
        self.executing = True
        while self.executing: # se ejecuta mientras el juego este corriendo 
            if not self.playing:  #y si no mostramos el menu 
                self.show_menu()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.score.current_score = 0
        self.initialize_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()
    
    def initialize_game(self): #Metodo para resetear
        #self.obstacle_manager.reset_obstacles() #para reseterar los obstaculos cuando pierda
        #self.score.current_score = 0                  #Resetemos el score
        self.game_speed = INITIAL_GAME_SPEED         #Resetemos la velocidad
        self.player_heart_manager.reset_heart_count() #Reseteamos los corazones
        #self.power_up_manager.reset_power_ups()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False

    def update(self):
        user_input = pygame.key.get_pressed() #de pygame (key)el modulo tecla.(get_pressed) nos devuelva la tecla presionada
        self.player.update(user_input)   #le pasamos al metodo update de nuestra clase dinosaur
        self.obstacle_manager.update(self) #llamamos para que se actualize los obstaculos 
        self.score.update(self)
        self.power_up_manager.update(self.score.current_score, self.game_speed, self.player) #Para actualizar el power_up

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen) #despues de que se dibuja le pasamos el screen
        self.player.check_power_up(self.screen)
        self.obstacle_manager.draw(self.screen) #hacemos que se dibujen los obstaculos
        self.score.draw(self.screen)  #Dibujar el score   (Lo que esta en parentesis, es para pasarle la pantalla, (self, screen))
        self.player_heart_manager.draw(self.screen) #Para dibujar los corazones
        self.power_up_manager.draw(self.screen)  #Actualizamos la pantalla
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        pass

    def show_menu(self):
        #Poner color al fondo*
        self.screen.fill((0,221,221))
        half_screen_width = SCREEN_WIDTH // 2  
        half_screen_height = SCREEN_HEIGHT // 2
        #Mostrar mensaje de inicio
        if self.death_count == 0:
            self.screen.blit(DINO_START, (half_screen_width - 20, half_screen_height -140))
            draw_message_component("Press any key to start", self.screen)
            
        else:
            self.screen.fill((83,0,0))
            #Mostrar mensaje de reinicio
            self.screen.blit(GAME_OVER, (half_screen_width -175 , half_screen_height -200))
            self.screen.blit(DINO_DEAD, (half_screen_width - 20, half_screen_height -140))
            draw_message_component(" Press any key to restart the game", self.screen)
        
            #Mostrar los puntos obtenidos
            draw_message_component(
                f"Your Score: {self.score.current_score}", 
                self.screen,
                pos_y_center = half_screen_height + 100
                )
            #Mostrar muertes totales
            draw_message_component(
                f"Number of deaths: {self.death_count}", 
                self.screen,
                pos_y_center = half_screen_height + 150
                )

        #Mostrar imagen como icono
        #self.screen.blit(DINO_START, (half_screen_width - 20, half_screen_height -140)) #movemos la imagen que queremos que aparezca para que no se solapen con el centro
        #Actualizar pantalla
        pygame.display.flip()
        #Manejar eventos
        self.handle_menu_events()

    def handle_menu_events(self):
        for event in pygame.event.get():                 #iteramos sobre los eventos
            if event.type == pygame.QUIT:                #si se salio, salimos de todo
                self.playing = False       
                self.executing = False
            elif event.type == pygame.KEYDOWN:           #si no tratamos de ver de que tipo es el vento si es igual a cualquier tecla precionda hacemos correr el run (el juego)
                self.run()



    



   
            

    
    
    
