################
# Windows 
################
"""
Windows will pass data along to the Display.
!! Display should NOT call a Window.
!! No window sub class should call display
"""
import pygame
from display import Display

class Window():
    def __init__(self, display: Display, tag: str):
        self.display = display
        self.tag = tag                                   # Identifying str for window
        self.window_group = pygame.sprite.Group()        # The sprite_group for window
        self.display.new_window(tag, self.window_group)  # Add initial group to the display
        self.images = self.display.get_collection()      # Retrieve the image collection

    def _add_sprite(self, sprite):
        """Adds a new sprite to the sprite_group."""
        self.window_group.add(sprite)
        self.display.insert_window(self.tag, sprite)

    def _bulk_add_sprites(self, sprite_list):
        """Adds multiple sprites from a list."""
        for sprite in sprite_list:
            self._add_sprite(sprite)
    
    #def _update_sprite(self, index, updated_sprite):
     #   """Updates a specific sprite at given index"""
      #  self.display.update_window(self.tag, index, updated_sprite)

    def activate_window(self):
        """Performs any updates that switching windows may require.  Method must exist for all windows.
        Functionality overwritten on sub-classes as needed."""
        print(self.tag, "WINDOW ACTIVATED")


    def _change_window(self, tag):
        """Activates window then switches the active window on display.
        Window classes should call this version and not the Display class version."""
        self.display.change_window(tag)
        self.activate_window()

        
    
# Sprites will only check position on a click even
# Their on_click function updates sprite.
# Their update function does something different
# mouse_pos = pygame.mouse.get_pos(
