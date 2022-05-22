################
# Highscores Window 
################
from windows.window import Window
from sys_info import screen_x, screen_y
import sprite_classes as spc

class highscores_window(Window):
    def __init__(self, display, tag: str):
        super().__init__(display, tag)
        # Initial Sprites for this window
        highscores_sprites = [           
            spc.Button(self.images, ("close", "close"), (100,100), (screen_x-100,0), lambda: display.change_window("title")),
            spc.Text("1.)",  50, (255,115,0), (50, 50)),
            spc.Text("2.)",  50, (255,115,0), (50, 100)),
            spc.Text("3.)",  50, (255,115,0), (50, 150)),
            spc.Text("4.)",  50, (255,115,0), (50, 200)),
            spc.Text("5.)",  50, (255,115,0), (50, 250))]
        
        self.bulk_add_sprites(highscores_sprites)    