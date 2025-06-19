import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (255, 0, 255)

# Paddle
paddle_width, paddle_height = 100, 10
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - 50
paddle_speed = 6

# Ball
ball_radius = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx, ball_dy = 4, -4

# Bricks
brick_rows, brick_cols = 5, 8
brick_width, brick_height = 80, 20
bricks = []

for row in range(brick_rows):
    for col in range(brick_cols):
        bricks.append(pygame.Rect(col * (brick_width + 10) + 35, row * (brick_height + 10) + 50, brick_width, brick_height))

# Game loop
running = True
while running:
    pygame.time.delay(20)
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed

    # Ball movement
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with walls
    if ball_x <= 0 or ball_x >= WIDTH - ball_radius:
        ball_dx = -ball_dx
    if ball_y <= 0:
        ball_dy = -ball_dy

    # Ball collision with paddle
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    if paddle_rect.colliderect(ball_x, ball_y, ball_radius, ball_radius):
        ball_dy = -ball_dy

    # Ball collision with bricks
    for brick in bricks[:]:
        if brick.colliderect(ball_x, ball_y, ball_radius, ball_radius):
            bricks.remove(brick)
            ball_dy = -ball_dy

    # Game over condition
    if ball_y >= HEIGHT:
        print("Game Over!")
        running = False

    # Draw elements
    pygame.draw.rect(screen, BLUE, paddle_rect)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    for brick in bricks:
        pygame.draw.rect(screen, GREEN, brick)

    pygame.display.update()


pygame.quit()
