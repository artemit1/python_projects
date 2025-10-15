import pygame
import random
import time

# Ініціалізація Pygame
pygame.init()

# Налаштування вікна
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")

# Кольори
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Параметри мішені
TARGET_RADIUS = 30

# Шрифт
font = pygame.font.SysFont(None, 36)

# Змінні гри
target_x = random.randint(TARGET_RADIUS, WIDTH - TARGET_RADIUS)
target_y = random.randint(TARGET_RADIUS, HEIGHT - TARGET_RADIUS)
hits = 0
start_time = time.time()
reaction_time = 0

# Основний цикл
running = True
while running:
    window.fill(WHITE)

    # Малюємо мішень
    pygame.draw.circle(window, RED, (target_x, target_y), TARGET_RADIUS)

    # Події
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обробка кліку миші
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            distance = ((mouse_x - target_x) ** 2 + (mouse_y - target_y) ** 2) ** 0.5
            if distance <= TARGET_RADIUS:
                hits += 1
                reaction_time = round((time.time() - start_time) * 1000)  # мс
                start_time = time.time()
                # Нова позиція мішені
                target_x = random.randint(TARGET_RADIUS, WIDTH - TARGET_RADIUS)
                target_y = random.randint(TARGET_RADIUS, HEIGHT - TARGET_RADIUS)

    # Текст
    hit_text = font.render(f"Hits: {hits}", True, BLACK)
    time_text = font.render(f"Reaction: {reaction_time} ms", True, BLACK)

    window.blit(hit_text, (10, 10))
    window.blit(time_text, (10, 50))

    pygame.display.flip()
    pygame.time.Clock().tick(60)  # FPS

pygame.quit()
