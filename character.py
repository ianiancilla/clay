""" Classes to keep track of player and enemies"""
from random import random

import pygame
from pygame.sprite import Sprite


class Character(Sprite):
    """ a super class for player and enemies"""
    # TODO Character class
    def __init__(self, game, weapon, tile, hp):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.tile = tile

        #set weapon, image, and position
        self.weapon = weapon
        self._update_wp_img(self.weapon)
        self.place(tile)

        self.hp = hp

        # draw the character
        # assign HP
        pass

    def _update_wp_img(self, weapon):
        """ sets self.wp_img to the correct image for given weapon, and updates self.rect"""
        if weapon == "sword":
            self.image = pygame.image.load(self.settings.wp_sword)
        elif weapon == "axe":
            self.image = pygame.image.load(self.settings.wp_axe)
        elif weapon == "lance":
            self.image = pygame.image.load(self.settings.wp_lance)
        self.rect = self.image.get_rect()

    def place(self, tile):
        """ places character sprite centered on given tile """
        self.rect.center = tile.rect.center

    def apply_damage(self):    # TODO apply_damage
        """ applies damage to character """
        pass


class Player(Character):
    """ a class for the player """
    # TODO Player class
    def __init__(self, game, tile):
        self.settings = game.settings
        super().__init__(game, "sword", tile, self.settings.player_start_HP)

    def kill(self):    # TODO player kill
        pass

    def change_weapon(self):    # TODO change weapon
        pass


class Enemy(Character):
    """ a class for enemies """
    _nextID = 0

    def __init__(self, game, tile):
        self.settings = game.settings
        super().__init__(game, random.choice["sword", "axe", "lance"], tile, self.settings.enemy_start_HP)
        # TODO add everything

        # assign an ID to the enemy, each enemy created will have a new ID
        self.ID = self._nextID
        self._nextID += 1

    def kill(self):    # TODO enemy kill
        pass

    def move(self):    # TODO enemy move
        pass