#################
# Unit Sprites
#################
from sprites.sprite_classes import ScreenSprite

class Unit(ScreenSprite):
    def __init__(self, directory, image_name, size, coords, stat_block: dict):
        super().__init__(directory, image_name, size, coords)
        self._hitpoints = stat_block["hp"]
        self._current_hitpoints = stat_block["hp"]
        self._damage = stat_block["dmg"]
        self._type = stat_block["type"]

    def get_name(self):
        return self._name

    def get_damage(self):
        return self._damage

    def get_health(self):
        return self._current_hitpoints

    def take_damage(self, damage):
        self._current_hitpoints -= damage

    def get_type(self):
        return self._type

    def check_pulse(self):
        if self._current_hitpoints <= 0:
            return False
        else: return True

class FriendlyUnit(Unit):
    def __init__(self, directory, image_name, size, coords, stat_block):
        super().__init__(directory, image_name, size, coords, stat_block)
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
    def __init__(self, directory, image_name, size, coords, stat_block):
        super().__init__(directory, image_name, size, coords, stat_block)
        self._value = stat_block["value"]