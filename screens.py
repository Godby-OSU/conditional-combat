#################
# Screens 
################
"""
Includes information required to manage visuals active on the current screen.
"""
import sys_info as sys
import screen_sprites as ss
import pygame
import json
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
            ss.Button(("guide_on", "guide_off"), (200,75), (int(sys.screen_x-200),int(sys.screen_y-75)), lambda: screen.load_screen("guide")), 
            ss.Button(("scores_off", "scores_on"), (400,150), (int(sys.screen_x/2-200),350), lambda: self.update_highscores())]      
        self.highscores = [
            ss.Button(("close", "close"), (100,100), (sys.screen_x-100,0), lambda: screen.load_screen("menu")),
            ss.Text("1.)",  50, (255,115,0), (50, 50)),
            ss.Text("2.)",  50, (255,115,0), (50, 100)),
            ss.Text("3.)",  50, (255,115,0), (50, 150)),
            ss.Text("4.)",  50, (255,115,0), (50, 200)),
            ss.Text("5.)",  50, (255,115,0), (50, 250))]
        
        self.battle =[]  

        self.windows = {
            "selection": self.selection,
            "guide": self.guide,
            "menu": self.menu,
            "battle": self.battle,
            "highscores": self.highscores
        }

        self.primary_unit = create_friendly("wizard")
        sprite = ss.Screen_Sprite("wizard", (200,200), (250,200))
        self.primary_unit.set_sprite(sprite)
        self.selection.append(sprite)

        self.battle.append(self.primary_unit.get_sprite())
        self.selection[1].set_function(self.primary_unit.toggle_aoe)

    def update_highscores(self):
        """Uses JSON file to generate a list of highscores."""
        # Access JSON
        with open('highscores.json', 'r') as read:
            data = json.load(read)

        # Update Highscores Table
        for n in range(1,6):
            try:
                new_text = (n, '.)', ' ', data[str(n)][0], '  ---', ' ', 'Round: ', data[str(n)][1])
                string = ''.join(map(str, new_text))    # https://www.geeksforgeeks.org/python-program-to-convert-a-tuple-to-a-string/
                print(string)
                self.highscores[n].change_text(string)
            except:
                pass

        # Display the table
        self._screen.load_screen("highscores")


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