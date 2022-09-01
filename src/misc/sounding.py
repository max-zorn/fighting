from pygame.mixer import init
from pygame.mixer import Sound
from pygame.mixer import music


def sound_effects(
    game_sound: str,
    p1_weapon_sound: str,
    p2_weapon_sound: str,
) -> tuple[Sound, Sound]:
    init()

    music.load(game_sound)
    music.set_volume(0.5)
    music.play(-1, 0.0, 5000)

    p1_fx = Sound(p1_weapon_sound)
    p1_fx.set_volume(0.5)

    p2_fx = Sound(p2_weapon_sound)
    p2_fx.set_volume(0.5)
    return p1_fx, p2_fx
