import pygame
# from images import Image_Collection as img_col
import sys_info as sys


class Game():
    def __init__(self):
        # Start Pygame Window
        pygame.init()
        self.display = pygame.display.set_mode((sys.screen_x, sys.screen_y))
        pygame.display.set_caption(sys.caption)

        # Load Graphical Windows
        import screens  # This should go at top but current produces error if called before display init
        import battle
        self.screen = screens.Screens(self.display)
        self.windows = screens.Objects(self.screen)
        self.screen.update_windows(self.windows)
        self.screen.load_screen("menu")
        self.battle = battle.Battle(self.screen)
        self.windows.selection[0].set_function(lambda: self.battle.start_combat())
        self.battle.add_friendly(self.windows.primary_unit)  # This should not happen here
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            pressed = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pressed = True
                if event.type == pygame.QUIT:
                    pygame.quit()

            # Run Combat
            self.battle.run_round()

            # Update sprites
            self.screen.mouse_updates(pressed)
            self.screen.update()

            self.clock.tick(sys.fps)

def main():
    game = Game()
    while True:
        game.run()

if __name__ == '__main__':
    main()
