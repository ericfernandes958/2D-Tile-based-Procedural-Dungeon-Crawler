import pygame

WIN_WIDTH = 1280
WIN_HEIGHT = 720


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Riftborn Realms")

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((30, 30, 40))
            pygame.display.flip()

        pygame.quit


game = Game()
game.run()
