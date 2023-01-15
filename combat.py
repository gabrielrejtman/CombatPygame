import pygame
from math import *

pygame.init()

# config.py

pygame.init()
score_p1 = 0
score_p2 = 0

screenInf = pygame.display.Info()
screen_size = [screenInf.current_w, screenInf.current_h]
player_1 = pygame.image.load("Player1 - Sprite.png")
player_1_y = screen_size[1] / 2
player_1_x = screen_size[0] + 100 - screen_size[0]
player_2 = pygame.image.load("Player2 - Sprite.png")
player_2_y = screen_size[0] / 3.5
player_2_x = screen_size[1] + 300
game_clock = pygame.time.Clock()
player_size = 60
# colours
Black = (100, 45, 15)
White = (255, 255, 255)
Red = (162, 8, 0)
Green = (0, 127, 33)
Yellow = (197, 199, 37)
Blue = (0, 0, 255)
screen = pygame.display.set_mode(screen_size)
angle_1 = 1
angle_2 = 1.2


def move_p1():
    if event.type == pygame.KEYDOWN:
        global player_1_y, player_1_x, angle_1, player_2_y, player_2_x, angle_2

        if event.key == pygame.K_RIGHT:
            angle_1 += 5 * -1
        if event.key == pygame.K_LEFT:
            angle_1 += 5
        if event.key == pygame.K_UP:
            player_1_y -= 5 * cos(radians(angle_1))
            player_1_x -= 5 * sin(radians(angle_1))
        if event.key == pygame.K_INSERT:
            angle_2 += 5 * -1
        if event.key == pygame.K_PAGEUP:
            angle_2 += 5
        if event.key == pygame.K_HOME:
            player_2_y -= 5 * cos(radians(angle_2))
            player_2_x -= 5 * sin(radians(angle_2))


def limit_borders(players, walls,):
    global player_1_y
    if players <= walls:
        player_1_y = walls


def limit_borders_p2(players, walls):
    global player_2_y
    if players <= walls:
        player_2_y = walls


# player 1 ball
ball_p1 = pygame.image.load("Player1 - Sprite.png")
ball_size = (5, 5)
ball_p1 = pygame.transform.scale(ball_p1, ball_size)
ball_p1_x = 50
ball_p1_y = 150
ball_p1_dx = 1
ball_p1_dy = 1

# player 2 ball
ball_p2 = pygame.draw.circle()
ball_size = (5, 5)
ball_p2 = pygame.transform.scale(ball_p2, ball_size)
ball_p2_x = 50
ball_p2_y = 150
ball_p2_dx = 1
ball_p2_dy = 1

# player 1 score
score_p1_font = pygame.font.SysFont('IMPACT', 50)
score_p1_text = score_p1_font.render('0', True, Green)
score_p1_text_rect = score_p1_text.get_rect()
score_p1_text_rect.center = (300, 30)

# player 2 score
score_p2_font = pygame.font.SysFont('IMPACT', 50)
score_p2_text = score_p2_font.render('0', True, Blue)
score_p2_text_rect = score_p2_text.get_rect()
score_p2_text_rect.center = (1000, 30)


score_1_text = score_p1


run = True

while run:
    screen.fill(Black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    score_space = 70
    border_thickness = 25
    # drawing borders
    pygame.draw.line(screen, Yellow, (0, score_space), (screen_size[0], score_space), border_thickness)
    pygame.draw.line(screen, Yellow, (screen_size[0] - border_thickness / 2, score_space),
                     (screen_size[0] - border_thickness / 2, screen_size[1]), border_thickness)
    pygame.draw.line(screen, Yellow, (0, screen_size[1] - border_thickness / 2),
                     (screen_size[0], screen_size[1] - border_thickness / 2), border_thickness)
    pygame.draw.line(screen, Yellow, (border_thickness / 2, score_space), (border_thickness / 2, screen_size[1]),
                     border_thickness)

    limit_borders(player_1_y, score_space)
    limit_borders_p2(player_2_y, score_space)
    move_p1()
    # show elements on screen
    surf = pygame.transform.rotate(player_1, angle_1)
    surf2 = pygame.transform.rotate(player_2, angle_2)
    screen.blit(surf, (player_1_x, player_1_y))
    screen.blit(surf2, (player_2_x, player_2_y))
    screen.blit(score_p1_text, score_p1_text_rect)
    screen.blit(score_p2_text, score_p2_text_rect)
    screen.blit(ball_p1, (ball_p1_x, ball_p1_y))
    screen.blit(ball_p2, (ball_p2_x, ball_p2_y))

    pygame.display.flip()
    game_clock.tick(100)
