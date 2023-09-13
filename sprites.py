import pygame
from settings import *

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image = pygame.Surface([BIRD_WIDTH, BIRD_HEIGHT])
        self.original_image = pygame.image.load('bird.jpg').convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (BIRD_WIDTH, BIRD_HEIGHT))
        self.image = self.original_image.copy()  # This creates a copy of the original image for rotation
        # self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = BIRD_START_X
        self.rect.y = BIRD_START_Y
        self.y_speed = 0

    def update(self, game_started=False):
        if game_started:
            # Add gravity to the bird
            self.y_speed += GRAVITY
            self.rect.y += self.y_speed
            
            if self.y_speed < 0:
                self.image = pygame.transform.rotate(self.original_image, 20)
            elif self.y_speed > 0:
                self.image = pygame.transform.rotate(self.original_image, -20)
            else:
                self.image = pygame.transform.rotate(self.original_image, 0)
                
            # Set the colorkey for transparency after rotation
            self.image.set_colorkey((255, 255, 255))
            
    def flap(self):
        self.y_speed = BIRD_JUMP_HEIGHT


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, is_upper):
        super().__init__()
        
        if is_upper:
            self.image = pygame.Surface([PIPE_WIDTH, y])
            self.rect = self.image.get_rect()
            self.rect.bottomleft = (x, y)
        else:
            self.image = pygame.Surface([PIPE_WIDTH, WINDOW_HEIGHT - y])
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
        
        self.image.fill(GREEN)
        
    def update(self, game_started=False):
        if game_started:
            self.rect.x -= PIPE_SPEED


