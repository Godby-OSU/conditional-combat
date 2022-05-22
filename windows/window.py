################
# Windows 
################
"""
Windows will pass data along to the Display.
!! Display should NOT call a Window.
"""
import pygame

class Window():
    def __init__(self, display, tag: str):
        self.display = display
        self.tag = tag                                   # Identifying str for window
        self.window_group = pygame.sprite.Group()        # The sprite_group for window
        self.display.new_window(tag, self.window_group)  # Add group to the display
        self.images = self.display.get_collection()      # Retrieve the image collection

    def add_sprite(self, sprite):
        """Adds a new sprite to the sprite_group."""
        self.window_group.add(sprite)
        self.display.insert_window(self.tag, sprite)

    def bulk_add_sprites(self, sprite_list):
        """Add multiple sprites from a list."""
        for sprite in sprite_list:
            self.add_sprite(sprite)

    def change_window(self, tag):
        """Changes the active window on the display."""
        self.display.change_window(tag)
        
    
# Sprites will only check position on a click even
# Their on_click function updates sprite.
# Their update function does something different
# mouse_pos = pygame.mouse.get_pos(
