"""
Квадратний Pac-Man — оновлена версія (з головним меню, налаштуваннями та повноекранним режимом)
Автор: згенеровано ChatGPT (2025)

Управління:
  Стрілки — рух
  R — перезапуск після смерті або перемоги
  ESC — вихід
  ENTER — підтвердити / вибрати
"""

import pygame
import sys
import random

# ---------- Базові налаштування ----------
CELL = 28
COLS = 21
ROWS = 19
FPS = 60
PLAYER_SPEED = 150
ENEMY_SPEED = 100

# Кольори
BG = (10, 10, 30)
WALL_COLOR = (40, 40, 120)
FOOD_COLOR = (230, 230, 90)
PLAYER_COLOR = (80, 220, 80)
ENEMY_COLOR = (220, 80, 80)
TEXT_COLOR = (240, 240, 240)
BUTTON_HOVER = (255, 255, 0)

# ---------- Лабіринт ----------
MAZE = [
    "111111111111111111111",
    "100000000001000000001",
    "101111011101110111101",
    "100000010000010000001",
    "111011110111011110111",
    "100010000100000100001",
    "101110111101110111101",
    "100000100000010000001",
    "111111101111011111111",
    "000000001000010000000",
    "111111101111011111111",
    "100000100000010000001",
    "101110111101110111101",
    "100010000100000100001",
    "111011110111011110111",
    "100000010000010000001",
    "101111011101110111101",
    "100000000001000000001",
    "111111111111111111111",
]

# ---------- Допоміжні функції ----------
def cell_to_rect(r, c):
    return pygame.Rect(c * CELL, r * CELL, CELL, CELL)

def get_neighbours(rc):
    r, c = rc
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and MAZE[nr][nc] == '0':
            yield (nr, nc)

