import pygame
import config
import classes

pygame.init()
pygame.font.init()

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print(joysticks)

size = (1000, 750)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Combat Game")

font = pygame.font.Font("PressStart2P.ttf", 30)

score_point_player1 = font.render("0", True, (0, 255, 0))
score_point_player1_rect = score_point_player1.get_rect()
score_point_player1_rect.center = (350, 30)

score_point_player2 = font.render("0", True, (0, 0, 255))
score_point_player2_rect = score_point_player2.get_rect()
score_point_player2_rect.center = (650, 30)

player1_image = "player1_nobc.png"
player1_coord = config.player1_init_cord
player1_angle = config.player1_init_angle
player1 = classes.Tank(player1_image, player1_coord, player1_angle)
player2_image = "player2_nobc.png"
player2_coord = config.player2_init_cord
player2_angle = config.player2_init_angle
player2 = classes.Tank(player2_image, player2_coord, player2_angle)

clock = pygame.time.Clock()

run_game = True

while run_game:
    screen.fill("#9f4100")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run_game = False
        if event.type == pygame.JOYBUTTONDOWN:
            print(event)
            if pygame.joystick.Joystick(0).get_button(0):
                shot = classes.Shot(player1.coord, player1.angle, config.shot_size)
            if pygame.joystick.Joystick(0).get_button(11):
                player1.move()
            if pygame.joystick.Joystick(0).get_button(14):
                player1.turn(-1)
            if pygame.joystick.Joystick(0).get_button(13):
                player1.turn(1)

    pygame.draw.polygon(screen, "#c29f2e",
                        [(110, 300), (160, 300), (160, 500), (110, 500), (110, 480), (140, 480), (140, 320),
                         (110, 320)])
    pygame.draw.polygon(screen, "#c29f2e",
                        [(890, 300), (840, 300), (840, 500), (890, 500), (890, 480), (860, 480), (860, 320),
                         (890, 320)])

    pygame.draw.rect(screen, "#c29f2e", (480, 155, 40, 100))
    pygame.draw.rect(screen, "#c29f2e", (480, 550, 40, 100))
    pygame.draw.rect(screen, "#c29f2e", (255, 380, 100, 40))
    pygame.draw.rect(screen, "#c29f2e", (625, 380, 100, 40))

    pygame.draw.rect(screen, "#c29f2e", (0, 50, 1000, 700), 25)

    player1.draw(screen)
    player2.draw(screen)

    clock.tick(30)

    pygame.display.update()