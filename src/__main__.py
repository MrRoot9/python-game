#! usr/bin/env python3
# -*- coding: utf-8 -*-

# Импорты модулей
import sys
from settings import *
from game_objects import Cell, Sun, Person

# Инициализация библиотеки pygame
pygame.init()

# Создание окна
window = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Heroes of cave")


# Функция рисования
def drawing():
    # Рисование фона неба
    pygame.draw.rect(window, SKY_COLOR, (0, 0, SKY_WIDTH, SKY_HEIGHT))

    # Рисование солнца
    sun.draw(window)

    # Рисование фона командного интерфейса
    pygame.draw.rect(window, INT_COLOR, (WIDTH - INT_WIDTH, 0, INT_WIDTH, INT_HEIGHT))

    # Рисование ячеек
    for item in cells:
        item.draw(window)

    # Рисование персонажей игрока
    player_list.draw(window)
    for pp in player_list:
        pp.draw_par(window)

    # Рисование персонажей компьютера
    ai_list.draw(window)
    for ap in ai_list:
        ap.draw_par(window)

    # Обновление графических данных
    pygame.display.update()


# Создание объекта Солнце
sun = Sun(SUN_X, SUN_Y, SUN_R, SUN_COLOR)

# Получение ячеек
# Создание списка ячеек
cells = []
# Получение числа ячеек в строке
number_in_row = int(GF_WIDTH / CELL_SIZE)
# Получение числа ячеек в столбце
number_in_column = int(GF_HEIGHT / CELL_SIZE)
# Создание ячеек в цикле
for i in range(number_in_row):
    x = i * 100
    for j in range(number_in_column):
        y = j * 100 + SKY_HEIGHT
        cells.append(Cell(x, y, CELL_SIZE, CELL_COLORS))

# Создание персонажей
# Создание персонажей игрока
player_list.add(Person(cells[0].x_center, cells[0].y_center, 'player', 'barbarian', PLAYER_COLORS))
player_list.add(Person(cells[2].x_center, cells[2].y_center, 'player', 'barbarian', PLAYER_COLORS))
player_list.add(Person(cells[4].x_center, cells[4].y_center, 'player', 'barbarian', PLAYER_COLORS))
# Создание персонажей игрока
ai_list.add(Person(cells[-5].x_center, cells[-5].y_center, 'ai', 'barbarian', PLAYER_COLORS))
ai_list.add(Person(cells[-3].x_center, cells[-3].y_center, 'ai', 'barbarian', PLAYER_COLORS))
ai_list.add(Person(cells[-1].x_center, cells[-1].y_center, 'ai', 'barbarian', PLAYER_COLORS))


# Главный цикл
while True:
    # Обработка событий
    for event in pygame.event.get():
        # Обработка кнопки закрытия окна
        if event.type == pygame.QUIT:
            sys.exit()

        # Получение позиции курсора
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            print(pos)

    # Обновление положения солнца
    sun.update()

    # Обновление границ ячеек
    for cell in cells:
        cell.update_cursor(pos)

    # Функция рисования
    drawing()
