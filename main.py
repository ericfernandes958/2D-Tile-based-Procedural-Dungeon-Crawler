import pygame

from asset_manager import AssetManager
from renderer import Renderer
from player import Player


WIN_WIDTH = 1280
WIN_HEIGHT = 720


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Riftborn Realms")

        self.clock = pygame.time.Clock()

        self.assets = AssetManager()
        self.player = Player(100, 100)
        self.renderer = Renderer(self.screen, self.assets)

        self.running = True

    def run(self):

        while self.running:
            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.player.update(dt)

            self.screen.fill((20, 20, 30))
            self.renderer.draw(self.player)

            pygame.display.flip()

        pygame.quit


game = Game()
game.run()
