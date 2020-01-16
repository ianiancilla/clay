""" Classes to keep track of player and enemies"""
from random import random
from itertools import cycle

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
        self.tile.toggle_free()

        #set weapon, image, and position
        self.weapon = weapon
        self.update_wp_img()
        self.rect = self.image.get_rect()
        self.place(self.tile)

        self.hp = hp

        # draw the character
        # assign HP
        pass

    def update_wp_img(self):
        """ sets self.wp_img to the correct image for given weapon, and updates self.rect"""
        if self.weapon == "sword":
            self.image = pygame.image.load(self.settings.wp_sword)
        elif self.weapon == "axe":
            self.image = pygame.image.load(self.settings.wp_axe)
        elif self.weapon == "lance":
            self.image = pygame.image.load(self.settings.wp_lance)


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

    def update(self):
        self.update_wp_img()

    def change_weapon(self):    # TODO change weapon
        self.weapon = next(self.settings.wp_cycle)



class Enemy(Character):
    """ a class for enemies """
    # TODO enemy class
    # TODO test enemy IDs
    _nextID = 0

    def __init__(self, game, tile):
        self.settings = game.settings
        super().__init__(game, random.choice[self.settings.wp_list], tile, self.settings.enemy_start_HP)

        # assign an ID to the enemy, each enemy created will have a new ID
        self.ID = self._nextID
        self._nextID += 1

    def kill(self):    # TODO enemy kill
        pass

    def move(self):    # TODO enemy move
        pass