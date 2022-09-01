from pygame import mixer


def sound_effects(
    game_sound: str,
    p1_weapon_sound: str,
    p2_weapon_sound: str,
) -> tuple[mixer.Sound, mixer.Sound]:
    mixer.init()

    mixer.music.load(game_sound)
    mixer.music.set_volume(0.5)
    mixer.music.play(-1, 0.0, 5000)

    p1_fx = mixer.Sound(p1_weapon_sound)
    p1_fx.set_volume(0.5)

    p2_fx = mixer.Sound(p2_weapon_sound)
    p2_fx.set_volume(0.5)
    return p1_fx, p2_fx
