import sys
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
        self.bg_color = self.settings.bg_color

        # create and draw grid
        self.grid = Grid(self)

        # TODO make initialise chars method?
        # create player
        self.player = Player(self, self.grid.tiles_dict["player_tile"][0])
        # TODO create enemies
        self.enemies = pygame.sprite.Group()
        # create character group
        self.characters = pygame.sprite.Group()
        self.characters.add(self.player)

    def run_game(self):
        """
        Runs the main loop for the game
        """
        while True:
            # checks user input and handles it
            self._check_events()
            # refresh screen
            self._update_screen()
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
                        pass
                    elif event.key == self.settings.key_change_wp:  # if player changed weapon
                        self.player.change_weapon()

    def _update_screen(self):
        """ updates the screens with all changes before it can be refreshed"""
        self.characters.update()
        self.characters.draw(self.screen)


if __name__ == '__main__':
    game = Game()
    game.run_game()
