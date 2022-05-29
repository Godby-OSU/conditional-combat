################
# Display 
################
"""
Renders sprites and backgrounds to the screen.
"""
import pygame
import sys_info as sys
from sprite_groups import sprite_dictionary
from backgrounds import Backgrounds

class Display():
    """Class that tracks current sprites and renders the different windows to the screen."""
    def __init__(self):
        self.screen = pygame.display.set_mode(sys.screen_size)  # Start screen
        pygame.display.set_caption(sys.caption)                 # Set title for window
        self.active_group = pygame.sprite.RenderUpdates()       # Active group is sprite sub-class that tracks updates
        self.background = pygame.Surface((sys.screen_size))     # Current background
        self.window = None
   
    def initalize_backgrounds(self):
        """Creates a selection of backgrounds"""
        self.bg_col = Backgrounds()

    def change_window(self, tag):
        """Switch window currently being rendered"""
        self.active_group = sprite_dictionary[tag]
        self.window = tag
        self.background = self.bg_col.dictionary[tag]
        self.screen.blit(self.background, (0,0))

    def get_clicked(self):
        """Updates sprites that respond to mouse clicks."""
        # Check all sprites that have a get_clicked attribute
        try:
            for sprite in self.active_group:
                sprite.get_clicked()
        # Skip over them if they do not
        except:
            pass

    def update(self):
        """Perform update function on sprites in active group"""
        self.active_group.update()

    def render_screen(self):
        """Renders any updated sprites."""
        self.update()
        self.active_group.clear(self.screen, self.background)   # Clears the sprites in group from screen       
        sprites = self.active_group.draw(self.screen)           # Specifies which group needs drawn
        pygame.display.update(sprites)                          # Updates the screen with drawn sprites
      

display = Display()



