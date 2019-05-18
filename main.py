#! usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pygame
from settings import *
from game_objects import Cell

pygame.init()

window = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Heroes of cave")


def drawing():
    pygame.draw.rect(window, INT_COLOR, (WIDTH - INT_WIDTH, 0, INT_WIDTH, INT_HEIGHT))
    pygame.draw.rect(window, GF_COLOR, (0, HEIGHT - GF_HEIGHT, GF_WIDTH, GF_HEIGHT))
    pygame.draw.rect(window, SKY_COLOR, (0, 0, SKY_WIDTH, SKY_HEIGHT))

    for cell in cells:
        cell.draw(window)

    pygame.display.update()


# Получение ячеек
cells = []

number_in_row = int(GF_WIDTH / CELL_SIZE)
number_in_column = int(GF_HEIGHT / CELL_SIZE)

for i in range(number_in_row):
    x = i * 100
    for j in range(number_in_column):
        y = j * 100 + SKY_HEIGHT
        cells.append(Cell(x, y, CELL_SIZE, COLORS))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            coordinates = pygame.mouse.get_pos()
            print(coordinates)
    drawing()
