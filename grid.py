"""
Grid class, and Tile class that is used to build it
"""

import pygame


class Grid:
    """a class for the movement grid"""
    def __init__(self, game):
        """ initialise a movement grid"""
        self.settings = game.settings
        self.screen = game.screen

        # set grid dimensions and position
        self.height = self.settings.tiles_size
        self.width = self.settings.tiles_size * (self.settings.tiles_per_side * 2 + 1)
        self.rect = pygame.Rect((0, 0), (self.width, self.height))
        self.rect.center = self.screen.get_rect().center

        # add tiles to grid
        self.tiles_dict = self._add_tiles()
        # blit entire grid
        self.blit_tiles()

    def _add_tiles(self):
        """ creates tiles. Returns a dictionary:
        {left_tiles: [list of Tiles], player_tile: [Tile], right_tiles [list of Tiles].
        Tiles in lists of enemy tiles are sorted so that Tile 0 is adjacent to player tile."""
        tiles_dict = {"left_tiles": self._create_enemy_tiles(0, "left")[::-1],            # create left side
                      "player_tile": [Tile(self, self.settings.grid_bg_player,    # create player tile
                                           (self.rect.left + self.settings.tiles_size * self.settings.tiles_per_side),
                                           "center")],
                      "right_tiles": self._create_enemy_tiles(                    # create right side
                                          self.settings.tiles_size * (self.settings.tiles_per_side + 1), "right")}
        return tiles_dict

    def _create_enemy_tiles(self, x_start, side):
        """ creates and returns a list of Tile objects for enemies, of len tiles_per_side.
            only used by grid._add_tiles """
        tile_list = []
        x_start += self.rect.left
        for tile_num in range(self.settings.tiles_per_side):
            tile_list.append(Tile(self,
                                  self.settings.grid_bg_enemy,
                                  (x_start + (self.settings.tiles_size * tile_num)),
                                  side))
        return tile_list

    def blit_tiles(self):
        """ blits all tiles in self.tiles_dict """
        for tileset in self.tiles_dict.values():
            for tile in tileset:
                self.screen.blit(tile.bg, tile.rect)


class Tile:
    """ a class for grid tiles. Only used by Grid class """
    def __init__(self, grid, bg_img, x_left, side):
        """ initialise a tile """
        self.grid = grid
        self.settings = grid.settings
        self.screen = grid.screen
        self.side = side
        self.character = None
        # draw the tile
        self._position_tile(bg_img, x_left)

    def get_character(self):
        return self.character

    def set_character(self, character):
        self.character = character

    def _position_tile(self, bg_img, x_left):
        """ set tile dimensions and position """
        self.bg = pygame.image.load(bg_img)
        self.rect = self.bg.get_rect()
        self.rect.top = self.grid.rect.top
        self.rect.left = x_left

    # TODO remove
    # def toggle_free(self):
    #     """ toggles the free status from True to False and vice versa """
    #     if self.free:
    #         self.free = False
    #     else:
    #         self.free = True

    def next(self):
        """ returns the next tile, where next is closer to the player.
         Returns None if next tile is Player tile"""
        if self.side == "left":
            tiles = self.grid.tiles_dict["left_tiles"]
        elif self.side == "right":
            tiles = self.grid.tiles_dict["right_tiles"]

        ind = tiles.index(self)
        if ind > 0:
            return tiles[ind-1]
