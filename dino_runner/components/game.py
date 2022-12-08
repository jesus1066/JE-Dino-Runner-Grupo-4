import pygame

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.score import Score
from dino_runner.utils.constants import BG, DINO_START, FORNT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.score = Score()
        self.death_count = 0
        self.total_score=0        

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
        self.obstacle_manager.reset_obstacles() #para reseterar los obstaculos cuando pierda
        self.score.reset_score()
        self.reset_scores()
        while self.playing:
            self.events()
            self.update()
            self.draw()

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

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen) #despues de que se dibuja le pasamos el screen
        self.obstacle_manager.draw(self.screen) #hacemos que se dibujen los obstaculos
        self.score.draw(self.screen)
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
        self.screen.fill((255,255,255))
        half_screen_width = SCREEN_WIDTH // 2  
        half_screen_height = SCREEN_HEIGHT // 2
        #Mostrar mensaje de inicio
        if not self.death_count:
            font = pygame.font.Font(FORNT_STYLE, 30) #nombre de la fuente y el tamaño
            message = font.render('press any key to start', True, (0, 0, 0)) #render nos permite pasar cual str que queramos 
            message_rect = message.get_rect()
            message_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(message, message_rect)
        else:
            #self.mensaje()
            self.number_deaths()
            
        #Mostrar imagen como icono
        self.screen.blit(DINO_START, (half_screen_width - 20, half_screen_height -140)) #movemos la imagen que queremos que aparezca para que no se solapen con el centro
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
    def number_deaths(self):
        self.screen.fill((255,255,255))
        half_screen_width = SCREEN_WIDTH // 2  +10

        if self.death_count > 0:
            font = pygame.font.Font(FORNT_STYLE, 30) #nombre de la fuente y el tamaño
            text = font.render('press any key to restart the game', True, (0, 0, 0)) 
            messages = font.render(f'Your Score: {self.total_score}', True, (0, 0, 0))
            message = font.render(f'number of deaths: {self.death_count}', True, (0, 0, 0)) #render nos permite pasar cual str que queramos 
            message_recto = text.get_rect()
            message_rect = message.get_rect()
            messages_rect = messages.get_rect()
            message_recto.center = (SCREEN_WIDTH // 2+10, SCREEN_HEIGHT//2)
            messages_rect.center = (half_screen_width, SCREEN_HEIGHT // 2 +100)
            message_rect.center = (half_screen_width, SCREEN_HEIGHT // 2 +130)
            self.screen.blit(text, message_recto)
            self.screen.blit(messages, messages_rect)
            self.screen.blit(message, message_rect)
            
    def reset_scores(self):
        self.total_score = 0

   # def mensaje(self):
    #    self.screen.fill((255,255,255))
     #   half_screen_width = SCREEN_WIDTH // 2  
      #  half_screen_height = SCREEN_HEIGHT // 2
       # font = pygame.font.Font(FORNT_STYLE, 30) 
        #text = font.render('press any key to restart the game', True, (0, 0, 0)) 
        #message_recto = text.get_rect()
        #message_recto.center = (half_screen_width, half_screen_height)
        #self.screen.blit(text, message_recto)

    



   
            

    
    
    
