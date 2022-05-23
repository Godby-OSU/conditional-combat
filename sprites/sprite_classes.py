#################
# UI Sprites
#################
"""
TODO: Remove the need to use directory as a parameter.
"""

import pygame as pg

class ScreenSprite(pg.sprite.Sprite):
    """Base class for any image on screen.  Directory is passed down from the display class"""
    def __init__(self, directory, image_name, size, coords):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(directory.get_img(image_name), size)
        self.rect = self.image.get_rect(topleft = coords)
        self._name = image_name
        self._coords = coords
        self._size = size

    def get_name(self):
        return self._name

    def set_pos(self, pos):
        self._coords = pos

    def get_clicked(self):
        """Exists only to allow calling this function on a group of sprites"""
        pass
        
        
class Button(ScreenSprite):
    """Basic button that glows when hovers and performs function when clicked.
    Note that image_names a tuple with two names."""
    def __init__(self, directory, image_names, size, coords, function = None):
        super().__init__(directory, image_names[0], size, coords)
        self._on = pg.transform.scale(directory.get_img(image_names[0]), size)
        self._off = pg.transform.scale(directory.get_img(image_names[1]), size)
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
    def __init__(self, directory, image_names, size, coords, function = None):
        super().__init__(directory, image_names, size, coords, function)
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

    def update(self):
        """Updates font to current message."""
        self.image = self.font.render(self.msg, 0, self.color)
