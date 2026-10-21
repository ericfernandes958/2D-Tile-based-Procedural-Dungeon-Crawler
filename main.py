import pygame

from asset_manager import AssetManager
from renderer import Renderer


WIN_WIDTH = 1280
WIN_HEIGHT = 720


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Riftborn Realms")

        self.assets = AssetManager()
        self.renderer = Renderer(self.screen, self.assets)

        self.running = True

    def run(self):

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.renderer.draw()
            pygame.display.flip()

        pygame.quit


game = Game()
game.run()
