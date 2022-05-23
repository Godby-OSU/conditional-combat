################
# Sprite Lists 
################
"""
Tracks sprites that are used by more than one window.
"""
import pygame
import sprites.unit_classes as unit
from display import Display 
import sprites.stat_blocks as stats

class SpriteGroup:
    def __init__(self, display: Display):
        self.sprite_list = []
        self.images = display.get_collection()

    def _add_sprite(self, sprite):
        """Adds a new sprite to the sprite_group."""
        self.sprite_list.append(sprite)

    def _bulk_add_sprites(self, sprite_list):
        """Adds multiple sprites from a list."""
        for sprite in sprite_list:
            self._add_sprite(sprite)

    def get_list(self):
        return self.sprite_list

class FriendlySprites(SpriteGroup):
    def __init__(self, display):
        super().__init__(display)
        starting_sprites = [
        unit.FriendlyUnit(self.images, "wizard", (200,200), (250,200), stats.friendly_info["wizard"])
        ]

        self._bulk_add_sprites(starting_sprites) 

# Unused at the moment due to no innate sprites
class EnemySprites(SpriteGroup):
    def __init__(self, display):
        super().__init__(display)

# Unused at the moment due to no innate sprites
class ReserveSprites(SpriteGroup):
    def __init__(self, display):
        super().__init__(display)



