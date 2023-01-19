import pygame
from tiles import AnimatedTile
from random import randint

class Enemy(AnimatedTile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, './graphics/enemy/run')
        self.rect.y += size - self.image.get_size()[1]
        self.speed = randint(3, 5)

    def move(self):
        self.rect.x += self.speed

    def update(self, x_shift):
        self.rect.x += x_shift
        self.animate()
        self.move()