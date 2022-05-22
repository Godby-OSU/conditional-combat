################
# Selection Window 
################
from windows.window import Window
from sys_info import screen_x, screen_y
import sprite_classes as spc

class selection_window(Window):
    def __init__(self, display, tag: str):
        super().__init__(display, tag)
        # Initial Sprites for this window
        selection_sprites = [           
            spc.Button(self.images, ("battle_on", "battle_off"), (400,150), (int(screen_x-400),int(screen_y-150))),
            spc.Toggle_Button(self.images, ("aoe_on", "aoe_off"), (200,75), (250,100))
        ]
        
        self.bulk_add_sprites(selection_sprites)    