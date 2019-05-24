#! usr/bin/env python3
# -*- coding: utf-8 -*-

# Импорт модулей
import pygame


# Класс ячеек
class Cell(object):
    # Функция инициализатор
    def __init__(self, x, y, size, colors):
        self.__x = x
        self.__y = y
        self.__size = size
        self.__xx = self.__x + self.__size
        self.__yy = self.__y + self.__size
        self.__x_center = self.__x + self.__size / 2
        self.__y_center = self.__y + self.__size / 2

        self.__colors = colors
        self.__color_not_active = self.__colors[0]
        self.__color_active = self.__colors[1]
        self.__color_help = self.__colors[2]
        self.__color_enemy = self.__colors[3]
        self.__border_not_active = self.__colors[4]
        self.__border_active = self.__colors[1]

        # Актуальные цвета
        self.__color = self.__color_not_active
        self.__border = self.__border_not_active

    # Метод обновления цвета границы ячеек
    def update_cursor(self, pos):
        if self.__x < pos[0] < self.__xx and self.__y < pos[1] < self.__yy:
            self.__border = self.__border_active
        else:
            self.__border = self.__border_not_active

    # Метод рисования
    def draw(self, window):
        # Рисование ячейки
        pygame.draw.rect(window, self.__color, (self.__x, self.__y, self.__size, self.__size))
        # Рисование границы ячейки
        pygame.draw.rect(window, self.__border, (self.__x, self.__y, self.__size, self.__size), 2)

    # Свойства
    @property
    def x_center(self):
        return self.__x_center

    @property
    def y_center(self):
        return self.__y_center


# Класс солнца
class Sun(object):
    # Функция инициализатор
    def __init__(self, x, y, r, color):
        self.__x = x
        self.__y = y
        self.__r = r
        self.__color = color

    # Метод обновления координат солнца
    def update(self):
        self.__x += 1

    # Метод рисования
    def draw(self, window):
        pygame.draw.circle(window, self.__color, (self.__x, self.__y), self.__r)


# Класс персонажа
class Person(pygame.sprite.Sprite):
    # Функция инициализатор
    def __init__(self, x, y, host, character, colors):
        # Получение атрибутов и методов класса pygame.sprite.Sprite()
        pygame.sprite.Sprite.__init__(self)
        # Получение остальных атрибутов
        self.__x = x
        self.__y = y
        self.__host = host
        self.__character = character
        self.__health = 10
        self.__start_health = 10
        self.__colors = colors
        self.__color_health = self.__colors[0]
        self.__mana = self.__colors[1]
        # Атрибуты отрисовки параметров
        self.__width = 40  # px
        self.__height = 70  # px
        self.__indent = 5  # px
        self.__p_x = self.__x - self.__width / 2
        self.__p_y = self.__y - self.__height / 2 - 3 * self.__indent
        self.__p_w = self.__width * (self.__health / self.__start_health)
        self.__p_h = 5  # px

        # Атрибуты класса pygame.sprite.Sprite()
        if self.__host == 'player':
            self.__image = pygame.image.load('sprites/{}/right.png'.format(self.__character))
            self.__rect = self.__image.get_rect(center=(self.__x, self.__y))
        else:
            self.__image = pygame.image.load('sprites/{}/left.png'.format(self.__character))
            self.__rect = self.__image.get_rect(center=(self.__x, self.__y))

    # Функция рисования параметров персонажа
    def draw_par(self, window):
        pygame.draw.rect(window, self.__color_health, (self.__p_x, self.__p_y, self.__p_w, self.__p_h))

    # Свойства
    # image
    @property
    def image(self):
        return self.__image

    # rect
    @property
    def rect(self):
        return self.__rect
