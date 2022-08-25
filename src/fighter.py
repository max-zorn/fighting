import pygame


class Fighter:
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0

    def move(self, screen_width):
        SPEED = 10
        dx = 0
        dy = 0

        # get keypress
        key = pygame.key.get_pressed()

        # movement
        if key[pygame.K_a]:
            dx = -SPEED
        if key[pygame.K_d]:
            dx = SPEED
        # jump
        if key[pygame.K_w]:
            self.vel_y = -30

        dy += self.vel_y

        # ensure fighter stays on screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right

        # update fighter position
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
