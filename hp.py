from pygame.sprite import Sprite

class HP(Sprite):
    """ class to create and update HP counters """
    def __init__(self, character):
        """ initialise HP counter """
        super().__init__()

        # attributes taken from outside
        self.character = character
        self.screen = character.screen
        self.settings = character.settings

        # own attributes
        self.font = self.settings.hp_font
        self.color = self.settings.hp_color

        # add to hp_counters Group, so all can be drawn and handled at once from game class
        self.character.game.hp_counters_group.add(self)

        self.update_hp()

    def update_hp(self):
        """ turn HP to a rendered image and places it on the screen """
        # create an image of the hp, as only images can be drawn
        hp_str = str(self.character.hp)
        self.image = self.font.render(hp_str, True, self.color)

        # name and place rect for the HP counter
        self.rect = self.image.get_rect()
        self.rect.center = self.character.rect.center
        self.rect.bottom = self.character.rect.top - self.settings.hp_dist



