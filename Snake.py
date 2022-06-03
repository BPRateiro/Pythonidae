# Hello!
# This is BPRateiro 's implementation of Snake, an old school game I'm very fond of.
# I followed FreeCodeCamp's 'Learn Python by Building Five Games' tutorial.
# The full tutorial can be found at: https://www.youtube.com/watch?v=XGf2GcyHPhc&t=2736s
# My objective is to practice OOP and try some of Python's libraries.
# Hope we have some fun!
import ctypes
import random
import pygame
import tkinter as tk
from tkinter import messagebox

# Defining RGB colors used in game
COLORS = {'black': (0, 0, 0),
          'white': (255, 255, 255),
          'red': (255, 0, 0),
          'green': (0, 255, 0),
          'blue': (0, 0, 255)}
# Defining some window parameters:
SIZE = (500, 500)
ROWS = 20


# Classes Definition
class Cube(object):
    def __init__(self, position, x_direction=1, y_direction=0, color=COLORS['red']):
        self.position = position
        self.x_direction = x_direction
        self.y_direction = y_direction
        self.color = color

    def move(self, x_direction, y_direction):
        self.x_direction = x_direction
        self.y_direction = y_direction
        self.position += self.x_direction, self.y_direction

    def draw(self, surface, eyes=False):
        distance = SIZE[0] // ROWS
        i = self.position[0]
        j = self.position[1]

        square = (i*distance+1, j*distance+1, distance-2, distance-2)
        pygame.draw.rect(surface, self.color, square)

        if eyes:
            square_center = distance//2
            radius = 3
            circle_center_1 = (i*distance+square_center-radius, j*distance+8)
            circle_center_2 = (i*distance+distance-radius*2, j*distance+8)
            pygame.draw.circle(surface, COLORS['black'], circle_center_1, radius)
            pygame.draw.circle(surface, COLORS['black'], circle_center_2, radius)


class Snake(object):
    body = []  # Snake is a sequence of ordered cubes
    turns = {}  # Keys are the position where the snake turned and the Values are its direction.

    def __init__(self, color, position):
        self.color = color
        self.head = Cube(position)
        self.body.append(self.head)
        self.x_direction = 0
        self.y_direction = 1
        pass

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for _ in keys:
                if keys[pygame.K_LEFT]:
                    self.x_direction = -1
                    self.y_direction = 0
                elif keys[pygame.K_RIGHT]:
                    self.x_direction = 1
                    self.y_direction = 0
                elif keys[pygame.K_UP]:
                    self.x_direction = 0
                    self.y_direction = 1
                elif keys[pygame.K_DOWN]:
                    self.x_direction = 0
                    self.y_direction = -1
                else:  # If other buttons were pressed, no need to remember the snake position/direction
                    break
                self.turns[self.head.position[:]] = (self.x_direction, self.y_direction)

        # This loop makes sure the tails follows the head
        for index, cube in enumerate(self.body):
            position = cube.position[:]

            # If the current cube is at a square that it should turn, give it directions
            if position in self.turns:
                turn = self.turns[position]
                cube.move(*turn)
                if index == len(self.body) - 1:
                    self.turns.pop(position)  # After the tail turns, drop turning directions.
            else:  # If it's not at a turning square, it will continue to move
                # If it's about to trespass a border, put it in the other side of the window
                if cube.x_direction == -1 and cube.position[0] <= 0:
                    cube.position = (ROWS - 1, cube.position[1])
                elif cube.x_direction == 1 and cube.position[0] >= ROWS - 1:
                    cube.position = (0, cube.position[1])
                elif cube.y_direction == -1 and cube.position[1] <= 0:
                    cube.position = (cube.position[0], ROWS - 1)
                elif cube.y_direction == 1 and cube.position[1] >= ROWS - 1:
                    cube.position = (cube.position[0], 0)
                else:  # If it's not, then continue moving ahead
                    cube.move(cube.x_direction, cube.y_direction)

    def draw(self, surface):
        for index, cube in enumerate(self.body):
            if index == 0:
                cube.draw(surface, True)
            else:
                cube.draw(surface)


# Functions Definition
def draw_grid(surface):
    """Divides the window into grids according to the number of rows"""
    width = surface.get_width()
    size_between = width // ROWS
    x, y = 0, 0

    for line in range(ROWS):
        x += size_between
        y += size_between

        pygame.draw.line(surface, COLORS['white'], (x, 0), (x, width))
        pygame.draw.line(surface, COLORS['white'], (0, y), (width, y))


def redraw_window(surface: pygame.Surface, snake: Snake):
    """Erases the window, draws the grid and updates the visual"""
    surface.fill(COLORS['black'])
    draw_grid(surface)
    snake.draw(surface)
    pygame.display.update()


def main():
    """Controls the game flow."""
    window = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    snake = Snake(COLORS['blue'], (ROWS // 2, ROWS // 2))  # RGB values, coordinates

    pygame.init()

    while True:
        pygame.time.delay(50)  # 50ms so that the game doesn't run too fast
        clock.tick(10)  # Speed in FPS

        snake.move()
        redraw_window(window, snake)


# Good luck, have fun!
main()
