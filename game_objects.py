#! usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame


class Cell(object):
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

        self.__color = self.__color_not_active
        self.__border = self.__border_not_active

    def draw(self, window):
        pygame.draw.rect(window, self.__color, (self.__x, self.__y, self.__size, self.__size))
        pygame.draw.rect(window, self.__border, (self.__x, self.__y, self.__size, self.__size), 2)


class Sun(object):
    def __init__(self, x, y, r, color):
        self.__x = x
        self.__y = y
        self.__r = r
        self.__color = color

    def draw(self, window):
        pygame.draw.circle(window, self.__color, (self.__x, self.__y), self.__r)
