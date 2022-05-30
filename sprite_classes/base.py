import pygame as pg
from assets import assets

class BaseSprite(pg.sprite.Sprite):
    """Base class for any image on screen.  Directory is passed down from the display class"""
    def __init__(self, image_name, size, coords):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(assets.get_img(image_name), size)
        self.rect = self.image.get_rect(topleft = coords)
        self._name = image_name
        self._coords = coords
        self._size = size

    def get_name(self):
        return self._name

    def set_pos(self, pos):
        self._coords = pos
        self.rect.move_ip(pos)

    def get_coords(self):
        return self._coords

    def get_clicked(self):
        """All sprites need this attribute regardless of if used."""
        pass
        