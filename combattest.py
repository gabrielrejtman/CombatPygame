import pygame

# Initialize the game engine
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((800, 600))

# Define colors
WHITE = (255, 255, 255)

# Load font
font = pygame.font.Font(None, 36)

# Create player squares
player1 = pygame.Rect(50, 50, 50, 50)
player2 = pygame.Rect(700, 500, 50, 50)

# Create projectiles
player1_projectile = None
player2_projectile = None

# Define shooting variables
player1_shoot = False
player2_shoot = False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player 1 movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1.y -= 5
    if keys[pygame.K_s]:
        player1.y += 5
    if keys[pygame.K_a]:
        player1.x -= 5
    if keys[pygame.K_d]:
        player1.x += 5

    # Handle player 2 movement
    if keys[pygame.K_UP]:
        player2.y -= 5
    if keys[pygame.K_DOWN]:
        player2.y += 5
    if keys[pygame.K_LEFT]:
        player2.x -= 5
    if keys[pygame.K_RIGHT]:
        player2.x += 5

    # Handle player 1 shooting
    if keys[pygame.K_r]:
        player1_shoot = True
        player1_projectile = pygame.Rect(player1.x + 25, player1.y + 25, 5, 5)

    # Handle player 2 shooting
    if keys[pygame.K_l]:
        player2_shoot = True
        player2_projectile = pygame.Rect(player2.x + 25, player2.y + 25, 5, 5)

    # Move player 1 projectile
    if player1_shoot:
        player1_projectile.x += 5

    # Move player 2 projectile
    if player2_shoot:
        player2_projectile.x -= 5

    # Check for collision
    if player1_shoot and player1_projectile.colliderect(player2):
        running = False
        message = font.render("Player 1 wins!", True, WHITE)
        screen.blit(message, (350, 300))
    if player2_shoot and player2_projectile.colliderect(player1):
        running = False
        message = font.render("Player 2 wins!", True, WHITE)
        screen.blit(message, (350, 300))

        # Fill the screen with black
    screen.fill((0, 0, 0))

    # Update the display
    pygame.display.update()

    # Draw player squares
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)

    # Draw projectiles
    # Check for collision
    if player1_shoot and player1_projectile.colliderect(player2):
        running = False
        message = font.render("Player 1 wins!", True, WHITE)
        screen.blit(message, (350, 300))
        pygame.display.update()
    if player2_shoot and player2_projectile.colliderect(player1):
        running = False
        message = font.render("Player 2 wins!", True, WHITE)
        screen.blit(message, (350, 300))
        pygame.display.update()

pygame.quit()
