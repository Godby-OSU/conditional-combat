#################
# Screen Sprites
#################
"""Creates the classes for the sprites that will be rendered on the screen.
This is the only file that should be touching the image collection directly."""

# TODO: Update function is clunky.  Need to either find a way to have just ONE on the main class OR

from images import Image_Collection
import pygame as pg
import sys_info as sys

img_dir = Image_Collection(sys.img_dir)

class Screen_Sprite(pg.sprite.Sprite):
    """Base class for any image on screen."""
    def __init__(self, image_name, size, coords):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(img_dir.get_img(image_name), size)
        self.rect = self.image.get_rect(topleft = coords)
        self._name = image_name
        self._coords = coords
        self._size = size

    def get_size(self):
        return self._size

    def get_name(self):
        return self._name

    def set_pos(self, pos):
        self._coords = pos
        
        
class Button(Screen_Sprite):
    """Requires a tuple with two image names"""
    def __init__(self, image_names, size, coords, function = None):
        super().__init__(image_names[0],  size,coords )
        self._on = pg.transform.scale(img_dir.get_img(image_names[0]), size)
        self._off = pg.transform.scale(img_dir.get_img(image_names[1]), size)
        self._function = function

    def set_function(self, function):
        self._function = function

    def update(self, mouse, pressed):
        if self.rect.collidepoint(mouse):
            self.image = self._on
            if pressed is True:
                self._function()
                """
                try:
                    self._function()
                except:
                    print("Your function did not work")
                    print(self._function)"""

        else:
            self.image = self._off

class Toggle_Button(Button):
    def __init__(self, image_names, size, coords, function = None):
        super().__init__(image_names, size, coords, function)
        self.image = self._off
        self._active = False

    def update(self, mouse, pressed):
        if self.rect.collidepoint(mouse):
            if pressed is True:
                self._function()
                if self._active is True:
                    self.image = self._off
                    self._active = False
                else:
                    self.image = self._on
                    self._active = True

class Text(pg.sprite.Sprite):
    """Renders text objects to screen."""
    def __init__(self, msg, size, color, coords):
        pg.sprite.Sprite.__init__(self)
        self.font = pg.font.Font(None, size)
        self.image = self.font.render(msg, 1, color)
        self.color = color
        self.rect = self.image.get_rect().move(coords)
        self.msg = msg

    def change_text(self, new_text):
        self.msg = new_text
        self.image = self.font.render(self.msg, 1, self.color)

    def update(self, mouse, pressed):
        self.image = self.font.render(self.msg, 0, self.color)
