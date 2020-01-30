import sys
from random import random
from time import sleep

import pygame

from settings import Settings
from grid import Grid
from character import Character, Player, Enemy


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

        # create and draw grid
        self.grid = Grid(self)

        # create sprite groups
        self.characters_group = pygame.sprite.Group()    # used for all characters (player and enemies)
        self.hp_counters_group = pygame.sprite.Group()    # used for all HP counter (player and enemies)
        self.enemies_group = pygame.sprite.Group()    # used for enemy characters only

        # create player
        self.player = Player(self, self.grid.tiles_dict["player_tile"][0])
        self.characters_group.add(self.player)

    # GAME LOOP
    def run_game(self):
        """
        Runs the main loop for the game
        """
        self._update_screen()
        while self.running:
            # checks user input and handles it
            self._check_events()
            # draws new screen
            self._draw_screen()
            pygame.display.flip()
        pygame.quit()

    # EVENT HANDLING
    def _check_events(self):
        """Checks for and responds to mouse and kb events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                elif event.type == pygame.KEYDOWN:  # key down events
                    if event.key == self.settings.key_quit:    # quit game TODO remove or change quit key
                        self.quit_game()
                elif event.type == pygame.KEYUP:    # key up events
                    if event.key == self.settings.key_keep_wp:    # if player kept weapon
                        self.keep_wp()
                    elif event.key == self.settings.key_change_wp:  # if player changed weapon
                        self.change_wp()

    def quit_game(self):
        """ quits the game by ending the game loop """
        self.running = False

    def keep_wp(self):
        """ player keeps current weapon, and fights with adjacent enemies """
        self.settings.sfx_kp_wp.play()    # keep_weapon sound
        sleep(self.settings.sfx_kp_wp.get_length())    # small wait

        if self.player.get_adj_enemies() != [None, None]:
            # everyone deals damage
            for en in self.player.get_adj_enemies():
                if en:
                    en.apply_damage(self.player)
                    self.player.apply_damage(en)

            self.settings.sfx_fight.play()    # fighting sound
            sleep(self.settings.sfx_fight.get_length())

        self._update_screen()

    def change_wp(self):
        """ player swaps to next weapon, receives damage according to new weapon but deals none """
        self.player.change_weapon()
        self.player.update()
        self.settings.sfx_ch_wp.play()    # change_weapon sound
        sleep(self.settings.sfx_ch_wp.get_length())    # small wait

        if self.player.get_adj_enemies() != [None, None]:
            # enemies deal damage (player does not)
            for en in self.player.get_adj_enemies():
                if en:
                    en.apply_damage(self.player)
            self.settings.sfx_fight.play()    # fighting sound
            sleep(self.settings.sfx_fight.get_length())

        self._update_screen()

    # TURN CHANGE ACTIONS

    def _update_screen(self):
        """ updates the screens with all turn changes before it can be refreshed"""
        # updates existing characters
        self.characters_group.update()
        # spawns new enemies if possible
        self._spawn_enemies()

    def _spawn_enemies(self):
        """ has chance to spawn enemies on outermost tiles, if they are free """
        outer_tiles = [self.grid.tiles_dict["left_tiles"][-1], self.grid.tiles_dict["right_tiles"][-1]]
        for tile in outer_tiles:
            if not tile.get_character():
                if random() < self.settings.enemy_spawn_prob:
                    new_enemy = Enemy(self, tile)
                    self.enemies_group.add(new_enemy)
                    self.characters_group.add(new_enemy)

    # DRAWING

    def _draw_screen(self):
        """ draws the current game situation to the screen """
        self.screen.fill(self.settings.bg_color)
        self.grid.blit_tiles()
        self.characters_group.draw(self.screen)
        self.hp_counters_group.draw(self.screen)


if __name__ == '__main__':
    game = Game()
    game.run_game()
