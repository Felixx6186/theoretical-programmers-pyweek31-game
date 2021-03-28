import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 550))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 40)
pygame.display.set_caption("cop running simulator - theoretical programmers")
screen.fill((235, 225, 52))

class Button:
    "Create a button, then blit the surface in the while loop"

    def __init__(self, text,  x, y, bg="black"):
        self.x = x
        self.y = y
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        self.text = font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

start_button = Button("Start", x=365, y=200, bg="green")
end_button = Button("Quit",x=370,y=280, bg="red")

def show_buttons():
    screen.blit(start_button.surface, (start_button.x, start_button.y))
    screen.blit(end_button.surface,(end_button.x,end_button.y))


def button1_click(event):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed()[0]:
            if start_button.rect.collidepoint(x, y):
                pass
                #start game
            elif end_button.rect.collidepoint(x,y):
                sys.exit()


loop = 1
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = 0
        button1_click(event)
    pygame.draw.rect(screen, (0, 0, 0), (250, 160, 300, 200))
    show_buttons()
    pygame.display.update()
    clock.tick(30)

pygame.quit()
