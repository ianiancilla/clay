class Settings:
    """class to manage game settings"""
    def __init__(self):
        """initialise game settings"""

        self.game_title = "Clay"

        #display settings
        self.full_screen = False
        self.screen_width = 1024
        self.screen_height = 768
        self.bg_color = (0, 0, 0)

        #grid settings
        self.tiles_per_side = 5
        self.tiles_size = 80 #size of tiles, in pixel

        #image settings
        self.tile_bg_enemy = "images/tile_enemy.bmp"
        self.tile_bg_player = "images/tile_player.bmp"


        #TODO player settings

        #TODO enemy settings

        #TODO score settings