import pygame

from fighter import Fighter

pygame.init()

# screen game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brawler")

# set framerate
clock = pygame.time.Clock()
FPS = 60

# define colors
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# define fighter variables
WARRIOR_SIZE = 162
WARRIOR_SCALE = 4
WARRIOR_OFFSET = [72, 56]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 107]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

# load background image
IMAGE_PATH = "assets/images/background/background.jpg"
bg_image = pygame.image.load(IMAGE_PATH).convert_alpha()

WARRIOR_IMAGE_PATH = "assets/images/warrior/Sprites/warrior.png"
WIZARD_IMAGE_PATH = "assets/images/wizard/Sprites/wizard.png"
warrior_sheet = pygame.image.load(WARRIOR_IMAGE_PATH).convert_alpha()
wizard_sheet = pygame.image.load(WIZARD_IMAGE_PATH).convert_alpha()

# define number of steps in each animation
WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]

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
    1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS
)
fighter_2 = Fighter(
    2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS
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

    # move fighters
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
    fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1)

    # update fighters
    fighter_1.update()
    fighter_2.update()

    # draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update display
    pygame.display.update()


# exit pygame
pygame.quit()
