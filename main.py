import pygame
import random
pygame.init()
#game set up
running = True
screen = pygame.display.set_mode([800,800])
clock = pygame.time.Clock()
FPS = 60


#game loop
while running:
    #fixes fps
    clock.tick(FPS)
    pygame.display.update()
    #changes screen color
    screen.fill((150,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()