import pygame
from random import randint

class Player:
    def __init__(self, ground_level: int, hp: int, def_x: int, screen):
        self.ground_level = ground_level
        self.hp = hp
        self.x_coord = def_x
        self.y_coord = ground_level
        self.jumping = False
        self.max_jump = 180
        self.jump_speed = 10
        self.screen = screen
        self.running_imgs = [pygame.image.load('imgs\\characters\\default1.png'), pygame.image.load('imgs\\characters\\default2.png')]
        self.discending = False
    def check_ground(self):  # To be used for collision detection (TO BE COMPLETED AND TESTED)
        if self.y_coord != self.ground_level:
            return False
        else:
            return True

    def jump(self):  # will take care of jump positioning (TO BE COMPLETED AND TESTED) needs some changes since y is
        # taken from upper edge and not from bottom
        if self.jumping:
            if self.max_jump < self.y_coord and self.discending is False:
                self.y_coord -= self.jump_speed
            elif self.max_jump == self.y_coord and self.discending is False:
                self.discending = True
                print('REACHED THE TOP')
            if self.discending is True and self.y_coord < self.ground_level:
                self.y_coord += self.jump_speed
            if self.discending and self.y_coord == self.ground_level:
                self.discending = False
                self.jumping = False


    def draw(self, number):  # if isnt jumping will return the right running image based on given number
        return self.screen.blit(self.running_imgs[number], (self.x_coord, self.y_coord))

class Bullet:
    def __init__(self, screen, speed):
        self.y = 350
        self.img = pygame.image.load('imgs\\bullet.png')
        self.x = 800
        self.speed = speed
        self.screen = screen

    def shot(self):
        self.screen.blit(self.img, (self.x, self.y))
        