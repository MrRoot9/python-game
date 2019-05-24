#! usr/bin/env python3
# -*- coding: utf-8 -*-

# Импорты модулей
import pygame

#  Все цвета
BURLY_WOOD = (222, 184, 135)
SKY = (117, 187, 253)
GRASS = (63, 155, 11)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Параметры экрана
WIDTH = 900  # px
HEIGHT = 600  # px
SIZE = (WIDTH, HEIGHT)

# Параметры командного интерфейса
INT_WIDTH = 200  # px
INT_HEIGHT = HEIGHT
INT_COLOR = BURLY_WOOD

# Параметры игрового поля
GF_WIDTH = WIDTH - INT_WIDTH
GF_HEIGHT = 500  # px
GF_COLOR = GRASS

# Параметры неба
SKY_WIDTH = WIDTH - INT_WIDTH
SKY_HEIGHT = HEIGHT - GF_HEIGHT
SKY_COLOR = SKY

# Параметры ячейки
CELL_SIZE = 100  # px
CELL_COLORS = (GRASS, GREEN, YELLOW, RED, BLACK)

# Парамаетры солнца
SUN_X = 50  # px
SUN_Y = 50  # px
SUN_R = 40  # px
SUN_COLOR = YELLOW

# Параметры персонажей
PLAYER_COLORS = (RED, BLUE)

# Стартовые параметры основного цикла
pos = (0, 0)

# Списки
# Список персонажей игрока
player_list = pygame.sprite.Group()
# Список персонажей компьютера
ai_list = pygame.sprite.Group()
