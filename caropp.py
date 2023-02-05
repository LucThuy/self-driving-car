import random
import math
import pygame

WIDTH = 1920
HEIGHT = 1080

CAR_SIZE_X = 60
CAR_SIZE_Y = 60

BORDER_COLOR = (255, 255, 255, 255)

SPEED = 5

class Caropp:
    def __init__(self):
        self.sprite = pygame.image.load('carbot.png').convert()
        self.sprite =  pygame.transform.scale(self.sprite, (CAR_SIZE_X, CAR_SIZE_Y))
        self.rotated_sprite = self.sprite

        self.position = [830, 920]
        self.angle = 0
        self.speed = SPEED

        self.center = [self.position[0] + CAR_SIZE_X/2, self.position[1] + CAR_SIZE_Y/2]

        self.alive = True

    def draw(self, screen):
        screen.blit(self.sprite, self.position)

    def check_collision(self, game_map, carbots):
        self.alive = True
        for point in self.corners:
            if game_map.get_at((int(point[0]), int(point[1]))) == BORDER_COLOR:
                self.alive = False
            for carbot in carbots:
                if carbot.is_alive():
                    if int(point[0]) >= int(carbot.center[0]) - CAR_SIZE_X / 2 and int(point[0]) <= int(carbot.center[0]) + CAR_SIZE_X / 2:
                        if int(point[1]) >= int(carbot.center[1]) - CAR_SIZE_Y / 2 and int(point[1]) <= int(carbot.center[1]) + CAR_SIZE_Y / 2:
                            self.alive = False
                            break
            if self.alive == False:
                break

    def update(self, game_map, carbots):
        self.rotated_sprite = self.rotate_center(self.sprite, self.angle)

        self.position[0] += math.cos(math.radians(360 - self.angle)) * self.speed
        self.position[0] = max(self.position[0], 20)
        self.position[0] = min(self.position[0], WIDTH - 120)

        self.position[1] += math.sin(math.radians(360 - self.angle)) * self.speed
        self.position[1] = max(self.position[1], 20)
        self.position[1] = min(self.position[1], HEIGHT - 120)

        self.center = [int(self.position[0]) + CAR_SIZE_X / 2, int(self.position[1]) + CAR_SIZE_Y / 2]

        length = 0.5 * CAR_SIZE_X
        left_top = [self.center[0] + math.cos(math.radians(360 - (self.angle + 30))) * length, self.center[1] + math.sin(math.radians(360 - (self.angle + 30))) * length]
        right_top = [self.center[0] + math.cos(math.radians(360 - (self.angle + 150))) * length, self.center[1] + math.sin(math.radians(360 - (self.angle + 150))) * length]
        left_bottom = [self.center[0] + math.cos(math.radians(360 - (self.angle + 210))) * length, self.center[1] + math.sin(math.radians(360 - (self.angle + 210))) * length]
        right_bottom = [self.center[0] + math.cos(math.radians(360 - (self.angle + 330))) * length, self.center[1] + math.sin(math.radians(360 - (self.angle + 330))) * length]

        self.corners = [left_top, right_top, left_bottom, right_bottom]

        self.check_collision(game_map, carbots)