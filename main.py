from settings import *
from sprites import *
import pygame
import random

# function within game class
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Juusan-Tsuki")
        self.clock = pygame.time.Clock()
        self.running = True

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.platforms = pygame.sprite.Group()
        platform1 = Platform(0, HEIGHT-20, WIDTH, 20)
        platform2 = Platform(50, 300, 300, 20)
        self.all_sprites.add(platform1)
        self.platforms.add(platform1)
        self.all_sprites.add(platform2)
        self.platforms.add(platform2)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()
        hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            self.player.pos.y = hits[0].rect.top
            self.player.vel.y = 0


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass



game = Game()
while game.running:
    game.new()

pygame.quit()
