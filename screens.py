#################
# Screens 
################
"""
Includes information required to manage visuals active on the current screen.
"""
import sys_info as sys
import screen_sprites as ss
import pygame
from units import create_friendly

class Objects:
    """"""
    def __init__(self, screen):
        self._screen = screen
        self.selection = [           
            ss.Button(("battle_on", "battle_off"), (400,150), (int(sys.screen_x-400),int(sys.screen_y-150))),
            ss.Toggle_Button(("aoe_on", "aoe_off"), (200,75), (250,100))]
        self.guide = [
            ss.Screen_Sprite(("guide_info"), (sys.screen_x, sys.screen_y), (0,0)),
            ss.Button(("close", "close"), (100,100), (sys.screen_x-100,0), lambda: screen.load_screen("menu"))]
        self.menu = [
            ss.Screen_Sprite("title", (sys.screen_x,200),(0,0)),
            ss.Button(("start_on", "start_off"), (400,150),(int(sys.screen_x/2-200),200),  lambda: screen.load_screen("selection")),            
            ss.Button(("guide_on", "guide_off"), (400,150), (int(sys.screen_x/2-200),350), lambda: screen.load_screen("guide")) ]      
        self.battle =[]  

        self.windows = {
            "selection": self.selection,
            "guide": self.guide,
            "menu": self.menu,
            "battle": self.battle
        }

        self.primary_unit = create_friendly("wizard")
        sprite = ss.Screen_Sprite("wizard", (200,200), (250,200))
        self.primary_unit.set_sprite(sprite)
        self.selection.append(sprite)

        self.battle.append(self.primary_unit.get_sprite())
        self.selection[1].set_function(self.primary_unit.toggle_aoe)


class Screens:
    def __init__(self, display):
        self._rendered_group = pygame.sprite.RenderUpdates()
        self._display = display
        self._background = pygame.Surface((sys.screen_x, sys.screen_y))
        self._windows = dict()


    def update_windows(self, objects: Objects):
        """Updates the dictionary of window objects."""
        print("WE ARE USING THIS LIST")
        print(objects)
        self._windows = objects.windows

    def update(self):
        """Calls an update to screen visuals with no required input."""
        self._rendered_group.clear(self._display, self._background)
        group = self._rendered_group.draw(self._display)
        pygame.display.update(group)

    def mouse_updates(self, pressed: bool):
        """Updates screen visuals based on mouse position and status.
        Intended for main loop where events are processed."""
        mouse_pos = pygame.mouse.get_pos()
        self._rendered_group.update((mouse_pos), pressed)

    def add_sprite(self, sprite: pygame.sprite):
        """Add a singular sprite to the current list of active sprites."""
        self._rendered_group.add(sprite)

    def create_sprite(self, unit, size, pos):
        """Creates a sprite then adds it to list of active sprites"""
        unit.set_sprite(ss.Screen_Sprite(unit.get_name(), size, pos))
        self.add_sprite(unit.get_sprite())

    def remove_sprite(self, sprite: pygame.sprite):
        self._rendered_group.remove(sprite)

    def load_screen(self, window: str):
        """Input the initial list of sprites meant to be present on screen."""
        sprite_list = self._windows[window]
        self._rendered_group.empty()
        for sprite in sprite_list:
            self._rendered_group.add(sprite)
        return self._rendered_group

    def set_background(self, background):
        pass