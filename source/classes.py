import pygame

class Player:
    def __init__(self, ground_level: int, hp: int, def_x: int, screen):
        self.ground_level = ground_level
        self.hp = hp
        self.x_coord = def_x
        self.y_coord = ground_level
        self.jumping = False
        self.max_jump = 100
        self.jump_speed = 10
        self.screen = screen
        self.running_imgs = [pygame.image.load('imgs\\characters\\default1.png'), pygame.image.load('imgs\\characters\\default2.png')]

    def check_ground(self):  # To be used for collision detection (TO BE COMPLETED AND TESTED)
        if self.y_coord < self.ground_level:
            return False
        else:
            return True

    def jump(self):  # will take care of jump positioning (TO BE COMPLETED AND TESTED) needs some changes since y is
        # taken from upper edge and not from bottom
        if self.jumping:
            if self.max_jump > self.y_coord:
                self.y_coord += self.jump_speed
            elif self.max_jump == self.y_coord:
                # max height animation
                pass
            elif self.check_ground():
                self.max_jump -= self.jump_speed

    def draw(self, number):  # if isnt jumping will return the right running image based on given number
        if self.jumping is False:
            return self.screen.blit(self.running_imgs[number], (self.x_coord, self.y_coord))