import pygame, sys
from settings import *
from level import Level
from overworld import Overworld
from game_data import level_0


class Game:
    def __init__(self):
        self.max_level = 2
        self.overworld = Overworld(1, self.max_level, screen)

    def run(self):
        self.overworld.run()

# pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
# level = Level(level_0, screen)
game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    game.run()

    # level.run()

    pygame.display.update()
    clock.tick(60)