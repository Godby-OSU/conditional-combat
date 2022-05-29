import pygame as pg

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