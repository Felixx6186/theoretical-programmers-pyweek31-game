import pygame
import sys
import time
from random import randint

list_of_imgs = ["imgs\\bkg_1house.png", "imgs\\bkg.png"]  # a list with all the images path
list_of_bgs = [pygame.image.load(x) for x in list_of_imgs]  # a list of images objects
current_bkg = 0  # a value to be incremented every time the image reaches the end
bkgs = [list_of_bgs[randint(0, len(list_of_bgs)-1)] for _ in range(1000)]   # a list of a thousend images to be used
# as list of possible images


def random_bkg(number):
    """ will pick a background based on the received number as input and return it could not seem usefull but i
    think later will"""
    global bkgs
    return bkgs[number]


def play(screen):
    """
    Play function
    Takes as input screen <- is the main app screen
    Runs currently at 60fps
    It moves the default image to the left to 'teleport' to the end once not seen in the screen
    """
    global current_bkg
    print('here')
    bg = pygame.image.load("imgs\\bkg_1house.png")

    x = 0
    now = time.time()
    speed = 6  # By increasing this the background will move faster to the left
    while 1:
        # region Logic to be run every 1/60 secs
        if time.time() - now > 0.0166666:  # if the time elapsed is higher than 1/60
            now = time.time()
            x += speed
            if x > 800:
                x = 0
                current_bkg += 1  # if the images disappears from the screen we need to move each images to the previous
                # object we can do it by increasing this value
        # endregion
        # region Image placing on the screen
        screen.blit(random_bkg(0+current_bkg), (0-x, 0))
        screen.blit(random_bkg(1+current_bkg), (800-x, 0))
        screen.blit(random_bkg(2+current_bkg), (1600-x, 0))
        # endregion
        # region events handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # endregion
        pygame.display.update()
