# Hello!
# This is BPRateiro 's implementation of Snake, an old school game I'm very fond of.
# I followed FreeCodeCamp's 'Learn Python by Building Five Games' tutorial.
# The full tutorial can be found at: https://www.youtube.com/watch?v=XGf2GcyHPhc&t=2736s
# My objective is to practice OOP and try some of Python's libraries.
# Hope we have some fun!

import random
import pygame
import sys
import tkinter as tk
from tkinter import messagebox


# Classes Definition
class Cube(object):
    rows = 0
    width = 0

    def __init__(self):
        pass


class Snake(object):
    def __init__(self, color, start):
        pass


# Functions Definition
def create_window(width=500, height=500):
    return pygame.display.set_mode((width, height))


def draw_grid(surface, rows: int):
    """Divides the window into grids according to the number of rows"""
    width = surface.get_width()
    size_between = width // rows
    x, y = 0, 0

    for line in range(rows):
        x += size_between
        y += size_between

        pygame.draw.line(surface, colors['white'], (x, 0), (x, width))
        pygame.draw.line(surface, colors['white'], (0, y), (width, y))


def redraw_window(surface: pygame.Surface, rows: int):
    """Updates frame"""
    surface.fill(colors['black'])
    draw_grid(surface, rows)
    pygame.display.update()


def main():
    """Controls the game flow."""
    rows = 20

    window = create_window()
    clock = pygame.time.Clock()
    snake = Snake(colors['blue'], (rows//2, rows//2))  # RGB values, coordinates

    pygame.init()

    while True:
        for event in pygame.event.get():  # Event handling
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.time.delay(50)  # 50ms so that the game doesn't run too fast
        clock.tick(10)  # Speed in FPS

        redraw_window(window, rows)


# Defining RGB colors used in game
colors = {'black': (0, 0, 0),
          'white': (255, 255, 255),
          'red': (255, 0, 0),
          'green': (0, 255, 0),
          'blue': (0, 0, 255)}
# Good luck, have fun!
main()
