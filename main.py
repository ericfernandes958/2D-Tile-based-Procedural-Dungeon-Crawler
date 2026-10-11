import pygame

WIN_WIDTH = 1280
WIN_HEIGHT = 720


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.pygame.set_caption("Riftborn Realms")


game = Game()
