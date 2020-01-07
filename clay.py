import sys
import pygame

from settings import Settings
from grid import Grid

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
        self.bg_color = (self.settings.bg_color)

        # create and draw grid
        self.grid = Grid(self)

    def run_game(self):
        """
        Runs the main loop for the game
        """
        while True:
            self._check_events()

            #refresh screen
            pygame.display.flip()

    def _check_events(self):
        """Checks for and responds to mouse and kb events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

if __name__ == '__main__':
    game = Game()
    game.run_game()