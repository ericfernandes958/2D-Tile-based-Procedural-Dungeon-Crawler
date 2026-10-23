import pygame


class Renderer:
    def __init__(self, screen, assets):
        self.screen = screen
        self.assets = assets
        self.player_image = assets.load_image("player.png")

    def draw(self, player):
        self.screen.blit(self.player_image, player.rect.topleft)
