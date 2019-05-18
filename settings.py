#! usr/bin/env python3
# -*- coding: utf-8 -*-

# Цвета
BURLY_WOOD = (222, 184, 135)
SKY = (117, 187, 253)
GRASS = (63, 155, 11)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Параметры экрана
WIDTH = 1200  # px
HEIGHT = 700  # px
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
COLORS = [GRASS, GREEN, YELLOW, RED, BLACK]
