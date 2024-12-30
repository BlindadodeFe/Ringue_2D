import pygame


class StartButton:
    def __init__(self, x, y, width, height, image):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = image

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)
        return self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]