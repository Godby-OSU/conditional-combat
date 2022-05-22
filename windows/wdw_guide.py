################
# Guide Window 
################
from windows.window import Window
from sys_info import screen_x, screen_y
import sprite_classes as spc

class guide_window(Window):
    def __init__(self, display, tag: str):
        super().__init__(display, tag)
        # Initial Sprites for this window
        guide_sprites = [
            spc.Screen_Sprite(self.images, ("guide_info"), (screen_x, screen_y), (0,0)),
            spc.Button(self.images, ("close", "close"), (100,100), (screen_x-100,0), lambda: display.change_window("title"))
        ]
        
        self.bulk_add_sprites(guide_sprites)    