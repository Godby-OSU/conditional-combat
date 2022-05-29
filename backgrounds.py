from assets import assets
from sys_info import screen_size
import pygame as pg

class Backgrounds():
    def __init__(self):
        self.stone = pg.transform.scale(assets.get_img("stone_background"), (screen_size))
        self.stage = pg.transform.scale(assets.get_img("stage_background"), (screen_size))
        self.battle = pg.transform.scale(assets.get_img("battle_background"), (screen_size))

        self.dictionary = {
            "title": self.stone,
            "selection": self.stage,
            "guide": self.stone,
            "battle": self.battle,
            "highscores": self.stone}

