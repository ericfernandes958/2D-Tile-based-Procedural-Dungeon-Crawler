from pathlib import Path
import pygame


class AssetManager:
    def __init__(self):
        root = Path(__file__).resolve().parent.parent
        self.asset_dir = root / "assets"
        self.images = {}

    def load_image(self, filename):
        if filename not in self.images:
            path = self.asset_dir / "images" / filename
            self.images[filename] = pygame.image.load(path).convert_alpha()

        return self.images[filename]
