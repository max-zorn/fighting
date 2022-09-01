from pygame.transform import scale
from pygame.image import load
from pygame.draw import rect
from pygame.font import Font
from pygame import Surface

from src.config.config import Colors


def draw_text(
    screen: Surface,
    text: str,
    font: Font,
    text_col: tuple[int, int, int],
    x: int,
    y: int,
) -> None:
    # function for drawing text
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def draw_bg(screen: Surface, image_path: str, width: int, height: int) -> None:
    # function for drawing background
    bg_image = load(image_path).convert_alpha()
    scale_bg = scale(bg_image, (width, height))
    screen.blit(scale_bg, (0, 0))


def draw_health_bar(
    screen: Surface, health: int, x: int, y: int, colors: Colors
) -> None:
    # function for drawing fighter health bars
    ratio = health / 100
    rect(screen, colors.white.rgb, (x - 2, y - 2, 404, 34))
    rect(screen, colors.red.rgb, (x, y, 400, 30))
    rect(screen, colors.yellow.rgb, (x, y, 400 * ratio, 30))
