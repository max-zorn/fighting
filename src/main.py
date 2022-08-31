import pygame
from pygame import mixer
from fighter import Fighter

mixer.init()
pygame.init()

# screen game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fighting")

# set framerate
clock = pygame.time.Clock()
FPS = 60

# define colors
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# define game variables
intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]  # pl1, pl2 scores
round_over = False
ROUND_OVER_COOLDOWN = 2000

# define fighter variables
WARRIOR_SIZE = 162
WARRIOR_SCALE = 4
WARRIOR_OFFSET = [72, 56]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 107]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

# load music and sounds
MUSIC_PATH = "assets/audio/music.mp3"
pygame.mixer.music.load(MUSIC_PATH)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)

SWORD_SOUND_PATH = "assets/audio/sword.wav"
sword_fx = pygame.mixer.Sound(SWORD_SOUND_PATH)
sword_fx.set_volume(0.5)

MAGIC_SOUND_PATH = "assets/audio/magic.wav"
magic_fx = pygame.mixer.Sound(MAGIC_SOUND_PATH)
magic_fx.set_volume(0.5)

# load background image
IMAGE_PATH = "assets/images/background/background.jpg"
bg_image = pygame.image.load(IMAGE_PATH).convert_alpha()

WARRIOR_IMAGE_PATH = "assets/images/warrior/Sprites/warrior.png"
WIZARD_IMAGE_PATH = "assets/images/wizard/Sprites/wizard.png"
warrior_sheet = pygame.image.load(WARRIOR_IMAGE_PATH).convert_alpha()
wizard_sheet = pygame.image.load(WIZARD_IMAGE_PATH).convert_alpha()

# load victory image
VICTORY_IMG_PATH = "assets/images/icons/victory.png"
victory_img = pygame.image.load(VICTORY_IMG_PATH).convert_alpha()

# define number of steps in each animation
WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]

# define font
COUNT_FONT_PATH = "assets/fonts/turok.ttf"
count_font = pygame.font.Font(COUNT_FONT_PATH, 80)
score_font = pygame.font.Font(COUNT_FONT_PATH, 30)


# function for drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# function for drawing background
def draw_bg():
    scale_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scale_bg, (0, 0))


# function for drawing fighter health bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))


# create two instances of fighters
fighter_1 = Fighter(
    1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx
)
fighter_2 = Fighter(
    2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx
)


# game loop
run = True
while run:
    clock.tick(FPS)
    # draw background
    draw_bg()

    # show fighters stats
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)
    draw_text("P1: " + str(score[0]), score_font, RED, 20, 60)
    draw_text("P2: " + str(score[1]), score_font, RED, 580, 60)

    # update countdown
    if intro_count <= 0:
        # move fighters
        fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over)
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, round_over)
    else:
        # display count timer
        draw_text(
            str(intro_count), count_font, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3
        )
        # update count timer
        if (pygame.time.get_ticks() - last_count_update) >= 1000:
            intro_count -= 1
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
            score[1] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
        elif not fighter_2.alive:
            score[0] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
    else:
        # display victory image
        screen.blit(victory_img, (360, 150))
        if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
            round_over = False
            intro_count = 3
            # TODO add reset
            fighter_1 = Fighter(
                1,
                200,
                310,
                False,
                WARRIOR_DATA,
                warrior_sheet,
                WARRIOR_ANIMATION_STEPS,
                sword_fx,
            )
            fighter_2 = Fighter(
                2,
                700,
                310,
                True,
                WIZARD_DATA,
                wizard_sheet,
                WIZARD_ANIMATION_STEPS,
                magic_fx,
            )

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update display
    pygame.display.update()


# exit pygame
pygame.quit()
