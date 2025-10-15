import pygame
import random
import time
import sys

pygame.init()

# ----------- Налаштування ---------------- #
# Можливі розширення
resolutions = [
    (800, 600),
    (1024, 768),
    (1280, 720)
]
current_resolution_index = 0  # За замовчуванням перше

# Кольори
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Шрифт
font = pygame.font.SysFont(None, 40)

# ------------------------------------------------ #
# Малюємо кнопку
def draw_button(screen, text, x, y, width, height, active_color, inactive_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x+width and y < mouse[1] < y+height:
        pygame.draw.rect(screen, active_color, (x, y, width, height))
        if click[0] == 1 and action is not None:
            pygame.time.delay(200)  # затримка, щоб не натискалось двічі
            action()
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))

    text_surf = font.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surf, text_rect)

# ------------------------------------------------ #
# Меню
def main_menu():
    global screen
    screen = pygame.display.set_mode(resolutions[current_resolution_index])
    pygame.display.set_caption("Aim Trainer - Menu")

    while True:
        screen.fill(WHITE)
        draw_button(screen, "Start", 100, 100, 200, 60, GRAY, WHITE, start_game)
        draw_button(screen, "Settings", 100, 200, 200, 60, GRAY, WHITE, settings_menu)
        draw_button(screen, "Exit", 100, 300, 200, 60, GRAY, WHITE, quit_game)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

# ------------------------------------------------ #
# Меню налаштувань
def settings_menu():
    global current_resolution_index, screen
    settings_running = True

    while settings_running:
        screen.fill(WHITE)

        text = font.render("Choose screen resolution:", True, BLACK)
        screen.blit(text, (100, 50))

        for i, res in enumerate(resolutions):
            res_text = f"{res[0]}x{res[1]}"
            draw_button(
                screen,
                res_text,
                100,
                120 + i * 70,
                200,
                50,
                GRAY,
                WHITE,
                lambda r=i: set_resolution(r)
            )

        draw_button(screen, "Back", 100, 350, 200, 60, GRAY, WHITE, lambda: exit_settings())

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

def set_resolution(index):
    global current_resolution_index, screen
    current_resolution_index = index
    screen = pygame.display.set_mode(resolutions[current_resolution_index])

def exit_settings():
    main_menu()

# ------------------------------------------------ #
# Вихід
def quit_game():
    pygame.quit()
    sys.exit()

# ------------------------------------------------ #
# Гра
def start_game():
    global screen
    WIDTH, HEIGHT = resolutions[current_resolution_index]
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Aim Trainer - Game")

    target_radius = 30
    target_x = random.randint(target_radius, WIDTH - target_radius)
    target_y = random.randint(target_radius, HEIGHT - target_radius)
    hits = 0
    start_time = time.time()
    reaction_time = 0

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(WHITE)
        pygame.draw.circle(screen, RED, (target_x, target_y), target_radius)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                distance = ((mx - target_x) ** 2 + (my - target_y) ** 2) ** 0.5
                if distance <= target_radius:
                    hits += 1
                    reaction_time = round((time.time() - start_time) * 1000)
                    start_time = time.time()
                    target_x = random.randint(target_radius, WIDTH - target_radius)
                    target_y = random.randint(target_radius, HEIGHT - target_radius)

        # Текст
        hits_text = font.render(f"Hits: {hits}", True, BLACK)
        time_text = font.render(f"Reaction: {reaction_time} ms", True, BLACK)

        screen.blit(hits_text, (10, 10))
        screen.blit(time_text, (10, 50))

        pygame.display.flip()
        clock.tick(60)

# ------------------------------------------------ #
# Запуск
main_menu()