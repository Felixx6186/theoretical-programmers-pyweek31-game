import pygame
import sys
import time


def play(screen):
    """
    Play function
    Takes as input screen <- is the main app screen
    Runs currently at 60fps
    It moves the default image to the left to 'teleport' to the end once not seen in the screen
    """
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
        # endregion
        # region Image placing on the screen
        screen.blit(bg, (0-x, 0))
        screen.blit(bg, (800-x, 0))
        screen.blit(bg, (1600-x, 0))
        # endregion
        # region events handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # endregion
        pygame.display.update()
