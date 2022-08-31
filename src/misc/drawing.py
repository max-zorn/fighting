from pygame.transform import scale
from pygame.draw import rect


def draw_text(screen, text, font, text_col, x, y):
    # function for misc text
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def draw_bg(screen, bg_image, SCREEN_WIDTH, SCREEN_HEIGHT):
    # function for misc background
    scale_bg = scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scale_bg, (0, 0))


def draw_health_bar(screen, health, x, y, WHITE, RED, YELLOW):
    # function for misc fighter health bars
    ratio = health / 100
    rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    rect(screen, RED, (x, y, 400, 30))
    rect(screen, YELLOW, (x, y, 400 * ratio, 30))
