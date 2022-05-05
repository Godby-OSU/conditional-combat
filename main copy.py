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
        import screencopy  # This should go at top but current produces error if called before display init
        self.screen = screencopy.Screens(self.display)
        self.windows = screencopy.Objects(self.screen)
        self.screen.load_screen(self.windows.menu)

        self.clock = pygame.time.Clock()

        # Create and store ally unit
        """
        primary_unit = create_friendly("wizard")
        self.display.add_unit_selection(primary_unit, (200,200), (0,0))
        self.battle.add_friendly(primary_unit)
        self.display.set_function("aoe_on", primary_unit.toggle_aoe)"""

    def run(self):
        while True:
            pressed = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pressed = True
                if event.type == pygame.QUIT:
                    pygame.quit()

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
