import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Функция для рисования злого смайла
def draw_evil_smiley():
    pygame.draw.circle(screen, 'YELLOW', (200, 200), 100)  # Рисуем желтую окружность (голову)
    pygame.draw.circle(screen, 'BLACK', (150, 170), 20)    # Рисуем черные глаза
    pygame.draw.circle(screen, BLACK, (250, 170), 20)
    pygame.draw.circle(screen, BLACK, (150, 170), 10)    # Рисуем черные зрачки
    pygame.draw.circle(screen, BLACK, (250, 170), 10)
    pygame.draw.rect(screen, RED, (150, 250, 100, 20))   # Рисуем злой рот



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    screen.fill(WHITE)
    draw_evil_smiley()
    pygame.display.update()
pygame.quit()