# ---------- Класи ----------
class Player:
    def __init__(self, r, c):
        self.r, self.c = r, c
        self.x, self.y = c * CELL, r * CELL
        self.w, self.h = CELL - 6, CELL - 6
        self.vx = self.vy = 0

    def rect(self):
        return pygame.Rect(self.x + 3, self.y + 3, self.w, self.h)

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.x = max(0, min(self.x, WIDTH - CELL))
        self.y = max(0, min(self.y, HEIGHT - CELL))
        self.c = int((self.x + CELL // 2) // CELL)
        self.r = int((self.y + CELL // 2) // CELL)

    def move(self, direction):
        if direction == 'up': self.vx, self.vy = 0, -PLAYER_SPEED
        elif direction == 'down': self.vx, self.vy = 0, PLAYER_SPEED
        elif direction == 'left': self.vx, self.vy = -PLAYER_SPEED, 0
        elif direction == 'right': self.vx, self.vy = PLAYER_SPEED, 0
        else: self.vx = self.vy = 0

class Enemy:
    def __init__(self, r, c):
        self.r, self.c = r, c
        self.x, self.y = c * CELL, r * CELL
        self.w, self.h = CELL - 6, CELL - 6
        self.vx = self.vy = 0
        self.timer = 0

    def rect(self):
        return pygame.Rect(self.x + 3, self.y + 3, self.w, self.h)

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        cr, cc = int((self.y + CELL // 2)//CELL), int((self.x + CELL // 2)//CELL)
        if (cr, cc) != (self.r, self.c):
            self.r, self.c = cr, cc
        self.timer -= dt
        if self.timer <= 0:
            self.pick_new_direction()

    def pick_new_direction(self):
        opts = list(get_neighbours((self.r, self.c)))
        if not opts:
            self.vx = self.vy = 0; self.timer = 0.3; return
        nr, nc = random.choice(opts)
        dx, dy = nc - self.c, nr - self.r
        self.vx, self.vy = dx * ENEMY_SPEED, dy * ENEMY_SPEED
        self.timer = random.uniform(0.6, 1.4)

# ---------- Меню ----------
def draw_button(screen, font, text, y, selected):
    color = BUTTON_HOVER if selected else TEXT_COLOR
    txt = font.render(text, True, color)
    rect = txt.get_rect(center=(WIDTH // 2, y))
    screen.blit(txt, rect)
    return rect

def main_menu():
    global WIDTH, HEIGHT
    options = ["Start", "Settings", "Quit"]
    selected = 0
    font = pygame.font.SysFont(None, 60)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    choice = options[selected]
                    if choice == "Start":
                        return 'start'
                    elif choice == "Settings":
                        settings_menu()
                    elif choice == "Quit":
                        pygame.quit(); sys.exit()

        screen.fill(BG)
        title = font.render("Квадратний Pac-Man", True, TEXT_COLOR)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 120))

        for i, opt in enumerate(options):
            draw_button(screen, font, opt, 300 + i * 80, i == selected)

        pygame.display.flip()
        clock.tick(30)

# ---------- Меню налаштувань ----------
def settings_menu():
    global WIDTH, HEIGHT, FULLSCREEN
    resolutions = [(1920,1080), (1440,1080), (800,600)]
    modes = ["Windowed", "Fullscreen"]
    res_i = 0
    mode_i = 0
    font = pygame.font.SysFont(None, 48)
    selected = 0
    items = ["Resolution", "Mode", "Back"]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(items)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(items)
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        res_i = (res_i + 1) % len(resolutions)
                    elif selected == 1:
                        mode_i = (mode_i + 1) % len(modes)
                    elif selected == 2:
                        WIDTH, HEIGHT = resolutions[res_i]
                        FULLSCREEN = (modes[mode_i] == "Fullscreen")
                        if FULLSCREEN:
                            pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
                        else:
                            pygame.display.set_mode((WIDTH, HEIGHT))
                        return

        screen.fill(BG)
        title = font.render("Налаштування", True, TEXT_COLOR)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 120))

        res_text = f"Resolution: {resolutions[res_i][0]}x{resolutions[res_i][1]}"
        mode_text = f"Mode: {modes[mode_i]}"
        opts = [res_text, mode_text, "Back"]

        for i, opt in enumerate(opts):
            draw_button(screen, font, opt, 300 + i * 70, i == selected)

        pygame.display.flip()
        clock.tick(30)

# ---------- Основна гра ----------
def run_game():
    global WIDTH, HEIGHT
    walls, food = [], {}
    for r in range(ROWS):
        for c in range(COLS):
            if MAZE[r][c] == '1':
                walls.append(cell_to_rect(r, c))
            else:
                food[(r, c)] = cell_to_rect(r, c).inflate(-CELL//3, -CELL//3)

    player = Player(1,1)
    enemies = [Enemy(r, c) for r,c in random.sample([(r,c) for r in range(ROWS) for c in range(COLS) if MAZE[r][c]=='0' and (r,c)!=(1,1)], 4)]

    font = pygame.font.SysFont(None, 28)
    score = 0
    win = lose = False

    while True:
        dt = clock.tick(FPS)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 'menu'
                elif event.key == pygame.K_r and (win or lose):
                    return 'restart'
                elif not (win or lose):
                    if event.key == pygame.K_UP: player.move('up')
                    elif event.key == pygame.K_DOWN: player.move('down')
                    elif event.key == pygame.K_LEFT: player.move('left')
                    elif event.key == pygame.K_RIGHT: player.move('right')

        if not (win or lose):
            player.update(dt)
            pr, pc = int((player.y + CELL//2)//CELL), int((player.x + CELL//2)//CELL)
            if MAZE[pr][pc] == '1':
                player.move(None)
                player.x, player.y = player.c * CELL, player.r * CELL
            cell = (player.r, player.c)
            if cell in food:
                del food[cell]
                score += 1
                if not food: win = True
            for e in enemies:
                e.update(dt)
                if player.rect().colliderect(e.rect()): lose = True

        screen.fill(BG)
        for w in walls: pygame.draw.rect(screen, WALL_COLOR, w)
        for f in food.values(): pygame.draw.rect(screen, FOOD_COLOR, f)
        for e in enemies: pygame.draw.rect(screen, ENEMY_COLOR, e.rect())
        pygame.draw.rect(screen, PLAYER_COLOR, player.rect())

        hud = font.render(f"Score: {score}", True, TEXT_COLOR)
        screen.blit(hud, (10,10))

        if win:
            msg = font.render("Перемога! Натисніть R для перезапуску.", True, TEXT_COLOR)
            screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2))
        elif lose:
            msg = font.render("Поразка! Натисніть R для перезапуску.", True, TEXT_COLOR)
            screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2))

        pygame.display.flip()

# ---------- Запуск ----------
if __name__ == '__main__':
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    FULLSCREEN = False
    flags = pygame.FULLSCREEN if FULLSCREEN else 0
    screen = pygame.display.set_mode((WIDTH, HEIGHT), flags)
    clock = pygame.time.Clock()

    while True:
        action = main_menu()
        if action == 'start':
            result = run_game()
            if result == 'restart':
                continue
            else:
                continue
