import sys
from random import random

import pygame

from settings import Settings
from grid import Grid
from character import Character, Player, Enemy


class Game:
    """ a class to keep track of the entire game"""
    def __init__(self):
        """ Initialise game """
        pygame.display.init()
        self.settings = Settings()

        # draw window
        if self.settings.full_screen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.game_title)

        # create and draw grid
        self.grid = Grid(self)

        # TODO make initialise chars method?
        # create player
        self.player = Player(self, self.grid.tiles_dict["player_tile"][0])
        self.enemies = pygame.sprite.Group()    # TODO decide if this group is needed
        # create character group
        self.characters = pygame.sprite.Group()
        self.characters.add(self.player)

    def run_game(self):
        """
        Runs the main loop for the game
        """
        self._update_screen()
        while True:
            # checks user input and handles it
            self._check_events()
            # refresh screen
            self._draw_screen()
            pygame.display.flip()

    def _check_events(self):
        """Checks for and responds to mouse and kb events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:  # key down events
                    if event.key == self.settings.key_quit:    # quit game TODO remove or change quit key
                        sys.exit()
                elif event.type == pygame.KEYUP:    # key up events
                    if event.key == self.settings.key_keep_wp:    # if player kept weapon
                        self._update_screen()
                    elif event.key == self.settings.key_change_wp:  # if player changed weapon
                        self.player.change_weapon()
                        self._update_screen()

    def _draw_screen(self):
        """ draws the current game situation to the screen """
        self.screen.fill(self.settings.bg_color)
        self.grid.blit_tiles()
        self.characters.draw(self.screen)

    def _update_screen(self):
        """ updates the screens with all turn changes before it can be refreshed"""
        self.characters.update()
        self.spawn_enemies()

    def spawn_enemies(self):
        """ has chance to spawn enemies on outermost tiles, if they are free """
        outer_tiles = [self.grid.tiles_dict["left_tiles"][-1], self.grid.tiles_dict["right_tiles"][-1]]
        for tile in outer_tiles:
            if tile.free:
                if random() < self.settings.enemy_spawn_prob:
                    new_enemy = Enemy(self, tile)
                    self.enemies.add(new_enemy)    # TODO decide if this group is needed
                    self.characters.add(new_enemy)


if __name__ == '__main__':
    game = Game()
    game.run_game()
