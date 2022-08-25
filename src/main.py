import pygame

pygame.init()

# screen game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brawler")

# load background image
IMAGE_PATH = "assets/images/background/background.jpg"
bg_image = pygame.image.load(IMAGE_PATH).convert_alpha()


# function for drawing background
def draw_bg():
    scale_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scale_bg, (0, 0))


# game loop
run = True
while run:

    # draw background
    draw_bg()

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update display
    pygame.display.update()


# exit pygame
pygame.quit()
