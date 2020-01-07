import pygame


class Grid:
    """a class for the movement grid"""
    def __init__(self, game):
        """ initialise a movement grid"""
        self.settings = game.settings
        self.screen = game.screen


        #set grid dimensions and position
        self.height = self.settings.tiles_size
        self.width = (self.settings.tiles_size) * (self.settings.tiles_per_side * 2 + 1)
        self.rect = pygame.Rect((0, 0), (self.width, self.height))
        self.rect.center = self.screen.get_rect().center

        #add tiles to grid
        self.tiles_dict = self._add_tiles()
        self._blit_tiles()

    def _add_tiles(self):
        """ creates tiles and draws them.
        Returns a dictionary
        {left_tiles: [list of Tiles], player_tile: [Tile], right_tiles [list of Tiles].
        Tiles in value lists are sorted from left to right."""
        tiles_dict = {}

        #create left side
        tiles_dict["left_tiles"] = self._create_enemy_tiles(0)
        #create player tile
        tiles_dict["player_tile"] = [Tile(self, self.settings.tile_bg_player,
                                        (self.rect.left + self.settings.tiles_size * self.settings.tiles_per_side))]
        #create right tiles
        tiles_dict["right_tiles"] = self._create_enemy_tiles(self.settings.tiles_size * (self.settings.tiles_per_side + 1))

        return tiles_dict

    def _create_enemy_tiles(self, x_start):
        """ creates and returns a list of Tile objects for enemies, of len tiles_per_side"""
        tile_list = []
        x_start += self.rect.left
        for tile_num in range(self.settings.tiles_per_side):
            tile_list.append(Tile(self, self.settings.tile_bg_enemy, (x_start + (self.settings.tiles_size * tile_num))))
        return tile_list

    def _blit_tiles(self):
        """ blits all tiles in self.tiles_dict"""
        for tileset in self.tiles_dict.values():
            for tile in tileset:
                self.screen.blit(tile.bg, tile.rect)

class Tile:
    """ a class for grid tiles"""
    def __init__(self, grid, bg_img, x_left):
        """ initialise a tile"""
        self.grid = grid
        self.settings = grid.settings
        self.screen = grid.screen

        self._draw_tile(bg_img, x_left)

    def _draw_tile(self, bg_img, x_left):
        """ set tile dimensions and position """
        self.bg = pygame.image.load(bg_img)
        self.rect = self.bg.get_rect()
        self.rect.top = self.grid.rect.top
        self.rect.left = x_left

