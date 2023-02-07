import pygame
import config
import math


class Tank:

    def __init__(self, image, coord, angle):
        self.tank = pygame.image.load(image)
        self.tank = pygame.transform.scale(self.tank, (50, 50))
        self.coord = coord
        self.x = coord[0]
        self.y = coord[1]
        self.angle = angle

    def move(self):
        self.x += config.tank_move_speed * math.cos(self.angle)
        self.y += config.tank_move_speed * math.sin(self.angle)

    def turn(self, direction):
        self.angle += direction

    def draw(self, screen):
        screen.blit(self.tank, self.coord)
        pygame.transform.rotate(self.tank, self.angle)


class Shot:
    def __init__(self, coord, angle, size):
        self.ball = pygame.rect.Rect((coord[0], coord[1], size[0], size[1]))
        self.color = 'white'
        self.coord = coord
        self.x = coord[0]
        self.y = coord[1]
        self.angle = angle

    def move(self):
        self.x += config.shot_speed * math.cos(self.angle)
        self.y += config.shot_speed * math.sin(self.angle)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.ball)