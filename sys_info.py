# Consolidated most imported files here for now to simplify code.
import pygame as pg

### Tracks basic game information ###
screen_x = 1000
screen_y = 500

def top_right(size):
    """Takes size boolean and returns top right coords."""
    x = screen_x - size[0]
    y = 0
    return (x, y)

caption = "Auto Battler"
img_dir = "./images"
fps = 60
white = (255, 255, 255)

