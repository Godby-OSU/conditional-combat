################
# Title Window 
################
from windows.window import Window
from sys_info import screen_x, screen_y
import sprites.sprite_classes as spc
import json
"""
TODO: - This is an improvement but there are still some problems I'd like to change.
1.) It would be best to pass the sprite list as a JSON or XML object.
       I would need to pass the screen size variable to JSON before importing it 
       AND figure out to store or format a lambda class function effectively.
2.) Hard-coding in window tags before they're created is also not favorable.
       Consider using the add_function command to add these in AFTER the windows are created.
3.) Calling display at the start of each of these is clunky.  It's required to access the image directory.
        I would like to have the variable directly on the sprite_class page as I did before so it can be built
        into functions directly.  However, I would need to do so without recreating the problem this fixes.
        (importing things mid function because of initialization order requirements)
"""
# Window Information
class TitleWindow(Window):
    def __init__(self, display, tag: str):
        super().__init__(display, tag)
        # Initial Sprites for this window
        menu_sprites = [
            spc.ScreenSprite(self.images, "title", (screen_x,200),(0,0)),
            spc.Button(self.images, ("start_on", "start_off"), (400,150),(int(screen_x/2-200),200),  lambda: self._change_window("selection")),            
            spc.Button(self.images, ("guide_on", "guide_off"), (200,75), (int(screen_x-200),int(screen_y-75)), lambda: self._change_window("guide")), 
            spc.Button(self.images, ("scores_off", "scores_on"), (400,150), (int(screen_x/2-200),350), lambda: self._change_window("highscores"))
        ]     
        self._bulk_add_sprites(menu_sprites)    

