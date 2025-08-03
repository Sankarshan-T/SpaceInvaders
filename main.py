import pygame, sys


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GREY = (29, 29, 27)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

clock = pygame.time.Clock()

while True:
    #check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Drawing
    screen.fill(GREY)

    pygame.display.update()
    clock.tick(60)

