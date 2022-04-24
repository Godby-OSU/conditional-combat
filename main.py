import pygame
# from images import Image_Collection as img_col
import sys_info as sys
from units import create_friendly


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((sys.screen_x, sys.screen_y))
        import screens as display
        import screen_sprites as ss
        from battle import Battle
        self.clock = pygame.time.Clock()
        self.background = pygame.Surface((sys.screen_x, sys.screen_y))  # Blank background to clear objects
        pygame.display.set_caption(sys.caption)

        self.all = pygame.sprite.RenderUpdates()
        self.display = display.Screens(self.all)
        self.battle = Battle(self.display)
        self.display.set_function("battle_on", self.battle.start_combat)

        # Create and store ally unit
        primary_unit = create_friendly("wizard")
        self.display.add_unit_selection(primary_unit, (200,200), (0,0))
        self.battle.add_friendly(primary_unit)
        self.display.set_function("aoe_on", primary_unit.toggle_aoe)

        # Load main menu
        self.display.load_menu()
        self.round = 1 

    def run(self):

        while True:
            pressed = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pressed = True
                if event.type == pygame.QUIT:
                    pygame.quit()

            # Update sprites
            self.battle.update()
            mouse_position = pygame.mouse.get_pos()
            self.all.clear(self.screen, self.background)
            self.all.update(mouse_position, pressed)
            dirty = self.all.draw(self.screen)
            pygame.display.update(dirty)

            self.clock.tick(sys.fps)



def main():
    game = Game()
    while True:
        game.run()

if __name__ == '__main__':
    main()
