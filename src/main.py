import pygame

from fighter import Fighter
from config.config import load_config, Config
from misc.drawing import draw_bg, draw_text, draw_health_bar
from misc.sounding import sound_effects


def run_game(config: Config) -> None:
    sword_fx, magic_fx = sound_effects(
        game_sound=config.game.music,
        p1_weapon_sound=config.fighters.warrior.weapon_sound,
        p2_weapon_sound=config.fighters.wizard.weapon_sound,
    )

    pygame.init()

    screen = pygame.display.set_mode(
        size=(config.game.screen.width, config.game.screen.height)
    )
    pygame.display.set_caption(config.game.screen.title)

    # load victory image
    victory_img = pygame.image.load(config.game.victory).convert_alpha()

    # define font
    count_font = pygame.font.Font(config.game.font, 80)
    score_font = pygame.font.Font(config.game.font, 30)

    # create two instances of fighters
    fighter_1 = Fighter(
        1,
        200,
        310,
        False,
        config.fighters.warrior.size,
        config.fighters.warrior.scale,
        config.fighters.warrior.offset,
        config.fighters.warrior.image,
        config.fighters.warrior.animation_steps,
        sword_fx,
    )
    fighter_2 = Fighter(
        2,
        700,
        310,
        True,
        config.fighters.wizard.size,
        config.fighters.wizard.scale,
        config.fighters.wizard.offset,
        config.fighters.wizard.image,
        config.fighters.wizard.animation_steps,
        magic_fx,
    )
    # game loop
    clock = pygame.time.Clock()
    run = True
    round_over = False
    last_count_update = pygame.time.get_ticks()
    while run:
        clock.tick(config.game.screen.fps)

        # draw background
        draw_bg(
            screen=screen,
            image_path=config.game.background,
            width=config.game.screen.width,
            height=config.game.screen.height,
        )

        # show fighters stats
        draw_health_bar(screen, fighter_1.health, 20, 20, config.game.colors)
        draw_health_bar(screen, fighter_2.health, 580, 20, config.game.colors)
        draw_text(
            screen,
            "P1: " + str(config.game.score[0]),
            score_font,
            config.game.colors.red.rgb,
            20,
            60,
        )
        draw_text(
            screen,
            "P2: " + str(config.game.score[1]),
            score_font,
            config.game.colors.red.rgb,
            580,
            60,
        )

        # update countdown
        if config.game.intro_count <= 0:
            # move fighters
            fighter_1.move(
                config.game.screen.width,
                config.game.screen.height,
                fighter_2,
                round_over,
            )
            fighter_2.move(
                config.game.screen.width,
                config.game.screen.height,
                fighter_1,
                round_over,
            )
        else:
            # display count timer
            draw_text(
                screen,
                str(config.game.intro_count),
                count_font,
                config.game.colors.red.rgb,
                config.game.screen.width / 2,
                config.game.screen.height / 3,
            )
            # update count timer
            if (pygame.time.get_ticks() - last_count_update) >= 1000:
                config.game.intro_count -= 1
                last_count_update = pygame.time.get_ticks()

        # update fighters
        fighter_1.update()
        fighter_2.update()

        # draw fighters
        fighter_1.draw(screen)
        fighter_2.draw(screen)

        # check for player defeat
        if not round_over:
            if not fighter_1.alive:
                config.game.score[1] += 1
                round_over = True
                round_over_time = pygame.time.get_ticks()
            elif not fighter_2.alive:
                config.game.score[0] += 1
                round_over = True
                round_over_time = pygame.time.get_ticks()
        else:
            # display victory image
            screen.blit(victory_img, (360, 150))
            if (
                pygame.time.get_ticks() - round_over_time
                > config.game.round_over_cooldown
            ):
                round_over = False
                fighter_1.reset()
                fighter_2.reset()

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # update display
        pygame.display.update()

    # exit pygame
    pygame.quit()


def main(event, context):
    run_game(config=load_config(path="config"))


if __name__ == "__main__":
    main(1, 1)
