import pygame

class UI:
    def __init__(self, game):
        self.game = game
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Blizzard Bonanza")