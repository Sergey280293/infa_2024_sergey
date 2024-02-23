import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров окна
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Панда и бамбук')

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Функция для рисования панды
def draw_panda(x, y):
    # Рисуем тело панды
    pygame.draw.ellipse(window, BLACK, (x + 50, y + 30, 200, 150))
    # Рисуем лицо панды
    pygame.draw.circle(window, WHITE, (x + 120, y + 90), 80)
    pygame.draw.circle(window, BLACK, (x + 120, y + 90), 80, 3)
    # Глаза
    pygame.draw.circle(window, BLACK, (x + 90, y + 60), 10)
    pygame.draw.circle(window, BLACK, (x + 150, y + 60), 10)
    # Нос
    pygame.draw.polygon(window, BLACK, [(x + 120, y + 90), (x + 110, y + 110), (x + 130, y + 110)])
    # Рот
    pygame.draw.arc(window, BLACK, (x + 100, y + 80, 40, 40), 0, -3.14, 3)
    # Лапы
    pygame.draw.ellipse(window, WHITE, (x + 20, y + 130, 100, 60))
    pygame.draw.ellipse(window, WHITE, (x + 150, y + 130, 100, 60))
    pygame.draw.ellipse(window, WHITE, (x + 40, y + 160, 60, 100))
    pygame.draw.ellipse(window, WHITE, (x + 160, y + 160, 60, 100))

# Функция для рисования бамбука
def draw_bamboo(x, y):
    pygame.draw.rect(window, GRAY, (x + 60, y + 200, 20, 100))
    pygame.draw.ellipse(window, BLACK, (x, y + 150, 140, 100))
    pygame.draw.ellipse(window, BLACK, (x + 50, y + 100, 140, 100))
    pygame.draw.ellipse(window, BLACK, (x + 100, y + 150, 140, 100))

# Основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(WHITE)  # Заливка окна белым цветом
    draw_panda(200, 250)  # Рисуем панду
    draw_bamboo(500, 100)  # Рисуем бамбук
    draw_bamboo(100, 100)  # Рисуем бамбук
    pygame.display.update()  # Обновление экрана
