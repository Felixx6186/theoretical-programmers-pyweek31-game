import pygame
import threading
import sys
import time
from random import randint
from source.classes import Player, Bullet

list_of_imgs = ["imgs\\bkg_1house.png", "imgs\\bkg.png"]  # a list with all the images path
list_of_bgs = [pygame.image.load(x) for x in list_of_imgs]  # a list of images objects
current_bkg = 0  # a value to be incremented every time the image reaches the end
bkgs = [list_of_bgs[randint(0, len(list_of_bgs)-1)] for _ in range(1000)]   # a list of a thousend images to be used
# as list of possible images
pygame.mixer.init()

def background_music():
    while True:
        pygame.mixer.music.load("music\\Anttis instrumentals - A guy walks into a bar and orders 6 8.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
            
def random_bkg(number):
    """ will pick a background based on the received number as input and return it could not seem usefull but i
    think later will"""
    global bkgs
    return bkgs[number]
                        
def play(screen, player: Player):
    """
    Play function
    Takes as input screen <- is the main app screen
    Runs currently at 60fps
    It moves the default image to the left to 'teleport' to the end once not seen in the screen
    """
    global current_bkg
    x = threading.Thread(target=background_music, daemon=True)
    x.start()
    x = 0
    now = time.time()
    now2 = time.time()
    speed = 6  # By increasing this the background will move faster to the left
    to_draw = 0
    shooting =  False
    while 1:
        # region Logic to be run every 1/60 secs
        if time.time() - now > 0.0166666:  # if the time elapsed is higher than 1/60
            now = time.time()
            x += speed
            if x > 800:
                x = 0
                current_bkg += 1  # if the images disappears from the screen we need to move each images to the previous
                # object we can do it by increasing this value
            if x % 60 == 0:
                if to_draw == 1:
                    to_draw = 0
                else:
                    to_draw += 1
            # region Image placing on the screen
            screen.blit(random_bkg(0 + current_bkg), (0 - x, 0))
            screen.blit(random_bkg(1 + current_bkg), (800 - x, 0))
            screen.blit(random_bkg(2 + current_bkg), (1600 - x, 0))
            # endregion
            player.jump()
            player.draw(to_draw)
            if randint(0, 100) > 90 and shooting is False:
                shooting = Bullet(screen, 5)
            if shooting is not False :
                if shooting.x > -100:
                    shooting.x -= 12
                if shooting.x <= -100:
                    shooting = False
            if shooting is not False:
                shooting.shot()
            if shooting is not False:
                if shooting.x in range(player.x_coord, player.x_coord+100) and shooting.y in range(player.y_coord, player.y_coord+100):
                    player.hp -= 1
                    shooting = False
                    if player.hp == 0:
                        break



        # endregion
        # region Logic to be run every 1/5 secs
        if time.time() - now2 > 1/5:  # if the time elapsed is higher than 1/60
            now2 = time.time()

        # endregion
        # region events handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player.jumping is False:
                        player.jumping = True
        # endregion
        pygame.display.update()
