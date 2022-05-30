#################
# Unit Sprites
#################
from sprite_classes.base import BaseSprite
from sprite_classes.text import Text
from sprite_groups import battle_sprites
from display import display
import time

class Unit(BaseSprite):
    def __init__(self, image_name, size, coords, stat_block: dict):
        super().__init__(image_name, size, coords)
        self._hitpoints = stat_block["hp"]
        self._current_hitpoints = stat_block["hp"]
        self._damage = stat_block["dmg"]
        self._faction = stat_block["faction"]

    def get_name(self):
        return self._name

    def get_damage(self):
        return self._damage

    def get_health(self):
        return self._current_hitpoints

    def display_damage(self, damage):
        text = Text(str(damage), 100, (200, 25, 0), (self._coords))
        battle_sprites.add(text)
        display.render_screen()
        battle_sprites.remove(text)

    def take_damage(self, damage):
        self._current_hitpoints -= damage
        self.display_damage(damage)

    def get_faction(self):
        return self._faction

    def check_pulse(self):
        if self._current_hitpoints <= 0:
            return False
        else: return True

    def reset_health(self):
        self._current_hitpoints = self._hitpoints


class FriendlyUnit(Unit):
    def __init__(self, image_name, size, coords, stat_block):
        super().__init__(image_name, size, coords, stat_block)
        self._aoe = stat_block["aoe"]

    def get_aoe(self):
        return self._aoe

    def toggle_aoe(self):
        if self._aoe is False:
            print("Area of effect is on")
            self._aoe = True
        else:
            print("Area of effect is off")
            self._aoe = False

    def get_damage(self):
        if self._aoe:
            return int(self._damage/2)
        else:
            return self._damage
        

class EnemyUnit(Unit):
    def __init__(self, image_name, size, coords, stat_block):
        super().__init__(image_name, size, coords, stat_block)
        self._value = stat_block["value"]
