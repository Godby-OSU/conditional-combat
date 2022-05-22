import pygame
import sys_info as sys
from display import Display
from assets import Image_Collection

from windows.wdw_title import title_window
from windows.wdw_guide import guide_window
from windows.wdw_selection import selection_window
from windows.wdw_highscores import highscores_window

class Game():
    def __init__(self):
        pygame.init()                               
        self.clock = pygame.time.Clock()
        self.img_collection = Image_Collection(sys.img_dir)
        self.display = Display(self.img_collection)
        self.img_collection.load_directory()  
        
        # Create all windows 
        # (Seems better to front-load this instead of spreading it out)
        title_window(self.display, "title")
        guide_window(self.display, "guide")
        selection_window(self.display, "selection")
        highscores_window(self.display, "highscores")

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
                    

            # Run Combat
            #self.battle.run_round()

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
