import pygame, sys
from settings import *
from level import Level
from overworld import Overworld
from ui import UI

class Game:
    def __init__(self):

        # game init
        self.max_level = 0
        self.max_health = 100
        self.cur_health = 100
        self.coins = 0
        self.hearts = 3

        # audio
        self.level_bg_music = pygame.mixer.Sound('./audio/level_music.wav')
        self.level_bg_music.set_volume(0.5)
        self.overworld_bg_music = pygame.mixer.Sound('./audio/overworld_music.wav')
        self.overworld_bg_music.set_volume(0.5)

        # overworld creation
        self.overworld = Overworld(0, self.max_level, screen, self.create_level)
        self.status = 'overworld'
        self.overworld_bg_music.play(loops = -1)

        # user interface
        self.ui = UI(screen)

    def create_level(self, current_level):
        self.level = Level(current_level, screen, self.create_overworld, self.change_coins, self.change_health, self.reset_after_death, self.lose_heart)
        self.status = 'level'
        self.overworld_bg_music.stop()
        self.level_bg_music.play(loops = -1)

    def create_overworld(self, current_level, new_max_level):
        if new_max_level > self.max_level:
            self.max_level = new_max_level
        self.overworld = Overworld(current_level, self.max_level, screen, self.create_level)
        self.status = 'overworld'
        self.level_bg_music.stop()
        self.overworld_bg_music.play(loops = -1)

    def change_coins(self, amount):
        self.coins += amount

    def reset_after_death(self):
        self.coins = 0
        self.cur_health = 100

    def change_health(self, amount):
        self.cur_health += amount

    def lose_heart(self):
        self.hearts -= 1

    def add_heart(self):
        if self.coins >=10:
            self.hearts += 1
            self.coins = 0

    def check_game_over(self):
        if self.cur_health <= 0:
            self.cur_health = 100
            self.coins = 0
            self.max_level = 0
            self.overworld = Overworld(0, self.max_level, screen, self.create_level)
            self.status = 'overworld'
            self.level_bg_music.stop()
            self.overworld_bg_music.play(loops = -1)

    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
        else:
            self.level.run()
            self.ui.show_health(self.cur_health, self.max_health)
            self.ui.show_coins(self.coins)
            self.ui.show_heart(self.hearts)
            self.add_heart()
            self.check_game_over()

# pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('grey')
    game.run()

    # level.run()

    pygame.display.update()
    clock.tick(60)