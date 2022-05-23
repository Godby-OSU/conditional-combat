import pygame
import sys_info as sys
from display import Display
from assets import Image_Collection
import sprites.sprite_lists as spl

from windows.wdw_title import TitleWindow
from windows.wdw_guide import GuideWindow
from windows.wdw_selection import SelectionWindow
from windows.wdw_highscores import HighscoresWindow
from windows.wdw_battle import BattleWindow

class Game():
    def __init__(self):
        pygame.init()                               
        self.clock = pygame.time.Clock()
        self.img_collection = Image_Collection(sys.img_dir)
        self.display = Display(self.img_collection)
        self.img_collection.load_directory()  
        
        # Generate Sprite Groups
        friendly_sprites = spl.FriendlySprites(self.display)
        # enemy_sprites = spg.EnemySprites(self.display)
        # reserve_sprites = spg.ReserveSprites(self.display)

        # Create all windows 
        TitleWindow(self.display, "title")
        GuideWindow(self.display, "guide")
        BattleWindow(self.display, "battle", friendly_sprites)
        SelectionWindow(self.display, "selection", friendly_sprites)
        HighscoresWindow(self.display, "highscores")

        # Load the title window
        self.display.change_window("title")
        

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.display.get_clicked()
                if event.type == pygame.QUIT:
                    running = False
                    
            # Update the screen
            self.display.update()
            self.display.render_screen()
            self.clock.tick(sys.fps)

        pygame.quit()


def main():
    game = Game()
    while True:
        game.run()

if __name__ == '__main__':
    main()
