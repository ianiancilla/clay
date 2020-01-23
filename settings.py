from itertools import cycle

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
        self.bg_color = pygame.Color("blue") #(0, 0, 0)

        # GRID settings
        self.tiles_per_side = 5
        self.tiles_size = 80    # size of tiles, in pixel

        # IMAGE settings
        self.grid_bg_enemy = "images/tile_enemy.bmp"
        self.grid_bg_player = "images/tile_player.bmp"
        self.wp_sword = "images/weapon_sword.png"
        self.wp_axe = "images/weapon_axe.png"
        self.wp_lance = "images/weapon_lance.png"

        # FONT settings
        self.hp_font = pygame.font.SysFont(None, 50)
        self.hp_color = pygame.Color("green")
        self.hp_dist = 20    # distance in px between HP counter and character

        ### GAMEPLAY SETTINGS ###
        # PLAYER settings
        self.player_start_HP = 100
        # ENEMY settings
        self.enemy_start_HP = 10
        self.enemy_spawn_prob = 0.3    #probability of an enemy spawning on outermost tile, each turn

        # WEAPON settings
        self.wp_list = ["lance", "axe", "sword"]
        self.wp_cycle = cycle(self.wp_list)

        # DAMAGE settings
        self.dam_mult_even = 1    # multiplier for same weapon
        self.dam_mult_win = 2    # multiplier for weapon advantage
        self.dam_mult_lose = 0    # multiplier for weapon disadvantage

        # TODO score settings

        # KEY MAPPING
        self.key_quit = pygame.K_q
        self.key_keep_wp = pygame.K_a
        self.key_change_wp = pygame.K_d
