################
# Selection Window 
################
from windows.window import Window
from sys_info import screen_x, screen_y
import sprites.sprite_classes as spc

class SelectionWindow(Window):
    def __init__(self, display, tag: str, friendly_unit_class):
        super().__init__(display, tag)
        # Initial Sprites for this window
        friendly_units = friendly_unit_class.get_list()

        selection_sprites = [           
            spc.Button(self.images, ("battle_on", "battle_off"), (400,150), (int(screen_x-400),int(screen_y-150)), lambda: self._change_window("battle")),
            spc.ToggleButton(self.images, ("aoe_on", "aoe_off"), (200,75), (250,100), friendly_units[0].toggle_aoe)
        ]
        self._bulk_add_sprites(selection_sprites) # Adds the selection screen UI
        self._bulk_add_sprites(friendly_units)    # Adds friendly units to screen
