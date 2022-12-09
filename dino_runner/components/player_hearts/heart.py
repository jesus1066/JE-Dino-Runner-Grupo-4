from dino_runner.utils.constants import HEART

class Heart:
    def __init__(self, x_position, y_position):
        self.image = HEART                   #importamos la imagen
        self.rect = self.image.get_rect()   

        self.rect.x = x_position            #imagen en posicion x,y
        self.rect.y = y_position

    def draw(self, screen):
        screen.blit(self.image, self.rect)   #dibujamos la imagen