from sprite_classes.base import BaseSprite
import pygame as pg
from assets import assets

class Button(BaseSprite):
    """Basic button that glows when hovers and performs function when clicked.
    Note that image_names a tuple with two names."""
    def __init__(self, image_names, size, coords, function = None):
        super().__init__(image_names[0], size, coords)
        self._on = pg.transform.scale(assets.get_img(image_names[0]), size)
        self._off = pg.transform.scale(assets.get_img(image_names[1]), size)
        self._function = function

    def set_function(self, function):
        self._function = function

    def get_clicked(self):
        """Function called when click event occurs"""
        if self.image == self._on:  # Only activates if button is currently on.
            self._function()

    def update(self):
        """Updates button appearance when hovered."""
        mouse_pos = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.image = self._on
        else:
            self.image = self._off


class ToggleButton(Button):
    """Button subclass that allows button to be toggled on and off."""
    def __init__(self, image_names, size, coords, function = None):
        super().__init__(image_names, size, coords, function)
        self.image = self._off
        # self._active = False

    def get_clicked(self):
        """Activated when click event occurs in pygame"""
        mouse_pos = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            # Run function if it exists
            if self._function:
                self._function()

            # Toggle on or off
            if self.image == self._on: 
                self.image = self._off
            else:
                self.image = self._on

    def update(self):
        """Overrides and disables the update function in super class Button."""
        pass