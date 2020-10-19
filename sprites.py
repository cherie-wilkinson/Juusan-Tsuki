import pygame
from settings import *
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface ((30,40))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0, 0)
        self.acc = vec(0,0)


    def update(self):
        self.acc = vec(0,0.8)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.pos.x >= 15:
                self.acc.x = -PLAYER_ACC

        if keys[pygame.K_RIGHT]:
            if self.pos.x <= WIDTH - 15:
                self.acc.x = PLAYER_ACC


# set the new position with relation to acceleration
        self.acc += self.vel * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x < 15:
            self.acc.x = 0
            self.vel.x = 0

        if self.pos.x > WIDTH-15:
            self.acc.x = 0
            self.vel.x = 0

        self.rect.midbottom = self.pos


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w,h))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

