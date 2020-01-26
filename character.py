""" Classes to keep track of player and enemies"""
import random

import pygame
from pygame.sprite import Sprite

from hp import HP


class Character(Sprite):
    """ a super class for player and enemies"""
    def __init__(self, game, weapon, tile, hp):
        """ initialises a Character (super class)
            attributes will be:
            tile - the Tile it occupies
            weapon, image, rect, hp
        """
        super().__init__()
        self.settings = game.settings
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.tile = tile
        self.tile.set_character(self)

        # set weapon, image, and position
        self.weapon = weapon
        self._update_wp_img()
        self.rect = self.image.get_rect()
        self.place()

        self.hp = hp
        self.hp_counter = HP(self)

    def set_hp(self, hp):
        self.hp = hp

    def get_hp(self):
        return self.hp

    def get_wp(self):
        return self.weapon

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

    def apply_damage(self, opponent):
        """ applies damage to character """
        # set damage multiplier
        if self.get_wp() == opponent.get_wp():
            mult = self.settings.dam_mult_even
        elif self.settings.wp_list[self.settings.wp_list.index(opponent.get_wp())] == \
            self.settings.wp_list[self.settings.wp_list.index(self.get_wp()) - 1] :
            mult = self.settings.dam_mult_win
        else:
            mult = self.settings.dam_mult_lose

        # set new HP
        damage = self.get_hp() * mult
        if damage > opponent.get_hp():
            opponent.set_hp(0)
        else:
            opponent.set_hp(opponent.get_hp() - damage)


class Player(Character):
    """ a class for the player """
    def __init__(self, game, tile):
        self.settings = game.settings
        super().__init__(game, "sword", tile, self.settings.player_start_HP)

    def update(self):
        self._update_wp_img()
        self.hp_counter.update_hp()

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
        self.hp_counter.update_hp()

    def kill(self):    # TODO enemy kill
        self.game.characters_group.remove(self)
        self.game.enemies_group.remove(self)
        self.game.hp_counters_group.remove(self.hp_counter)
        self.tile.character = None

    def _move(self):
        """ checks if next tile towards player is free, and moves there if so """
        if self.tile.next() and not self.tile.next().get_character():
            self.tile.set_character(None)
            self.tile = self.tile.next()
            self.place()
            self.tile.set_character(self)

