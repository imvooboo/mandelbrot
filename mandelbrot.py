import pygame as pg
import color

# pseudo constants
_screen_x = 200
_screen_y = 200



def main():

    # Initialize pygame engine, the game window, and colors.
    pg.init()
    fps_clock = pg.time.Clock()
    ds = pg.display.set_mode((_screen_x, _screen_y))
    pg.display.set_caption('Mandelbrot ({}, {})'.format(_screen_x, _screen_y))
    black = (0, 0, 0)
    white = (255, 255, 255)
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)


if __name__ == '__main__': main()