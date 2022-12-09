from dino_runner.components.player_hearts.heart import Heart

DEFAULT_HEART_COUNT = 3

class PlayerHeartManager:
    def __init__(self):
        self.heart_count = DEFAULT_HEART_COUNT    #contador  de corazones 

    def reduce_heart_count(self):  #Metodo para reducir los corazones
        self.heart_count -= 1

    def draw(self, screen):     
        x_position = 10         #Posicion del corazon y valor
        y_position = 20

        for counter in range(self.heart_count):    #Para que los corazones se renderize, en el rando de los corazones que tenemos
            heart = Heart(x_position, y_position)  #Use la clase corazon para rederizar la imagen en x , y
            heart.draw(screen)                     #Para que se dibuje el corazon
            x_position += 30                       #Para que no se solapen y se pongan al ladito 

    def reset_heart_count(self):          #Metodo para resetear cuando reiniciemos el juego   
        self.heart_count = DEFAULT_HEART_COUNT