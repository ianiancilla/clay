import pygame


class Settings:
    """class to manage game settings"""
    def __init__(self):
        """initialise game settings"""

        self.game_title = "Clay"

        # DISPLAY settings
        self.full_screen = False
        self.screen_width = 1024
        self.screen_height = 768
        self.bg_color = (0, 0, 0)

        # GRID settings
        self.tiles_per_side = 5
        self.tiles_size = 80    # size of tiles, in pixel

        # IMAGE settings
        self.grid_bg_enemy = "images/tile_enemy.bmp"
        self.grid_bg_player = "images/tile_player.bmp"
        self.wp_sword = "images/weapon_sword.png"
        self.wp_axe = "images/weapon_axe.png"
        self.wp_lance = "images/weapon_lance.png"

        # TODO player settings
        # PLAYER settings
        self.player_start_HP = 50

        # TODO enemy settings
        # ENEMY settings
        self.enemy_start_HP = 20

        # TODO score settings

        # key mapping
        self.key_quit = pygame.K_q
