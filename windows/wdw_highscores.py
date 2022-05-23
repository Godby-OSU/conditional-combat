################
# Highscores Window 
################
from windows.window import Window
from sys_info import screen_x, screen_y
import sprites.sprite_classes as spc
import json

class HighscoresWindow(Window):
    def __init__(self, display, tag: str):
        super().__init__(display, tag)
        # Initial Sprites for this window
        highscores_sprites = [           
            spc.Button(self.images, ("close", "close"), (100,100), (screen_x-100,0), lambda: self._change_window("title")),
            spc.Text("1.)",  50, (255,115,0), (50, 50)),
            spc.Text("2.)",  50, (255,115,0), (50, 100)),
            spc.Text("3.)",  50, (255,115,0), (50, 150)),
            spc.Text("4.)",  50, (255,115,0), (50, 200)),
            spc.Text("5.)",  50, (255,115,0), (50, 250))]
        
        self._bulk_add_sprites(highscores_sprites) 

    def _update_highscores(self):
        """Uses JSON file to generate a list of highscores."""
        # Access JSON
        print("GOING IN")
        with open('highscores.json', 'r') as read:
            data = json.load(read)

        # Update Highscores Table
        for n in range(1,6):
            try:
                new_text = (n, '.)', ' ', data[str(n)][0], '  ---', ' ', 'Round: ', data[str(n)][1])
                string = ''.join(map(str, new_text))    # https://www.geeksforgeeks.org/python-program-to-convert-a-tuple-to-a-string/
                self.highscores_sprites[n].change_text(string)
                #self._update_sprite(n, self.highscores_sprites[n])
            except:
                pass

    def activate_window(self):
        """Updates the highscores when this window is opened"""
        self._update_highscores()