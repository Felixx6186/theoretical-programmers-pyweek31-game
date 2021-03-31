import pygame
import sys
from game import play

#initializing window with yellow colour and window title
pygame.init()
screen = pygame.display.set_mode((800, 550))
font = pygame.font.Font("fonts/Retro Gaming.ttf", 40)
pygame.display.set_caption("cop running simulator - theoretical programmers")
screen.fill((235, 225, 52))

#main title and credits
title_font = pygame.font.Font("fonts/Retro Gaming.ttf", 45)
credits_font = pygame.font.Font("fonts/Retro Gaming.ttf", 17)
title = title_font.render("Cop Running Simulator!", 1, (0,0,0))
credit = credits_font.render("By:- Theoretical Programmers",1,(70,70,70))
screen.blit(title, (80, 50))
screen.blit(credit, (420, 116))

#button class to easily create buttons and manage them
class Button:
    def __init__(self, text,  x, y, bg="black"):
        self.x = x
        self.y = y
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        self.text = font.render(text, 1, pygame.Color("Black"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

#start and quit buttons under a rectangular black surface
pygame.draw.rect(screen, (0, 0, 0), (215, 200, 370,170))
start_button = Button("Start", x=333, y=220, bg="green")
end_button = Button("Quit",x=350,y=300, bg=(255,0,0))
screen.blit(start_button.surface, (start_button.x, start_button.y))
screen.blit(end_button.surface,(end_button.x,end_button.y))

#handling mouse click events
def button1_click(event):
    x, y = pygame.mouse.get_pos()
    #making buttons responsive by chaning colour if hovered over
    if start_button.rect.collidepoint(x,y):
        start_button.change_text("Start",bg="white")
    else:
        start_button.change_text("Start",bg="green")
    if end_button.rect.collidepoint(x,y):
        end_button.change_text("Quit",bg="white")
    else:
        end_button.change_text("Quit",bg="red")
    if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed()[0]:
            if start_button.rect.collidepoint(x, y):
                play(screen)
            elif end_button.rect.collidepoint(x,y):
                sys.exit()

#main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        button1_click(event)
    screen.blit(start_button.surface, (start_button.x, start_button.y))
    screen.blit(end_button.surface,(end_button.x,end_button.y))
    pygame.display.update()
