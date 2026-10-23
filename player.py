import pygame


class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 32, 32)
        self.speed = 200

    def update(self, dt):
        keys = pygame.key.get_pressed()

        direction = pygame.Vector2(0, 0)

        if keys[pygame.K_w]:
            direction.y -= 1
        if keys[pygame.K_a]:
            direction.x -= 1
        if keys[pygame.K_s]:
            direction.y += 1
        if keys[pygame.K_d]:
            direction.x += 1

        if direction.length_squared() > 0:
            direction = direction.normalize()

        self.rect.x += round(direction.x * self.speed * dt)
        self.rect.y += round(direction.y * self.speed * dt)
