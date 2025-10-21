import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Баскетбол з квадратом")

WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
RED = (255, 50, 50)
BLACK = (0, 0, 0)

# Гравець
player_size = 40
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 6
ball_vel_y = 0
is_jumping = False

# Кошик
basket_size = 60
basket_x = random.randint(0, WIDTH - basket_size)
basket_y = 150  # високий кошик

# Звук


font = pygame.font.SysFont("arial", 28)
score = 0

clock = pygame.time.Clock()
running = True

# Фіксований “стрибок” до кошика
def jump_to_basket():
    global player_y, is_jumping
    player_y = basket_y + basket_size - player_size // 2  # прямо до кошика
    is_jumping = False

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and not is_jumping:
        is_jumping = True
        jump_to_basket()  # миттєво до кошика

    # Перевірка попадання
    basket_rect = pygame.Rect(basket_x, basket_y, basket_size, basket_size)
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

    if basket_rect.colliderect(player_rect):
        score += 1

        basket_x = random.randint(0, WIDTH - basket_size)
        basket_y = random.randint(100, 200)
        player_y = HEIGHT - player_size - 10
        is_jumping = False

    pygame.draw.rect(screen, BLUE, player_rect)
    pygame.draw.rect(screen, RED, basket_rect)
    text = font.render(f"Рахунок: {score}", True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
