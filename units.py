###############
# Units
###############
"""Manages information about different units."""

# TODO: These dictionaries can be moved somewhere else once things are working.
# TODO: They are currently only here for quick adjustment as the classes that use them are finalized.

#####
# Unit Information
friendly_info = {
"wizard": {
    "name": "Wizard",
    "value": None,
    "img": "wizard",
    "hp": 3,
    "dmg": 2,
    "type": "wizard",
    "faction": "ally",
    "aoe": False
    }
}

enemy_info = {
"slime": {
    "name": "Slime",
    "value": 1,
    "img": "slime",
    "hp": 2,
    "dmg": 1,
    "type": "basic",
    "faction": "enemy"
    }
}

#####
# Funtions to create enemy and ally units.
def create_friendly(key):
    name = friendly_info[key]["name"]
    img = friendly_info[key]["img"]
    hp = friendly_info[key]["hp"]
    dmg = friendly_info[key]["dmg"]
    type = friendly_info[key]["type"]
    aoe = friendly_info[key]["aoe"]

    return Friendly_Unit(name, img, hp, dmg, type, aoe)


def create_enemy(key):
    name = enemy_info[key]["name"]
    img = enemy_info[key]["img"]
    hp = enemy_info[key]["hp"]
    dmg = enemy_info[key]["dmg"]
    type = enemy_info[key]["type"]
    value = enemy_info[key]["value"]
    
    return Enemy_Unit(name, img, hp, dmg, type, value)

#####
# Unit classes.
"""The above functions should be used to create units.  These classes should only be called after creation."""

class Unit():
    """Base class that includes values used by both friendly and enemy units.
    The sprite is not created when class is initialized.  It is created by a function class when needed."""

    def __init__(self, name, img_name, hp, dmg, type):
        self._unit_name = name
        self._image_name = img_name
        self._hitpoints = hp
        self._current_hitpoints = hp
        self._damage = dmg
        self._type = type
        self._sprite = None

    def get_name(self):
        return self._image_name

    def get_sprite(self):
        return self._sprite

    def get_damage(self):
        return self._damage

    def get_health(self):
        return self._current_hitpoints

    def take_damage(self, damage):
        self._current_hitpoints -= damage

    def set_sprite(self, sprite):
        self._sprite = sprite

    def check_pulse(self):
        if self._current_hitpoints <= 0:
            return False
        else: return True

class Friendly_Unit(Unit):
    def __init__(self, name, img, hp, dmg, type, aoe):
        super().__init__(name, img, hp, dmg, type)
        self._aoe = aoe

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
        

class Enemy_Unit(Unit):
    def __init__(self, name, img, hp, dmg, type, value):
        super().__init__(name, img, hp, dmg, type)
        self._value = value
            
        
        

