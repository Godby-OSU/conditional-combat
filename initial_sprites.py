from sprite_classes.base import BaseSprite
from sprite_classes.buttons import Button, ToggleButton
from sprite_classes.text import Text
from sprite_classes.units import FriendlyUnit
from stat_blocks import friendly_info
from sys_info import screen_x, screen_y
from display import display
from highscores import update_highscores
from battle import battle
import sprite_groups as group

def add_sprites(sprite_list, group):
    """Adds sprite to specified sprite group."""
    for sprite in sprite_list:
        group.add(sprite)

def activate_highscores():
    update_highscores()
    display.change_window("highscores")


# Lists containing all initial sprites by window
title = [
BaseSprite("title", (screen_x,200),(0,0)),
Button(("start_on", "start_off"), (400,150),(int(screen_x/2-200),200),  lambda: display.change_window("selection")),            
Button(("guide_on", "guide_off"), (200,75), (int(screen_x-200),int(screen_y-75)), lambda: display.change_window("guide")), 
Button(("scores_off", "scores_on"), (400,150), (int(screen_x/2-200),350), lambda: activate_highscores())
]

guide = [
BaseSprite("guide_info", (screen_x, screen_y), (0,0)),
Button(("close", "close"), (100,100), (screen_x-100,0), lambda: display.change_window("title"))
]

scores = [
Text("1.)",  50, (255,115,0), (50, 50)),
Text("2.)",  50, (255,115,0), (50, 100)),
Text("3.)",  50, (255,115,0), (50, 150)),
Text("4.)",  50, (255,115,0), (50, 200)),
Text("5.)",  50, (255,115,0), (50, 250))
]

highscores = [
Button(("close", "close"), (100,100), (screen_x-100,0), lambda: display.change_window("title"))
]

friendly_sprites = [
FriendlyUnit("wizard", (200,200), (250,200), friendly_info["wizard"])
]

selection = [           
Button(("battle_on", "battle_off"), (400,150), (int(screen_x-400),int(screen_y-150)), lambda: battle.execute_battle()),
ToggleButton(("aoe_on", "aoe_off"), (200,75), (250,100), friendly_sprites[0].toggle_aoe),
friendly_sprites[0]
]


def initialize_sprites():
    """Adds all sprites from lists to the corresponding sprite groups"""
    add_sprites(title, group.title_sprites)
    add_sprites(guide, group.guide_sprites)
    add_sprites(highscores, group.highscore_sprites)
    add_sprites(scores, group.highscore_sprites)
    add_sprites(scores, group.score_sprites)
    add_sprites(friendly_sprites, group.friendly_sprites)
    add_sprites(selection, group.selection_sprites)