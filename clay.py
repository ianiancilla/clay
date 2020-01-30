import pygame

from game_session import Game_session
from settings import Settings


class Game:
    """ a class to keep track of the entire game"""
    def __init__(self):
        """ Initialise game """
        pygame.display.init()
        pygame.font.init()
        pygame.mixer.init()
        self.settings = Settings()
        self.running = True

        # create window
        if self.settings.full_screen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.game_title)

        # set initial state
        self.state = Game_session(self)    # TODO change starting state

    # GAME LOOP
    def run_game(self):
        """
        Runs the main loop for the game
        """
        self.state.update_screen()
        while self.running:
            # checks user input and handles it depending on state
            self.state.check_events()
            # draws new screen depending on current state
            self.state.draw_screen()
            pygame.display.flip()
        pygame.quit()

    def quit_game(self):
        """ quits the game by ending the game loop """
        self.running = False


if __name__ == '__main__':
    game = Game()
    game.run_game()
