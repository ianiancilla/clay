import pygame
from pygame.sprite import Sprite

class HP(Sprite):
    """ class to create and update HP counters """
    def __init__(self, character):
        """ initialise HP counter """
        super().__init__()

        # define attributes
        self.screen = character.game.screen
        self.settings = character.game.settings
        self.character = character
        self.font = self.settings.hp_font
        self.color = self.settings.hp_color

        self.update_hp()

    def update_hp(self):
        """ turn HP to a rendered image and TODO places it and draws it on the screen """
        # create an image of the hp, as only images can be drawn
        hp_str = str(self.character.hp)
        self.hp_image = self.font.render(hp_str, True, self.color)

        # name and place rect for the HP counter
        self.rect = self.hp_image.get_rect()
        self.rect.center = self.character.rect.center
        self.rect.bottom = self.character.rect.top - self.settings.hp_dist

        # TODO move this away in a more sensible place
        self.screen.blit(self.hp_image, self.rect)



