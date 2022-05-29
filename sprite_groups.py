import pygame

# Window Groups
title_sprites = pygame.sprite.RenderUpdates()
selection_sprites = pygame.sprite.RenderUpdates()
guide_sprites = pygame.sprite.RenderUpdates()
battle_sprites = pygame.sprite.RenderUpdates()
highscore_sprites = pygame.sprite.RenderUpdates()
score_sprites = pygame.sprite.RenderUpdates()       # Only the score text form highscores

# Unit Groups
friendly_sprites = pygame.sprite.RenderUpdates()
enemy_sprites = pygame.sprite.RenderUpdates()
reserve_sprites = pygame.sprite.RenderUpdates()

# Group Dictionary
sprite_dictionary = {
    "title": title_sprites,
    "selection": selection_sprites,
    "guide": guide_sprites,
    "battle": battle_sprites,
    "highscores": highscore_sprites,
    "friendly_sprites": friendly_sprites,
    "enemy_sprites": enemy_sprites,
    "reserve_sprites": reserve_sprites
}