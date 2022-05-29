import pygame
pygame.init()
import sys_info as sys
from display import display
from assets import assets
assets.load_directory()
from initial_sprites import initialize_sprites

class Game():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.display = display
        display.initalize_backgrounds()
        initialize_sprites()
        
        # Load the title window
        self.display.change_window("title")
        
    def run(self):
        running = True
        while running:
            # Check for Events
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.display.get_clicked()
                if event.type == pygame.QUIT:
                    running = False
              
            # Update the screen
            self.display.render_screen()
            self.clock.tick(sys.fps)

        pygame.quit()


def main():
    game = Game()
    while True:
        game.run()

if __name__ == '__main__':
    main()
