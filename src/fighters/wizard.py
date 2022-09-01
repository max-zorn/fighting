from pygame.mixer import Sound
from pygame import Rect

from src.fighters.fighter import Fighter
from src.config.config import load_config

config = load_config(path="config")


class Wizard(Fighter):
    def __init__(self, pl: int, x: int, y: int, flip: bool, sound: Sound):
        super().__init__()
        self.player = pl
        self.flip = flip
        self.x = x
        self.y = y
        self.rect = Rect((self.x, self.y, 80, 180))
        self.attack_sound = sound

        self.size = config.fighters.wizard.size
        self.image_scale = config.fighters.wizard.scale
        self.offset = config.fighters.wizard.offset
        self.sprite_sheet = config.fighters.wizard.image
        self.animation_steps = config.fighters.wizard.animation_steps

        self.animation_list = super().load_images()
        self.image = self.animation_list[self.action][self.frame_index]
