################
# Display 
################
"""
Renders sprites and backgrounds to the screen.
Display should NOT call anything.
"""

import pygame
import sys_info as sys

class Display():
    """Class that tracks current sprites and renders the different windows to the screen."""
    def __init__(self, image_collection):
        self.screen = pygame.display.set_mode(sys.screen_size)  # Start screen
        pygame.display.set_caption(sys.caption)                 # Set title for window
        self.img_col = image_collection                         # Save dictionary of all image assets
        self.windows = {}                                       # Format {"tag": sprite_group}        
        self.active_group = pygame.sprite.RenderUpdates()       # Active group is sprite sub-class that tracks updates
        self.background = pygame.Surface((sys.screen_size))     # Current background

    def get_collection(self):
        """Used to pass the image collection to the windows that create sprites"""
        return self.img_col
    
    def change_window(self, tag):
        """Switch window currently being rendered"""
        self.active_group.empty()               # Clear current active group
        for sprite in self.windows[tag]:        # Add sprites from the new group
            self.active_group.add(sprite)

    def new_window(self, tag, sprite_group):
        """Add new windows to list of sprite groups"""
        self.windows[tag] = sprite_group

    def insert_window(self, tag, new_sprite):
        """Add new sprite to specified window"""
        self.windows[tag].add(new_sprite)

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
        self.active_group.update()

    def render_screen(self):
        """Renders any updated sprites."""
        self.active_group.clear(self.screen, self.background)   # Clears the sprites in group from screen       
        sprites = self.active_group.draw(self.screen)           # Specifies which group needs drawn
        pygame.display.update(sprites)                          # Updates the screen with drawn sprites
        





