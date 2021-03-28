import pygame
pygame.font.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("cop running simulator - theoretical programmers")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((0,0,255))
    pygame.display.update()
window.mainloop()