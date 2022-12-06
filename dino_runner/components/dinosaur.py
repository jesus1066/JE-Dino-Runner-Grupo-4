import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import  RUNNING


class Dinosaur(Sprite):
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = 80
        self.dino_rect.x = 310
        self.jump_velocity = 8.5
        self.step_index = 0

        self.running = True
        self.jumping = True


    def update(self, user_input):
        if self.running:
            self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
            self.step_index += 1
        elif self.jumping:
            self.image = JUMPING
            self.dino_rect.y -= self.jump_velocity * 4


        if user_input[pygame.K_UP] and not self.jumping:
            self.jumping = True
            self.running = False
        elif not self.jumping:
            self.running = True

        if self.step_index >= 10:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))