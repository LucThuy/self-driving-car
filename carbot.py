import random

import pygame

WIDTH = 1920
HEIGHT = 1080

CAR_SIZE_X = 60
CAR_SIZE_Y = 60

SPEED = 5

class Carbot:
    def __init__(self):
        self.sprite = pygame.image.load('carbot.png').convert()
        self.sprite =  pygame.transform.scale(self.sprite, (CAR_SIZE_X, CAR_SIZE_Y))

        self.position = [random.randint(6, 6)*100 + 1000, 1000]
        self.speed = SPEED

        self.alive = True

        self.center = [self.position[0] + CAR_SIZE_X/2, self.position[1] + CAR_SIZE_Y/2]

    def draw(self, screen):
        screen.blit(self.sprite, self.position)

    def check_collision(self, game_map):
        self.alive = True
        if self.center[1] <= 100:
            self.alive = False
    
    def update(self, game_map):
        self.position[1] -= self.speed
        self.position[1] = max(self.position[1], 20)
        self.position[1] = min(self.position[1], HEIGHT - 120)

        self.center = [int(self.position[0]) + CAR_SIZE_X / 2, int(self.position[1]) + CAR_SIZE_Y / 2]

        self.check_collision(game_map)

    def is_alive(self):
        return self.alive