""" Classes to keep track of player and enemies"""
import random

import pygame
from pygame.sprite import Sprite


class Character(Sprite):
    """ a super class for player and enemies"""
    def __init__(self, game, weapon, tile, hp):
        """ initialises a Character (super class)
            attributes will be:
            tile - the Tile it occupies
            weapon, image, rect, hp
        """
        self.settings = game.settings
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.tile = tile
        self.tile.toggle_free()

        # set weapon, image, and position
        self.weapon = weapon
        self._update_wp_img()
        self.rect = self.image.get_rect()
        self.place()

        self.hp = hp

    def _update_wp_img(self):
        """ sets self.wp_img to the correct image based on self.weapon """
        if self.weapon == "sword":
            self.image = pygame.image.load(self.settings.wp_sword)
        elif self.weapon == "axe":
            self.image = pygame.image.load(self.settings.wp_axe)
        elif self.weapon == "lance":
            self.image = pygame.image.load(self.settings.wp_lance)

    def place(self):
        """ places character sprite centered on given tile """
        self.rect.center = self.tile.rect.center

    def apply_damage(self):    # TODO apply_damage
        """ applies damage to character """
        pass


class Player(Character):
    """ a class for the player """
    def __init__(self, game, tile):
        self.settings = game.settings
        super().__init__(game, "sword", tile, self.settings.player_start_HP)

    def update(self):
        self._update_wp_img()

    def change_weapon(self):
        """ cycles player weapon (not image!) to the next one in self.settings.wp_cycle """
        self.weapon = next(self.settings.wp_cycle)

    def kill(self):    # TODO player kill
        pass

class Enemy(Character):
    """ a class for enemies """
    # TODO test enemy IDs
    _nextID = 0

    def __init__(self, game, tile):
        """ initialises an enemy """
        self.settings = game.settings
        super().__init__(game, random.choice(self.settings.wp_list), tile, self.settings.enemy_start_HP)

        # assign an ID to the enemy, each enemy created will have a new ID
        self.ID = self._nextID
        self._nextID += 1

    def update(self):
        """ updates enemies with actions required each turn """
        self._move()

    def kill(self):    # TODO enemy kill
        pass

    def _move(self):
        """ checks if next tile towards player is free, and moves there if so """
        if self.tile.next() and self.tile.next().free:
            self.tile.toggle_free()
            self.tile = self.tile.next()
            self.place()
            self.tile.toggle_free()

